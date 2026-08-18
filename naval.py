import os
os.system('cls')
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

    def mostrar_tabuleiro(self):
        print("---------------- QUADRANTE INIMIGO ----------------   |   ----------------- QUADRANTE AMIGO -----------------")
        print('    ', end='')
        for i in range(self.tamanho):
            print(i , end='    ')

        print('|        ', end='')
        for i in range(self.tamanho):
            print(i , end='    ')

        print('\n                                                      |')
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                print(f'{chr(97 +i)}  ' if j == 0 else '', self.prenchimento[i][j], end='   ')
            print(' |    ', end='')
            for j in range(self.tamanho):
                print(f'{chr(97 +i)}  ' if j == 0 else '', self.prenchimento[i][j], end='   ')
            print('\n                                                      |')
    

def menu():
    opcao = ''
    while opcao not in ('1', '2'):
        os.system('cls')
        print('Escolha uma opcao:')
        print('1. Novo Jogo')
        print('2. Sair')
        opcao = input()
    return opcao

def entrada_posicao(tabuleiro, cabecalho):
    while True:
        os.system('cls')
        tabuleiro.mostrar_tabuleiro()
        escolha =  input(f'Escolha uma posicao para {cabecalho}').strip().upper()
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
            
            input("Pressione Enter para continuar...")
            return letra, numero

def escolha_frota():
    
    porta_avioes = navio("Porta-Aviões", 5)
    encouracado = navio("Encouraçado", 4)
    cruzador1 = navio("Cruzador 1", 3)
    cruzador2 = navio("Cruzador 2", 3)
    submarino1 = navio("Submarino 1", 2)
    submarino2 = navio("Submarino 2", 2)

    #minha_frota = [porta_avioes, encouracado, cruzador1, cruzador2, submarino1, submarino2]
    minha_frota = [porta_avioes]

    return minha_frota

def posicionamento(frota,tabuleiro):
    for i in range(len(frota)):
        navio = frota[i]
        opcao = ''
        while opcao not in ('1', '2', '3', '4'):
            os.system('cls')
            print(f'Escolha a orientação do navio {navio.nome}:')
            print('1. HORIZONTAL olhando para DIREITA')
            print('2. HORIZONTAL olhando para ESQUERDA')
            print('3. VERTICAL olhando para CIMA')
            print('4. VERTICAL olhando para BAIXO')
            opcao = input()
        match opcao:
            case '1':
                while True:
                    letra, numero = entrada_posicao(tabuleiro, f'posicionar {navio.nome}: ')
                    letra = int(ord(letra.lower())) - 97
                    if (numero - navio.tamanho < -1): 
                        print("Impossivel posicinar apartir dessa posicao")
                        input("Pressione Enter para continuar...")
                        continue
                    
                    posicao = False
                    for j in range(navio.tamanho):
                        if tabuleiro.prenchimento[letra][numero - j] == 0:
                            posicao = True
                            break

                    if posicao == True:
                        print("Impossivel posicinar apartir dessa posicao")
                        input("Pressione Enter para continuar...")
                        continue
                    break
                for j in range(navio.tamanho):
                    tabuleiro.prenchimento[letra][numero - j] = 0
                    navio.posicao.append(chr(letra + 97).upper()+str(numero - j))

            case '2':
                while True:
                    letra, numero = entrada_posicao(tabuleiro, f'POSICIONANDO O {navio.nome} NO TABULEIRO!!!')
                    letra = int(ord(letra.lower())) - 97
                    if (numero + navio.tamanho > 10): 
                        print("Impossivel posicinar apartir dessa posicao")
                        input("Pressione Enter para continuar...")
                        continue

                    posicao = False
                    for j in range(navio.tamanho):
                        if tabuleiro.prenchimento[letra][numero + j] == 0:
                            posicao = True
                            break

                    if posicao == True:
                        print("Impossivel posicinar apartir dessa posicao")
                        input("Pressione Enter para continuar...")
                        continue
                    break
                for j in range(navio.tamanho):
                    tabuleiro.prenchimento[letra][numero + j] = 0
                    navio.posicao.append(chr(letra + 97).upper()+str(numero + j))
            case '3':
                while True:
                    letra, numero = entrada_posicao(tabuleiro, f'POSICIONANDO O {navio.nome} NO TABULEIRO!!!')
                    letra = int(ord(letra.lower())) - 97
                    if (letra + navio.tamanho > 10): 
                        print("Impossivel posicinar apartir dessa posicao")
                        input("Pressione Enter para continuar...")
                        continue

                    posicao = False
                    for j in range(navio.tamanho):
                        if tabuleiro.prenchimento[letra + j][numero] == 0:
                            posicao = True
                            break

                    if posicao == True:
                        print("Impossivel posicinar apartir dessa posicao")
                        input("Pressione Enter para continuar...")
                        continue
                    break
                for j in range(navio.tamanho):
                    tabuleiro.prenchimento[letra + j][numero] = 0
                    navio.posicao.append(chr(letra + 97 + j).upper()+str(numero))
            case '4':
                while True:
                    letra, numero = entrada_posicao(tabuleiro, f'POSICIONANDO O {navio.nome} NO TABULEIRO!!!')
                    letra = int(ord(letra.lower())) - 97
            
                    if (letra - navio.tamanho < -1): 
                        print("Impossivel posicinar apartir dessa posicao")
                        input("Pressione Enter para continuar...")
                        continue

                    posicao = False
                    for j in range(navio.tamanho):
                        if tabuleiro.prenchimento[letra - j][numero] == 0:
                            posicao = True
                            break

                    if posicao == True:
                        print("Impossivel posicinar apartir dessa posicao")
                        input("Pressione Enter para continuar...")
                        continue
                    break
                for j in range(navio.tamanho):
                    tabuleiro.prenchimento[letra - j][numero] = 0
                    navio.posicao.append(chr(letra + 97 - j).upper()+str(numero))

def main():
    match menu():
        case "1":

            tabuleiro_j1 = tabuleiro(dono="Jogador 1", tamanho=10, tipo="Principal")

            frota = escolha_frota()
            posicionamento(frota, tabuleiro_j1)

            while True:
                l,n = entrada_posicao(tabuleiro_j1, 'travar alvo:')
                tiro = l+str(n)
                l = int(ord(l.lower())) - 97
                tabuleiro_j1.prenchimento[l][n] = "X"
                for navio in frota:
                    veri = navio.navio_alvejado(tiro)
                    if veri == True:
                        print('Acertouuuuuu')
                        if navio.verifica_status() == 'MORTO':
                            print(f'O {navio.nome} foi afundado!')
                            tabuleiro_j1.num_destrocos += 1
                        break
                if veri == False:
                    print("Errouuuuuuu")
                input()
                if tabuleiro_j1.num_destrocos >= len(frota):
                    print("PERDEU")
                    input()
                    break
                


        case "2":
            print('Saindo...')
        case _:
            print('Opcao invalida!')

if __name__ == "__main__":
    main()