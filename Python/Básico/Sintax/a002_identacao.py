# Identação em Python

# O que é identação?
# Identação é o espaço colocado no início das linhas do código.
# Em Python, a identação é obrigatória para definir blocos de código.

# Por que isso é importante?
# O Python usa a identação para saber quais comandos pertencem a qual bloco (por exemplo, dentro de funções, if, loops, etc).

# Exemplo correto de identação:
nome = 'Emanoel'

def imprimir_nome(nome):
    if nome:
        print(nome)
    else:
        print("Nome não atribuído")

# Veja:
# - A função 'imprimir_nome' tem tudo que está dentro dela com 4 espaços à direita.
# - O 'if' e o 'else' também têm seus comandos identados (com 4 espaços).

# Exemplo incorreto de identação:
numero = 2025
def imprimir_numero(numero):
print(numero)  # <-- ERRO! Não está identado.

# O erro acima acontece porque o Python espera que tudo dentro da função esteja identado.
# Se rodar esse código, verá um erro assim:
# IndentationError: expected an indented block after function definition

# Dicas:
# - Sempre use 4 espaços para identar (não use TAB).
# - Não misture espaços e TABs.
# - Todo bloco de código (função, if, for, etc) deve ser identado.

"""
Documentação Python (2.1.8):

"O espaço em branco (espaços e tabulações) no início de uma linha lógica é usado para calcular o nível de indentação da linha, que por sua vez 
é usado para determinar o agrupamento de instruções."

Ou seja, a identação serve para que o interpretador identifique blocos lógicos em seu código.

Tabulações: Conjunto de espaços, podendo variar de um a oito espaços.

O padrão de identação para criar um bloco de código, é de quatro espaços. Desta forma, usar de tabulações no código, torna-se uma má prática de 
programação por conta da variação de espaços em diferentes sistemas/interpretadores.

Desta forma, tome cuidado para não misturar tabulações com espaços e garanta que seus blocos de códigos estão devidamente espaçados, caso contrário, 
o erro "IndentationError" será retornado em seu terminal.
"""