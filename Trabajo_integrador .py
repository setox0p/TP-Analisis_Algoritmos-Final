import time
import random
import os

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def ordenamiento_burbuja(lista):
    n = len(lista)
    lista_copia = lista.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_copia[j] > lista_copia[j + 1]:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    return lista_copia

def medir_tiempos():
    tamaños = [100, 500, 1000, 2000]
    
    ruta_escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
    archivo_final = os.path.join(ruta_escritorio, "resultados_tiempos.txt")
    
    print("Iniciando pruebas de rendimiento...")
    print("-----------------------------------------")
    
    with open(archivo_final, "w") as archivo:
        archivo.write("Tamaño,Busqueda Lineal (s),Busqueda Binaria (s),Ordenamiento Cuadratica (s)\n")
        
        for tamaño in tamaños:
            print(f"Procesando listas de tamaño: {tamaño}...")
            
            lista_desordenada = [random.randint(1, 10000) for _ in range(tamaño)]
            lista_ordenada = sorted(lista_desordenada)
            objetivo = random.choice(lista_desordenada)
            
            # Búsqueda Lineal
            inicio = time.perf_counter()
            busqueda_lineal(lista_desordenada, objetivo)
            fin = time.perf_counter()
            tiempo_lineal = fin - inicio
            
            # Búsqueda Binaria
            inicio = time.perf_counter()
            busqueda_binaria(lista_ordenada, objetivo)
            fin = time.perf_counter()
            tiempo_binaria = fin - inicio
            
            # Ord. Burbuja
            inicio = time.perf_counter()
            ordenamiento_burbuja(lista_desordenada)
            fin = time.perf_counter()
            tiempo_cuadratica = fin - inicio
            
            archivo.write(f"{tamaño},{tiempo_lineal:.8f},{tiempo_binaria:.8f},{tiempo_cuadratica:.8f}\n")
            
    print("-----------------------------------------")
    print("Pruebas finalizadas con exito")
    print(f"El reporte se guardó directamente en tu Escritorio como: 'resultados_tiempos.txt'")

if __name__ == "__main__":
    medir_tiempos()
