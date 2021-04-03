pesos = input('Cuántos Pesos Colombianos Tienes??: ')

dolar = input('Cuantos dolares tienes??: ')

pesos = float(pesos)

dolar = float(dolar)

dolar_value = 3875

dolares = pesos / dolar_value

peso_value = 3875 * dolar

peso_value = round(peso_value, 3)

dolares = round(dolares, 3)

dolares = str(dolares)

peso_value = str(peso_value)

print('Tienes $' + dolares + ' Dólares')

print('Tienes $' + peso_value + ' Pesos')
