menu = """ 
Bienvenido al conversor de monedas

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input('Cuántos Pesos Colombianos Tienes??: ')
    pesos = float(pesos)
    dolar_value = 3875
    dolares = pesos / dolar_value
    dolares = round(dolares, 3)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' Dólares')
elif opcion == 2:
    pesos = input('Cuántos Pesos Argentinos Tienes??: ')
    pesos = float(pesos)
    dolar_value = 65
    dolares = pesos / dolar_value
    dolares = round(dolares, 3)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' Dólares')
elif opcion == 3:
    pesos = input('Cuántos Pesos Mexicanos Tienes??: ')
    pesos = float(pesos)
    dolar_value = 24
    dolares = pesos / dolar_value
    dolares = round(dolares, 3)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' Dólares')
else:
    print('Ingresa Una opcion Válida por favor')


