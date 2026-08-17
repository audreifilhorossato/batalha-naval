import os
os.system('cls')
linhas_validas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
colunas_validas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tabuleiro1 = [["~" for _ in range(10)] for _ in range(10)]
def mostrar_tabuleiro():
    print('    ', end='')
    for i in range(10):
        print(i , end='    ')
    print('\n')
    for i in range(10):
        for j in range(10):
            print(f'{chr(97 +i)}  ' if j == 0 else '', tabuleiro1[i][j], end='   ')
        print('\n')

def menu():
    opcao = ''
    while opcao not in ('1', '2'):
        os.system('cls')
        print('Escolha uma opcao:')
        print('1. Novo Jogo')
        print('2. Sair')
        opcao = input()
    return opcao

def entrada_posicao():
    while True:
        os.system('cls')
        mostrar_tabuleiro()
        escolha =  input('Escolha o a posicao: ').strip().upper()
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
    escolha = [5,4,3,3,2]
    return escolha

def posicionamento(frota):
    for i in range(frota):
        while opcao not in ('1', '2', '3', '4'):
            os.system('cls')
            print('Escolha a orientação do navio {navio}:') #não finalizado
            print('1. HORIZONTAL olhando para DIREITA')
            print('2. HORIZONTAL olhando para ESQUERDA')
            print('3. VERTICAL olhando para CIMA')
            print('4. VERTICAL olhando para BAIXO')
            opcao = input()
        match opcao:
            case '1':
                while True:
                    letra, numero = entrada_posicao()
                    letra = int(ord(letra.lower())) - 97
                    if (letra - frota[0] < 0): 
                        print("ERRO")
            case '2':
                while True:
                    letra, numero = entrada_posicao()
                    letra = int(ord(letra.lower())) - 97
                    if (letra - frota[0] < 0): 
                        print("ERRO")
            case '3':
                while True:
                    letra, numero = entrada_posicao()
                    letra = int(ord(letra.lower())) - 97
                    if (letra - frota[0] < 0): 
                        print("ERRO")
            case '4':
                while True:
                    letra, numero = entrada_posicao()
                    letra = int(ord(letra.lower())) - 97
                    if (letra - frota[0] < 0): 
                        print("ERRO")

def main():
    match menu():
        case "1":
            while True:
                posicionamento(escolha_frota())
                tabuleiro1[int(ord(letra.lower())) - 97][numero] = 0
        case "2":
            print('Saindo...')
        case _:
            print('Opcao invalida!')

if __name__ == "__main__":
    main()