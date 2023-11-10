import random

class Jogador():
    def __init__(self, nome, fichas):
        self.nome = nome
        self.fichas = fichas
        self.cartas_jogador = []

class Jogo():
    def __init__(self):
        self.jogador1 = None
        self.jogador2 = None
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
        option = int(input("What you want to do? "))
        print("---------------------------------------------------------------------------------------------------------------")

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

    def sortear_cartas(self):
        for _ in range(2):
            carta = random.choice(list(self.baralho.keys()))
            self.jogador1.cartas_jogador.append(carta)
            del self.baralho[carta]

            carta = random.choice(list(self.baralho.keys()))
            self.jogador2.cartas_jogador.append(carta)
            del self.baralho[carta]

    def start_game(self):
        print("Let's start!")

        self.sortear_cartas()

        while True:
            print(f'Cartas {self.jogador1.nome}: {self.jogador1.cartas_jogador}')

            print(f'Cartas {self.jogador2.nome}: {self.jogador2.cartas_jogador}')

            acao_jogador1 = int(input(f'{self.jogador1.nome}, deseja:'
                                      f'1- Pedir cartas'
                                      f'2- Parar'))

            acao_jogador2 = int(input(f'{self.jogador2.nome} deseja pedir cartas?:'
                                      f'\n1- Sim'
                                      f'\n2- Não'))

            match acao_jogador1:
                case 1:
                    self.sortear_cartas(self.jogador1)
                    self.verificar_vencedor()

                case 2:
                    self.verificar_vencedor()

            match acao_jogador2:
                case 1:
                    self.sortear_cartas(self.jogador2)
                    self.verificar_vencedor()

                case 2:
                    self.verificar_vencedor()

    def verificar_vencedor(self):
        soma_jogador1 = self.soma_jogador1 = sum(self.cartas_jogador)
        soma_jogador2 = self.soma_jogador2 = sum(self.cartas_jogador)

        if soma_jogador1 == 21:
            print(f'{self.jogador1.nome}, you won! Congrats!')
            self.menu()

        elif soma_jogador2 == 21:
            print(f'{self.jogador2.nome}, you won! Congrats!')
            self.menu()

        elif soma_jogador1 > 21 and soma_jogador2 > 21:
            print("You tied")
            self.menu()

        elif soma_jogador1 > 21:
            print(f'{self.jogador1.nome}, você ultrapassou 21. Você perdeu!')
            self.menu()

        elif soma_jogador2 > 21:
            print(f'{self.jogador2.nome}, você ultrapassou 21. Você perdeu!')
            self.menu()

        elif 21 >= soma_jogador1 > soma_jogador2:
            print(f'{self.jogador1.nome}, you won! Congrats!')
            self.menu()

        elif 21 >= soma_jogador2 > soma_jogador1:
            print(f'{self.jogador2.nome}, you won! Congrats!')
            self.menu()

        elif soma_jogador1 == soma_jogador2:
            print("You tied!")
            self.menu()

jogador1 = Jogador("Jogador 1", 100)
jogador2 = Jogador("Jogador 2", 100)

jogo = Jogo()
jogo.jogador1 = jogador1
jogo.jogador2 = jogador2

jogo.menu()