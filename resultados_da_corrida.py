import random
print(" CADASTRO DE RESULTADO DA CORRIDA ")

resultado_id = random.randint(10000, 99999)
corrida_id = random.randint(10000, 99999)
piloto_id = random.randint(10000, 99999)

while True:
    tempo_total = input("Tempo total (ex: 00:00:00): ").strip() 
    if tempo_total and len(tempo_total) == 8:
        break
    print("Campo e obrigatorio , digite os 8 digitos")
    
while True:
    try:
        pontos_somados = int(input("Pontos somados: "))
        if pontos_somados >=0:
            break
        else:
            print("Pontos devem ser de acordo com a corrida")
    except:
        print("Campo e obrigatorio , digite os 8 digitos")
print("\nResultado ID:", resultado_id)
print("Corrida ID:", corrida_id)
print("Piloto ID:", piloto_id)
print("Tempo:", tempo_total)
print("Pontos:", pontos_somados)
print("\nCadastro feito!")
