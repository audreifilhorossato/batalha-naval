# Batalha Naval

Jogo de batalha naval para o terminal, escrito em Python puro: você contra o computador, num tabuleiro de 10×10 casas.

O repositório guarda **duas versões** do jogo:

|                     | Versão principal — `main.py`                      | Versão inicial — `naval.py`                    |
| ------------------- | ------------------------------------------------- | ---------------------------------------------- |
| Organização         | Separada em modelos, controles e visões           | Um único arquivo                               |
| Frotas              | Três frotas à escolha                             | Uma frota fixa de 6 navios                     |
| Interface           | Menus em caixas, mensagens animadas e cores       | Texto simples, com cores no tabuleiro          |
| Depois da partida   | Volta ao menu                                     | Encerra o programa                             |
| Situação            | **Versão recomendada para jogar**                 | Primeira versão, mantida como histórico        |

---

## Sumário

- [Requisitos](#requisitos)
- [Como executar](#como-executar)
- [Como jogar](#como-jogar)
- [A versão inicial (`naval.py`)](#a-versão-inicial-navalpy)
- [Como o computador joga](#como-o-computador-joga)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Gerar um executável](#gerar-um-executável)
- [Problemas conhecidos](#problemas-conhecidos)

---

## Requisitos

- **Python 3.10 ou mais novo** — o código usa `match`/`case`, que não existe no 3.9. Testado do 3.10 ao 3.14.
- **Nenhuma biblioteca externa** — só a biblioteca padrão do Python.
- **Um terminal com cores e pelo menos 113 colunas × 37 linhas.** Os dois tabuleiros ficam lado a lado; numa janela menor o desenho se espalha ou quebra. Maximizar a janela costuma bastar.

O jogo foi desenvolvido no Windows e testado no Linux. O código tem caminhos próprios para Windows e para Linux/macOS na hora de limpar a tela e de descartar teclas digitadas.

## Como executar

```bash
git clone https://github.com/audreifilhorossato/batalha-naval.git
cd batalha-naval
```

| Sistema         | Versão principal  | Versão inicial     |
| --------------- | ----------------- | ------------------ |
| Windows         | `py main.py`      | `py naval.py`      |
| Linux / macOS   | `python3 main.py` | `python3 naval.py` |

## Como jogar

As instruções abaixo são da versão principal (`main.py`).

### 1. Menu

| Tecla | Ação               |
| ----- | ------------------ |
| `1`   | Iniciar novo jogo  |
| `2`   | Sair do jogo       |

### 2. Escolha da frota

| Opção | Frota                      | Navios (tamanho)                                                                 | Casas |
| ----- | -------------------------- | -------------------------------------------------------------------------------- | ----- |
| `1`   | Clássica (balanceada)      | Porta-Aviões (5), Encouraçado (4), Cruzador (3), Destroyer (3), Submarino (2)     | 17    |
| `2`   | Pesada (alto calibre)      | Porta-Aviões 1 (5), Porta-Helicopteros (5), Encouraçado (4), Fragata (3)          | 17    |
| `3`   | Furtiva (ágil e tática)    | Encouraçado (4), Cruzador (3), Destroyer (3), Fragata (3), Corveta (2), Submarino (2) | 17 |

O computador sorteia a frota dele entre as três, sem revelar qual é. Como todas ocupam 17 casas, a partida fica equilibrada seja qual for o sorteio.

### 3. Posicionamento dos navios

Para cada navio, o jogo pede a **direção** e depois a **coordenada inicial**. O navio começa na coordenada e se estende na direção escolhida:

| Opção | Direção                  | Exemplo: Cruzador (3) em `E5` |
| ----- | ------------------------ | ----------------------------- |
| `1`   | ◄ para a esquerda (oeste) | E5, E4, E3                   |
| `2`   | ► para a direita (leste)  | E5, E6, E7                   |
| `3`   | ▲ para cima (norte)       | E5, D5, C5                   |
| `4`   | ▼ para baixo (sul)        | E5, F5, G5                   |

Os navios podem encostar uns nos outros, mas não podem se cruzar nem passar da borda. Se isso acontecer, o jogo mostra *"Erro: Limites excedidos ou colisão."* e pergunta de novo a direção e a coordenada daquele navio.

### 4. Coordenadas

Uma coordenada é a **letra da linha** (`A` a `J`) seguida do **número da coluna** (`0` a `9`), por exemplo `B7` ou `j0`. Maiúsculas e minúsculas valem igual; no tabuleiro as linhas aparecem em minúsculas.

### 5. Combate

Você atira primeiro, depois o computador, e assim por diante. A tela mostra dois quadrantes:

- **Quadrante inimigo** (esquerda): seus tiros no mar do computador.
- **Quadrante amigo** (direita): seus navios e os tiros que o computador já deu neles.

| Símbolo | Cor      | Significado                                   |
| ------- | -------- | --------------------------------------------- |
| `~`     | azul     | Água ainda não atacada                        |
| `N`     | verde    | Seu navio (só aparece no quadrante amigo)     |
| `X`     | cinza    | Tiro na água                                  |
| `F`     | vermelho | Acerto — navio em chamas                      |

Quando um navio afunda, de qualquer lado, aparece um alerta tático; aperte **ENTER** para continuar.

> **Dica:** as mensagens aparecem letra por letra, e o jogo descarta o que for digitado durante essa animação (para evitar jogadas acidentais). Espere a mensagem terminar antes de digitar.

### 6. Fim de jogo

Vence quem afundar primeiro a frota inteira do adversário. Aparece a tela de **Vitória Naval** ou de **Derrota Naval**; aperte ENTER para voltar ao menu.

### Exemplo de tela

Uma partida em andamento, com dois navios inimigos atingidos à esquerda e a sua frota à direita:

```text
---------------- QUADRANTE INIMIGO ----------------   │   ----------------- QUADRANTE AMIGO -----------------
    0    1    2    3    4    5    6    7    8    9    │        0    1    2    3    4    5    6    7    8    9
                                                      │
a   ~    ~    ~    ~    X    ~    X    X    F    X    │    a   ~    ~    ~    ~    ~    ~    X    ~    F    ~
                                                      │
b   ~    F    X    ~    ~    ~    ~    ~    ~    X    │    b   ~    F    X    ~    ~    ~    X    ~    F    ~
                                                      │
c   ~    ~    ~    ~    ~    ~    ~    X    ~    ~    │    c   ~    F    ~    ~    ~    ~    ~    ~    F    X
                                                      │
d   X    ~    ~    ~    ~    ~    ~    ~    ~    ~    │    d   X    F    X    X    ~    N    N    N    ~    X
                                                      │
e   ~    X    ~    ~    ~    ~    X    ~    ~    ~    │    e   ~    F    ~    X    ~    ~    ~    ~    ~    ~
                                                      │
f   X    ~    ~    X    X    X    ~    ~    ~    ~    │    f   ~    F    ~    ~    ~    X    ~    X    ~    ~
                                                      │
g   ~    ~    ~    ~    X    ~    ~    ~    X    ~    │    g   ~    X    ~    ~    ~    ~    ~    ~    ~    X
                                                      │
h   X    ~    X    ~    X    ~    ~    ~    ~    ~    │    h   ~    X    X    N    N    N    N    ~    ~    ~
                                                      │
i   ~    ~    ~    X    ~    X    ~    ~    ~    X    │    i   ~    ~    ~    ~    ~    ~    ~    ~    X    ~
                                                      │
j   ~    ~    ~    ~    ~    ~    ~    ~    ~    ~    │    j   ~    ~    ~    ~    ~    ~    ~    ~    N    N
                                                      │
>>> Almirante, qual a coordenada para travar o alvo?
```

## A versão inicial (`naval.py`)

É a primeira versão do jogo, num arquivo só. Ela é jogável, mas tem bugs conhecidos (veja [Problemas conhecidos](#problemas-conhecidos)); para jogar, prefira `main.py`. As diferenças em relação à versão principal:

- **Frota fixa**, igual para você e para o computador: Porta-Aviões (5), Encouraçado (4), Cruzador 1 (3), Cruzador 2 (3), Submarino 1 (2) e Submarino 2 (2) — 19 casas.
- **A orientação diz para onde a proa aponta**, e o navio se estende para o lado oposto:

  | Opção | Texto no jogo                       | O navio se estende | Exemplo: Cruzador em `E5` |
  | ----- | ----------------------------------- | ------------------ | ------------------------- |
  | `1`   | HORIZONTAL olhando para DIREITA     | para a esquerda    | E5, E4, E3                |
  | `2`   | HORIZONTAL olhando para ESQUERDA    | para a direita     | E5, E6, E7                |
  | `3`   | VERTICAL olhando para CIMA          | para baixo         | E5, F5, G5                |
  | `4`   | VERTICAL olhando para BAIXO         | para cima          | E5, D5, C5                |

- Se a posição for recusada, só dá para trocar a coordenada; a orientação escolhida fica.
- Não há animações nem escolha de frota.
- Ao fim da partida aparece **GANHOU** ou **PERDEU** e o programa termina, sem voltar ao menu.

## Como o computador joga

As duas versões usam a mesma estratégia, uma pequena máquina de estados:

1. **Aleatório** — atira numa casa sorteada entre as que ainda não foram atacadas.
2. **Verificar laterais** — depois de um acerto, testa as casas vizinhas (acima, abaixo, à esquerda e à direita) para descobrir a direção do navio.
3. **Afundar** — com dois acertos em linha, segue a linha pelas duas pontas até o navio afundar.
4. Quando um navio afunda, ou a linha acaba, volta ao modo aleatório.

Em 9.000 partidas simuladas, o computador afundou a frota inteira com 54 a 71 tiros em média, conforme a frota (quem atira ao acaso precisa de uns 95). Ele nunca repete um tiro nem atira fora do tabuleiro.

O posicionamento da frota do computador também é sorteado: direção e casa inicial aleatórias, tentando de novo até o navio caber.

## Estrutura do projeto

```text
batalha-naval/
├── main.py              # ponto de entrada da versão principal (laço do menu)
├── controles/
│   └── jogo.py          # classe Jogo: prepara a partida e executa os turnos
├── modelos/
│   ├── jogador.py       # Jogador, JogadorHumano e JogadorComputador (a IA)
│   ├── navio.py         # Navio, StatusNavio e as três frotas
│   └── tabuleiro.py     # Tabuleiro 10×10 e regras de posicionamento
├── visoes/
│   └── interface.py     # tudo o que aparece na tela: menus, tabuleiros, mensagens
├── naval.py             # versão inicial, completa num único arquivo
├── main.spec            # configuração do PyInstaller para gerar o executável
└── build/               # arquivos intermediários de uma compilação anterior
```

A versão principal segue uma divisão simples entre **modelos** (os dados do jogo), **visões** (o que é desenhado no terminal) e **controles** (a regra dos turnos). Uma partida corre assim:

1. `main.py` mostra o menu (`Interface.menu_principal`).
2. `Jogo.iniciar()` pede a frota, cria o jogador humano e o computador e posiciona as duas frotas.
3. `Jogo.executar_turno()` roda em laço: tiro do jogador, checagem de vitória, tiro do computador, checagem de derrota.
4. Ao fim, `Interface.tela_vitoria()` ou `Interface.tela_derrota()` e volta ao menu.

Cada jogador tem dois tabuleiros: o de **defesa**, com os próprios navios, e o de **ataque**, com os tiros dados no adversário.

## Gerar um executável

O arquivo `main.spec` gera um executável de console da versão principal com o [PyInstaller](https://pyinstaller.org/):

```bash
pip install pyinstaller
pyinstaller main.spec
```

O resultado fica em `dist/`: `dist/main.exe` no Windows ou `dist/main` no Linux e no macOS. O executável só roda no sistema em que foi gerado, e as pastas `build/` e `dist/` podem ser apagadas depois.

## Problemas conhecidos

Encontrados nos testes de 6 de outubro de 2026 (commit `278f614`):

| Versão    | Problema                                                                                          |
| --------- | ------------------------------------------------------------------------------------------------- |
| Principal | Atirar de novo numa casa já acertada troca o `F` por `X` e gasta a vez, sem aviso.                |
| Ambas     | O computador às vezes abandona um navio que já atingiu, principalmente com navios encostados.     |
| Ambas     | O tiro do computador não é anunciado; ele só aparece no quadrante amigo.                         |
| Ambas     | `Ctrl+C` ou `Ctrl+D` fecham o jogo com uma mensagem de erro do Python.                            |
| Inicial   | Atirar várias vezes na mesma casa conta como novos acertos e afunda o navio inteiro.              |
| Inicial   | As mensagens "Acertou" e "Errou" são apagadas antes de dar para ler.                              |
| Inicial   | Coordenadas com caracteres a mais são aceitas: `A5XYZ` vira `A5`.                                 |

## Autor

Desenvolvido por [audreifilhorossato](https://github.com/audreifilhorossato).