import random, re
def input_email():
    while True:
        e = input("Email: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", e):
            return e
        print("Email invalido!")

def input_senha():
    while True:
        s = input("Senha (minima 6 letras): ")
        if len(s) >= 6:
            return s
        print("Senha curta demais!")
usuario_id = random.randint(10000, 99999)

print("\n Criar login ")
email = input_email()
senha = input_senha()
login_id = random.randint(10000, 99999)

print("\n- ID Gerado ")
print("User ID:", usuario_id)
print("Login ID:", login_id)
print("Email:", email)
print("Senha:", '*' * len(senha)) 
