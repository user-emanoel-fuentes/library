# Identação: 

"""
Documentação Python (2.1.8): 

"O espaço em branco (espaços e tabulações) no início de uma linha lógica é usado para calcular o nível de indentação da linha, que por sua vez 
é usado para determinar o agrupamento de instruções."

Ou seja, a identação serve para que o interpretador identifique blocos lógicos em seu código. 

Tabulações: Conjunto de espaços, podendo variar de um a oito espaços. 

O padrão de identação para criar um bloco de código, é de quatro espaços. Desta forma, usar de tabulações no código, torna-se uma má pratica de 
programação por conta da variação de espaços em diferentes sistemas/interpretadores.

"""


# Exemplo Correto:
nome = 'Emanoel'

def imprimir_nome(nome):
    if nome:
        print(nome)
    else:
        print("Nome não atribuído")

"""
Não se preocupe em entender o comportamento deste código, apenas em observar como ele está espaçado.
Veja que as palavras "if" e "else", estão com o mesmo espaçamento. Assim como a palavra "print" nas duas linhas que aparece, está no mesmo espaçamento. 

Isto é o que chamamos de bloco. O primeiro "print" está dentro do bloco "if", já o segundo, no "else". Enquanto ambos, estão dentro do bloco "def".
"""

# Exemplo incorreto:
numero = 2025
def imprimir_numero(numero):
print(numero)

"""
Novamente, não se preocupe em entender o comportamento do código. Apenas observe que desta vez, o texto "print" não está com espaçamento, logo, não está 
dentro do bloco "def".

Quando você iniciar a execução deste arquivo, o seguinte erro será exposto no seu terminal: 

    IndentationError: expected an indented block after function definition on line nº
"""


"""
Desta forma, tome cuidado para não misturar tabulações com espaços e garanta que seus blocos de códigos estão devidamente espaçados, caso contrário, 
o erro "IdentationError" será retornado em seu terminal.  
"""