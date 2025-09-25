import random, re

def input_data():
    while True:
        d = input("Data da sessão (dd-mm-aaaa): ")
        if re.match(r"^\d{2}-\d{2}-\d{4}$", d):
            return d
        print("Formato inválido! Use dd-mm-aaaa.")

def input_duracao():
    while True:
        try:
            duracao = int(input("Duração da sessão (minutos): "))
            if duracao > 0:
                return duracao
            else:
                print("Duração deve ser maior que zero!")
        except:
            print("Digite um número válido.")
treino_id = random.randint(10000, 99999)
corrida_id = random.randint(10000, 99999)
data_sessao = input_data()
duracao_sessao = input_duracao()


print("\n--- Sessão de Treino ---")
print("Treino ID:", treino_id)
print("Corrida ID:", corrida_id)
print("Data da Sessão:", data_sessao)
print("Duração (minutos):", duracao_sessao)


