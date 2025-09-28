# =========================================================
# importaciones iniciales
# =========================================================

from functools import reduce
import math

# =========================================================
# 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena.
#  Los espacios no deben ser considerados.
# =========================================================

def frecuencia_letras(cadena):
    """
    Calcula la frecuencia de cada letra en la cadena, ignorando espacios.

    Args:
        cadena (str): Texto de entrada.

    Returns:
        dict: Diccionario con letras como claves y su frecuencia como valores.
    """
    cadena_sin_espacios = cadena.replace(" ", "")
    frecuencias = {}
    
    for caracter in cadena_sin_espacios:
        frecuencias[caracter] = frecuencias.get(caracter, 0) + 1

    return frecuencias

# =========================================================
# 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
# =========================================================

def duplicar_valores(lista_numeros):
    """
    Devuelve una nueva lista con el doble de cada número usando map().

    Args:
        lista_numeros (list): Lista de números (int o float) a procesar.

    Returns:
        list: Lista con los valores originales multiplicados por 2.
    """
    # map() aplica la función lambda a cada elemento de lista_numeros
    
    return list(map(lambda x: x * 2, lista_numeros))

# =========================================================
# 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista 
# con todas las palabras de la lista original que contengan la palabra objetivo.
# =========================================================

def filtrar_palabras_objetivo(lista_palabras, palabra_objetivo):
    """
    Filtra las palabras que contienen la palabra objetivo.

    Args:
        lista_palabras (list): Lista de palabras a analizar.
        palabra_objetivo (str): Texto a buscar dentro de cada palabra.

    Returns:
        list: Lista con las palabras que contienen la palabra objetivo.
    """
    
    palabras_filtradas = []

    for palabra in lista_palabras:
      
        if palabra_objetivo in palabra:
            palabras_filtradas.append(palabra)

    return palabras_filtradas

# =========================================================
# 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()
# =========================================================

def diferencia_listas (lista1, lista2):
    """
    Calcula la diferencia entre valores de dos listas (lista1 - lista2) 

    Args:
        lista1 (list): Primera lista de números (int o float).
        lista2 (list): Segunda lista de números (int o float).

    Returns:
        list: Lista con las diferencias elemento a elemento.
    """
    return list(map(lambda a, b: a-b, lista1, lista2))

# =========================================================
# 5. Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe 
# calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", 
# de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado
# =========================================================

def evaluar_nota (lista_numeros, nota_aprobado = 5):
    """
    Calcula la media de una lista de números y determina el estado.

    Args:
        lista_numeros (list): Lista de números .
        nota_aprobado (int or float, opcional): Nota mínima para aprobar. Por defecto es 5.

    Returns:
        tuple: (media, estado) 
    """

    media = sum(lista_numeros) / len(lista_numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    
    return media, estado

# =========================================================
# 6. Escribe una función que calcule el factorial de un número de manera recursiva
# =========================================================

def factorial(numero):
    """
    Calcula el factorial de un número de forma recursiva.

    Args:
        n (int): Número entero.

    Returns:
        int: Factorial de n.
    """
    if numero < 0:
        raise ValueError("El número debe ser entero no negativo.")
    
    if numero == 0:
        return 1

    resultado = numero * factorial(numero - 1)
    
    return resultado

# =========================================================
# 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()
# =========================================================

def tupla_a_string(lista_tuplas):
    """

    Convierte una lista de tuplas en una lista de strings.

    Args:
        lista_tuplas (list): Lista de tuplas

    Returns:
        list: Lista de strings
    """


    return list(map(lambda t: ",".join(map(str, t)), lista_tuplas))

# =========================================================
# 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, 
# maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.
# =========================================================

def dividir_numeros():
    """
    Pide dos números al usuario e intenta dividirlos.
    Maneja errores de valor no numérico y división por cero.
    """
    try:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))

        resultado = a / b

    except ValueError:
        print("Error: Debes introducir valores numéricos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
    else:
        print(f"División correcta. El resultado de la división es {resultado}")
    finally:
        print("Fin de la ejecución.")


# =========================================================
# 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas 
# en España. La lista de mascotas a excluir es ["Mapache", "Tigre","Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()
# =========================================================

def filtrar_mascotas_prohibidas(lista_mascotas):
    """
    Filtra una lista de mascotas, excluyendo aquellas prohibidas en España.

    Args:
        lista_mascotas (list): Lista con nombres de mascotas.

    Returns:
        list: Lista con las mascotas permitidas.
    """

    #constante con la lista de mascotas prohibidas
    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]


    return list(filter(lambda mascota: mascota not in mascotas_prohibidas, lista_mascotas))

# =========================================================
# 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente
# =========================================================


def promedio(lista_numeros):
    """
    Calcula el promedio de una lista de números.

    Args:
        lista_numeros (list): Lista de números.

    Returns:
        float: Promedio de los valores de la lista.

    Raises:
        ValueError: Si la lista está vacía.
    """

    try:

        if not lista_numeros:
            raise ValueError("No se puede calcular el promedio de una lista vacía.")
        
        return sum(lista_numeros) / len(lista_numeros)

    except ValueError as e:
        print("Error:", e)


# =========================================================
# 11.  Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado
#  (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones adecuadamente.
# =========================================================

def pedir_edad():
    """
    Pide al usuario su edad, controlando que el valor introducido sea correcto.

    Args:
        Ninguno (solicita input al usuario).

    Returns:
        int | None: La edad válida introducida, o None si ocurrió un error.
    """
    try:
       
        edad = int(input("Introduce tu edad: "))

        # Validamos que esté en el rango esperado
        if edad < 0 or edad > 120:
            raise ValueError("Fuera de rango")

    except ValueError as e:
    # Distinguimos el mensaje de error
        if str(e) == "Fuera de rango":
            print("Error: La edad debe estar entre 0 y 120.")
        else:
            print("Error: Debes introducir un valor numérico válido.")
        return None
    else:
        print("Edad registrada correctamente.")
        return edad
    finally:
        print("Fin de la ejecución.")


# =========================================================
# 12.Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()
# =========================================================

def longitud_palabras(frase):
    """
    Devuelve una lista con la longitud de cada palabra en la frase.

    Args:
        frase (str): Texto con una o más palabras separadas por espacios.

    Returns:
        list: Lista de enteros representando la longitud de cada palabra.
    """
    palabras = frase.split()  
    return list(map(len, palabras)) 

# =========================================================
# 13.Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas.
# Las letras no pueden estar repetidas .Usa la función
# =========================================================

def tupla_mayus_minus(conjunto_caracteres):
    """
    Genera una lista de tuplas (mayúscula, minúscula) para cada carácter único.

    Args:
        conjunto_caracteres: Conjunto de caracteres.

    Returns:
        list: Lista de tuplas con cada carácter en mayúscula y minúscula.
    """

    # Usamos set() para eliminar repetidos. Ademas lo pasamos a minúsculas para unificar y quiter bien los repetidos
    caracteres_unicos = set(c.lower() for c in conjunto_caracteres)

    return list(map(lambda caracter: (caracter.upper(), caracter.lower()), caracteres_unicos))

# =========================================================
# 14.Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter()
# =========================================================

def filtrar_por_letra(lista_palabras, letra):
    """
    Devuelve las palabras que comienzan con la letra especificada.

    Args:
        lista_palabras (list): Lista de palabras (str).
        letra (str): Letra inicial a buscar.

    Returns:
        list: Lista de palabras que empiezan con la letra dada.
    """
    return list(filter(lambda palabra: palabra.startswith(letra), lista_palabras))


# =========================================================
# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
# =========================================================

def sumar_tres(lista_numeros):
    """
    Devuelve una nueva lista sumando 3 a cada número.

    Args:
        lista_numeros (list): Lista de números (int o float).

    Returns:
        list: Lista con los valores sumando 3.
    """

    try:
        return list(map(lambda x: x + 3, lista_numeros))    
    
    except TypeError:
        print("Error: la lista debe contener solo valores numéricos.")
        return []
    
    
# =========================================================
# 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que 
# sean más largas que n. Usa la función filter()
# =========================================================

def palabras_mas_largas(cadena, n):
    """
    Devuelve las palabras de la cadena que tienen longitud mayor a n.

    Args:
        cadena (str): Texto de entrada.
        n (int): Longitud mínima que deben superar las palabras.

    Returns:
        list: Lista de palabras con longitud mayor que n.
    """
    try:
        n = int(n)  # intentamos asegurar que sea un entero
    except Exception:
        print("Error: n debe ser un número entero.")
        return []

    palabras = cadena.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))


# =========================================================
# 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 
# quinientos setenta y dos (572). Usa la función reduce()
# =========================================================

def lista_a_numero(digitos):
    """
    Convierte una lista de dígitos en el número correspondiente.

    Args:
        digitos (list): Lista de enteros de un solo dígito (0–9).

    Returns:
        int: Número formado por los dígitos de la lista.
    """
    
    try:
        # Intentamos convertir todos los elementos a int
        digitos = [int(d) for d in digitos]

        # Validamos que sean entre 0 y 9
        for d in digitos:
            if d < 0 or d > 9:
                raise ValueError(f"{d} no es un dígito válido (0–9).")

        return reduce(lambda acc, elemento: acc * 10 + elemento, digitos)


    except Exception as e:
        print("Error:", e)
        return None
    

# =========================================================
# 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes (nombre, edad, calificación) 
# y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90. Usa la función filter()
# =========================================================

def filtrar_estudiantes(estudiantes):
    """
    Filtra los estudiantes con calificación >= 90.

    Args:
        estudiantes (list): Lista de diccionarios con claves 'nombre', 'edad', 'calificacion'.

    Returns:
        list: Lista de estudiantes que cumplen la condición.
    """
    return list(filter(lambda est: est["calificacion"] >= 90, estudiantes))


# Ejemplo de uso

estudiantes = [
    {"nombre": "Maria", "edad": 20, "calificacion": 95},
    {"nombre": "Raul", "edad": 22, "calificacion": 85},
    {"nombre": "Marc", "edad": 21, "calificacion": 90},
    {"nombre": "Marta", "edad": 23, "calificacion": 70}
]

filtrar_estudiantes(estudiantes)

# =========================================================
# 19. Crea una función lambda que filtre los números impares de una lista dada.
# =========================================================

def filtrar_impares(lista_numeros):
    """
    Filtra los números impares de una lista.

    Args:
        lista_numeros (list): Lista de números enteros.

    Returns:
        list: Lista con solo los números impares.
    """
    try:
        return list(filter(lambda x: x % 2 != 0, lista_numeros))
    
    except Exception:
        print("Error: la lista debe contener solo valores numéricos.")
        return []
    

# =========================================================
# 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter()
# =========================================================

def filtrar_enteros(lista):
    """
    Filtra los valores enteros de una lista que puede contener ints y strings.

    Args:
        lista (list): Lista con elementos de tipo int y str.

    Returns:
        list: Lista con solo los valores enteros.
    """
    return list(filter(lambda x: type(x) == int, lista))


# =========================================================
# 21. Crea una función que calcule el cubo de un número dado mediante una función lambda
# =========================================================

def calcular_cubo(numero):
    """
    Calcula el cubo de un número.

    Args:
        numero (int or float): Número a elevar al cubo.

    Returns:
        int or float | None: El número elevado al cubo, o None si ocurre un error.
    """
    try:
        cubo = lambda x: x ** 3
        return cubo(numero)
    except Exception:
        print("Error: el argumento debe ser un número (int o float).")
        return None


# =========================================================
# 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce()
# =========================================================

def producto_lista(lista_numeros):
    """
    Calcula el producto de todos los valores en una lista.

    Args:
        lista_numeros (list): Lista de números (int o float).

    Returns:
        int or float: Producto total de los valores, o None si ocurre un error.
    """
    try:
        return reduce(lambda acc, valor: acc * valor, lista_numeros)
    except Exception:
        print("Error: la lista debe contener solo números y no puede estar vacía.")
        return None


# =========================================================
# 23. Concatena una lista de palabras.Usa la función reduce()
# =========================================================

def concatenar_palabras(lista_palabras):
    """
    Concatena todas las palabras de una lista en un solo string usando reduce().

    Args:
        lista_palabras (list): Lista de palabras.

    Returns:
        str: Palabras concatenadas en un único string.
    """
    try:
        return reduce(lambda acc, palabra: acc + palabra, lista_palabras)
    
    except Exception:
        print("Error: la lista debe contener solo strings y no estar vacía.")
        return ""
    

# =========================================================
# 24.  Calcula la diferencia total en los valores de una lista. Usa la función reduce()
# =========================================================

def diferencia_total(lista_numeros):
    """
    Calcula la diferencia total acumulada de los valores de una lista .

    Args:
        lista_numeros (list): Lista de números (int o float).

    Returns:
        int or float: Resultado de restar los valores de izquierda a derecha.
    """
    try:
        return reduce(lambda acc, num: acc - num, lista_numeros)
    except Exception:
        print("Error: la lista debe contener solo números y no estar vacía.")
        return None
    

# =========================================================
# 25. Crea una función que cuente el número de caracteres en una cadena de texto dada.
# =========================================================

def contar_caracteres(cadena):
    """
    Cuenta el número de caracteres en una cadena de texto.

    Args:
        cadena (str): Cadena de texto.

    Returns:
        int: Número total de caracteres en la cadena.
    """
    return len(cadena)


# =========================================================
# 26. Crea una función lambda que calcule el resto de la división entre dos números dados
# =========================================================

resto_lambda = lambda num1, num2: num1 % num2


# =========================================================
#27. Crea una función que calcule el promedio de una lista de números
# =========================================================

def promedio_v2(lista_numeros):
    """
    Calcula el promedio de una lista de números.

    Args:
        lista_numeros (list): Lista de números (int o float).

    Returns:
        float | None: Promedio de los valores o None si la lista está vacía.
    """
    try:
        return sum(lista_numeros) / len(lista_numeros)
    except ZeroDivisionError:
        print("Error: la lista está vacía, no se puede calcular el promedio.")
        return None
    except Exception:
        print("Error: la lista debe contener solo valores numéricos.")
        return None
    

# =========================================================
#28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
# =========================================================

def primer_duplicado(lista):
    """
    Busca el primer elemento duplicado en una lista.

    Args:
        lista (list): Lista de elementos.

    Returns:
        elemento | None: El primer elemento duplicado, o None si no hay duplicados.
    """
    vistos = set()

    for elem in lista:
        if elem in vistos:
            return elem
        vistos.add(elem)

    return None

# =========================================================
# 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.
# =========================================================

def enmascarar_variable(valor):
    """
    Convierte una variable a cadena de texto y enmascara todos los caracteres con '#',
    excepto los últimos cuatro.

    Args:
        valor (any): Cualquier valor a convertir en string.

    Returns:
        str: Cadena enmascarada.
    """
    try:
        texto = str(valor)  

        if len(texto) <= 4:
            return texto
        else:
            return "#" * (len(texto) - 4) + texto[-4:]
        
    except Exception:
        print("Error: no se pudo convertir el valor a string.")
        return ""
    

# =========================================================
# 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden
# =========================================================

def palabras_anagramas(palabra1, palabra2):
    """
    Determina si dos palabras son anagramas.

    Args:
        palabra1 (str): Primera palabra.
        palabra2 (str): Segunda palabra.

    Returns:
        bool: True si son anagramas, False en caso contrario.
    """
    return sorted(palabra1.lower()) == sorted(palabra2.lower())


# =========================================================
# 31. Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. 
# Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción
# =========================================================

def buscar_nombre():
    """
    Pide al usuario una lista de nombres y busca un nombre específico dentro de ella.

    Returns:
        str: Mensaje indicando si se encontró el nombre o se produjo un error.
    """
    try:
        entrada = input("Introduce una lista de nombres separados por comas: ")
        lista_nombres = [n.strip() for n in entrada.split(",")]

        nombre_buscar = input("Introduce el nombre que deseas buscar: ").strip()

        if nombre_buscar in lista_nombres:
            mensaje = f"El nombre '{nombre_buscar}' fue encontrado en la lista."
            return mensaje
        else:
            raise ValueError(f"El nombre '{nombre_buscar}' no está en la lista.")

    except ValueError as e:
        print("Error:", e)
        return None
    except Exception:
        print("Error inesperado: asegúrate de ingresar datos válidos.")
        return None
    

# =========================================================
# 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado
#  si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
# =========================================================

def buscar_empleado(nombre_completo, lista_empleados):
    """
    Busca un empleado en lista de empleados y devolver su puesto.

    Args:
        nombre_completo (str): Nombre completo del empleado a buscar.
        lista_empleados (list): Lista de diccionarios con claves 'nombre' y 'puesto'.

    Returns:
        str: Puesto del empleado o mensaje si no se encuentra.
    """
    try:
        for empleado in lista_empleados:
            if empleado.get("nombre", "").lower() == nombre_completo.lower():
                return f"{nombre_completo} trabaja como {empleado.get('puesto')}."
            
        return f"{nombre_completo} no trabaja aquí."
    
    except Exception:
        return "Error: formato de lista inválido. Se esperaba lista de diccionarios."


# =========================================================
# 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas.
# =========================================================

def sumar_listas(lista1, lista2):
    """
    Suma los elementos correspondientes de dos listas usando lambda.

    Args:
        lista1 (list): Primera lista de números.
        lista2 (list): Segunda lista de números.

    Returns:
        list: Lista con la suma de los elementos correspondientes.
    """
    try:
        return list(map(lambda x, y: x + y, lista1, lista2))
    except Exception:
        print("Error: las listas deben contener solo números.")
        return []
    

# =========================================================
# 34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son: 
# crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para manipular la estructura del árbol.
# =========================================================

class Arbol:
    def __init__(self):
        """
        Inicializa un árbol con un tronco de longitud 1 y una lista vacía de ramas.
        """
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        """
        Aumenta la longitud del tronco en 1.
        """
        self.tronco += 1

    def nueva_rama(self):
        """
        Agrega una nueva rama con longitud 1.
        """
        self.ramas.append(1)

    def crecer_ramas(self):
        """
        Aumenta en 1 la longitud de todas las ramas.
        """
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        """
        Elimina una rama en la posición indicada (índice de lista).
        """
        try:
            self.ramas.pop(posicion)
        except IndexError:
            print("Error: la posición indicada no existe.")

    def info_arbol(self):
        """
        Devuelve información del árbol: tronco, número de ramas y longitudes.

        Returns:
            str: Información formateada del árbol.
        """
        return {
            "tronco": self.tronco,
            "num_ramas": len(self.ramas),
            "long_ramas": self.ramas
        }
    
# Casos de Uso 34
# 1. Crear un árbol
arbol = Arbol()

# 2. Hacer crecer el tronco del árbol una unidad
arbol.crecer_tronco()

# 3. Añadir una nueva rama al árbol
arbol.nueva_rama()

# 4. Hacer crecer todas las ramas del árbol una unidad
arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas al árbol
arbol.nueva_rama()
arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2 
arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol
print(arbol.info_arbol())


# =========================================================
# 36.  Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. 
# Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.
# =========================================================

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente=True):
        """
        Inicializa un usuario de banco.

        Args:
            nombre (str): Nombre del usuario.
            saldo (float): Saldo inicial.
            cuenta_corriente (bool): Si tiene cuenta corriente (True/False).
        """
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        """
        Retira dinero del saldo.

        Args:
            cantidad (float): Cantidad a retirar.

        Raises:
            ValueError: Si la cantidad es mayor que el saldo disponible.
        """

        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo.")
        self.saldo -= cantidad

        return f"{self.nombre} ha retirado {cantidad}€. Saldo actual: {self.saldo}€"

    def transferir_dinero(self, receptor, cantidad):
        """
        Transfiere dinero desde el usuario actual hacia otro usuario.

        Args:
            receptor (UsuarioBanco): Usuario que recibe el dinero.
            cantidad (float): Cantidad a transferir.

        Raises:
            ValueError: Si el usuario no tiene fondos suficientes.
        """

        if not isinstance(receptor, UsuarioBanco):
            raise ValueError("El receptor debe ser un objeto UsuarioBanco.")
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir debe ser positiva.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene suficiente saldo para realizar la transferencia.")
        
        self.saldo -= cantidad
        receptor.saldo += cantidad

        return f"{self.nombre} transfirió {cantidad}€ a {receptor.nombre}. Saldo actual: {self.saldo}€"

    def agregar_dinero(self, cantidad):
        """
        Agrega dinero al saldo del usuario.

        Args:
            cantidad (float): Cantidad a agregar.
        """
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser positiva.")
        
        self.saldo += cantidad
        
        return f"{self.nombre} agregó {cantidad}€. Saldo actual: {self.saldo}€"
    
#Casos de uso
# 1. Crear dos usuarios
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 unidades de saldo a "Bob"
bob.agregar_dinero(20)

# 3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia"
alicia.transferir_dinero(bob, 80)

# 4. Retirar 50 unidades de saldo a "Alicia"
alicia.retirar_dinero(50)


# =========================================================
# 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras , reemplazar_palabras , 
# eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto 
# =========================================================

def contar_palabras(texto):
    """
    Cuenta cuántas veces aparece cada palabra en el texto.

    Args:
        texto (str): Texto de entrada.

    Returns:
        dict: Diccionario.
    """
    palabras = texto.split()
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """
    Reemplaza todas las ocurrencias de una palabra por otra en el texto.

    Args:
        texto (str): Texto de entrada.
        palabra_original (str): Palabra a reemplazar.
        palabra_nueva (str): Nueva palabra.

    Returns:
        str: Texto con la palabra reemplazada.
    """
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra_a_eliminar):
    """
    Elimina todas las ocurrencias de una palabra del texto.

    Args:
        texto (str): Texto de entrada.
        palabra_a_eliminar (str): Palabra a eliminar.

    Returns:
        str: Texto sin la palabra eliminada.
    """
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra_a_eliminar]
    return " ".join(palabras_filtradas)


def procesar_texto(texto, opcion, *args):
    """
    Procesa un texto según la opción especificada:
    - "contar": cuenta las palabras
    - "reemplazar": reemplaza palabra_original por palabra_nueva
    - "eliminar": elimina una palabra

    Args:
        texto (str): Texto de entrada.
        opcion (str): Opción a realizar: "contar", "reemplazar" o "eliminar".
        *args: Argumentos adicionales según la opción.

    Returns:
        dict | str: Resultado del procesamiento.
    """
    try:
        if opcion == "contar":
            return contar_palabras(texto)
        elif opcion == "reemplazar":
            palabra_original, palabra_nueva = args
            return reemplazar_palabras(texto, palabra_original, palabra_nueva)
        elif opcion == "eliminar":
            (palabra_a_eliminar,) = args
            return eliminar_palabra(texto, palabra_a_eliminar)
        else:
            raise ValueError("Opción inválida. Usa 'contar', 'reemplazar' o 'eliminar'.")
        
    except Exception as e:
        return f"Error: {e}"
    
#casos de uso:
texto_prueba = "el perro juega en el jardín con el perro"

# 1. Contar palabras
print(procesar_texto(texto_prueba, "contar"))

# 2. Reemplazar "perro" por "gato"
print(procesar_texto(texto_prueba, "reemplazar", "perro", "gato"))

# 3. Eliminar "el"
print(procesar_texto(texto_prueba, "eliminar", "el"))



# =========================================================
# 38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
# =========================================================

def momento_dia(hora):
    """
    Pedir al usuario una hora y confirmar si es mañana, tarde o noche.
    """
    try:
        if hora < 0 or hora > 23:
            raise ValueError("La hora debe estar entre 0 y 23.")

        if 6 <= hora < 12:
            resultado ="Es de mañana."
        elif 12 <= hora < 20:
            resultado ="Es de tarde."
        else:
            resultado = "Es de noche."

        return resultado  
    except ValueError as e:
        print("Error:", e)
        return None
    except Exception:
        print("Error inesperado: introduce un número entero válido.")
        return None
    

# =========================================================
# 39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
# =========================================================

def calificacion(nota):
    """
    Determina la calificación en texto a partir de la nota numérica.

    Args:
        nota (int): Calificación numérica (0-100).

    Returns:
        str: Texto con la calificación correspondiente.
    """
    try:
        if nota < 0 or nota > 100:
            raise ValueError("La calificación debe estar entre 0 y 100.")

        if nota <= 69:
            return "insuficiente"
        elif nota <= 79:
            return "bien"
        elif nota <= 89:
            return "muy bien"
        else:
            return "excelente"
        
    except Exception as e:
        return f"Error: {e}"


# =========================================================
# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" ) y datos 
# (una tupla con los datos necesarios para calcular el área de la figura)
# =========================================================

def calcular_area(figura, datos):
    """
    Calcula el área de una figura geométrica.

    Args:
        figura (str): Tipo de figura ("rectangulo", "circulo", "triangulo").
        datos (tuple): Datos necesarios para calcular el área.
            - rectangulo: (base, altura)
            - circulo: (radio,)
            - triangulo: (base, altura)

    Returns:
        float: Área de la figura.
    """
    try:
        figura = figura.lower()

        if figura == "rectangulo":
            base, altura = datos
            return base * altura
        elif figura == "circulo":
            (radio,) = datos
            return math.pi * (radio ** 2)
        elif figura == "triangulo":
            base, altura = datos
            return (base * altura) / 2
        else:
            return "Error: figura no reconocida. Usa rectangulo, circulo o triangulo."
        
    except Exception as e:
        return f"Error en los datos: {e}"
    

# =========================================================
# 41. Programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento
# =========================================================

def compra(precio, tiene_cupon, descuento=0):
    """
    Calcula el monto final de una compra interactuando con el usuario.
    """
    try:
        if tiene_cupon == "S":
                        
            if descuento > 0:
                precio_final = precio - descuento
                if precio_final < 0:
                    precio_final = 0
                print(f"Precio final con descuento: {precio_final}€")
                return precio_final
            else:
                print("El cupón no es válido, se aplica precio completo.")
                return precio
        elif tiene_cupon == "N":
            print(f"Precio final sin descuento: {precio}€")
            return precio
        else:
            print("Respuesta no válida. No se aplica descuento.")
            return precio
        
    except ValueError:
        print("Error: introduce un valor numérico válido.")
        return None
    