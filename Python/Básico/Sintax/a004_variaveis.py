# Variáveis em Python

# Variáveis são usadas para armazenar dados na memória do computador.
# Você cria uma variável usando o operador de atribuição (=).

# Exemplo:
nome = 'Emanoel'  # variável chamada nome recebe o valor 'Emanoel'

# Você pode criar outras variáveis:
numero1 = 1
numero2 = 2
numero3 = 4

# Regras para nomes de variáveis:
# - Podem conter letras, números e underlines (_)
# - Não podem começar com número
# - Use nomes que façam sentido para o valor armazenado
# - Evite caracteres especiais
# - Não use letras maiúsculas no início

# Convenção: use snake_case para nomes com mais de uma palavra
# Exemplo:
nome_completo = "Maria Silva"

# Tipos de valores que podem ser armazenados:
texto = "Olá, isso é um texto"  # string
numero = 25                     # inteiro
decimal = 9.5                   # número decimal (float)
booleano = True                 # booleano (verdadeiro ou falso)

# Python detecta automaticamente o tipo do valor atribuído à variável.

# Você pode mudar o valor de uma variável a qualquer momento:
var = "Texto"   # tipo str (string)
print(var, type(var))

var = 2025      # tipo int (inteiro)
print(var, type(var))

var = True      # tipo bool (booleano)
print(var, type(var))

# A função type() mostra o tipo do valor armazenado na variável.

# Dicas:
# - Use nomes de variáveis claros e descritivos
# - Não use nomes genéricos como "x" ou "teste" sem necessidade
# - Não use caracteres especiais como ` ´ ^ ~ ç
# - Evite nomes de variáveis que sejam palavras reservadas do Python (como "if", "for", "while", etc.)
