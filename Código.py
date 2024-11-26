import csv

# Função para carregar os dados do arquivo
def carregar_dados(arquivo):
    with open(arquivo, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')  # Certifica-se de que o delimitador é vírgula
        return [
            {key.strip().lower(): value.strip() for key, value in linha.items()} 
            for linha in reader
        ]

# Função para buscar clientes por parte do nome
def buscar_clientes_por_nome(dados, parte_nome):
    nomes = {linha['cliente'] for linha in dados if parte_nome.lower() in linha['cliente'].lower()}
    return sorted(nomes)

# Função para listar números de casos de um cliente
def listar_casos_cliente(dados, nome_cliente):
    casos = [linha['caso'] for linha in dados if linha['cliente'].lower() == nome_cliente.lower()]
    return casos

# Função para detalhar um caso
def detalhes_caso(dados, numero_caso):
    for linha in dados:
        if linha['caso'] == numero_caso:
            despesa = float(linha['despesa'])
            receita = float(linha['receita'])
            return linha['cliente'], despesa, receita, receita - despesa
    return None

# Função para calcular a despesa total
def calcular_despesa_total(dados):
    return sum(float(linha['despesa']) for linha in dados)

# Função para calcular a receita total
def calcular_receita_total(dados):
    return sum(float(linha['receita']) for linha in dados)

# Função para encontrar o caso com maior despesa
def caso_maior_despesa(dados):
    return max(dados, key=lambda linha: float(linha['despesa']))

# Função para encontrar o caso com maior receita
def caso_maior_receita(dados):
    return max(dados, key=lambda linha: float(linha['receita']))

# Função para exportar dados de um cliente para arquivo
def exportar_dados_cliente(dados, nome_cliente):
    dados_cliente = [linha for linha in dados if linha['cliente'].lower() == nome_cliente.lower()]
    if not dados_cliente:
        return False

    with open(f"{nome_cliente.replace(' ', '_')}_dados.csv", mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Cliente", "Caso", "Despesa", "Receita"])
        total_despesa = total_receita = 0

        for linha in dados_cliente:
            despesa = float(linha['despesa'])
            receita = float(linha['receita'])
            total_despesa += despesa
            total_receita += receita
            writer.writerow([linha['cliente'], linha['caso'], despesa, receita])

        writer.writerow([])
        writer.writerow(["Totais", "", total_despesa, total_receita])
        writer.writerow(["Diferença", "", "", total_receita - total_despesa])

    return True

# Função para exibir o menu
def menu():
    print("\nMenu de Opções:")
    print("1. Buscar clientes por parte do nome")
    print("2. Listar números de casos de um cliente")
    print("3. Detalhes de um caso")
    print("4. Exibir despesa total")
    print("5. Exibir receita total")
    print("6. Caso com maior despesa")
    print("7. Caso com maior receita")
    print("8. Exportar dados de um cliente para arquivo")
    print("9. Sair")

# Função principal
def main():
    arquivo = input("Digite o nome do arquivo de registro: ")
    dados = carregar_dados(arquivo)

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            parte_nome = input("Digite parte do nome do cliente: ")
            clientes = buscar_clientes_por_nome(dados, parte_nome)
            print("\nClientes encontrados:")
            print("\n".join(clientes) if clientes else "Nenhum cliente encontrado.")

        elif opcao == '2':
            nome_cliente = input("Digite o nome completo do cliente: ")
            casos = listar_casos_cliente(dados, nome_cliente)
            print(f"\nCasos do cliente {nome_cliente}:")
            print(", ".join(casos) if casos else "Nenhum caso encontrado.")

        elif opcao == '3':
            numero_caso = input("Digite o número do caso: ")
            detalhes = detalhes_caso(dados, numero_caso)
            if detalhes:
                cliente, despesa, receita, diferenca = detalhes
                print(f"\nCliente: {cliente}\nDespesa: {despesa}\nReceita: {receita}\nDiferença: {diferenca}")
            else:
                print("Caso não encontrado.")

        elif opcao == '4':
            print(f"\nDespesa total: {calcular_despesa_total(dados)}")

        elif opcao == '5':
            print(f"\nReceita total: {calcular_receita_total(dados)}")

        elif opcao == '6':
            maior_despesa = caso_maior_despesa(dados)
            print(f"\nCaso com maior despesa:\nCliente: {maior_despesa['cliente']}\nCaso: {maior_despesa['caso']}\nDespesa: {maior_despesa['despesa']}\nReceita: {maior_despesa['receita']}")

        elif opcao == '7':
            maior_receita = caso_maior_receita(dados)
            print(f"\nCaso com maior receita:\nCliente: {maior_receita['cliente']}\nCaso: {maior_receita['caso']}\nDespesa: {maior_receita['despesa']}\nReceita: {maior_receita['receita']}")

        elif opcao == '8':
            nome_cliente = input("Digite o nome completo do cliente: ")
            if exportar_dados_cliente(dados, nome_cliente):
                print(f"\nDados do cliente {nome_cliente} exportados com sucesso.")
            else:
                print("Cliente não encontrado.")

        elif opcao == '9':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    main()
