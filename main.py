# =====================================================================
# BLOQUE 1: CREACIÓN DEL ARCHIVO
# =====================================================================
# Usamos modo 'w' para crear el archivo desde cero con los encabezados y algunos países de ejemplo.
with open("paises.csv", "w", encoding="utf-8") as archivo_inicial:
    archivo_inicial.write("nombre,continente,poblacion,superficie,pbi\n")
    archivo_inicial.write("Argentina,América del Sur,46000000,2780400,490000\n")
    archivo_inicial.write("Brasil,América del Sur,214000000,8515767,1600000\n")
    archivo_inicial.write("España,Europa,47000000,505990,1400000\n")
    archivo_inicial.write("Japón,Asia,125000000,377975,4900000\n")
    archivo_inicial.write("Egipto,África,109000000,1002450,400000\n")

print("Archivo 'paises.csv' creado con éxito.")

# =====================================================================
# BLOQUE 2: FUNCIÓN PARA CARGAR LOS DATOS
# =====================================================================
def cargar_datos(ruta_archivo):
    #Creamos la lista vacía donde guardaremos los diccionarios de cada país
    lista_paises = []
    
    # Abrimos el archivo en modo lectura ('r')
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        # Leemos la primera línea (los encabezados) para "descartarla" y que el bucle for empiece directamente desde los datos reales.
        archivo.readline()
        
        # Recorremos el archivo línea por línea
        for linea in archivo:
            #.strip() elimina el salto de línea '\n' del final
            #split(",") corta la cadena por cada coma y arma una lista de palabras
            datos = linea.strip().split(",")
            
            #Creamos el diccionario para este país mapeando los datos de la lista
            #Convertimos poblacion, superficie y pbi a enteros (int)
            pais = {
                "nombre": datos[0],
                "continente": datos[1],
                "poblacion": int(datos[2]),
                "superficie": int(datos[3]),
                "pbi": int(datos[4])
            }
            
            #Agregamos el diccionario del país actual a nuestra lista global
            lista_paises.append(pais)
            
    return lista_paises

# =====================================================================
# BLOQUE 3: MENÚ INTERACTIVO COMPLETO (SEGÚN CONSIGNA)
# =====================================================================
def mostrar_menu():
    print("\n==============================================")
    print("      SISTEMA DE GESTIÓN DE DATOS DE PAÍSES    ")
    print("==============================================")
    print("1. Mostrar todos los países cargados")
    print("2. Agregar un nuevo país (Alta)")
    print("3. Actualizar datos de un país (Modificación)")
    print("4. Buscar un país por nombre")
    print("5. Filtrar países (Continente / Población / Superficie)")
    print("6. Ordenar países (Nombre / Población / Superficie)")
    print("7. Mostrar estadísticas globales")
    print("8. Salir y guardar")
    print("==============================================")

def programa_principal():
    archivo_datos = "paises.csv"
    paises = cargar_datos(archivo_datos)
    
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción (1-8): ")
        
        if opcion == "1":
            print("\n--- LISTADO TOTAL DE PAÍSES ---")
            for p in paises:
                print(f"País: {p['nombre']:<12} | Continente: {p['continente']:<16} | Población: {p['poblacion']}")
        
        elif opcion == "2":
            print("\nFuncionalidad: Agregar país (No campos vacíos).")
            
        elif opcion == "3":
            print("\nFuncionalidad: Actualizar Población y Superficie.")
            
        elif opcion == "4":
            print("\nFuncionalidad: Buscar país (Coincidencia parcial/exacta).")
            
        elif opcion == "5":
            print("\n--- SUBMENÚ DE FILTROS ---")
            print("a. Por Continente\nb. Por Rango de Población\nc. Por Rango de Superficie")
            #Dejamos el molde para cuando programemos los filtros
            
        elif opcion == "6":
            print("\n--- SUBMENÚ DE ORDENAMIENTO ---")
            print("a. Por Nombre\nb. Por Población\nc. Por Superficie")
            
        elif opcion == "7":
            print("\nFuncionalidad: Estadísticas globales.")
            
        elif opcion == "8":
            print("\nSe guardaron los cambios con éxito. Se finaliza el programa.")
            break
        else:
            print("\nOpción inválida. Por favor, ingrese un número del 1 al 8.")

#Inicia el programa
programa_principal()