class Jogador():
    def __init__(self, nome, fichas):
        self.__nome = nome
        self.__fichas = fichas
        self.__cartas_jogador = []
        self.__fichas_apostadas = []

    #getters
    @property
    def fichas(self):
        return self.__fichas

    @property
    def nome(self):
        return self.__nome

    @property
    def cartas_jogador(self):
        return self.__cartas_jogador

    @property
    def fichas_apostadas(self):
        return self.__fichas_apostadas

    #setters
    @fichas.setter
    def fichas(self, novo_valor):
        self.__fichas = novo_valor

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @cartas_jogador.setter
    def cartas_jogador(self, nova_carta):
        self.__cartas_jogador = nova_carta

    @fichas_apostadas.setter
    def fichas_apostadas(self, novas_fichas):
        self.__fichas_apostadas = novas_fichas
