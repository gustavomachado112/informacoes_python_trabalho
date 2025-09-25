import random
print(" CADASTRO DE CIRCUITO ")

circuito_id = random.randint(10000, 99999)
while True:
    nome_do_circuito = input("Nome do circuito: ").strip()
    if nome_do_circuito:
        break
    print("Nome é obrigatório!")

while True:
    pais = input("País: ").strip()
    if pais:
        break
    print("País é obrigatório!")

while True:
    try:
        extensao_km = float(input("Extensão em km: "))
        if extensao_km > 0:
            break
        else:
            print("Extensão deve ser maior que zero!")
    except:
        print("Digite um número válido!")
recordes_do_circuito = input("Recordes do circuito: ").strip()

print("\nCircuito ID:", circuito_id)
print("Nome do circuito:", nome_do_circuito)
print("País:", pais)
print("Extensão:", extensao_km, "km")
print("Recordes:", recordes_do_circuito)
print("\nCircuito cadastrado!")
