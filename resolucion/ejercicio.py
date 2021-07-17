import string

def resolucion(palabra):
    # Defino mi variable diccionario con la que voy a trabajar, la cual sera un "diccionario"
    diccionario = {}

    # Funcion para obtener el abecedario completo en minuscula
    def getLetters():
        return list(string.ascii_lowercase)

    # Guardo el abecedario en la variable "arrayLetters"
    arrayLetters = getLetters()

    # Guardo en un arreglo el teclado (para escribir se usa del 2 al 9)
    teclado = []
    for a in range(2, 10):
        teclado.append(str(a))

    # Utilizo el diccionario creado al principio para asociar el numero de veces que se debe apretar la tecla para obtener dicha letra.
    # "a" asociada a "2"
    # "b" asociada a "22" 
    # "j" asociada a "5"
    # "o" asociado a "666"
    # etc...

    cantidad = 1
    valor = "2"

    for n in arrayLetters:       
        diccionario[n] = teclado[teclado.index(valor)] * cantidad
        
        if(cantidad == 3 and valor != "7" and valor != "9"): 
            valor = str(int(valor) + 1)
            cantidad = 0
        elif (cantidad == 4 and (valor == "7" or valor == "9")):
            valor = str(int(valor) + 1)
            cantidad = 0
            
        cantidad = cantidad + 1

    # REALIZO LA CONVERSION !!!
    conversion = ''
    for a in palabra:
        if a != ' ':
            if conversion != '' and conversion[-1] == diccionario[a][0] and diccionario[a][0]:
                conversion = conversion + ' ' + diccionario[a]
            else:
                conversion = conversion + diccionario[a]
        else:
            conversion = conversion + '0'

    # Imprimo por pantalla la conversión realizada en el paso anterior
    print('\b')
    print('INPUT: ', palabra)
    print('OUTPUT: ', conversion)
    print('\b')
    print('--== FIN ==--')

    return conversion


    # --== FIN ==--

