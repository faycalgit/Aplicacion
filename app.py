from funciones import esPrimo

numero = int(input("Escribe un numero> "))
resultado=esPrimo(numero)

if resultado==True:
    print(f"El numero {numero} es primo")
else:
    print(f"El numero {numero} NO es primo")
