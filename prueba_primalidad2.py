def es_primo(numero):
    for i in range(1, numero + 1):
        divisor = numero / i
        cociente = numero % i
        if divisor <= cociente:
            return True
        else:
            return False


def run():
    numero = int(input('PorFavor escribe un número: '))
    if es_primo(numero):
        print('Es Primo')
    else:
        print('No es Primo')
if __name__ == '__main__':
    run()
