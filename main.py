class Jogador():
    def __init__(self, nome, fichas, idade):
        self.nome = nome
        self.fichas = fichas
        self.idade = idade

    def menu(self):
        print("Welcome to my 21 game")
        print("Let's start!")
        print("")

    def cartas(self, az, one, two, three, four, five, six, seven, eight, nine, ten, Q, J, K):
        self.az = 1
        self.two = 2
        self.three = 3
        self.four = 4
        self.five = 5
        self.six = 6
        self.seven = 7
        self.eight = 8
        self.nine = 9
        self.ten = 10
        self.Q = 10
        self.J = 10
        self.K = 10


