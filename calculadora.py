print("Bem-vindo à Calculadora Simples")

calculo = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y if y != 0 else "Divisão por zero!"
        }

operadores = '\'+\' (soma), \'-\' (subtração), \'*\'(multiplicação), \'/\' (divisão).\n'

while True:    
    try:
        num1 = float(input('Número 1: '))
        operacao = input('Digite o operador: ' + operadores)
        num2 = float(input('Número 2: '))

       

        if operacao not in calculo:
            raise ValueError("Operador inválido.")

        resultado = calculo[operacao](num1, num2)

        if resultado == "Divisão por zero!":
            print(resultado)
        else:
            print(f"{num1} {operacao} {num2} = {resultado:.2f}\n")

        print("-------------") 

    except ValueError as e:
        print(f"Erro: {e}")
        continue
