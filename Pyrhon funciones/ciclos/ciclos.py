pwd_user = ("contraseña")
pwd = input("Contraseña:     ")

if pwd == pwd_user and len(pwd)>=8:
    print("acceso concedido")
else:
    print("acceso denegado")

# "len" para definir uuna cantidad de caracterestes