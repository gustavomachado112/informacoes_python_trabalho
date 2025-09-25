import random

def cadastrar_equipe():
    print("=== CADASTRO DE EQUIPE ===")
    equipe_id = str(random.randint(100000, 999999))
    nome = input("Digite o nome da equipe: ")
    pais = input("Digite o país da equipe: ")
    
    while True:
        historia_da_equipe = input("Digite a história da equipe (mínimo 20 caracteres): ")
        if len(historia_da_equipe) >= 20:
            break
        else:
            print("A história precisa ter pelo menos 20 caracteres. Tente novamente.")
    

    patrocinador_id = str(random.randint(100000, 999999))
    print(f"ID do Patrocinador gerado: {patrocinador_id}")
    print("\n=== INFORMAÇÕES RECEBIDAS ===")
    print(f"ID da Equipe: {equipe_id}")
    print(f"Nome: {nome}")
    print(f"País: {pais}")
    print(f"História: {historia_da_equipe}")
    print(f"ID do Patrocinador: {patrocinador_id}")
    
    return {
        'equipe_id': equipe_id,
        'nome': nome,
        'pais': pais,
        'historia_da_equipe': historia_da_equipe,
        'patrocinador_id': patrocinador_id
    }

if __name__ == "__main__":
    equipe = cadastrar_equipe()
    print("\nDados prontos, obrigado por responder!")
