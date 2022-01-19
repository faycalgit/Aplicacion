def esPrimo(numero):
    divisores=0
    for i in range(2,numero):
        resto = numero % i
        if resto == 0: 
            divisores=divisores+1
    return divisores == 0