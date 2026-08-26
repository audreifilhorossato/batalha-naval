import os 
from modelos.jogador import Jogador, JogadorComputador, JogadorHumano
from visoes.interface import Interface
from modelos.navio import StatusNavio, Navio

class Jogo:
    def __init__(self):
        self.j1 = JogadorHumano('Audrei')
        self.j2 = JogadorComputador('AI')

    def iniciar(self):
        self.j2.posicionar_frota()
        self.j1.posicionar_frota()
        veri_fim_jogo = True
        while veri_fim_jogo:
            veri_fim_jogo = self.executar_turno()
            
    def executar_turno(self):
        
        cood, l, n = self.j1.fazer_jogada()

        self.j2.tab_defesa.alterar_posicao(l,n,'X') 
        self.j1.tab_ataque.alterar_posicao(l,n,'X')
        
        for navio in self.j2.frota:
            
            if navio.navio_alvejado(cood):
                self.j2.tab_defesa.alterar_posicao(l,n,'F')
                self.j1.tab_ataque.alterar_posicao(l,n,'F')
                
                if navio.verifica_status() == StatusNavio.AFUNDADO:
                    Interface.limpar_tela()
                    Interface.aviso_afundamento(navio.nome, inimigo=True)
                    input()
                    self.j1.tab_ataque.num_destrocos += 1
                break


        if self.j1.tab_ataque.num_destrocos  >= len(self.j2.frota):
            Interface.tela_vitoria()
            return False
        
        cood, l, n = self.j2.fazer_jogada()

        self.j1.tab_defesa.alterar_posicao(l,n,'X') 
        self.j2.tab_ataque.alterar_posicao(l,n,'X')
        
        for navio in self.j1.frota:
            
            if navio.navio_alvejado(cood):
                self.j1.tab_defesa.alterar_posicao(l,n,'F')
                self.j2.tab_ataque.alterar_posicao(l,n,'F')
                
                if navio.verifica_status() == StatusNavio.AFUNDADO:
                    Interface.limpar_tela()
                    Interface.aviso_afundamento(navio.nome, inimigo=False)
                    input()
                    self.j2.tab_ataque.num_destrocos += 1
                break


        if self.j2.tab_ataque.num_destrocos  >= len(self.j1.frota):
            Interface.tela_derrota()
            return False

        return True

    def _verificar_fim_de_jogo(self):
        return False