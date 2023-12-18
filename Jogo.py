import random
from Jogador import Jogador

class Jogo():
    def __init__(self):
        self.jogador1 = None
        self.jogador2 = None
        self.jogadores = [self.jogador1, self.jogador2]
        self.baralho = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 5  # pq o baralho tem 50 cartas
        self.num = 21

    def menu(self):
        try:
            print("------"
                  "|   Welcome to my Blackjack game!   |"
                  "------")
            print("1- Start game")
            print("2- See value of cards")
            print("3- Rules")
            print("4- Exit game")
            option = int(input("What you want to do? "))
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
        for i in range(2):
            carta = random.choice(self.baralho)  # Fixed this line
            jogador.cartas_jogador.append(carta)
            self.baralho.remove(carta)  # Fixed this line

    def somar_cartas(self, jogador):
        return sum(jogador.cartas_jogador)

    def start_game(self):
        print("Let's start!")

        try:
            self.sortear_cartas(self.jogador1)
            self.sortear_cartas(self.jogador2)

            while True:
                print("-" * 50)
                print(f'Cartas {self.jogador1.nome}: {self.jogador1.cartas_jogador}')
                print(f'Cartas {self.jogador2.nome}: {self.jogador2.cartas_jogador}')
                print("-" * 50)

                acao_jogador1 = int(input(f'{self.jogador1.nome}, deseja:'
                                          f'\n1- Pedir cartas'
                                          f'\n2- Parar'))

                print(" ")
                acao_jogador2 = int(input(f'{self.jogador2.nome} deseja pedir cartas?:'
                                          f'\n1- Pedir cartas'
                                          f'\n2- Parar'))

                if acao_jogador1 == 1:
                    self.sortear_cartas(self.jogador1)

                if acao_jogador2 == 1:
                    self.sortear_cartas(self.jogador2)

                if acao_jogador1 == 2 or acao_jogador2 == 2:
                    self.verificar_vencedor()
                    break

        except ValueError:
            print("Invalid data")
            self.start_game()

    def verificar_vencedor(self):
        soma_jogador1 = self.somar_cartas(self.jogador1)
        soma_jogador2 = self.somar_cartas(self.jogador2)

        if soma_jogador1 == self.num:
            print(f'{self.jogador1} you won!')

        if soma_jogador2 == self.num:
            print(f'{self.jogador2} you won!')

        if soma_jogador1 < self.num:
            print(f'{self.jogador1.nome} you are just with :{soma_jogador1}, play again!')
            pass

        if soma_jogador2 < self.num:
            print(f'{self.jogador2.nome} you are just with :{soma_jogador2}, play again!')
            pass

        if soma_jogador1 > self.num:
            print(f'{self.jogador1.nome} you exceeded the value!\n {self.jogador2.nome}, you won!')

        if soma_jogador2 > self.num:
            print(f'{self.jogador2.nome} you exceeded the value!\n {self.jogador1.nome}, you won!')

        else:
            pass


jogador1 = Jogador("Jogador 1", 100)
jogador2 = Jogador("Jogador 2", 100)

jogo = Jogo()
jogo.jogador1 = jogador1
jogo.jogador2 = jogador2

jogo.menu()
