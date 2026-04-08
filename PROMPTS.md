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
  Patrón Paso a paso.
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
    return f"Hola, {nombre}!"
```
*Ejer 2:* 
```def suma_enteros(a: int, b: int) -> int:
    """
    Retorna la suma de dos enteros.

    Args:
        a (int): El primer número.
        b (int): El segundo número.

    Returns:
        int: La suma de a y b.
    """
    return a + b
```
*Ejer 3:*
Receta paso a paso
Definir la función: Usamos def es_mayor_de_edad(edad: int) -> bool:. Esto indica que la función recibe un entero (int) y va a devolver un valor booleano (bool, es decir, True o False).

Documentar: Agregamos el docstring explicando la lógica, qué parámetro recibe y qué retorna.

Evaluar y retornar: En lugar de hacer un bloque if/else tradicional (que ocuparía 4 líneas), podemos devolver directamente el resultado de la evaluación lógica. La expresión edad >= 18 se evalúa sola y da como resultado True o False, por lo que podemos escribir simplemente return edad >= 18.

```python
def es_mayor_de_edad(edad: int) -> bool:
    """
    Determina si una persona es mayor de edad (18 años o más).
    
    Args:
        edad (int): La edad de la persona.
        
    Returns:
        bool: True si la edad es mayor o igual a 18, False en caso contrario.
    """
    return edad >= 18
```
*Ejer 4*
Receta paso a paso
Definir la función: Escribimos `def tipo_de_dato(valor) -> str:`. En este caso, no le ponemos una pista de tipo a valor porque, como dice tu requisito, puede recibir cualquier tipo de dato.

Documentar: Abrimos comillas triples y escribimos el docstring detallando el comportamiento esperado.

Obtener el tipo: Usamos la función integrada type(valor). Si a esa función le pasás un entero, te devuelve `<class 'int'>`.

Extraer solo el nombre (opcional pero más limpio): Aunque podríamos devolver str(type(valor)), si queremos devolver estrictamente el nombre puro `(ej: "int", "str", "list")`, podemos acceder al atributo `__name__` de la clase. Por lo tanto, usaremos type(valor).`__name__.`

Retornar el resultado: Anteponemos return a la expresión del paso 4.
```python
def tipo_de_dato(valor) -> str:
    """
    Retorna el nombre del tipo de dato del valor recibido.
    
    Args:
        valor (Any): Un valor de cualquier tipo.
        
    Returns:
        str: El nombre del tipo de dato (por ejemplo, 'int', 'str', 'bool').
    """
    return type(valor).__name__
```
*Ejer 5*
Receta paso a paso
Definir la función: Usamos `def convertir_a_float(valor: str) -> float:`. Las pistas de tipo indican que la función espera recibir una cadena de texto (str) y va a devolver un número con decimales (float).

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
 `Gemini AI`

**Prompt usado** 
**Ejer 1 al 4 (Agrupados)**
Interaccion invertida 
> **Usuario:** Quiero implementar cuatro funciones con condicionales en Python: `clasificar_numero`, `mayor_de_tres`, `clasificar_nota` y `es_bisiesto`. Antes de escribir el código, haceme 3 preguntas para confirmar enfoques y prioridades lógicas.
>
> **IA:** ¡Perfecto! Antes de codear, confirmame esto:
> 1. Para `mayor_de_tres`, ¿puedo usar la función nativa `max()` o preferís que use condicionales `if/elif/else` para practicar la lógica?
> 2. Para `clasificar_nota`, el orden de las evaluaciones importa mucho. ¿Estás de acuerdo con evaluar de mayor a menor (ej: primero >= 9, luego >= 7) para que las notas no se pisen?
> 3. Para `es_bisiesto`, ¿preferís una sola línea con operadores lógicos (`and`, `or`) o una estructura `if/elif/else` clara paso a paso?
>
> **Usuario:** 
> 1. Usá condicionales puros (if/elif/else), nada de max().
> 2. Sí, evaluá de mayor a menor para evitar bugs.
> 3. Usá if/elif/else claro, evaluando primero la regla de los 400 años que es la más estricta.

> 

**Resultado obtenido**:
(Se generaron las 4 funciones utilizando estrictamente estructuras de control de flujo `if/elif/else`, documentadas con docstrings).

```python

def clasificar_numero(n: int) -> str:
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "cero"

def mayor_de_tres(a: int, b: int, c: int) -> int:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def clasificar_nota(nota: float) -> str:
    if nota >= 9:
        return "Sobresaliente"
    elif nota >= 7:
        return "Bueno"
    elif nota >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"

def es_bisiesto(anio: int) -> bool:
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False
```

**¿Lo usaste tal cual o lo modificaste**
 > Usado tal cual. 

### 3 - listas.py

**Herramienta**: 
 `Gemini AI`
**Prompt usado**:
> Estoy resolviendo un ejercicio de manipulación de listas en Python con estas 5 funciones:
> 1. `suma_lista`: devuelve la suma total.
> 2. `filtrar_pares`: devuelve solo los pares.
> 3. `invertir_lista`: invierte sin modificar la original.
> 4. `eliminar_duplicados`: borra repetidos manteniendo el orden.
> 5. `aplanar_lista`: convierte lista de listas en una sola.
> 
> ¿Podés revisar mi lógica como verificador cognitivo?
> - Enumerá casos borde que debería testear (ej: listas vacías).
> - Decime errores típicos (ej: mutar la lista original al invertir).
> - Proponé tests con entradas y salidas esperadas.
> - Una vez verificado esto, escribí el código final validando estas reglas.
> 

**Resultado obtenido**:
(El asistente validó casos borde como listas vacías, advirtió sobre no usar métodos destructivos como `.reverse()`, y luego generó el código final usando `sum()`, comprensión de listas y slicing `[::-1]` para asegurar la inmutabilidad).

```python
def suma_lista(numeros: list) -> int | float:
    return sum(numeros)

def filtrar_pares(numeros: list) -> list:
    return [n for n in numeros if n % 2 == 0]

def invertir_lista(lista: list) -> list:
    return lista[::-1]

def eliminar_duplicados(lista: list) -> list:
    resultado = []
    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)
    return resultado

def aplanar_lista(lista: list) -> list:
    resultado = []
    for sublista in lista:
        resultado.extend(sublista)
    return resultado
```

**¿Lo usaste tal cual o lo modificaste?**
Tal cual

---

### 4 - diccionarios.py


**Herramienta**: 
`Gemini AI`
**Prompt usado**:
> Generá 5 ejemplos distintos de cómo se comportan estas operaciones de diccionarios en Python:
> 1. Contar frecuencias de palabras en textos con mayúsculas y minúsculas mezcladas.
> 2. Invertir diccionarios (intercambiar claves por valores).
> 3. Fusionar dos diccionarios donde hay claves que se pisan.
> 4. Filtrar diccionarios reteniendo solo valores numéricos mayores o iguales a un límite.
>
> Para cada ejemplo, mostrámelo con entradas y salidas esperadas. Luego, extraé una regla general o enfoque eficiente para implementar en Python las funciones `contar_palabras`, `invertir_diccionario`, `merge_diccionarios` y `filtrar_por_valor`. Generá el código final con docstrings basado en esos patrones.
> 

**Resultado obtenido**:
```python
def contar_palabras(texto: str) -> dict:
    palabras = texto.lower().split()
    frecuencias = {}
    for p in palabras:
        frecuencias[p] = frecuencias.get(p, 0) + 1
    return frecuencias

def invertir_diccionario(d: dict) -> dict:
    return {valor: clave for clave, valor in d.items()}

def merge_diccionarios(d1: dict, d2: dict) -> dict:
    return d1 | d2

def filtrar_por_valor(d: dict, minimo: int) -> dict:
    return {clave: valor for clave, valor in d.items() if valor >= minimo}
```

**¿Lo usaste tal cual o lo modificaste?**
>Usado tal cual. 

---

### 5 - loops.py

**Herramienta**: 
`Gemini AI`
**Prompt usado**:
Patron: Refinamiento de preguntas
> P1: ¿Cómo puedo usar loops en Python para generar secuencias numéricas (como contar hasta N o tablas de multiplicar) y devolver listas?
> P2: ¿Cuál es la forma más eficiente de usar loops para sumar los dígitos de un número entero o evaluar si un número es primo iterando sus divisores?
> P3: En el caso de la secuencia de Fibonacci iterativa, ¿cómo manejo los casos base si me piden generar los primeros N números y N es muy chico (ej: 0 o 1)?
> P4: Teniendo en cuenta mis preguntas anteriores, mostrame la implementación óptima en Python para estas cinco funciones usando loops y rangos: `contar_hasta`, `tabla_multiplicar`, `suma_digitos`, `es_primo` y `fibonacci`.
> 

**Resultado obtenido**:
(El asistente fue refinando la lógica en cada paso, optando por comprensiones de listas cuando era más limpio, iterando sobre la raíz cuadrada para optimizar la validación de números primos, y manejando correctamente los casos de N pequeños en la sucesión de Fibonacci antes de mostrar el código definitivo).

```python
def contar_hasta(n: int) -> list:
    return list(range(1, n + 1))

def tabla_multiplicar(n: int) -> list:
    return [n * i for i in range(1, 11)]

def suma_digitos(n: int) -> int:
    suma = 0
    for digito in str(n):
        suma += int(digito)
    return suma

def es_primo(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n: int) -> list:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    resultado = [0, 1]
    for _ in range(2, n):
        resultado.append(resultado[-1] + resultado[-2])
    return resultado
```

**¿Lo usaste tal cual o lo modificaste?**
> Tal cual

---

### 6 - funciones.py

**Herramienta**: 
`Gemini AI`
**Prompt usado**:
> Necesito implementar 4 funciones de orden superior y programación funcional en Python para un TP: `aplicar_funcion`, `componer`, `memoizar` y `reducir`.
> Antes de escribir el código, quiero comparar enfoques para `memoizar` y `reducir`:
> 1. Para `memoizar`, analizá pros/contras de usar el decorador `lru_cache` de functools vs. crear un closure manual con un diccionario `cache = {}`.
> 2. Para `reducir`, analizá pros/contras de hacerlo con recursión vs. un bucle `for` tradicional.
> 
> Analizá performance, simplicidad y restricciones del TP (no usar `functools.reduce`). Luego recomendá un enfoque para cada uno y escribí el código final con docstrings para las 4 funciones.
> 

**Resultado obtenido**:
(El asistente reflexionó indicando que, aunque `lru_cache` es más robusto para memoización, construir un closure manual es mejor para aprender el concepto en un TP. Para la reducción, recomendó el bucle iterativo sobre la recursión para evitar el límite de profundidad y mejorar la legibilidad. Luego generó el código usando lambdas y comprensiones de listas donde era oportuno).

```python
def aplicar_funcion(lista: list, func) -> list:
    return [func(elemento) for elemento in lista]

def componer(f, g):
    return lambda x: f(g(x))

def memoizar(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def reducir(lista: list, func, inicial):
    acumulador = inicial
    for elemento in lista:
        acumulador = func(acumulador, elemento)
    return acumulador
```

**¿Lo usaste tal cual o lo modificaste?**
> Tal cual

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
