from modelos.navio import criar_frota_padrao
from visoes.interface import Interface
from modelos.tabuleiro import Tabuleiro, TipoTabuleiro

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.tab_defesa = Tabuleiro(nome, 10, TipoTabuleiro.DEFESA)
        self.tab_ataque = Tabuleiro(nome, 10, TipoTabuleiro.ATAQUE)
        self.frota = criar_frota_padrao()
        self.destrocos_inimigos = 0

class JogadorHumano(Jogador):
    def __init__(self, nome):
        super().__init__(nome)
    
    def posicionar_frota(self):
        for navio in self.frota:
            while True:
                Interface.limpar_tela()

                Interface.mostrar_dois_tabuleiros(self.tab_ataque, self.tab_defesa)
                
                orientacao = Interface.pedir_orientacao(navio)
                
                coordenada, linha, coluna = Interface.receber_coordenadas(f" >>> Almirante, qual a coordenada inicial para o {navio.nome}?")
                
                sucesso = self.tab_defesa.tentar_posicionar(navio, coordenada, linha, coluna, orientacao)
                
                if sucesso:
                    Interface.mostrar_mensagem(f">>> {navio.nome} posicionado com sucesso!", velocidade=0.01)
                    break
                else:
                    Interface.mostrar_mensagem(">>> Erro: Limites excedidos ou colisão.")
                    continue

class JogadorComputador(Jogador):
    def __init__(self, nome="Computador"):
        super().__init__(nome)
        
        self.modo = 'aleatorio'
        self.primeiro_fogo = None
        self.segundo_fogo = None
        self.lados_desconhecidos = []