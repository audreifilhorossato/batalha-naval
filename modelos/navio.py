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
        if (coordenadas in self.coordenadas) and (coordenadas not in self.coordenadas_alvejadas):
            self.coordenadas_alvejadas.append(coordenadas)
            return True
        else:
            return False

def criar_frota_padrao(opcao):
    match opcao:
        case 1:
            return [ #Frota Classica
                Navio("Porta-Aviões", 5),
                Navio("Encouraçado", 4),
                Navio("Cruzador", 3),
                Navio("Destroyer", 3),
                Navio("Submarino", 2)
            ]
        case 2:
            return [ #Frota Pesada
                Navio("Porta-Aviões 1", 5),
                Navio("Porta-Helicopteros", 5),
                Navio("Encouraçado", 4),
                Navio("Fragata", 3),
            ]
        case 3:
            return [ #Frota Furtiva
                Navio("Encouraçado", 4),
                Navio("Cruzador", 3),
                Navio("Destroyer", 3),
                Navio("Fragata", 3),
                Navio("Corveta", 2),
                Navio("Submarino", 2)
            ]