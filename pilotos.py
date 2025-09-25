import random
def cadastrar_piloto():
    print("CADASTRO DE PILOTO ")
    
    piloto_id = random.randint(10000, 99999)
    equipe_id = random.randint(10000, 99999)
    while True:
        nome = input("Digite o nome do piloto: ")
        if nome.strip(): 
            break
        print("Nome é obrigatório! Digite novamente.")
    
    while True:
        nacionalidade = input("Digite a nacionalidade do piloto: ")
        if nacionalidade.strip():  
            break
        print("Nacionalidade é obrigatória! Digite novamente.")
    while True:
        try:
            vitorias = int(input("Digite o número de vitórias: "))
            break
        except:
            print("Digite um número válido para vitórias!")
    recordes = input("Digite os recordes do piloto: ")
    
    while True:
        try:
            titulos = int(input("Digite o número de títulos: "))
            break
        except:
            print("Digite um número válido para títulos!")
    
    print("\n=== INFORMAÇÕES RECEBIDAS ===")
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
