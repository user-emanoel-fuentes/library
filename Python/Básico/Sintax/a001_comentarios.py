# ===========================================================
# Comentários em Python
# ===========================================================

"""
O que são comentários?

Comentários são textos no código que servem para explicar o que ele faz.
Eles ajudam outras pessoas (e você mesmo no futuro) a entender o código.

Por que usar comentários?

    - Facilitam a compreensão do código
    - Ajudam na manutenção e atualização
    - Servem como documentação interna
    - Evitam mal-entendidos
    - Ajudam na depuração (encontrar erros)

Obs: Comentários são ignorados pelo Python, ou seja, não afetam o funcionamento do programa.
"""

# -----------------------------------------------------------
# Como fazer comentários em Python?
# -----------------------------------------------------------

# 1. Comentário de linha única: use o símbolo #
# Exemplo:
# Este é um comentário de linha única.

# 2. Comentário de múltiplas linhas: use três aspas simples (''') ou duplas (""")
'''
Este é um comentário
de múltiplas linhas.
Você pode escrever várias linhas aqui.
'''

"""
Outro exemplo de
comentário de múltiplas linhas.
"""

# -----------------------------------------------------------
# Exemplos práticos
# -----------------------------------------------------------

# EXEMPLO 1: Comentário de linha única explicando o código
print("Olá, mundo!")  # Este comando exibe uma mensagem na tela

# EXEMPLO 2: Comentário de múltiplas linhas antes de um bloco de código
'''
O bloco abaixo faz uma saudação personalizada.
'''
nome = "Maria"
print(f"Olá, {nome}!")