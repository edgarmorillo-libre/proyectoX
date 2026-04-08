# tesoreria.py - Script simple para calcular el promedio de una lista de números

def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.
    
    Args:
    numeros (list): Lista de números.
    
    Returns:
    float: El promedio de los números.
    """
    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de ejemplo
    lista_numeros = [10, 20, 30, 40, 50]
    promedio = calcular_promedio(lista_numeros)
    print(f"La lista de números es: {lista_numeros}")
    print(f"El promedio es: {promedio}")
    
    # Permitir entrada del usuario
    try:
        entrada = input("\nIngresa números separados por comas (ej: 1,2,3): ")
        numeros_usuario = [float(x.strip()) for x in entrada.split(',')]
        promedio_usuario = calcular_promedio(numeros_usuario)
        print(f"El promedio de tus números es: {promedio_usuario}")
    except ValueError:
        print("Error: Ingresa solo números válidos.")
