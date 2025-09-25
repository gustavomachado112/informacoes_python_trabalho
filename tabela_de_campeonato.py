import random

print(" CADASTRO DE CAMPEONATO ")
construct_id = random.randint(10000, 99999)
equipe_id = random.randint(10000, 99999)
piloto_id = random.randint(10000, 99999)
resultado_id = random.randint(10000, 99999)

while True:
    pontos_equipe = int(input("Pontos da equipe: "))
    if pontos_equipe >= 0:
        break
    print("Pontos devem ser zero ou maior!")

while True:
    pontos_piloto = int(input("Pontos do piloto: "))
    if pontos_piloto >= 0:
        break
    print("Pontos devem ser zero ou maior!")

print("\n=== INFORMAÇÕES ===")
print("Construct ID:", construct_id)
print("Equipe ID:", equipe_id)
print("Piloto ID:", piloto_id)
print("Resultado ID:", resultado_id)
print("Pontos Equipe:", pontos_equipe)
print("Pontos Piloto:", pontos_piloto)
print("\nCadastro feito!")
