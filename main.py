from modelos.tabuleiro import Tabuleiro, TipoTabuleiro
from visoes.interface import Interface
from modelos.jogador import Jogador, JogadorComputador, JogadorHumano
from controles.jogo import Jogo


def main():
    '''t1 = Tabuleiro(dono='a', tamanho=10, tipo=TipoTabuleiro.ATAQUE)
    t2 = Tabuleiro(dono='a', tamanho=10, tipo=TipoTabuleiro.DEFESA)
    
    Interface.limpar_tela()
    Interface.mostrar_mensagem('asjdgfvalibksdlavudbsfnvi')
    Interface.mostrar_dois_tabuleiros(t1,t2)

    t1.alterar_posicao(0,4,'F')
    Interface.mostrar_dois_tabuleiros(t1,t2)

    Interface.pedir_orientacao(21)

    Interface.receber_coordenadas('>>> Almirante, informe o alvo: ')

    #Interface.receber_coordenadas(f'>>> Almirante, informe as coordenadas do {navio}: ')'''
    '''j1 = JogadorComputador('Audrei')
    j1.posicionar_frota()
    Interface.mostrar_dois_tabuleiros(j1.tab_ataque,j1.tab_defesa)'''
    jogo = Jogo()
    jogo.iniciar()
    
if __name__ == "__main__":
    main()