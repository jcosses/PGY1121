# EJEMPLO DE USO DE REPOSITORIO

print("DATOS PERSONALES")
print("----------------\n")
vNom = input("Ingrese su Nombre: ")
while True:
    try:
        vEdad = int(input("Ingrese su Edad: "))
    except:
        print("Valor no Corresponde")
print("---------------------------")
print(f"Su Nombres es: {vNom}")
print(f"Su Edad es: {vEdad}")
print("I LOVE FORTNITE")
print("Programa Finalizado....")
