from resolucion import ejercicio

def main():
    # Inicio el input para que el usuario pueda tipear una palabra o una frase 
    palabra = input('*** Tipear una/s palabra/s para realizar la respectiva conversión: ***\n===> ')
    ejercicio.resolucion(palabra)

if __name__ == "__main__":
    main()