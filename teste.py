# -*- coding: utf-8 -*-
from random import randint, choice
import time

cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
cartas_jogador = []
cartas_computador = []
qtd_cartas = 0
qtd_cartas_computador = 0

FALAS_COMPUTADOR = ["Mais uma !", "Ta fácil, mais uma carta", "Vou tentar denovo!"]
QTD_TENTATIVAS = 5
VINTE_E_UM = 21
PARADA_COMPUTADOR = [18, 19, 20]


def computador_falando(falas=FALAS_COMPUTADOR):
    print(choice(falas))


def remove_carta_do_jogo(cartas, index_carta):
    cartas.pop(index_carta)


def pedir_carta(cartas):
    index_carta = randint(0, len(cartas) - 1)
    carta = cartas[index_carta]
    remove_carta_do_jogo(cartas, index_carta)
    return carta


def mostrar_cartas_atuais(cartas):
    print("Suas Cartas: [{}]: {}".format(sum(cartas_jogador), cartas_jogador))
    print("")


def soma_cartas(cartas_em_maos):
    return sum(cartas_em_maos)


def valida_vinte_um(cartas):
    return sum(cartas) == VINTE_E_UM


def vencedor(jogador, computador):
    soma_jogador = soma_cartas(jogador)
    soma_computador = soma_cartas(computador)
    if all([valida_vinte_um(jogador), valida_vinte_um(computador)]):
        return "Empate!"
    elif soma_jogador == soma_computador:
        return "Empate!"
    elif valida_vinte_um(jogador):
        return "Você Venceu!"
    elif valida_vinte_um(computador):
        return "Computador Venceu!"

    if soma_jogador > VINTE_E_UM:
        return "Computador Venceu!"
    elif soma_jogador < VINTE_E_UM and soma_computador > soma_jogador and soma_computador < VINTE_E_UM:
        return "Computador Venceu!"
    else:
        return "Você Venceu!"


while qtd_cartas != QTD_TENTATIVAS:
    cartas_jogador.append(pedir_carta(cartas))
    mostrar_cartas_atuais(cartas_jogador)
    acao = int(input("1- Pedir carta | 0- Parar "))
    if acao == 1:
        qtd_cartas += 1
    else:
        break


while qtd_cartas_computador != QTD_TENTATIVAS:
    if soma_cartas(cartas_jogador) > VINTE_E_UM:
        break
    cartas_computador.append(pedir_carta(cartas))
    soma = soma_cartas(cartas_computador)
    if soma == VINTE_E_UM or soma > VINTE_E_UM or soma in PARADA_COMPUTADOR:
        break
    else:
        computador_falando()
        time.sleep(2)
        qtd_cartas_computador += 1


msg = vencedor(cartas_jogador, cartas_computador)

print("")
print("==============RESULTADO===================")
print("Suas Cartas - TOTAL[{}] :".format(soma_cartas(cartas_jogador)))
print(cartas_jogador)
print("Cartas Computador - TOTAL[{}] :".format(soma_cartas(cartas_computador)))
print(cartas_computador)
print(msg)