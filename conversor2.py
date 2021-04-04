def conversiones(moneda, dolar_value):
    pesos = input('Cuántos Pesos' + moneda + 'Tienes??: ')
    pesos = float(pesos)
    dolares = pesos / dolar_value
    dolares = round(dolares, 3)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' Dólares')


menu = """ 
Bienvenido al conversor de monedas

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversiones('Colombianos', 3875)
elif opcion == 2:
    conversiones('Argentinos', 38)
elif opcion == 3:
    conversiones('Mexicanos', 64)
else:
    print('Ingresa Una opcion Válida por favor')


