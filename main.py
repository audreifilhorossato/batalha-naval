from modelos.tabuleiro import Tabuleiro, TipoTabuleiro
from visoes.interface import Interface
from modelos.jogador import Jogador, JogadorComputador, JogadorHumano
from controles.jogo import Jogo

def main():
    while True:
        Interface.limpar_tela()
        opcao = Interface.menu_principal()
        match opcao:
            case 1:
                jogo = Jogo()
                jogo.iniciar()
                continue
            case 2:
                Interface.mostrar_mensagem("Desligando sistemas. Até a próxima, Almirante!")
                break

if __name__ == "__main__":
    main()