import random
def input_ano():
    while True:
        try:
            a = int(input("Ano do carro: "))
            if 1900 <= a <= 2100:  
                return a
            else:
                print("Ano invalido!")
        except:
            print("Digite um numero valido!")

carro_id = random.randint(10000, 99999)
equipe_id = random.randint(1000, 9999)  
modelo = input("Modelo do carro: ")
ano = input_ano()

print("\n Carro")
print("Carro ID:", carro_id)
print("Modelo:", modelo)
print("Ano:", ano)
print("Equipe ID:", equipe_id)
print("Dados feito, obrigado por responder!")
