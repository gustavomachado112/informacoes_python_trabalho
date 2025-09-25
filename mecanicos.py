import random
def cadastrar_mecanico():
    print("=== CADASTRO DE MECÂNICO ===")
    mecanico_id = random.randint(10000, 99999)
    equipe_id = random.randint(10000, 99999)
    nome_do_mecanico = input("Digite o nome do mecânico: ")
  
    while True:
        especialidade_do_mecanico = input("Digite a especialidade do mecânico: ")
        if especialidade_do_mecanico.strip(): 
            break
        print("Especialidade é obrigatória! Digite novamente.")
    
    print("\n=== INFORMAÇÕES RECEBIDAS ===")
    print(f"ID do Mecânico: {mecanico_id}")
    print(f"Nome: {nome_do_mecanico}")
    print(f"Especialidade: {especialidade_do_mecanico}")
    print(f"ID da Equipe: {equipe_id}")
    
    return {
        'mecanico_id': mecanico_id,
        'nome_do_mecanico': nome_do_mecanico,
        'especialidade_do_mecanico': especialidade_do_mecanico,
        'equipe_id': equipe_id
    }
if __name__ == "__main__":
    mecanico = cadastrar_mecanico()
    print("\nMecânico cadastrado com sucesso!")
