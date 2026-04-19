def get_int(mensaje:str, mensaje_error: str, minimo: int, maximo: int, reintentos: int) -> int|None:
   """ Pide un numero al usuario

    Args: 
         mensaje: El mensaje que se imprime antes de que el usuario ingrese un numero
         mensaje_error: Mensaje de error en caso de que el dato ingresado sea invalido
         minimo (int): Valor minimo admitido 
         maximo (int): Valor maximo admitido
         reintentos (int): Cantidad de veces que se volvera a pedir el dato 

    Returns:
        int: None 

    """
   while reintentos > 0:
      numero = input(mensaje)
      if numero.isnumeric():
         numero = int(numero)

         if minimo <= numero <= maximo:
            return numero
         
      print(mensaje_error)

      from des import get_int

numero = get_int("Ingrese un numero del 1 al 10:", "Numero incorrecto", 1, 10, 3)

                

if numero != None:
    print("Igresaste:", numero) 
else:
    print("Superaste los reintentos")


print("resultado:", numero)
   
      reintentos -= 1

   return None

