from modelos.navio import criar_frota_padrao
from visoes.interface import Interface
from modelos.tabuleiro import Tabuleiro, TipoTabuleiro
import random

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

    def fazer_jogada(self):
        Interface.limpar_tela()
        Interface.mostrar_dois_tabuleiros(self.tab_ataque, self.tab_defesa)

        coordenada, linha, coluna = Interface.receber_coordenadas(f" >>> Almirante, qual a coordenada para travar o alvo? ")
        return coordenada, linha, coluna


class JogadorComputador(Jogador):
    def __init__(self, nome="Computador"):
        super().__init__(nome)
        
        self.modo = 'aleatorio'
        self.primeiro_fogo = ['l','n']
        self.segundo_fogo = ['l','n']
        self.lados_desconhecidos = []
        self.lados_desconhecidos2 = []
        self.extremidades = []
        self.terceiro_fogo = ['l','n']
        self.ulttamfrota = self.tab_ataque.num_destrocos
        self.cont = 0
    
    def posicionar_frota(self):
        for navio in self.frota:
            while True:
                
                orientacao = str(random.randint(1, 4))
                
                linha = int(random.randint(0, 9))
                coluna = int(random.randint(0, 9))
                coordenada = str(chr(linha + 65)) + str(coluna)
                
                sucesso = self.tab_defesa.tentar_posicionar(navio, coordenada, linha, coluna, orientacao)
                
                if sucesso:
                    
                    break
                else:
                    
                    continue
    
    def fazer_jogada(self):
        while True:
            match self.modo:
                case 'aleatorio':
                    if self.primeiro_fogo != ['l','n']:
                        if self.tab_ataque.dados[self.primeiro_fogo[0]][self.primeiro_fogo[1]] == 'F':
                            self.modo = 'verificarlaterais'
                            continue
                    l = random.randint(0, self.tab_ataque.tamanho -1)
                    n = random.randint(0, self.tab_ataque.tamanho -1)
                    while self.tab_ataque.dados[l][n] != '~':
                        l = random.randint(0, self.tab_ataque.tamanho -1)
                        n = random.randint(0, self.tab_ataque.tamanho -1)
                    self.primeiro_fogo[0] = l
                    self.primeiro_fogo[1] = n
                    cood = str(chr(l + 65) + str(n))
                    return cood, l, n
                case 'verificarlaterais':
                    if self.segundo_fogo != ['l','n']:
                        if self.tab_ataque.dados[self.segundo_fogo[0]][self.segundo_fogo[1]] == 'F':
                            self.modo = 'afundar'
                            #input('PAUSEEEE')
                            continue
                    self.lados_desconhecidos = []
                    try:
                        if self.tab_ataque.dados[self.primeiro_fogo[0] + 1][self.primeiro_fogo[1]] == '~':
                            self.lados_desconhecidos.append([self.primeiro_fogo[0] + 1, self.primeiro_fogo[1]])
                    except:
                        pass

                    try:
                        if self.tab_ataque.dados[self.primeiro_fogo[0] - 1][self.primeiro_fogo[1]] == '~':
                            if self.primeiro_fogo[0] - 1 >= 0:
                                self.lados_desconhecidos.append([self.primeiro_fogo[0] - 1, self.primeiro_fogo[1]])
                    except:
                        pass

                    try:
                        if self.tab_ataque.dados[self.primeiro_fogo[0]][self.primeiro_fogo[1] + 1] == '~':
                            self.lados_desconhecidos.append([self.primeiro_fogo[0], self.primeiro_fogo[1] + 1])
                    except:
                        pass

                    try:
                        if self.tab_ataque.dados[self.primeiro_fogo[0]][self.primeiro_fogo[1] - 1] == '~':
                            if self.primeiro_fogo[1] - 1 >= 0:
                                self.lados_desconhecidos.append([self.primeiro_fogo[0], self.primeiro_fogo[1] - 1])
                    except:
                        pass
                    if len(self.lados_desconhecidos) == 0:
                        self.ulttamfrota = self.tab_ataque.num_destrocos
                        '''print(self.primeiro_fogo)
                        print(self.segundo_fogo)
                        print(self.terceiro_fogo)
                        print(self.lados_desconhecidos2)
                        input()'''
                        self.modo = 'aleatorio'
                        self.primeiro_fogo = ['l','n']
                        self.segundo_fogo = ['l','n']
                        self.lados_desconhecidos = []
                        self.lados_desconhecidos2 = []
                        self.terceiro_fogo = ['l','n']
                        self.cont = 0
                        continue

                    tiro = random.randint(0, len(self.lados_desconhecidos) - 1)
                    l = self.lados_desconhecidos[tiro][0]
                    n = self.lados_desconhecidos[tiro][1]
                    self.segundo_fogo[0] = l
                    self.segundo_fogo[1] = n

                    cood = str(chr(l + 65) + str(n))
                    return cood, l, n

                case 'afundar':
                    if  self.ulttamfrota != self.tab_ataque.num_destrocos:
                        self.ulttamfrota = self.tab_ataque.num_destrocos
                        self.modo = 'aleatorio'
                        self.primeiro_fogo = ['l','n']
                        self.segundo_fogo = ['l','n']
                        self.lados_desconhecidos = []
                        self.lados_desconhecidos2 = []
                        self.terceiro_fogo = ['l','n']
                        self.cont = 0
                        continue

                    if self.primeiro_fogo[0] == self.segundo_fogo[0]:
                        print('Horizontal')
                        if self.lados_desconhecidos2 == []:
                            self.extremidades = [['l','n'],['l','n']]
                            try:
                                c = 0 
                                while self.tab_ataque.dados[self.primeiro_fogo[0]][self.primeiro_fogo[1] + c] == 'F':
                                    self.extremidades[0][0] = self.primeiro_fogo[0]
                                    self.extremidades[0][1] = self.primeiro_fogo[1] + c
                                    c += 1
                            except:
                                pass

                            try:
                                c = 0 
                                while self.tab_ataque.dados[self.primeiro_fogo[0]][self.primeiro_fogo[1] - c] == 'F':
                                    if self.primeiro_fogo[1] - c >= 0:
                                        self.extremidades[1][0] = self.primeiro_fogo[0]
                                        self.extremidades[1][1] = self.primeiro_fogo[1] - c
                                    c += 1
                            except:
                                pass
                            
                            #input(self.extremidades)

                            try:
                                if self.tab_ataque.dados[self.extremidades[0][0]][self.extremidades[0][1] + 1] == '~':
                                    self.lados_desconhecidos2.append([self.extremidades[0][0], self.extremidades[0][1] + 1])
                            except:
                                pass

                            try:
                                if self.tab_ataque.dados[self.extremidades[1][0]][self.extremidades[1][1] - 1] == '~':
                                    if self.extremidades[1][1] - 1 >= 0:
                                        self.lados_desconhecidos2.append([self.extremidades[1][0], self.extremidades[1][1] - 1])
                            except:
                                pass

                            #input(self.lados_desconhecidos2)

                        if len(self.lados_desconhecidos2) == 0:
                            self.ulttamfrota = self.tab_ataque.num_destrocos
                            '''print(self.primeiro_fogo)
                            print(self.segundo_fogo)
                            print(self.terceiro_fogo)
                            print(self.lados_desconhecidos2)
                            input()'''
                            self.modo = 'aleatorio'
                            self.primeiro_fogo = ['l','n']
                            self.segundo_fogo = ['l','n']
                            self.lados_desconhecidos = []
                            self.lados_desconhecidos2 = []
                            self.terceiro_fogo = ['l','n']
                            self.cont = 0
                            continue
                        tiro = random.randint(0, len(self.lados_desconhecidos2) - 1)
                        l = self.lados_desconhecidos2[tiro][0]
                        n = self.lados_desconhecidos2[tiro][1]
                        self.lados_desconhecidos2.pop(tiro)
                        cood = str(chr(l + 65) + str(n))
                        return cood, l, n


                    else:
                        print('Vertical')
                        if self.lados_desconhecidos2 == []:
                            self.extremidades = [['l','n'],['l','n']]
                            try:
                                c = 0 
                                while self.tab_ataque.dados[self.primeiro_fogo[0] + c][self.primeiro_fogo[1]] == 'F':
                                    self.extremidades[0][0] = self.primeiro_fogo[0] + c
                                    self.extremidades[0][1] = self.primeiro_fogo[1] 
                                    c += 1
                            except:
                                pass

                            try:
                                c = 0 
                                while self.tab_ataque.dados[self.primeiro_fogo[0] - c][self.primeiro_fogo[1]] == 'F':
                                    if self.primeiro_fogo[0] - c >= 0:
                                        self.extremidades[1][0] = self.primeiro_fogo[0] - c
                                        self.extremidades[1][1] = self.primeiro_fogo[1]
                                    c += 1
                            except:
                                pass
                            
                            #input(self.extremidades)

                            try:
                                if self.tab_ataque.dados[self.extremidades[0][0] + 1][self.extremidades[0][1]] == '~':
                                    self.lados_desconhecidos2.append([self.extremidades[0][0] + 1 , self.extremidades[0][1]])
                            except:
                                pass

                            try:
                                if self.tab_ataque.dados[self.extremidades[1][0] - 1][self.extremidades[1][1]] == '~':
                                    if self.extremidades[1][0] - 1 >= 0:
                                        self.lados_desconhecidos2.append([self.extremidades[1][0] - 1, self.extremidades[1][1]])
                            except:
                                pass

                            #input(self.lados_desconhecidos2)

                        if len(self.lados_desconhecidos2) == 0:
                            self.ulttamfrota = self.tab_ataque.num_destrocos
                            '''print(self.primeiro_fogo)
                            print(self.segundo_fogo)
                            print(self.terceiro_fogo)
                            print(self.lados_desconhecidos2)
                            input()'''
                            self.modo = 'aleatorio'
                            self.primeiro_fogo = ['l','n']
                            self.segundo_fogo = ['l','n']
                            self.lados_desconhecidos = []
                            self.lados_desconhecidos2 = []
                            self.terceiro_fogo = ['l','n']
                            self.cont = 0
                            continue
                        tiro = random.randint(0, len(self.lados_desconhecidos2) - 1)
                        l = self.lados_desconhecidos2[tiro][0]
                        n = self.lados_desconhecidos2[tiro][1]
                        self.lados_desconhecidos2.pop(tiro)
                        cood = str(chr(l + 65) + str(n))
                        return cood, l, n


    