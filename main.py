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
            carta = random.choice(list(self.baralho.keys()))
            jogador.cartas_jogador.append(carta)
            del self.baralho[carta]

    def somar_cartas(self):



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

                if acao_jogador1 == 1 and acao_jogador2 == 1:
                    self.sortear_cartas(self.jogador1)
                    self.sortear_cartas(self.jogador2)
                    self.verificar_vencedor()

                elif acao_jogador1 == 2 or acao_jogador2 == 2:
                    self.verificar_vencedor()

                elif acao_jogador1 == 1 and acao_jogador2 == 2:
                    self.sortear_cartas(self.jogador1)
                    self.verificar_vencedor()

                elif acao_jogador1 == 2 and acao_jogador2 == 1:
                    self.sortear_cartas(self.jogador2)
                    self.verificar_vencedor()

        except TypeError:
            print("Invalid data")
            self.start_game()



    def verificar_vencedor(self):

            if self.somar_cartas1() == 21:
                print("Congratulations, you won")



                # print(f'{player.name}, your cards: {player.cards}, total: {score}')
                #
                # if score == 21:
                #     print(f'{player.name}, you won! Congrats!')
                #     self.menu()
                # elif score > 21:
                #     print(f'{player.name}, you exceeded 21. You lose!')
                #     self.menu()
                # else:
                #     continue


jogador1 = Jogador("Jogador 1", 100)
jogador2 = Jogador("Jogador 2", 100)

jogo = Jogo()
jogo.jogador1 = jogador1
jogo.jogador2 = jogador2

jogo.menu()