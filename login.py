import random, re
def input_email():
    while True:
        e = input("Email: ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", e):
            return e
        print("Email inválido!")

def input_senha():
    while True:
        s = input("Senha (mín 6 chars): ")
        if len(s) >= 6:
            return s
        print("Senha curta demais!")
uuario_id = random.randint(10000, 99999)


print("\n--- Criar login ---")
email = input_email()
senha = input_senha()
login_id = random.randint(10000, 99999)

print("\n--- IDs Gerados ---")
print("User ID:", usuario_id)
print("Login ID:", login_id)
print("Email:", email)
print("Senha:", '*' * len(senha)) 
