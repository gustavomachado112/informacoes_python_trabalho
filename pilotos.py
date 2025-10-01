import random
def cadastrar_piloto():
    print("CADASTRO DE PILOTO ")
    
    piloto_id = random.randint(10000, 99999)
    equipe_id = random.randint(10000, 99999)
    while True:
        nome = input("Digite o nome do piloto: ")
        if nome.strip(): 
            break
        print("Nome ele e obrigatorio.")
    
    while True:
        nacionalidade = input("Digite a nacionalidade do piloto: ")
        if nacionalidade.strip():  
            break
        print("a nacionalidade e obrigatorio .")
    while True:
        try:
            vitorias = int(input("Digite o número de vitórias: "))
            break
        except:
            print("Digite quantas vitórias.")
    recordes = input("Digite os recordes do piloto: ")
    
    while True:
        try:
            titulos = int(input("Digite o numero de titulos do pilotos: "))
            break
        except:
            print("Digite zero ou  a quantidade de titulos que o piloto tem")
    
    print("\n informacoes recebidas com sucesso. ")
    print(f"Piloto ID: {piloto_id}")
    print(f"Nome: {nome}")
    print(f"Nacionalidade: {nacionalidade}")
    print(f"Equipe ID: {equipe_id}")
    print(f"Vitórias: {vitorias}")
    print(f"Recordes: {recordes}")
    print(f"Títulos: {titulos}")
    
    return {
        'piloto_id': piloto_id,
        'nome': nome,
        'nacionalidade': nacionalidade,
        'equipe_id': equipe_id,
        'vitorias': vitorias,
        'recordes': recordes,
        'titulos': titulos
    }

if __name__ == "__main__":
    piloto = cadastrar_piloto()
    print("\nPiloto cadastrado com sucesso!")
