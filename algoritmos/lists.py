"""
Tema: Listas e manipulação de coleções
Descrição: Exemplos de criação, acesso e manipulação de listas em Python.
"""

# ---------------------------------------------------------
# 1. Criando uma lista
# ---------------------------------------------------------
lista_compras = ["arroz", "feijão", "macarrão", "leite"]
print("=== Lista inicial ===")
print(lista_compras)

# ---------------------------------------------------------
# 2. Acessando elementos por índice
# ---------------------------------------------------------
print("\n=== Acesso por índice ===")
print(f"Primeiro item: {lista_compras[0]}")
print(f"Último item: {lista_compras[-1]}")

# ---------------------------------------------------------
# 3. Adicionando itens
# ---------------------------------------------------------
lista_compras.append("café")            # adiciona no final
lista_compras.insert(1, "açúcar")       # adiciona na posição 1

print("\n=== Após adicionar itens ===")
print(lista_compras)

# ---------------------------------------------------------
# 4. Removendo itens
# ---------------------------------------------------------
lista_compras.remove("leite")           # remove pelo valor
ultimo_item = lista_compras.pop()       # remove e retorna o último

print("\n=== Após remover itens ===")
print(lista_compras)
print(f"Item removido com pop(): {ultimo_item}")

# ---------------------------------------------------------
# 5. Tamanho e ordenação
# ---------------------------------------------------------
print("\n=== Informações da lista ===")
print(f"Quantidade de itens: {len(lista_compras)}")
print(f"Lista ordenada: {sorted(lista_compras)}")

# ---------------------------------------------------------
# 6. Percorrendo a lista com for
# ---------------------------------------------------------
print("\n=== Percorrendo a lista ===")
for item in lista_compras:
    print(f"- {item}")

# ---------------------------------------------------------
# 7. Lista com diferentes tipos
# ---------------------------------------------------------
dados = ["Python", 2024, 3.11, True]
print("\n=== Lista com tipos variados ===")
print(dados)