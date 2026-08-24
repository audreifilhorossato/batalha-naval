import os
import random
os.system('color & cls' if os.name == 'nt' else 'clear')
linhas_validas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
colunas_validas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

class navio():
    def __init__(self,nome,tamanho):
        self.nome = nome
        self.tamanho = tamanho
        self.status = 'VIVO'
        self.posicao = []
        self.alvejado = []

    def navio_alvejado(self, coordenadas):
        if coordenadas in self.posicao:
            self.alvejado.append(coordenadas)
            return True
        else:
            return False

    def verifica_status(self):
        if self.status == 'MORTO':
            return 'JA_MORTO'

        if len(self.alvejado) == self.tamanho:
            self.status = 'MORTO'
        return self.status
        
class tabuleiro():
    def __init__(self,dono,tamanho,tipo):
        self.dono = dono
        self.tamanho = tamanho
        self.tipo = tipo
        self.num_destrocos = 0
        self.prenchimento = [["~" for _ in range(self.tamanho)] for _ in range(self.tamanho)]

    def colorir(self, simbolo):

        cores = {
        '~': '\033[34m~\033[0m', # Azul
        'N': '\033[32mN\033[0m', # Verde
        'F': '\033[1;31mF\033[0m', # Vermelho (Negrito)
        'X': '\033[90mX\033[0m' # Cinza
        }  

        return cores.get(simbolo, simbolo)

    def mostrar_tabuleiro(self, combate):
        print("---------------- QUADRANTE INIMIGO ----------------   |   ----------------- QUADRANTE AMIGO -----------------")
        print('    ', end='')
        for i in range(self.tamanho):
            print(i , end='    ')

        print('|        ', end='')
        for i in range(self.tamanho):
            print(i , end='    ')

        print('\n                                                      |')
        for i in range(self.tamanho):
            for j in range(combate.tamanho):
                print(f'{chr(97 +i)}  ' if j == 0 else '', combate.colorir(combate.prenchimento[i][j]), end='   ')
            print(' |    ', end='')
            for j in range(self.tamanho):
                print(f'{chr(97 +i)}  ' if j == 0 else '', self.colorir(self.prenchimento[i][j]), end='   ')
            print('\n                                                      |')
   
def menu():
    opcao = ''
    while opcao not in ('1', '2'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Escolha uma opcao:')
        print('1. Novo Jogo')
        print('2. Sair')
        opcao = input()
    return opcao

def entrada_posicao(tabuleiro, cabecalho, combate):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        tabuleiro.mostrar_tabuleiro(combate=combate)
        escolha =  input(f'Escolha uma posicao para {cabecalho}').strip().upper()
        #escolha = 'A2'
        if len(escolha) < 2:
            print('Formato invalido!')
            input("Pressione Enter para continuar...")
            continue
        letra = escolha[0]

        try:
            numero = int(escolha[1])
        except:
            print('Formato invalido!')
            input("Pressione Enter para continuar...")
            continue

        if (letra not in linhas_validas) or (numero not in colunas_validas):
            print('Formato invalido!')
            input("Pressione Enter para continuar...")
            continue
        else:
            print(f'Alvo travado em "{escolha}"')
            
            #input("Pressione Enter para continuar...")
            return letra, numero

def escolha_frota():
    
    porta_avioes = navio("Porta-Aviões", 5)
    encouracado = navio("Encouraçado", 4)
    cruzador1 = navio("Cruzador 1", 3)
    cruzador2 = navio("Cruzador 2", 3)
    submarino1 = navio("Submarino 1", 2)
    submarino2 = navio("Submarino 2", 2)

    minha_frota = [porta_avioes, encouracado, cruzador1, cruzador2, submarino1, submarino2]
    #minha_frota = [porta_avioes]

    return minha_frota

def posicionamento(frota,tabuleiro, combate):
    for i in range(len(frota)):
        navio = frota[i]
        opcao = ''
        while opcao not in ('1', '2', '3', '4'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'Escolha a orientação do navio {navio.nome}:')
            print('1. HORIZONTAL olhando para DIREITA')
            print('2. HORIZONTAL olhando para ESQUERDA')
            print('3. VERTICAL olhando para CIMA')
            print('4. VERTICAL olhando para BAIXO')
            opcao = input()
        match opcao:
            case '1':
                while True:
                    letra, numero = entrada_posicao(tabuleiro, f'posicionar {navio.nome}: ', combate)
                    letra = int(ord(letra.lower())) - 97
                    if (numero - navio.tamanho < -1): 
                        print("Impossivel posicinar apartir dessa posicao")
                        input("Pressione Enter para continuar...")
                        continue
                    
                    posicao = False
                    for j in range(navio.tamanho):
                        if tabuleiro.prenchimento[letra][numero - j] != '~':
                            posicao = True
                            break

                    if posicao == True:
                        print("Impossivel posicinar apartir dessa posicao")
                        input("Pressione Enter para continuar...")
                        continue
                    break
                for j in range(navio.tamanho):
                    tabuleiro.prenchimento[letra][numero - j] = 'N'
                    navio.posicao.append(chr(letra + 97).upper()+str(numero - j))

            case '2':
                while True:
                    letra, numero = entrada_posicao(tabuleiro, f'POSICIONANDO O {navio.nome} NO TABULEIRO!!!', combate)
                    letra = int(ord(letra.lower())) - 97
                    if (numero + navio.tamanho > 10): 
                        print("Impossivel posicinar apartir dessa posicao")
                        input("Pressione Enter para continuar...")
                        continue

                    posicao = False
                    for j in range(navio.tamanho):
                        if tabuleiro.prenchimento[letra][numero + j] != '~':
                            posicao = True
                            break

                    if posicao == True:
                        print("Impossivel posicinar apartir dessa posicao")
                        input("Pressione Enter para continuar...")
                        continue
                    break
                for j in range(navio.tamanho):
                    tabuleiro.prenchimento[letra][numero + j] = 'N'
                    navio.posicao.append(chr(letra + 97).upper()+str(numero + j))
            case '3':
                while True:
                    letra, numero = entrada_posicao(tabuleiro, f'POSICIONANDO O {navio.nome} NO TABULEIRO!!!', combate)
                    letra = int(ord(letra.lower())) - 97
                    if (letra + navio.tamanho > 10): 
                        print("Impossivel posicinar apartir dessa posicao")
                        input("Pressione Enter para continuar...")
                        continue

                    posicao = False
                    for j in range(navio.tamanho):
                        if tabuleiro.prenchimento[letra + j][numero] != '~':
                            posicao = True
                            break

                    if posicao == True:
                        print("Impossivel posicinar apartir dessa posicao")
                        input("Pressione Enter para continuar...")
                        continue
                    break
                for j in range(navio.tamanho):
                    tabuleiro.prenchimento[letra + j][numero] = 'N'
                    navio.posicao.append(chr(letra + 97 + j).upper()+str(numero))
            case '4':
                while True:
                    letra, numero = entrada_posicao(tabuleiro, f'POSICIONANDO O {navio.nome} NO TABULEIRO!!!', combate)
                    letra = int(ord(letra.lower())) - 97
            
                    if (letra - navio.tamanho < -1): 
                        print("Impossivel posicinar apartir dessa posicao")
                        input("Pressione Enter para continuar...")
                        continue

                    posicao = False
                    for j in range(navio.tamanho):
                        if tabuleiro.prenchimento[letra - j][numero] != '~':
                            posicao = True
                            break

                    if posicao == True:
                        print("Impossivel posicinar apartir dessa posicao")
                        input("Pressione Enter para continuar...")
                        continue
                    break
                for j in range(navio.tamanho):
                    tabuleiro.prenchimento[letra - j][numero] = 'N'
                    navio.posicao.append(chr(letra + 97 - j).upper()+str(numero))

def posicionamentoia(frota,tabuleiro):
    for i in range(len(frota)):
        navio = frota[i]
        opcao = str(random.randint(1, 4))
        match opcao:
            case '1':
                while True:
                    numero = random.randint(0, tabuleiro.tamanho -1)
                    letra = random.randint(0, tabuleiro.tamanho -1)
                    if (numero - navio.tamanho < -1): 
                        continue
                    
                    posicao = False
                    for j in range(navio.tamanho):
                        if tabuleiro.prenchimento[letra][numero - j] != '~':
                            posicao = True
                            break

                    if posicao == True:
                        continue
                    break
                for j in range(navio.tamanho):
                    tabuleiro.prenchimento[letra][numero - j] = 'N'
                    navio.posicao.append(chr(letra + 97).upper()+str(numero - j))

            case '2':
                while True:
                    numero = random.randint(0, tabuleiro.tamanho -1)
                    letra = random.randint(0, tabuleiro.tamanho -1)
                    if (numero + navio.tamanho > 10): 
                        continue

                    posicao = False
                    for j in range(navio.tamanho):
                        if tabuleiro.prenchimento[letra][numero + j] != '~':
                            posicao = True
                            break

                    if posicao == True:
                        continue
                    break
                for j in range(navio.tamanho):
                    tabuleiro.prenchimento[letra][numero + j] = 'N'
                    navio.posicao.append(chr(letra + 97).upper()+str(numero + j))
            case '3':
                while True:
                    numero = random.randint(0, tabuleiro.tamanho -1)
                    letra = random.randint(0, tabuleiro.tamanho -1)
                    if (letra + navio.tamanho > 10): 
                        continue

                    posicao = False
                    for j in range(navio.tamanho):
                        if tabuleiro.prenchimento[letra + j][numero] != '~':
                            posicao = True
                            break

                    if posicao == True:
                        continue
                    break
                for j in range(navio.tamanho):
                    tabuleiro.prenchimento[letra + j][numero] = 'N'
                    navio.posicao.append(chr(letra + 97 + j).upper()+str(numero))
            case '4':
                while True:
                    numero = random.randint(0, tabuleiro.tamanho -1)
                    letra = random.randint(0, tabuleiro.tamanho -1)
            
                    if (letra - navio.tamanho < -1): 
                        continue

                    posicao = False
                    for j in range(navio.tamanho):
                        if tabuleiro.prenchimento[letra - j][numero] != '~':
                            posicao = True
                            break

                    if posicao == True:
                        continue
                    break
                for j in range(navio.tamanho):
                    tabuleiro.prenchimento[letra - j][numero] = 'N'
                    navio.posicao.append(chr(letra + 97 - j).upper()+str(numero))

def e(tabuleiro):
    if not hasattr(e, 'modo'):
        e.modo = 'aleatorio'
        e.primeirofogo = ['l','n']
        e.segundofogo = ['l','n']
        e.ladosdesconhecidos = []
        e.ladosdesconhecidos2 = []
        e.extremidades = []
        e.terceirofogo = ['l','n']
        e.ulttamfrota = tabuleiro.num_destrocos
        e.cont = 0
    while True:
        match e.modo:
            case 'aleatorio':
                if e.primeirofogo != ['l','n']:
                    if tabuleiro.prenchimento[e.primeirofogo[0]][e.primeirofogo[1]] == 'F':
                        e.modo = 'verificarlaterais'
                        continue
                l = random.randint(0, tabuleiro.tamanho -1)
                n = random.randint(0, tabuleiro.tamanho -1)
                while tabuleiro.prenchimento[l][n] != '~':
                    l = random.randint(0, tabuleiro.tamanho -1)
                    n = random.randint(0, tabuleiro.tamanho -1)
                e.primeirofogo[0] = l
                e.primeirofogo[1] = n
                return l, n
            case 'verificarlaterais':
                if e.segundofogo != ['l','n']:
                    if tabuleiro.prenchimento[e.segundofogo[0]][e.segundofogo[1]] == 'F':
                        e.modo = 'afundar'
                        #input('PAUSEEEE')
                        continue
                e.ladosdesconhecidos = []
                try:
                    if tabuleiro.prenchimento[e.primeirofogo[0] + 1][e.primeirofogo[1]] == '~':
                        e.ladosdesconhecidos.append([e.primeirofogo[0] + 1, e.primeirofogo[1]])
                except:
                    pass

                try:
                    if tabuleiro.prenchimento[e.primeirofogo[0] - 1][e.primeirofogo[1]] == '~':
                        if e.primeirofogo[0] - 1 >= 0:
                            e.ladosdesconhecidos.append([e.primeirofogo[0] - 1, e.primeirofogo[1]])
                except:
                    pass

                try:
                    if tabuleiro.prenchimento[e.primeirofogo[0]][e.primeirofogo[1] + 1] == '~':
                        e.ladosdesconhecidos.append([e.primeirofogo[0], e.primeirofogo[1] + 1])
                except:
                    pass

                try:
                    if tabuleiro.prenchimento[e.primeirofogo[0]][e.primeirofogo[1] - 1] == '~':
                        if e.primeirofogo[1] - 1 >= 0:
                            e.ladosdesconhecidos.append([e.primeirofogo[0], e.primeirofogo[1] - 1])
                except:
                    pass
                if len(e.ladosdesconhecidos) == 0:
                    e.ulttamfrota = tabuleiro.num_destrocos
                    '''print(e.primeirofogo)
                    print(e.segundofogo)
                    print(e.terceirofogo)
                    print(e.ladosdesconhecidos2)
                    input()'''
                    e.modo = 'aleatorio'
                    e.primeirofogo = ['l','n']
                    e.segundofogo = ['l','n']
                    e.ladosdesconhecidos = []
                    e.ladosdesconhecidos2 = []
                    e.terceirofogo = ['l','n']
                    e.cont = 0
                    continue

                tiro = random.randint(0, len(e.ladosdesconhecidos) - 1)
                l = e.ladosdesconhecidos[tiro][0]
                n = e.ladosdesconhecidos[tiro][1]
                e.segundofogo[0] = l
                e.segundofogo[1] = n

                return l, n
            case 'afundar':
                if e.ulttamfrota != tabuleiro.num_destrocos:
                    e.ulttamfrota = tabuleiro.num_destrocos
                    e.modo = 'aleatorio'
                    e.primeirofogo = ['l','n']
                    e.segundofogo = ['l','n']
                    e.ladosdesconhecidos = []
                    e.ladosdesconhecidos2 = []
                    e.terceirofogo = ['l','n']
                    e.cont = 0
                    continue

                if e.primeirofogo[0] == e.segundofogo[0]:
                    print('Horizontal')
                    if e.ladosdesconhecidos2 == []:
                        e.extremidades = [['l','n'],['l','n']]
                        try:
                            c = 0 
                            while tabuleiro.prenchimento[e.primeirofogo[0]][e.primeirofogo[1] + c] == 'F':
                                e.extremidades[0][0] = e.primeirofogo[0]
                                e.extremidades[0][1] = e.primeirofogo[1] + c
                                c += 1
                        except:
                            pass

                        try:
                            c = 0 
                            while tabuleiro.prenchimento[e.primeirofogo[0]][e.primeirofogo[1] - c] == 'F':
                                if e.primeirofogo[1] - c >= 0:
                                    e.extremidades[1][0] = e.primeirofogo[0]
                                    e.extremidades[1][1] = e.primeirofogo[1] - c
                                c += 1
                        except:
                            pass
                        
                        #input(e.extremidades)

                        try:
                            if tabuleiro.prenchimento[e.extremidades[0][0]][e.extremidades[0][1] + 1] == '~':
                                e.ladosdesconhecidos2.append([e.extremidades[0][0], e.extremidades[0][1] + 1])
                        except:
                            pass

                        try:
                            if tabuleiro.prenchimento[e.extremidades[1][0]][e.extremidades[1][1] - 1] == '~':
                                if e.extremidades[1][1] - 1 >= 0:
                                    e.ladosdesconhecidos2.append([e.extremidades[1][0], e.extremidades[1][1] - 1])
                        except:
                            pass

                        #input(e.ladosdesconhecidos2)

                    if len(e.ladosdesconhecidos2) == 0:
                        e.ulttamfrota = tabuleiro.num_destrocos
                        '''print(e.primeirofogo)
                        print(e.segundofogo)
                        print(e.terceirofogo)
                        print(e.ladosdesconhecidos2)
                        input()'''
                        e.modo = 'aleatorio'
                        e.primeirofogo = ['l','n']
                        e.segundofogo = ['l','n']
                        e.ladosdesconhecidos = []
                        e.ladosdesconhecidos2 = []
                        e.terceirofogo = ['l','n']
                        e.cont = 0
                        continue
                    tiro = random.randint(0, len(e.ladosdesconhecidos2) - 1)
                    l = e.ladosdesconhecidos2[tiro][0]
                    n = e.ladosdesconhecidos2[tiro][1]
                    e.ladosdesconhecidos2.pop(tiro)
                    return l, n


                else:
                    print('Vertical')
                    if e.ladosdesconhecidos2 == []:
                        e.extremidades = [['l','n'],['l','n']]
                        try:
                            c = 0 
                            while tabuleiro.prenchimento[e.primeirofogo[0] + c][e.primeirofogo[1]] == 'F':
                                e.extremidades[0][0] = e.primeirofogo[0] + c
                                e.extremidades[0][1] = e.primeirofogo[1] 
                                c += 1
                        except:
                            pass

                        try:
                            c = 0 
                            while tabuleiro.prenchimento[e.primeirofogo[0] - c][e.primeirofogo[1]] == 'F':
                                if e.primeirofogo[0] - c >= 0:
                                    e.extremidades[1][0] = e.primeirofogo[0] - c
                                    e.extremidades[1][1] = e.primeirofogo[1]
                                c += 1
                        except:
                            pass
                        
                        #input(e.extremidades)

                        try:
                            if tabuleiro.prenchimento[e.extremidades[0][0] + 1][e.extremidades[0][1]] == '~':
                                e.ladosdesconhecidos2.append([e.extremidades[0][0] + 1 , e.extremidades[0][1]])
                        except:
                            pass

                        try:
                            if tabuleiro.prenchimento[e.extremidades[1][0] - 1][e.extremidades[1][1]] == '~':
                                if e.extremidades[1][0] - 1 >= 0:
                                    e.ladosdesconhecidos2.append([e.extremidades[1][0] - 1, e.extremidades[1][1]])
                        except:
                            pass

                        #input(e.ladosdesconhecidos2)

                    if len(e.ladosdesconhecidos2) == 0:
                        e.ulttamfrota = tabuleiro.num_destrocos
                        '''print(e.primeirofogo)
                        print(e.segundofogo)
                        print(e.terceirofogo)
                        print(e.ladosdesconhecidos2)
                        input()'''
                        e.modo = 'aleatorio'
                        e.primeirofogo = ['l','n']
                        e.segundofogo = ['l','n']
                        e.ladosdesconhecidos = []
                        e.ladosdesconhecidos2 = []
                        e.terceirofogo = ['l','n']
                        e.cont = 0
                        continue
                    tiro = random.randint(0, len(e.ladosdesconhecidos2) - 1)
                    l = e.ladosdesconhecidos2[tiro][0]
                    n = e.ladosdesconhecidos2[tiro][1]
                    e.ladosdesconhecidos2.pop(tiro)
                    return l, n

def main():
    match menu():
        case "1":

            tabuleiro_j1 = tabuleiro(dono="Jogador 1", tamanho=10, tipo="Principal")
            tabuleiro_j2 = tabuleiro(dono="Jogador 1", tamanho=10, tipo="Combate")

            frota = escolha_frota()
            posicionamento(frota, tabuleiro_j1, tabuleiro_j2)
            #posicionamentoia(frota, tabuleiro_j1)

            tabuleiro_c1 = tabuleiro(dono="Computador", tamanho=10, tipo="Principal")
            tabuleiro_c2 = tabuleiro(dono="Computador", tamanho=10, tipo="Combate")

            frotac = escolha_frota()
            posicionamentoia(frotac, tabuleiro_c1)

            while True:
                l,n = entrada_posicao(tabuleiro_j1, 'travar alvo:', tabuleiro_j2)
                #l,n = "a",1
                tiro = l+str(n)
                l = int(ord(l.lower())) - 97
                tabuleiro_j2.prenchimento[l][n] = "X"
                tabuleiro_c1.prenchimento[l][n] = "X"

                for navio in frotac:
                    veri = navio.navio_alvejado(tiro)
                    if veri == True:
                        print('Acertouuuuuu')
                        tabuleiro_j2.prenchimento[l][n] = "F"
                        tabuleiro_c1.prenchimento[l][n] = "F"
                        if navio.verifica_status() == 'MORTO':
                            print(f'O {navio.nome} foi afundado!')
                            input()
                            tabuleiro_j2.num_destrocos += 1
                        break
                if veri == False:
                    print("Errouuuuuuu")
                #input()

                if tabuleiro_j2.num_destrocos >= len(frotac):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("GANHOU")
                    input()
                    break

                '''os.system('cls' if os.name == 'nt' else 'clear')
                print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
                tabuleiro_c1.mostrar_tabuleiro(combate=tabuleiro_c2)'''
                
                l, n = e(tabuleiro_c2)
                l = (chr(l + 97).upper())
                tiro = l+str(n)
                l = int(ord(l.lower())) - 97

                tabuleiro_c2.prenchimento[l][n] = "X"
                tabuleiro_j1.prenchimento[l][n] = "X"

                for navio in frota:
                    veri = navio.navio_alvejado(tiro)
                    if veri == True:
                        tabuleiro_c2.prenchimento[l][n] = "F"
                        tabuleiro_j1.prenchimento[l][n] = "F"
                        if navio.verifica_status() == 'MORTO':
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f'O seu {navio.nome} foi afundado!')
                            input()
                            tabuleiro_c2.num_destrocos += 1
                        break

                if tabuleiro_c2.num_destrocos >= len(frota):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("PERDEU")
                    input()
                    break

        case "2":
            print('Saindo...')
        case _:
            print('Opcao invalida!')

if __name__ == "__main__":
    main()