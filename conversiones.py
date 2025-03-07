<<<<<<< HEAD
"""Ejercicio desarrollado de forma individual y compartido al grupo"""

# Importar la bibliotecas sys
import sys

# Tasas de conversión de Peso Chileno a otras monedas
tasas_conversion = {
    "Sol": 0.0046,
    "PesoArgentino": 0.093,
    "DolarAmericano": 0.0013
}

def convertir_pesos_chilenos(valor_pesos_chilenos):

    resultado = {}
    # Iterar sobre las tasas de conversión y calcular los valores convertidos
    for moneda, tasa in tasas_conversion.items():
        resultado[moneda] = valor_pesos_chilenos * tasa
    return resultado

if __name__ == "__main__":
    # Validar que se ingresaron los argumentos correctos
    if len(sys.argv) != 5:
        print("Error: Debes ingresar 4 argumentos: Sol, Peso Argentino, Dólar Americano y el valor en Peso Chileno a convertir.")
    else:
        # Convertir los argumentos a números de punto flotante
        """Slice que toma en cuenta desde la posicion 1 en adelante"""
        sol, peso_argentino, dolar_americano, valor_pesos_chilenos = map(float, sys.argv[1:]) 
        # Calcular los valores convertidos
        resultado_conversion = convertir_pesos_chilenos(valor_pesos_chilenos)
        # Imprimir los resultados
        print(f"Valor en Sol Peruano: {resultado_conversion['Sol']}")
        print(f"Valor en Peso Argentino: {resultado_conversion['PesoArgentino']}")
        print(f"Valor en Dólar Americano: {resultado_conversion['DolarAmericano']}")