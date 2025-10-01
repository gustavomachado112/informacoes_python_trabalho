import random

print(" CADASTRO DE CORRIDA ")
corrida_id = random.randint(10000, 99999)
circuito_id = random.randint(10000, 99999)

while True:
    nome = input("Nome da corrida: ")
    if nome:  
        break
    print("Nome é obrigatório!")

while True:
    local = input("Local da corrida: ")
    if local:
        break
    print("Local é obrigatório!")
    
while True:
    data = input("Data (dd-mm-aaaa): ")
    if data and len(data) == 10:
        break
    print("Data ela sera obrigatoria. Use dd-mm-aaaa")
print("\nCorrida ID:", corrida_id)
print("Nome:", nome)
print("Local:", local)
print("Data:", data)
print("Circuito ID:", circuito_id)
print("\nCorrida cadastrada!")
