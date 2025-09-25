import random
import re
def input_cpf():
    while True:
        cpf = input("CPF (com ou sem pontuação): ")
        cpf_limpo = cpf.replace('.', '').replace('-', '')
        if cpf_limpo.isdigit() and len(cpf_limpo) == 11:
            return cpf_limpo  
        
        print("CPF inválido! Digite 11 números (com ou sem pontuação).")
def input_data():
    while True:
        data = input("Data de Nascimento (dd-mm-aaaa): ")
        if re.match(r"^\d{2}-\d{2}-\d{4}$", data):
            return data
        print("Formato inválido! Use dd-mm-aaaa.")

def input_tel():
    while True:
        tel = input("Telefone (DDD+Número, ex: 41999999999): ")
        if tel.isdigit() and len(tel) >= 10:
            return tel
        print("Telefone inválido! Digite DDD + número.")

dados = {
    "Nome": input("Nome: "),
    "Data de Nascimento": input_data(),
    "Telefone": input_tel(),
    "Endereço(rua)": input("Endereço: "),
    "CPF": input_cpf()
}
print("\n--- Cadastro ---")
print("Nome:", dados["Nome"])
print("Data de Nascimento:", dados["Data de Nascimento"])
print("Telefone:", dados["Telefone"])
print("Endereço:", dados["Endereço(rua)"])
print("CPF:", dados["CPF"])
print("ID gerado:", random.randint(1000, 9999))
