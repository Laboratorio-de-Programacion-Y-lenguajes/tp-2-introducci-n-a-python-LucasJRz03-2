# ============================================================
# MÓDULO 7: Operaciones con Strings
# ============================================================


def es_palindromo(texto: str) -> bool:
    """
    Retorna True si el texto es palíndromo (ignorando espacios y mayúsculas).
    Ejemplo: es_palindromo("Anita lava la tina") -> True
    """
    # Limpiamos el texto: pasamos a minúsculas y sacamos los espacios
    texto_limpio = texto.lower().replace(" ", "")
    # Comparamos el texto limpio con su versión invertida usando slicing
    return texto_limpio == texto_limpio[::-1]


def capitalizar_palabras(texto: str) -> str:
    """
    Capitaliza la primera letra de cada palabra.
    Ejemplo: capitalizar_palabras("hola mundo") -> "Hola Mundo"
    """
    # El método .title() de Python hace exactamente esto
    return texto.title()


def contar_vocales(texto: str) -> int:
    """
    Retorna la cantidad de vocales (a,e,i,o,u) en el texto,
    sin distinguir mayúsculas/minúsculas.
    """
    vocales = "aeiou"
    # Usamos una expresión generadora para contar
    return sum(1 for letra in texto.lower() if letra in vocales)


def caesar_cipher(texto: str, desplazamiento: int) -> str:
    """
    Aplica el cifrado César al texto con el desplazamiento dado.
    Solo desplaza letras (a-z, A-Z), los demás caracteres no cambian.
    Ejemplo: caesar_cipher("abc", 1) -> "bcd"
    """
    resultado = ""
    for char in texto:
        if char.isalpha():
            # Definimos la base ASCII (65 para mayúsculas, 97 para minúsculas)
            base = 65 if char.isupper() else 97
            # Aplicamos la fórmula matemática del cifrado con módulo 26 (letras del alfabeto)
            nuevo_char = chr((ord(char) - base + desplazamiento) % 26 + base)
            resultado += nuevo_char
        else:
            # Los caracteres que no son letras se agregan sin cambios
            resultado += char
    return resultado
