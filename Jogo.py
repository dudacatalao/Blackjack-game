import random
from Jogador import Jogador

class Jogo():
    def __init__(self):
        self.jogador1 = None
        self.jogador2 = None
        self.jogadores = [self.jogador1, self.jogador2]
        self.baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.num = 21
        self.diferenca_jogador1 = 0
        self.diferenca_jogador2 = 0

    def menu(self):
        try:
            print("-" * 50)
            print("1- Start game")
            print("2- See value of cards")
            print("3- Rules")
            print("4- Exit game")
            option = int(input("What you want to do? \n"))
            print("-" * 50)

            match option:
                case 1:
                    self.start_game()

                case 2:
                    print("Value of cards:")
                    print(self.get_baralho())
                    self.menu()

                case 3:
                    self.regras()

                case 4:
                    exit()
        except ValueError:
            print("-" * 50)
            print("Invalid data")
            self.menu()

    def get_baralho(self):
        return self.baralho

    def regras(self):
        print("Rules blackjack")
        print("\nObjective: Get as close as possible to 21 points without exceeding it."
              "\nCard Distribution:"
              "\nEach player and the dealer receive two cards."
              "\nWinning and Losing:"
              "\nBlackjack: Having 21 points with the first two cards automatically wins"
              "\nGoing Over 21: Immediate loss."
              "\nTies:"
              "\nThe bet is typically returned in case of a tie.")
        self.menu()

    def sortear_cartas(self, jogador):
        for i in range(1):
            carta = random.choice(self.baralho)
            jogador.cartas_jogador.append(carta)
            self.baralho.remove(carta)

    def somar_cartas(self, jogador):
        return sum(jogador.cartas_jogador)


    def dif(self, soma_jogador):
        if soma_jogador > self.num:
            return soma_jogador - self.num
        else:
            return self.num - soma_jogador

    def start_game(self):
        print("Let's start!")

        try:
            self.jogador1 = Jogador(input("What is the name of the first player?"), 100)
            self.jogador2 = Jogador(input("What is the name of the second player?"), 100)
            print("Both of you start's with 100 betting chips")

            self.sortear_cartas(self.jogador1)
            self.sortear_cartas(self.jogador2)

            while True:
                print("-" * 50)
                print(f'Cards {self.jogador1.nome}: {self.somar_cartas(self.jogador1)}')
                print(f'Cards {self.jogador2.nome}: {self.somar_cartas(self.jogador2)}')
                print("-" * 50)

                acao_jogador1 = int(input(f'{self.jogador1.nome}, you want?:'
                                          f'\n1- Ask for cards'
                                          f'\n2- Stop\n'))

                print(" ")
                acao_jogador2 = int(input(f'{self.jogador2.nome} you want?:'
                                          f'\n1- Ask for cards'
                                          f'\n2- Stop\n'))

                if acao_jogador1 == 1:
                    self.sortear_cartas(self.jogador1)

                if acao_jogador1 == 1 and acao_jogador2 == 2:
                    self.sortear_cartas(self.jogador1)

                if acao_jogador1 == 2 and acao_jogador2 == 1:
                    self.sortear_cartas(self.jogador2)

                if acao_jogador2 == 1:
                    self.sortear_cartas(self.jogador2)

                if acao_jogador1 == 2 or acao_jogador2 == 2:
                    self.verificar_vencedor()
                    break

        except ValueError:
            print("Invalid data")
            self.start_game()

    def verificar_vencedor(self):
        self.soma_jogador1 = self.somar_cartas(self.jogador1)
        self.soma_jogador2 = self.somar_cartas(self.jogador2)

        diferenca_jogador1 = self.dif(self.soma_jogador1)
        diferenca_jogador2 = self.dif(self.soma_jogador2)

        if self.soma_jogador1 == self.num:
            print(f'{self.jogador1.nome} you won!')

        elif self.soma_jogador2 == self.num:
            print(f'{self.jogador2.nome} you won!')

        elif self.soma_jogador1 > self.num and self.soma_jogador2 > self.num:
            print('It\'s a draw! Both players exceeded the target value.')

        elif diferenca_jogador1 < diferenca_jogador2:
            print(f'{self.jogador1.nome} you have :{self.soma_jogador1}, you are closer to 21,  you won!\nand {self.jogador2.nome}, you have {self.soma_jogador2}')

        elif diferenca_jogador2 < diferenca_jogador1:
            print(f'{self.jogador2.nome} you have :{self.soma_jogador2}, you are closer to 21, you won!\nand {self.jogador1.nome}, you have {self.jogador1}')

        else:
            print('It\'s a draw! Both players have the same difference from 21.')

        exit()


if __name__ == '__main__':
    print("------"
           "|   WELCOME TO MY BLACKJACK GAME!   |"
           "------")

    jogo = Jogo()
    jogo.menu()
