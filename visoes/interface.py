import time
import os

class Interface:
    @staticmethod
    def colorir(simbolo):

        cores = {
        '~': '\033[34m~\033[0m', # Azul
        'N': '\033[32mN\033[0m', # Verde
        'F': '\033[1;31mF\033[0m', # Vermelho (Negrito)
        'X': '\033[90mX\033[0m' # Cinza
        }  

        return cores.get(simbolo, simbolo)

    @staticmethod
    def mostrar_mensagem(texto, velocidade=0.03, pausar=True):
        print(">>> ", end='') 
        
        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(velocidade)
            
        print()
        
        if pausar:
            time.sleep(0)

    @staticmethod       
    def mostrar_dois_tabuleiros(tabuleiro_defesa, tabuleiro_ataque):
        print("---------------- QUADRANTE INIMIGO ----------------   │   ----------------- QUADRANTE AMIGO -----------------")
        print('    ', end='')
        for i in range(tabuleiro_ataque.tamanho):
            print(i , end='    ')

        print('│        ', end='')
        for i in range(tabuleiro_ataque.tamanho):
            print(i , end='    ')

        print('\n                                                      │')
        for i in range(tabuleiro_ataque.tamanho):
            for j in range(tabuleiro_defesa.tamanho):
                print(f'{chr(97 +i)}  ' if j == 0 else '', Interface.colorir(tabuleiro_defesa.dados[i][j]), end='   ')
            print(' │    ', end='')
            for j in range(tabuleiro_ataque.tamanho):
                print(f'{chr(97 +i)}  ' if j == 0 else '', Interface.colorir(tabuleiro_ataque.dados[i][j]), end='   ')
            print('\n                                                      │')
    
    @staticmethod
    def limpar_tela():
        os.system('color & cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def receber_coordenadas(texto):
        while True:
            entrada = input(texto).strip().upper()
            if len(entrada) != 2:
                Interface.mostrar_mensagem('Erro: Formato inválido! Digite uma letra e um número (Ex: A5).')
                continue
        
            try:
                linha = int(ord((entrada[0]))) - 65
                if linha < 0 or linha > 9:
                    Interface.mostrar_mensagem('Erro: Letra inválida! Use letras de A até J.')         
                    continue

            except:
                Interface.mostrar_mensagem('Erro: Letra inválida! Use letras de A até J.')
                continue

            try:
                coluna = int(entrada[1])
                if coluna < 0 or coluna > 9:
                    Interface.mostrar_mensagem('Erro: Número inválido! Use letras de 0 até 9.')         
                    continue
            except:
                Interface.mostrar_mensagem('Erro: Número inválido! Use letras de 0 até 9.')
                continue
            break
        return entrada, linha, coluna

    @staticmethod
    def pedir_orientacao(navio):
        while True:
            print("\n┌────────────────────────────────────────────────────────┐")
            print(f"│  ORDEM DO COMANDO: POSICIONAMENTO DE FROTA             │")
            print(f"│  Embarcação : {navio.nome.upper():<25} Comprimento : {navio.tamanho}│")
            print("├────────────────────────────────────────────────────────┤")
            print("│  Selecione a proa da embarcação para manobra:          │")
            print("│    [1] ◄── Horizontal (Proa voltada para a OESTE)      │")
            print("│    [2] ──► Horizontal (Proa voltada para a LESTE)      │")
            print("│    [3]  ▲  Vertical   (Proa voltada para o NORTE)      │")
            print("│    [4]  ▼  Vertical   (Proa voltada para o SUL)        │")
            print("└────────────────────────────────────────────────────────┘")
            
            opcao = input(">>> Aguardando coordenadas táticas, Almirante: ").strip()

            if opcao in ['1', '2', '3', '4']:
                return opcao
                
            Interface.mostrar_mensagem('Erro: Número inválido! Use letras de 0 até 4.', velocidade=0.02)