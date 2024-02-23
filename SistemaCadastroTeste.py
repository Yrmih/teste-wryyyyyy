class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        
    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}"

def Cadastrar_cliente():
    nome = input("Cadastrar o nome do cliente: ")
    email = input("Cadastrar o email do cliente: ")
    telefone = input("Cadastrar o telefone do cliente: ")
    
    return Cliente(nome, email, telefone)

def Exibir_clientes(Clientes):
    print("\nClientes Cadastrados:")
    for cliente in Clientes:
        print(cliente)

def main():
    clientes = []  # Armazenar os clientes em uma lista separada
    
    while True:
        print("\n1 - Cadastrar cliente")
        print("2 - Exibir clientes cadastrados")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cliente = Cadastrar_cliente()  # Armazenar o novo cliente em uma variável temporária
            clientes.append(cliente)  # Adicionar o novo cliente à lista de clientes
            print("Cliente cadastrado com sucesso!")
         
        elif opcao == "2":
            Exibir_clientes(clientes)  # Chamar a função Exibir_clientes com a lista de clientes
        elif opcao == "3":  # Movido para dentro do bloco do if
            print("Saindo do programa...")
            exit(0)
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
