"""
Tema: Variáveis, tipos de dados e entrada de usuário
Descrição: Exemplos básicos de declaração de variáveis,
           tipos de dados e interação com o usuário.
"""

# ---------------------------------------------------------
# 1. Declaração simples de variáveis
# ---------------------------------------------------------
nome = "Aline"          # string
idade = 25              # inteiro
altura = 1.65           # float
estudante = True        # booleano

print("=== Dados cadastrados ===")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")
print(f"Estudante: {estudante}")

# ---------------------------------------------------------
# 2. Verificando o tipo de cada variável
# ---------------------------------------------------------
print("\n=== Tipos das variáveis ===")
print(type(nome))
print(type(idade))
print(type(altura))
print(type(estudante))

# ---------------------------------------------------------
# 3. Entrada de dados pelo usuário
# ---------------------------------------------------------
print("\n=== Entrada de dados ===")
nome_usuario = input("Digite seu nome: ")
idade_usuario = int(input("Digite sua idade: "))

print(f"\nOlá, {nome_usuario}! Você tem {idade_usuario} anos.")

# ---------------------------------------------------------
# 4. Conversão entre tipos
# ---------------------------------------------------------
numero_texto = "42"
numero_inteiro = int(numero_texto)

print("\n=== Conversão de tipos ===")
print(f"Texto original: {numero_texto} (tipo {type(numero_texto).__name__})")
print(f"Convertido: {numero_inteiro} (tipo {type(numero_inteiro).__name__})")