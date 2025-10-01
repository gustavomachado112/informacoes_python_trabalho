import random
def cadastrar_penalidade():
    print(" CADASTRO DE PENALIDADE ")
    
    penalidade_id = random.randint(10000, 99999)
    piloto_id = random.randint(10000, 99999)
    
    while True:
        descricao_da_punicao = input("Digite a descrição do que aconteceu pra ocorrer a punicao: ")
        if descricao_da_punicao.strip():  
            break
        print("Descrição ela e obrigatoria.")
        
    while True:
        try:
            pontos_tomados_na_carteira = int(input("Digite os pontos que o piloto ira tomar na carteira: "))
            break
        except:
            print("Digite os pontos pro piloto")
    
    while True:
        try:
            avisos = int(input("Digite o total de aviso que ele recebeu: "))
            break
        except:
            print("Digite a quantidade que ele recebeu")
    print("\n informacoes recebidas")
    print(f"Penalidade ID: {penalidade_id}")
    print(f"Piloto ID: {piloto_id}")
    print(f"Descrição da Punicação: {descricao_da_punicao}")
    print(f"Pontos na Carteira: {pontos_tomados_na_carteira}")
    print(f"Avisos: {avisos}")
    
    return {
        'penalidade_id': penalidade_id,
        'piloto_id': piloto_id,
        'descricao_da_punicao': descricao_da_punicao,
        'pontos_tomados_na_carteira': pontos_tomados_na_carteira,
        'avisos': avisos
    }

if __name__ == "__main__":
    penalidade = cadastrar_penalidade()
    print("\nPenalidade cadastrada com sucesso!")
