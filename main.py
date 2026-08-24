from modelos.tabuleiro import Tabuleiro, TipoTabuleiro
from visoes.interface import Interface
from modelos.jogador import Jogador, JogadorComputador, JogadorHumano

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
    j1 = JogadorHumano('Audrei')
    j1.posicionar_frota()
    
if __name__ == "__main__":
    main()