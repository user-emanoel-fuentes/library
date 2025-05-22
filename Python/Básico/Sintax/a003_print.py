# Print / Imprimir (Saída no Console);

"""
O python possui alguns trechos de códigos que costumamos usar quando estamos começando, a função print é um desses 
trechos (não se preocupe em entender o que é função agora, só saiba que é).

Resumidamente, esta função é utilizada para fazer com que o interpretador "imprima" no console o que foi relacionado dentro do parentese.

SINTAX:

print(valor)
saída:  valor
"""

# Exemplos Práticos: 
print('Olá, Mundo!')
# saída: Olá, Mundo!


# Podemos imprimir diferentes valores separando com virgula:
nome = 'João'
sobrenome = 'Oliveira'
idade = 25
sexo = 'M'
print(nome, sobrenome, idade, sexo)
# saída: João Oliveira 25 M
# obs: será impresso na ordem que for atribuído os valores dentro dos parênteses.


# Também podemos imprimir os valores, alterando o separador, o dado que fica entre os valores (por padrão, um espaço), utilizando sep.
print(nome, sobrenome, idade, sexo, sep="-")
# saída: João-Oliveira-25-M



# Também podemos usar um argumento que altera o que será exibido ao final da impressão (padrão "\n" = quebra de linha):
print('Valor 1', end=" | ")
print('Valor 2')
# saída: Valor 1 | Valor 2
# No cado de não declarar um novo valor para o argumento "end", as impressões serão exibidas uma em cada linha:

print('Valor 3')
print('Valor 4')
# saída: 
# Valor 3
# Valor 4

"""
Essa função é muito importante para nos desenvolvermos no início, ajudando a exibir alguns valores no terminal, e no futuro, quando você estiver 
analisando algum trecho de cógido, também poderá de ajudar a identifcar qual a situação de um certo valor, chamamos isso de debug.

Obs: O print() não serve em arquivos em modo binário, nesse caso utilize file.write(...)

Você pode encontrar mais detalhes sobre essa função na documentação do Python: https://docs.python.org/pt-br/3/library/functions.html#print
"""