class Jogador():
    def __init__(self, nome, fichas):
        self.nome = nome
        self.fichas = fichas
        self.cartas_jogador = []
        self.fichas_apostadas = []

    # Getters
    # @property
    # def fichas(self):
    #     return self._fichas
    #
    # @property
    # def nome(self):
    #     return self._nome
    #
    # @property
    # def cartas_jogador(self):
    #     return self.cartas_jogador
    #
    # @property
    # def fichas_apostadas(self):
    #     return self._fichas_apostadas

    # Setters
    # @fichas.setter
    # def fichas(self, novo_valor):
    #     self._fichas = novo_valor
    #
    # @nome.setter
    # def nome(self, novo_nome):
    #     self._nome = novo_nome
    #
    # @cartas_jogador.setter
    # def cartas_jogador(self, nova_carta):
    #     self.cartas_jogador = nova_carta
    #
    # @fichas_apostadas.setter
    # def fichas_apostadas(self, novas_fichas):
    #     self._fichas_apostadas = novas_fichas
