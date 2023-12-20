import random
from Jogador import Jogador

class Jogo():
    def __init__(self):
        self.__jogador1 = None
        self.__jogador2 = None
        self.__jogadores = [self.__jogador1, self.__jogador2]
        self.__baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.__num = 21
        self.__diferenca_jogador1 = 0
        self.__diferenca_jogador2 = 0
        self.__winner = None
        self.__fichas_apostadas1 = []
        self.__fichas_apostadas2 = []

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

    @property
    def get_jogadores(self):
        return self.__jogadores

    def get_baralho(self):
        return self.__baralho

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
            carta = random.choice(self.__baralho)
            jogador.cartas_jogador.append(carta)
            self.__baralho.remove(carta)

    def somar_cartas(self, jogador):
        return sum(jogador.cartas_jogador)

    def dif(self, soma_jogador):
        if soma_jogador > self.__num:
            return soma_jogador - self.__num
        else:
            return self.__num - soma_jogador

    def aposta(self):
        if self.__winner == self.__jogador1:
            self.__jogador1.fichas += sum(self.__fichas_apostadas2)
            self.__fichas_apostadas2.clear()
        elif self.__winner == self.__jogador2:
            self.__jogador2.fichas += sum(self.__fichas_apostadas1)
            self.__fichas_apostadas1.clear()

    def start_game(self):
        print("Let's start!")

        try:
            self.__jogador1 = Jogador(input("What is the name of the first player?"), 100)
            self.__jogador2 = Jogador(input("What is the name of the second player?"), 100)
            print("-" * 50)
            print("Both of you start's with 100 betting chips")
            aposta_jogador1 = float(input(f'{self.__jogador1.nome} do you want to bet how many chips? R$'))
            aposta_jogador2 = float(input(f'{self.__jogador2.nome} do you want to bet how many chips? R$'))
            self.__fichas_apostadas1.append(aposta_jogador1)
            self.__fichas_apostadas2.append(aposta_jogador2)

            self.sortear_cartas(self.__jogador1)
            self.sortear_cartas(self.__jogador2)

            while True:
                print("-" * 50)
                print(f'Cards {self.__jogador1.nome}: {self.somar_cartas(self.__jogador1)}')
                print(f'Cards {self.__jogador2.nome}: {self.somar_cartas(self.__jogador2)}')
                print("-" * 50)

                acao_jogador1 = int(input(f'{self.__jogador1.nome}, you want?:'
                                          f'\n1- Ask for cards'
                                          f'\n2- Stop\n'))

                print(" ")
                acao_jogador2 = int(input(f'{self.__jogador2.nome} you want?:'
                                          f'\n1- Ask for cards'
                                          f'\n2- Stop\n'))

                if acao_jogador1 == 1:
                    self.sortear_cartas(self.__jogador1)

                if acao_jogador1 == 1 and acao_jogador2 == 2:
                    self.sortear_cartas(self.__jogador1)

                if acao_jogador1 == 2 and acao_jogador2 == 1:
                    self.sortear_cartas(self.__jogador2)

                if acao_jogador2 == 1:
                    self.sortear_cartas(self.__jogador2)

                if acao_jogador1 == 2 or acao_jogador2 == 2:
                    self.verificar_vencedor()
                    break

        except ValueError:
            print("Invalid data")
            self.start_game()

    def verificar_vencedor(self):
        self.soma_jogador1 = self.somar_cartas(self.__jogador1)
        self.soma_jogador2 = self.somar_cartas(self.__jogador2)

        diferenca_jogador1 = self.dif(self.soma_jogador1)
        diferenca_jogador2 = self.dif(self.soma_jogador2)

        if self.soma_jogador1 == self.__num:
            print(f'{self.__jogador1.nome} you won!')
            self.__winner = self.__jogador1
            self.aposta()
            print(f'Now {self.__winner.nome} has R${self.__jogador1.fichas} betting chips')

        elif self.soma_jogador2 == self.__num:
            print("-" * 50)
            print(f'{self.__jogador2.nome} you won!')
            self.__winner = self.__jogador2
            self.aposta()
            print(f'Now {self.__winner.nome} has R${self.__jogador2.fichas} betting chips')

        elif self.soma_jogador1 > self.__num and self.soma_jogador2 > self.__num:
            print("-" * 50)
            print(
                f'It\'s a draw! Both players exceeded the target value.\n{self.__jogador1.nome}:{self.soma_jogador1}\n{self.__jogador2.nome}:{self.soma_jogador2}')

        elif diferenca_jogador1 < diferenca_jogador2:
            print("-" * 50)
            print(
                f'{self.__jogador1.nome} you has :{self.soma_jogador1}, you are closer to 21,  you won!\nand {self.__jogador2.nome}, you have {self.soma_jogador2} :(')
            self.__winner = self.__jogador1
            self.aposta()
            print(f'Now {self.__winner.nome} has R${self.__jogador1.fichas} betting chips')

        elif diferenca_jogador2 < diferenca_jogador1:
            print("-" * 50)
            print(
                f'{self.__jogador2.nome} you has :{self.soma_jogador2}, you are closer to 21, you won!\nand {self.__jogador1.nome}, you have {self.soma_jogador1} :(')
            self.__winner = self.__jogador2
            self.aposta()
            print(f'Now {self.__winner.nome} has R${self.__jogador2.fichas} betting chips')

        else:
            print("-" * 50)
            print(
                f'It\'s a draw! Both players have the same difference from 21.\n{self.__jogador1.nome}:{self.soma_jogador1}\n{self.__jogador2.nome}:{self.soma_jogador2}')


if __name__ == '__main__':
    print("------"
           "|   WELCOME TO MY BLACKJACK GAME!   |"
           "------")

    jogo = Jogo()
    jogo.menu()
