import random
class Jogador():
    def __init__(self, nome, fichas):
        self.nome = nome
        self.fichas = fichas
        self.cartas_jogador = []

class Jogo():

    def __init__(self):
        self.jogador1 = Jogador("Jogador 1", 100, [])
        self.jogador2 = Jogador("Jogador 2", 100, [])
        self.jogadores = [self.jogador1, self.jogador2]
        self.baralho = {
            'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Q': 10, 'J': 10, 'K': 10
        }

    def menu(self):
        print("-------------------------------------"
              "|   Welcome to my Blackjack game!   |"
              "-------------------------------------")
        print("1- Start game")
        print("2- See value of cards")
        print("3- Rules")
        print("4- Exit game")
        option = int(input("What you want to do?"))

        match option:
            case 1:
                self.start_game()

            case 2:
                print(self.get_baralho())

            case 3:
                self.regras()

            case 4:
                exit()

    def get_baralho(self):
        return self.baralho


    def regras(self):
        print("---------------------------------")
        print("RULES BLACKJACK")
        print("Objective: Get as close as possible to 21 points without exceeding it."
              "Card Distribution:"
              "Each player and the dealer receive two cards."
              "Winning and Losing:"
              "Blackjack: Having 21 points with the first two cards automatically wins"
              "Going Over 21: Immediate loss."
              "Ties:"
              "The bet is typically returned in case of a tie.")



    def sortear_cartas(self, jogador):
        baralho_cartas = list(self.baralho.keys())
        contador = 0
        while contador < 2:
            for self.jogador in self.jogadores:
                self.cartas_sorteadas = random.choice(baralho_cartas)
                self.cartas_jogador.append(self.cartas_sorteadas)
                self.baralho_cartas.remove(self.cartas_sorteadas)
            contador = contador + 1


    def start_game(self):
        print("-------------------------------\nLet's start!")

        self.sortear_cartas(self.jogador1)
        self.sortear_cartas(self.jogador2)

        while True:
            print(f'Cartas {self.jogador1.nome}: {self.jogador1.cartas_jogador}'
                  f'Soma total: {self.soma}')

            print(f'Cartas {self.jogador2.nome}: {self.jogador2.cartas_jogador}'
                  f'Soma total: {self.soma}')

            acao_jogador1 = int(input(f'{self.jogador1.nome}, deseja:'
                                      f'1- Pedir cartas'
                                      f'2- Parar'))

            acao_jogador2 = int(input(f'{self.jogador2.nome}, deseja pedir cartas?:'
                                      f'1- Sim'
                                      f'2- Não'))

            match acao_jogador1:
                case 1:
                    self.sortear_cartas(self.jogador1)
                    self.verificar_vencedor()

                case 2:
                    continue
                    self.verificar_vencedor()

            match acao_jogador2:
                case 1:
                    self.sortear_cartas(self.jogador2)
                    self.verificar_vencedor()

                case 2:
                    continue
                    self.verificar_vencedor()

    def verificar_vencedor(self):
        self.soma_jogador1 = sum(self.jogador1.cartas_jogador)
        self.soma_jogador1 = sum(self.jogador2.cartas_jogador)

        if self.soma_jogador1 == 21:
            print()






