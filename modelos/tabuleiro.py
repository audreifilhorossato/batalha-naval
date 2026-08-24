from enum import Enum


class TipoTabuleiro(Enum):
    DEFESA = 1
    ATAQUE = 2

class Tabuleiro:
    def __init__(self,dono,tamanho,tipo):
        self.dono = dono
        self.tamanho = tamanho
        self.tipo = tipo
        self.num_destrocos = 0
        self.dados = [["~" for _ in range(self.tamanho)] for _ in range(self.tamanho)]

    def alterar_posicao(self, linha, coluna, alteração):
        self.dados[linha][coluna] = alteração

    def tentar_posicionar(self, navio, coordenada, linha, coluna, orientacao):

        direcoes = {
            '1': (0, -1), # Horizontal Esquerda
            '2': (0, 1),  # Horizontal Direita
            '3': (1, 0),  # Vertical Baixo
            '4': (-1, 0)  # Vertical Cima
        }
        
        d_linha, d_coluna = direcoes[orientacao]
        posicoes_temporarias = []

        for j in range(navio.tamanho):
            nova_linha = linha + (d_linha * j)
            nova_coluna = coluna + (d_coluna * j)

            if nova_linha < 0 or nova_linha > self.tamanho - 1 or nova_coluna < 0 or nova_coluna > self.tamanho - 1:
                return False
           
            if self.dados[nova_linha][nova_coluna] != '~':
                return False
                
            posicoes_temporarias.append((nova_linha, nova_coluna))

        for l, c in posicoes_temporarias:
            self.prenchimento[l][c] = 'N'
            navio.posicao.append(coordenada)

        return True