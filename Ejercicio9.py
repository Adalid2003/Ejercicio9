entrada = input("Ingrese un valor: ")

try:
    numero = int(entrada)
    print(numero)
except ValueError:
    pass

print("Fin de la ejecución")
