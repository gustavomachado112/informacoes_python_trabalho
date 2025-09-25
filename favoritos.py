import random
def cadastrar_favorito():
    print(" CADASTRO DE FAVORITOS ")
    
    favorite_id = random.randint(10000, 99999)
    usuario_id = random.randint(10000, 99999)
    piloto_id = random.randint(10000, 99999)
    equipe_id = random.randint(10000, 99999)
    corrida_id = random.randint(10000, 99999)
    
    print("\n IDs GERADOS ")
    print(f"Favorite ID: {favorite_id}")
    print(f"Usuário ID: {usuario_id}")
    print(f"Piloto ID: {piloto_id}")
    print(f"Equipe ID: {equipe_id}")
    print(f"Corrida ID: {corrida_id}")
    
    return {
        'favorite_id': favorite_id,
        'usuario_id': usuario_id,
        'piloto_id': piloto_id,
        'equipe_id': equipe_id,
        'corrida_id': corrida_id
    }

if __name__ == "__main__":
    favorito = cadastrar_favorito()
    print("\nSeus favoritos foram cadastrados!")
