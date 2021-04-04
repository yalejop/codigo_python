#def imprimir_mensaje():
 #   print('Mensaje especial:')
 # print('Estoy Aprendiendo a usar funciones!')


#imprimir_mensaje()
#imprimir_mensaje()

def conversacion(mensaje):
    print('Hola')
    print('Cómo Estás? ')
    print(mensaje)
    print('Adios')



opcion = int(input('Elige una opción (1, 2, 3): '))
if opcion == 1:
    conversacion('Elegiste la Opción 1')
elif opcion == 2:
    conversacion('Elegiste la Opción 2')
elif opcion == 3:
    conversacion('Elegiste la Opción 3')
else:
    print('Debes Elegir una Opción correcta')