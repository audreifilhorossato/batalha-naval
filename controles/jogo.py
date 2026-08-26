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
        while not self._verificar_fim_de_jogo():
            self.executar_turno()
        print('FIM DE JOGO')
        input()
            
    def executar_turno(self):
        
        cood, l, n = self.j1.fazer_jogada()

        self.j2.tab_defesa.alterar_posicao(l,n,'X') 
        self.j1.tab_ataque.alterar_posicao(l,n,'X')
        
        for navio in self.j2.frota:
            
            if navio.navio_alvejado(cood):
                self.j2.tab_defesa.alterar_posicao(l,n,'F')
                self.j1.tab_ataque.alterar_posicao(l,n,'F')
                
                if navio.verifica_status() == StatusNavio.AFUNDADO:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'O {navio.nome} inimigo foi afundado!')
                    input()
                    self.j1.tab_ataque.num_destrocos += 1
                break


        if self.j1.tab_ataque.num_destrocos  >= len(self.j2.frota):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("GANHOU")
            input()
        
        cood, l, n = self.j2.fazer_jogada()

        self.j1.tab_defesa.alterar_posicao(l,n,'X') 
        self.j2.tab_ataque.alterar_posicao(l,n,'X')
        
        for navio in self.j1.frota:
            
            if navio.navio_alvejado(cood):
                self.j1.tab_defesa.alterar_posicao(l,n,'F')
                self.j2.tab_ataque.alterar_posicao(l,n,'F')
                
                if navio.verifica_status() == StatusNavio.AFUNDADO:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(f'O seu {navio.nome} foi afundado!')
                    input()
                    self.j2.tab_ataque.num_destrocos += 1
                break


        if self.j2.tab_ataque.num_destrocos  >= len(self.j1.frota):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("PERDEU")
            input()

    def _verificar_fim_de_jogo(self):
        return False