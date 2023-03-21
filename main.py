import secrets
import string

itens = (string.ascii_letters + string.digits)

senha = [secrets.choice(itens)
         for i in range(20)]
senha = ''.join(senha)

print(senha)