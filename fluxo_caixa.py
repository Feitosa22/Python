fluxo_caixa = []

print("---------")
print("Fluxo de Caixa")
print("---------")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("9 - Sair")

def adicionar_fluxo(opcao):
    nome = input("Nome: ")
    while True:
        try:
            valor = float(input("Valor: "))
            break
        except ValueError:
            print("Por favor, digite um número válido para o valor.")

    fluxo_caixa.append({
        "nome": nome,
        "valor": valor,
        "id": opcao
    })

def obter_opcao():
    while True:
        try:
            return int(input("Digite a opção: "))
        except ValueError:
            print("Por favor, digite um número inteiro.\n")
            continue

while True:
    opcao = obter_opcao()

    if opcao == 1 or opcao == 2:
        adicionar_fluxo(opcao)
    elif opcao == 9:
        print("Obrigado por usar nossos serviços!")
        break
    else:
        print("Digite uma opção válida!\n")
        continue

    total = 0
    print("\n--- Fluxo de Caixa ---")
    for fc in fluxo_caixa:
        tipo = "Receita" if fc['id'] == 1 else "Despesa"
        print(f"Nome: {fc["nome"]}, Tipo: {tipo}, Valor: R$ {fc['valor']:.2f}")
        total += fc['valor'] if fc['id'] == 1 else -fc['valor']
    print(f"Saldo atual: R$ {total:.2f}\n")
