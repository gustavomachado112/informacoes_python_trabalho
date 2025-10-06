import random
import re
def input_cpf():
    while True:
        cpf = input("CPF (com ou sem pontuação): ")
        cpf_limpo = cpf.replace('.', '').replace('-', '')
        if cpf_limpo.isdigit() and len(cpf_limpo) == 11:
            return cpf_limpo  
        
        print("CPF invalido! Digite 11 numeros (com ou sem pontuação).")
def input_data():
    while True:
        data = input("Data de Nascimento (dd-mm-aaaa): ")
        if re.match(r"^\d{2}-\d{2}-\d{4}$", data):
            return data
        print("Formato invalido! Use dd-mm-aaaa.")

def input_telefone():
    while True:
        telefone = input("Telefone (DDD+Numero, ex: 41999999999): ")
        if telefone.isdigit() and len(telefone) >= 10:
            return telefone
        print(" Esse telefone  esta invalido! Digite DDD + numero.")

dados = {
    "Nome": input("Nome: "),
    "Data de Nascimento": input_data(),
    "Telefone": input_telefone(),
    "Endereço(rua)": input("Endereço: "),
    "CPF": input_cpf()
}
print("\n Cadastro ")
print("Nome:", dados["Nome"])
print("Data de Nascimento:", dados["Data de Nascimento"])
print("Telefone:", dados["Telefone"])
print("Endereço:", dados["Endereço(rua)"])
print("CPF:", dados["CPF"])
print("ID gerado:", random.randint(1000, 9999))
