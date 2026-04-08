# ============================================================
# MÓDULO 1: Variables y Tipos de Datos
# ============================================================
# Completá cada función siguiendo las instrucciones.
# NO modifiques los nombres de las funciones ni sus parámetros.
# ============================================================


def crear_saludo(nombre: str) -> str:
    """
    Retorna un saludo personalizado.
    Ejemplo: crear_saludo("Ana") -> "Hola, Ana!"
    """

    """
    Genera un mensaje de saludo personalizado.

    Args:
        nombre (str): El nombre de la persona a saludar.

    Returns:
        str: Un mensaje de saludo con el formato "Hola, [nombre]!".
    """
    return f"Hola, {nombre}!"
    


def suma_enteros(a: int, b: int) -> int:
    """
    Retorna la suma de dos enteros.

    Args:
        a (int): El primer número.
        b (int): El segundo número.

    Returns:
        int: La suma de a y b.
    """
    return a + b


def es_mayor_de_edad(edad: int) -> bool:
    """
    Retorna True si edad >= 18, False caso contrario.
    
    Determina si una persona es mayor de edad (18 años o más).
    
    Args:
        edad (int): La edad de la persona.
        
    Returns:
        bool: True si la edad es mayor o igual a 18, False en caso contrario.
    """
    return edad >= 18


def tipo_de_dato(valor) -> str:
    """
    Retorna el nombre del tipo de dato del valor recibido.
    Ejemplo: tipo_de_dato(42) -> "int"
             tipo_de_dato("hola") -> "str"
    Retorna el nombre del tipo de dato del valor recibido.
    
    Args:
        valor (Any): Un valor de cualquier tipo.
        
    Returns:
        str: El nombre del tipo de dato (por ejemplo, 'int', 'str', 'bool').
    """
    return type(valor).__name__


def convertir_a_float(valor: str) -> float:
    """
    Convierte un string numérico a float.
    Ejemplo: convertir_a_float("3.14") -> 3.14
    
    Convierte una cadena de texto numérica a un número de punto flotante (float).
    
    Args:
        valor (str): Un string que representa un número (ej: "3.14" o "5").
        
    Returns:
        float: El valor convertido a número decimal.
    """
    return float(valor)
