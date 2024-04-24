def divisivelPor2(numero):
    if numero % 2 == 0:
        return True
    else:
        return False






def divisivelPorN(numero, divisor):
    if divisor == 0:
        print("Não é possível efetuar divisão por zero.")
        return False
    elif numero % divisor == 0:
        return True
    else:
        return False
