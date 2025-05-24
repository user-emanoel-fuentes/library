# Como imprimir informações no console com Python

# A função print() serve para mostrar mensagens na tela do computador.
# Você pode usar para ver resultados, textos ou valores de variáveis.

# Exemplo simples:
print('Olá, Mundo!')
# saída: Olá, Mundo!

# Você pode mostrar vários valores juntos, separados por vírgula:
nome = 'João'
sobrenome = 'Oliveira'
idade = 25
sexo = 'M'
print(nome, sobrenome, idade, sexo)
# saída: João Oliveira 25 M

# Se quiser mudar o que aparece entre os valores, use o argumento sep:
print(nome, sobrenome, idade, sexo, sep="-")
# saída: João-Oliveira-25-M

# Para mudar o que aparece no final da linha, use o argumento end:
print('Valor 1', end=" | ")
print('Valor 2')
# saída: Valor 1 | Valor 2

# Se não mudar o end, cada print fica em uma linha:
print('Valor 3')
print('Valor 4')
# saída:
# Valor 3
# Valor 4

"""
Dica: Use print() sempre que quiser ver o resultado de algo no seu código.
Isso ajuda muito quando você está aprendendo ou tentando encontrar erros (debug).

Mais informações: https://docs.python.org/pt-br/3/library/functions.html#print
"""
