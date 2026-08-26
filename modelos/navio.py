from enum import Enum

class StatusNavio(Enum):
    INTEIRO = 1
    AVARIADO = 2
    AFUNDADO = 3

class Navio:
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho
        self.status = StatusNavio.INTEIRO  
        self.coordenadas = []
        self.coordenadas_alvejadas = []

    def verifica_status(self):
        if self.status != StatusNavio.AFUNDADO:
            if len(self.coordenadas_alvejadas) == len(self.coordenadas):
                self.status = StatusNavio.AFUNDADO
        return self.status

    def navio_alvejado(self, coordenadas):
        if coordenadas in self.coordenadas:
            self.coordenadas_alvejadas.append(coordenadas)
            return True
        else:
            return False

def criar_frota_padrao():
    '''return [
        Navio("Porta-Aviões", 5),
        Navio("Encouraçado", 4),
        Navio("Cruzador 1", 3),
        Navio("Cruzador 2", 3),
        Navio("Submarino 1", 2)
    ]'''
    return [
        Navio("Porta-Aviões", 5),
        Navio("Encouraçado", 4)
    ]