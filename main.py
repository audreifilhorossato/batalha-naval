from modelos.tabuleiro import Tabuleiro, TipoTabuleiro
from visoes.interface import Interface
from modelos.jogador import Jogador, JogadorComputador, JogadorHumano
from controles.jogo import Jogo


def main():
    jogo = Jogo()
    jogo.iniciar()

if __name__ == "__main__":
    main()