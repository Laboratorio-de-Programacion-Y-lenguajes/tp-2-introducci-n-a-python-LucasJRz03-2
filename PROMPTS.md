# Registro de Prompts

En este archivo debés documentar los prompts que usaste con herramientas de IA
(GitHub Copilot, ChatGPT, etc.) durante el desarrollo del TP.

**¿Por qué?** Queremos que aprendas a trabajar con IA de forma reflexiva:
que sepas qué le pediste, qué obtuviste, y si tuviste que corregirlo.

---

## Formato para cada entrada

```
### [Número] - [Módulo]

**Herramienta**: GitHub Copilot / ChatGPT / otra

**Prompt usado**:
> Escribí acá exactamente lo que le pediste a la IA

**Resultado obtenido**:
Describí brevemente qué generó (código, explicación, etc.)

**¿Lo usaste tal cual o lo modificaste?**
Explicá qué cambios hiciste y por qué (o por qué no cambiaste nada).
```

---

## Mis prompts

### 1 - variables.py

**Herramienta**: 
 `Gemini AI`

**Prompt usado**:
 **Ejer 1:**
  Patrón: Paso a paso.
 `crear_saludo(nombre: str) -> str:`
  > Requisitos:
  >1.Recibir un nombre como parámetro.
  >2.Devolver un string con el formato "Hola, [nombre]!".
  >3.Usar f-strings para formatear el texto.
  >No uses librerías externas. Mostrame el código final con su docstring.**

 **Ejer 2:**
 Patrón: Receta.
  >Quiero una receta paso a paso para crear una función `suma_enteros(a:int, b: int) -> int`. 
  >Requisitos: 
  >1.Recibir 2 parámetros enteros(a y b).
  >2.Retornar la suma de ambos.
  >3.Incluir docString. Mostramelo en el código final. 

 **Ejer 3:** 
 Patrón: Paso a paso
 >Actúa como tutor de Python. Quiero definir una función `es_mayor_de_edad(edad: int) -> bool` para saber si una persona es o no es mayor de edad.
 Requisitos:
 1.recibir un parametro de tipo entero.
 2.retornar true si es mayor o igual a 18, en caso contrarío retornar falso.
 3.Incluir docString en el código. 

 **Ejer 4:**
 Patron: Receta.
 actúa como un tutor de Python y crea una función `tipo_de_dato(valor) -> str:` que retorne el nombre del tipo de dato del valor recibido.
Requisito:
>1.Que reciba un valor (de cualquier tipo).
>2.Que devuelva un str (texto) del tipo de dato del valor recibido.
>3.Incluir docString en el código.


*Ejer 5*
Patron: paso a paso. 
convertir_a_float(valor:str) -> float:
Requisito:
1.convierte un string númerico a float.
2.docString incluido

> 


**Resultado obtenido**:

*Ejer 1:*
```def crear_saludo(nombre: str) -> str:
    """
    Genera un mensaje de saludo personalizado.

    Args:
        nombre (str): El nombre de la persona a saludar.

    Returns:
        str: Un mensaje de saludo con el formato "Hola, [nombre]!".
    """
    return f"Hola, {nombre}!"```

*Ejer 2:* 
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

*Ejer 3:*
Receta paso a paso
Definir la función: Usamos def es_mayor_de_edad(edad: int) -> bool:. Esto indica que la función recibe un entero (int) y va a devolver un valor booleano (bool, es decir, True o False).

Documentar: Agregamos el docstring explicando la lógica, qué parámetro recibe y qué retorna.

Evaluar y retornar: En lugar de hacer un bloque if/else tradicional (que ocuparía 4 líneas), podemos devolver directamente el resultado de la evaluación lógica. La expresión edad >= 18 se evalúa sola y da como resultado True o False, por lo que podemos escribir simplemente return edad >= 18.

def es_mayor_de_edad(edad: int) -> bool:
    """
    Determina si una persona es mayor de edad (18 años o más).
    
    Args:
        edad (int): La edad de la persona.
        
    Returns:
        bool: True si la edad es mayor o igual a 18, False en caso contrario.
    """
    return edad >= 18

*Ejer 4*
Receta paso a paso
Definir la función: Escribimos `def tipo_de_dato(valor) -> str:`. En este caso, no le ponemos una pista de tipo a valor porque, como dice tu requisito, puede recibir cualquier tipo de dato.

Documentar: Abrimos comillas triples y escribimos el docstring detallando el comportamiento esperado.

Obtener el tipo: Usamos la función integrada type(valor). Si a esa función le pasás un entero, te devuelve `<class 'int'>`.

Extraer solo el nombre (opcional pero más limpio): Aunque podríamos devolver str(type(valor)), si queremos devolver estrictamente el nombre puro `(ej: "int", "str", "list")`, podemos acceder al atributo `__name__` de la clase. Por lo tanto, usaremos type(valor).`__name__.`

Retornar el resultado: Anteponemos return a la expresión del paso 4.
def tipo_de_dato(valor) -> str:
    """
    Retorna el nombre del tipo de dato del valor recibido.
    
    Args:
        valor (Any): Un valor de cualquier tipo.
        
    Returns:
        str: El nombre del tipo de dato (por ejemplo, 'int', 'str', 'bool').
    """
    return type(valor).__name__

*Ejer 5*
Receta paso a paso
Definir la función: Usamos def convertir_a_float(valor: str) -> float:. Las pistas de tipo indican que la función espera recibir una cadena de texto (str) y va a devolver un número con decimales (float).

Documentar: Abrimos comillas triples y escribimos el docstring explicando qué hace, qué recibe y qué retorna.

Convertir el tipo de dato: Usamos la función nativa de Python float(), pasándole la variable valor como argumento. Esto toma el texto (por ejemplo, "3.14") y lo transforma en un número decimal matemático (3.14).

Retornar el resultado: Anteponemos la palabra reservada return para devolver el valor ya convertido.
**¿Lo usaste tal cual o lo modificaste?**
 >Ejer 1: Sin modificar. 
 >Ejer 2: Sin modificar. 
 >Ejer 3: Sin modificar.
 >Ejer 4: Sin modificar.
 >Ejer 5: Sin modificar.
---

### 2 - condicionales.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 3 - listas.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 4 - diccionarios.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 5 - loops.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 6 - funciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

### 7 - operaciones.py

**Herramienta**: 

**Prompt usado**:
> 

**Resultado obtenido**:


**¿Lo usaste tal cual o lo modificaste?**


---

## Reflexión final

Respondé brevemente (3-5 oraciones):

- ¿Qué aprendiste sobre cómo formular buenos prompts?
- ¿En qué casos la IA fue útil y en cuáles no?
- ¿Qué harías diferente la próxima vez?
