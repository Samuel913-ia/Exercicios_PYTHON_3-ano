# Criação de um Gerador de IDs Sequenciais com Closure

def criar_gerador_id(start_id=1):
    current_id = start_id

    def proximo_id():
        nonlocal current_id # Permite modificar a variável do escopo externo
        id_gerado = current_id
        current_id += 1
        return id_gerado
    return proximo_id


# Criar dois geradores de IDs independentes
gerador_usuarios = criar_gerador_id(100)
gerador_produtos = criar_gerador_id(1)
print("\n--- Gerador de IDs de Usuários ---")
print(f"ID Usuário: {gerador_usuarios()}") # Saída: ID Usuário:
100
print(f"ID Usuário: {gerador_usuarios()}") # Saída: ID Usuário:
101
print("\n--- Gerador de IDs de Produtos ---")
print(f"ID Produto: {gerador_produtos()}") # Saída: ID Produto: 1
print(f"ID Produto: {gerador_produtos()}") # Saída: ID Produto: 2
print(f"ID Usuário: {gerador_usuarios()}") # Saída: ID Usuário:
