class Jogador():
    def __init__(self, nome, fichas):
        self.nome = nome
        self.fichas = fichas
        self.cartas_jogador = []

    @property
    def fichas(self):
        return self._fichas

    @fichas.setter
    def fichas(self, novo_valor):
        self._fichas = novo_valor
