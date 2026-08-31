import time
import os
import sys

class Interface:
    @staticmethod
    def limpar_buffer():
        if os.name == "nt":  # Windows
            import msvcrt
            while msvcrt.kbhit():
                msvcrt.getch()

        else:  # Linux, macOS
            import termios
            termios.tcflush(sys.stdin, termios.TCIFLUSH)

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
    def mostrar_mensagem(texto, velocidade=0.02, pausar=True):
        print(">>> ", end='') 
        
        for letra in texto:
            print(letra, end='', flush=True)
            time.sleep(velocidade)
            
        print()
        
        if pausar:
            time.sleep(1)

        Interface.limpar_buffer()
        return ''

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
        print("\n┌────────────────────────────────────────────────────────┐")
        print(f"│  ORDEM DO COMANDO: POSICIONAMENTO DE FROTA             │")
        print(f"│  Embarcação : {navio.nome.upper():<25} Comprimento : {navio.tamanho}│")
        print("├────────────────────────────────────────────────────────┤")
        print("│  Selecione a proa da embarcação para manobra:          │")
        print("│    [1] ◄── Horizontal (Preenche de LESTE para OESTE)   │")
        print("│    [2] ──► Horizontal (Preenche de OESTE para LESTE)   │")
        print("│    [3]  ▲  Vertical   (Preenche de SUL para NORTE)     │")
        print("│    [4]  ▼  Vertical   (Preenche de NORTE para SUL)     │")
        print("└────────────────────────────────────────────────────────┘")
        while True:

            Interface.mostrar_mensagem("Aguardando coordenadas táticas, Almirante: ")
            opcao = input()
            if opcao in ['1', '2', '3', '4']:
                return opcao
                
            Interface.mostrar_mensagem('Erro: Número inválido! Use letras de 0 até 4.')

    @staticmethod
    def tela_vitoria():
        Interface.limpar_tela()
        print("\n┌────────────────────────────────────────────────────────┐")
        print("│                  ★ VITÓRIA NAVAL! ★                    │")
        print("├────────────────────────────────────────────────────────┤")
        print(f"│  Parabéns, Almirante                                   │")
        print("│  A frota inimiga foi completamente aniquilada!         │")
        print("│  Os mares agora estão sob o seu total domínio.         │")
        print("└────────────────────────────────────────────────────────┘\n")
        Interface.mostrar_mensagem("Pressione ENTER para retornar à base...")
        input()

    @staticmethod
    def tela_derrota():
        Interface.limpar_tela()
        print("\n┌────────────────────────────────────────────────────────┐")
        print("│                  ☠ DERROTA NAVAL ☠                     │")
        print("├────────────────────────────────────────────────────────┤")
        print(f"│  Almirante!                                            │")
        print("│  Nossas forças foram abatidas e a frota afundou.       │")
        print("│  Ordem geral: Evacuar imediatamente o quadrante!       │")
        print("└────────────────────────────────────────────────────────┘\n")
        Interface.mostrar_mensagem("Pressione ENTER para encerrar a missão...")
        input()

    @staticmethod
    def aviso_afundamento(nome_navio, inimigo=True):
        alvo = "inimigo" if inimigo else "aliado"
        print(f"\n[!] ALERTA TÁTICO: O {nome_navio.upper()} ({alvo}) foi afundado!")

    @staticmethod
    def escolher_frota():
        Interface.limpar_tela()
        print("\n┌────────────────────────────────────────────────────────────────┐")
        print("│  ORDEM DO COMANDO: SELEÇÃO DE FROTA NAVAL                      │")
        print("├────────────────────────────────────────────────────────────────┤")
        print("│  Selecione a composição tática para o combate:                 │")
        print("│                                                                │")
        print("│  [1] Frota Clássica (Balanceada)                               │")
        print("│      ↳ Porta-Aviões (5) | Encouraçado (4) | Cruzador (3)       │")
        print("│        Destroyer (3) | Submarino (2)                           │")
        print("│                                                                │")
        print("│  [2] Frota Pesada (Alto Calibre)                               │")
        print("│      ↳ Porta-Aviões 1 (5) | Porta-Helicopteros (5)             │")
        print("│        Encouraçado (4) | Fragata (3)                           │")
        print("│                                                                │")
        print("│  [3] Frota Furtiva (Ágil e Tática)                             │")
        print("│      ↳ Encouraçado (4) | Cruzador (3) | Destroyer (3)          │")
        print("│        Fragata (3) | Corveta (2) | Submarino (2)               │")
        print("└────────────────────────────────────────────────────────────────┘")
        
        while True:
            Interface.mostrar_mensagem("Aguardando escolha estratégica, Almirante: ")
            opcao = input().strip()
            
            if opcao in ['1', '2', '3']:
                return int(opcao)
                
            Interface.mostrar_mensagem('Erro: Frota inválida! Digite o número 1, 2 ou 3.')
        
    @staticmethod
    def menu_principal():
        print("\n┌────────────────────────────────────────────────────────────────┐")
        print("│  COMANDO CENTRAL: BATALHA NAVAL                                │")
        print("├────────────────────────────────────────────────────────────────┤")
        print("│                                                                │")
        print("│      [1] INICIAR NOVO JOGO                                     │")
        print("│      [2] SAIR DO SISTEMA                                       │")
        print("│                                                                │")
        print("└────────────────────────────────────────────────────────────────┘")
        
        while True:
            Interface.mostrar_mensagem("Aguardando ordens, Almirante: ")
            opcao = input().strip()
            
            if opcao in ['1', '2']:
                return int(opcao)
                
            Interface.mostrar_mensagem('Erro: Comando inválido! Digite 1 para Jogar ou 2 para Sair.')