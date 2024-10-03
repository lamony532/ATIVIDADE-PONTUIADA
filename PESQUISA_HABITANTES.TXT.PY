import os 
os.system("cls || clear")

ALUNAS:
LAMONY DAS MERCÊS SILVA
LUANA DOS SANTOS CONCEIÇÃO

print("""=== menu===
     1.adicionar pessoas
      2.exibir resultados
      3.sair

      
      
      """)








def adicionar_pessoa():
    idade = int(input("Digite a idade da pessoa: "))
    sexo = input("Digite o sexo da pessoa (M/F): ")
    salario = float(input("Digite o salário da pessoa: "))

    return {"idade": idade, "sexo": sexo, "salario": salario}

def exibir_resultados(pessoas):
    if not pessoas:
        print("Nenhuma pessoa cadastrada.")
        return
    
    total_salarios = sum([pessoa['salario'] for pessoa in pessoas])
    media_salario = total_salarios / pessoas 

    idades = [pessoa['idade'] for pessoa in pessoas]
    maior_idade = max(idades)
    menor_idade = min(idades)

    mulheres_com_salarios_5000 = ([pessoa for pessoa in pessoas if pessoa['sexo'] == 'F' and pessoa['salario'] >= 5000])

    print("\nResutados:")
    print(f"- Media salarial do grupo : R$ {media_salario:.2f}")
    print(f"- Maior idade :{maior_idade} anos")
    print(f"- Menor idade:{menor_idade} anos")
    print(f"- Quantidade de muleres com salário a partir de R$ 5.000,00: {mulheres_com_salarios_5000}")
    
    def salvar_dados(pessoas):
        with open ("pesquisa_habitantes.txt , "w" as arquivo: "):
            for pessoa in pessoas:
                arquivo.write(f"{pessoa['idade']}, {'pessoa'}['sexo'], {'pessoa'}['salario'] \n")
                  print("Dados salvos com sucesso.")

    def carregar_dados():
        if not os.path.exists("pesquisa_habitantes.txt"):
            return []
        pessoas = [ ]
        with open("pesquisa_habitantes.txt, "r") as arquivo:
            for linha in arquivo:
                idade,sexo,salario = linha.strip().split(",")
                pessoas.append({"idade: int(idade), "sexo": sexo, "salario": float(salario)})

                return pessoas

    def menu():
       pessoas = carregar_dados()

       while True:
       print("\nMenu:")
       print("1. Adicionar pessoa")
       print("2. Exibir Resultados")
       print("3. Sair")

       opcao = int(input("Escolha uma opção: "))

       if opcao == 1:
           pessoa = adicionar_pessoa()
           pessoas.append(pessoa)
        elif opcao == 2:
           exibir_resultados(pessoas)
        elif opcao == 3:
            salvar_dados(pessoas)
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu():