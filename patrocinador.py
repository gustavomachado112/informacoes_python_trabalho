import random
import string

def cadastrar_patrocinador():
    print(" CADASTRO DE PATROCINADOR ")
     
    patrocinador_Id = random.randint(10000, 99999)
    
    nome_do_patrocinador = input("Digite o nome do patrocinador: ")
    setor_do_patrocinador = input("Digite o setor do patrocinador: ")
    anos_de_patrocinio = input("Digite os anos de patrocínio: ")
    valor_de_patrocinio = input("Digite o valor do patrocínio: ")
    
    
    print("\n INFORMACOES RECEBIDAS ")
    print(f"ID Gerado: {patrocinador_Id}")
    print(f"Nome: {nome_do_patrocinador}")
    print(f"Setor: {setor_do_patrocinador}")
    print(f"Anos de Patrocínio: {anos_de_patrocinio}")
    print(f"Valor: {valor_de_patrocinio}")
    
    return {
        'patrocinador_Id': patrocinador_Id,
        'nome_do_patrocinador': nome_do_patrocinador,
        'setor_do_patrocinador': setor_do_patrocinador,
        'anos_de_patrocinio': anos_de_patrocinio,
        'valor_de_patrocinio': valor_de_patrocinio
    }
cadastrar_patrocinador()
