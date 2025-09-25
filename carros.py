import random

def input_ano():
    while True:
        try:
            a = int(input("Ano do carro: "))
            if 1900 <= a <= 2100:  # limite razoável
                return a
            else:
                print("Ano inválido!")
        except:
            print("Digite um número válido!")

# IDs aleatórios
carro_id = random.randint(10000, 99999)
equipe_id = random.randint(1000, 9999)  # referência à tabela equipe

# Inputs do usuário
modelo = input("Modelo do carro: ")
ano = input_ano()

# Saída final
print("\n--- KOTB ---")
print("Carro ID:", carro_id)
print("Modelo:", modelo)
print("Ano:", ano)
print("Equipe ID:", equipe_id)
