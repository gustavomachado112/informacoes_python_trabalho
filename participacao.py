import random
print(" CADASTRO DE PARTICIPAÇÃO ")

participacao_id = random.randint(10000, 99999)
piloto_id = random.randint(10000, 99999)
corrida_id = random.randint(10000, 99999)

while True:
    try:
        posicao_final = int(input("Posição final (>= 1): "))
        if posicao_final >= 1:
            break
        else:
            print("Posição deve ser entre o vigesimo e o primeiro")
    except:
        print("Digite uma posicao valida")
print("\n INFORMAÇÕES ")
print("Participacao ID:", participacao_id)
print("Piloto ID:", piloto_id)
print("Corrida ID:", corrida_id)
print("Posição Final:", posicao_final)
print("\nParticipação cadastrada!")
