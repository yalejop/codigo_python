def run():
    poblacion_paises = {
      'Argentina': 44938712,
      'Brasil': 210147125,
      'Colombia': 50372424,
    }

    #print(poblacion_paises['Argentina'])
    #for pais in poblacion_paises.keys():
        #print(pais)
    #for pais in poblacion_paises.values():
        #print(pais)
    for pais, poblacion in poblacion_paises.items():
        print(pais + ' Tiene ' + str(poblacion) + ' Habitantes')

if __name__ == '__main__':
    run()  