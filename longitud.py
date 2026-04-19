def get_string(longitud: int) -> str|None:
    """Validar la longitud de la cadena 

    Args:
        longitud (int): Cantidad de caracteres 

    Returns:
        str|None: Retorna None
    
    """
    def validar_longitud(texto):
        if len(texto) >= 6:
            return True
        else:
            return False
        
    cadena = input("Ingrese una palabra:")

    if validar_longitud(cadena):
        print("Longitud valida:")
    else:
        print("Debe ingresar al menos 6 caracteres")

    get_string = None