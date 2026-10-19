"""
Tema: Estruturas condicionais (if / elif / else)
Descrição: Exemplos de tomada de decisão com estruturas condicionais.
"""

# ---------------------------------------------------------
# 1. Condicional simples
# ---------------------------------------------------------
idade = 18

if idade >= 18:
    print("Maior de idade")

# ---------------------------------------------------------
# 2. Condicional composta
# ---------------------------------------------------------
nota = 7.5

if nota >= 6:
    print(f"Nota {nota}: Aprovado ✅")
else:
    print(f"Nota {nota}: Reprovado ❌")

# ---------------------------------------------------------
# 3. Condicional encadeada (elif)
# ---------------------------------------------------------
media = 5.5

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")

# ---------------------------------------------------------
# 4. Operadores lógicos (and / or / not)
# ---------------------------------------------------------
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir 🚗")
else:
    print("Não pode dirigir 🚫")

# ---------------------------------------------------------
# 5. Condicional aninhada
# ---------------------------------------------------------
usuario = "admin"
senha = "1234"

if usuario == "admin":
    if senha == "1234":
        print("Acesso liberado")
    else:
        print("Senha incorreta")
else:
    print("Usuário não encontrado")

# ---------------------------------------------------------
# 6. Operador ternário (if inline)
# ---------------------------------------------------------
idade = 17
status = "Maior de idade" if idade >= 18 else "Menor de idade"
print(f"Status: {status}")

# ---------------------------------------------------------
# 7. Verificando se um item pertence a uma lista
# ---------------------------------------------------------
frutas = ["maçã", "banana", "uva"]

if "banana" in frutas:
    print("Banana está na lista ✅")
else:
    print("Banana não está na lista ❌")