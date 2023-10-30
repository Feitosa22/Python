import time

km_to_mi = lambda km: km / 1.61
mi_to_km = lambda mi: mi * 1.61

def converter_medida():
    while True:
        try:
            print("\nEscolha o tipo de conversão:","1 - Quilômetros para Milhas", "2 - Milhas para Quilômetros","9 - Sair\n", sep='\n')
            opcao = int(input("Opção: "))
            
            if opcao == 9:
                print("\nObrigado por usar nossos serviços!")
                break

            elif opcao not in [1, 2]:
                print("Opção inválida. Por favor, escolha 1, 2 ou 9.")
            else:
                medida = float(input("Digite a medida: "))
                
                if medida < 0:
                    print("Por favor, insira uma medida positiva.")
                else:
                    if opcao == 1:
                        resultado = km_to_mi(medida)
                        print(f"{medida} quilômetros é {round(resultado, 2)} milhas\n")
                    elif opcao == 2:
                        resultado = mi_to_km(medida)
                        print(f"{medida} milhas é {round(resultado, 2)} quilômetros\n")
                    
                    print("Recomeçando em 3 segundos...")
                    time.sleep(3)

        except ValueError:
            print("Por favor, insira um valor numérico válido.")


converter_medida()
