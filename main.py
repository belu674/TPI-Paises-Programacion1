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
# BLOQUE 1.2: GUARDAR DATOS EN ARCHIVO CSV
# =====================================================================
# def guardar_datos(archivo, lista_paises):
#     try:
#         #Abrimos con 'w' (write) para reescribir el archivo con todo lo nuevo
#         with open(archivo, "w", encoding="utf-8") as f:
#             for pais in lista_paises:
#                 #Armamos la línea pegando los datos separados por coma. Convertimos los números a str() para poder unirlos
#                 linea = f"{pais['nombre']},{pais['continente']},{pais['poblacion']},{pais['superficie']},{pais['pbi']}\n"
#                 f.write(linea)
#         print("\nArchivo CSV actualizado correctamente.")
#     except Exception as e:
#         print(f"\nNo se pudo guardar en el archivo: {e}")

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
# BLOQUE 3: MENÚ
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
            #Llamamos a la función de alta pasándole nuestra lista de países
            agregar_pais(paises)
            
        elif opcion == "3":
            #Llamamos a la función de modificación pasándole la lista
            actualizar_pais(paises)
            
        elif opcion == "4":
            #Llamamos a la función de búsqueda pasándole el dataset
            buscar_pais_por_nombre(paises)
            
        elif opcion == "5":
            #Llamamos a la función encargada de gestionar los filtros
            ejecutar_submenu_filtros(paises)
        elif opcion == "6":
            print("\n--- SUBMENÚ DE ORDENAMIENTO ---")
            print("a. Por Nombre\nb. Por Población\nc. Por Superficie")
            
        elif opcion == "7":
            print("\nFuncionalidad: Estadísticas globales.")
            
        elif opcion == "8":
            guardar_datos(archivo_datos, paises)
            print("\nSe guardaron los cambios con éxito. Se finaliza el programa.")
            break
        else:
            print("\nOpción inválida. Por favor, ingresá un número del 1 al 8.")

# =====================================================================
# BLOQUE 5: FUNCIÓN PARA AGREGAR UN PAÍS (ALTA)
# =====================================================================
def agregar_pais(lista_paises):
    print("\n--- REGISTRAR NUEVO PAÍS ---")
    
    #Validamos que el nombre no sea vacío
    nombre = input("Ingresá el nombre del país: ").strip()
    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Ingresá el nombre del país: ").strip()
        
    #Validamos que el continente no sea vacío
    continente = input("Ingresá el continente: ").strip()
    while continente == "":
        print("El continente no puede estar vacío.")
        continente = input("Ingresá el continente: ").strip()

    #Validamos que la población sea un número entero mayor a 0 y no vacío
    while True:
        poblacion_str = input("Ingresá la población (solo números): ").strip()
        if poblacion_str.isdigit() and int(poblacion_str) > 0:
            poblacion = int(poblacion_str)
            break
        print("Ingreso inválido. Debe ser un número entero mayor a 0.")

    #Validamos que la superficie sea un número entero mayor a 0 y no vacío
    while True:
        superficie_str = input("Ingresá la superficie en km² (solo números): ").strip()
        if superficie_str.isdigit() and int(superficie_str) > 0:
            superficie = int(superficie_str)
            break
        print("Ingreso inválido. Debe ser un número entero mayor a 0.")

    #Validamos que el PBI sea un número entero mayor a 0 y no vacío
    while True:
        pbi_str = input("Ingresá el PBI en millones (solo números): ").strip()
        if pbi_str.isdigit() and int(pbi_str) > 0:
            pbi = int(pbi_str)
            break
        print("Ingreso inválido. Debe ser un número entero mayor a 0.")

    #Creamos el nuevo diccionario del país con los datos limpios
    nuevo_pais = {
        "nombre": nombre,
        "continente": continente,
        "poblacion": poblacion,
        "superficie": superficie,
        "pbi": pbi
    }
    
    #Lo agregamos a nuestra lista
    lista_paises.append(nuevo_pais)
    print(f"\n{nombre} se agregó correctamente a la lista.")

# =====================================================================
# BLOQUE 6: FUNCIÓN PARA ACTUALIZAR DATOS
# =====================================================================
def actualizar_pais(lista_paises):
    print("\n--- ACTUALIZAR DATOS DE UN PAÍS ---")
    
    nombre_buscar = input("Ingresá el nombre del país que querés modificar: ").strip()
    while nombre_buscar == "":
        print("El nombre a buscar no puede estar vacío.")
        nombre_buscar = input("Ingresá el nombre del país: ").strip()
        
    #Variable "bandera" para saber si encontramos o no el país
    encontrado = False
    
    # Recorremos la lista buscando coincidencia exacta (sin importar mayúsculas)
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre_buscar.lower():
            encontrado = True
            print(f"\nPaís encontrado: {pais['nombre']} ({pais['continente']})")
            print(f"Valores actuales -> Población: {pais['poblacion']} | Superficie: {pais['superficie']} km²")
            print("-" * 50)
            
            #Validamos la nueva Población
            while True:
                nueva_pob_str = input("Ingresá la NUEVA población (solo números): ").strip()
                if nueva_pob_str.isdigit() and int(nueva_pob_str) > 0:
                    pais["poblacion"] = int(nueva_pob_str)
                    break
                print("Ingreso inválido. Debe ser un número entero mayor a 0.")
                
            #Validamos la nueva Superficie
            while True:
                nueva_sup_str = input("Ingresá la NUEVA superficie en km² (solo números): ").strip()
                if nueva_sup_str.isdigit() and int(nueva_sup_str) > 0:
                    pais["superficie"] = int(nueva_sup_str)
                    break
                print("Ingreso inválido. Debe ser un número entero mayor a 0.")
                
            print(f"\nLos datos de {pais['nombre']} fueron actualizados correctamente.")
            break  #Cortamos el bucle porque ya lo encontramos y modificamos
            
    if not encontrado:
        print(f"\nNo se encontró ningún país con el nombre '{nombre_buscar}' en el sistema.")

# =====================================================================
# BLOQUE 7: FUNCIÓN DE BÚSQUEDA (COINCIDENCIA PARCIAL O EXACTA)
# =====================================================================
def buscar_pais_por_nombre(lista_paises):
    print("\n--- BUSCAR PAÍS POR NOMBRE ---")
    
    busqueda = input("Ingresá el nombre (o parte del nombre) a buscar: ").strip()
    while busqueda == "":
        print("El campo de búsqueda no puede estar vacío.")
        busqueda = input("Ingresá el nombre a buscar: ").strip()
        
    #Lista para ir guardando todas las coincidencias que encontremos
    resultados = []
    
    #Recorremos el dataset entero
    for pais in lista_paises:
        #El operador 'in' nos va a permitir validar la coincidencia parcial
        if busqueda.lower() in pais["nombre"].lower():
            resultados.append(pais)
            
    #Mostramos los resultados obtenidos
    if len(resultados) > 0:
        print(f"\nSe encontraron {len(resultados)} coincidencia(s):")
        print("-" * 60)
        for r in resultados:
            print(f"-> {r['nombre']:<12} | Continente: {r['continente']:<16} | Población: {r['poblacion']}")
        print("-" * 60)
    else:
        print(f"\nNo se encontraron países que coincidan con '{busqueda}'.")

# =====================================================================
# FUNCIONES AUXILIARES DE FILTRADO
# =====================================================================
def filtrar_por_continente(lista_paises, continente_buscado):
    paises_filtrados = []
    for pais in lista_paises:
        if pais["continente"].lower() == continente_buscado.lower():
            paises_filtrados.append(pais)
    return paises_filtrados

def filtrar_por_rango_poblacion(lista_paises, minimo, maximo):
    resultados = []
    for pais in lista_paises:
        #Verificamos si la población está dentro del rango
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)
    return resultados

def filtrar_por_rango_superficie(lista_paises, minimo, maximo):
    resultados = []
    for pais in lista_paises:
        #Verificamos si la superficie está dentro del rango
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)
    return resultados

# =====================================================================
# BLOQUE 5: SUBMENÚ DE FILTROS
# =====================================================================
def ejecutar_submenu_filtros(paises):
    print("\n--- SUBMENÚ DE FILTROS ---")
    print("a. Filtrar por Continente")
    print("b. Filtrar por Rango de Población")
    print("c. Filtrar por Rango de Superficie")
    sub_opcion = input("Elegí una opción de filtrado (a, b o c): ").strip().lower()
    
    if sub_opcion == "a":
        continente = input("Ingresá el nombre del continente: ").strip()
        if continente != "":
            resultados = filtrar_por_continente(paises, continente)
            if len(resultados) > 0:
                print(f"\nPaíses en {continente}:")
                for p in resultados:
                    print(f"-> {p['nombre']} (Población: {p['poblacion']})")
            else:
                print(f"\nNo se encontraron países en '{continente}'.")
        else:
            print("El continente no puede estar vacío.")
            
    elif sub_opcion == "b":
        print("\n-- Rango de Población --")
        min_pob = input("Ingresá la población MÍNIMA: ").strip()
        max_pob = input("Ingresá la población MÁXIMA: ").strip()
        
        if min_pob.isdigit() and max_pob.isdigit():
            resultados = filtrar_por_rango_poblacion(paises, int(min_pob), int(max_pob))
            if len(resultados) > 0:
                print(f"\nPaíses dentro del rango de población ({min_pob} - {max_pob}):")
                for p in resultados:
                    print(f"-> {p['nombre']} (Población: {p['poblacion']})")
            else:
                print("\nNo hay países en ese rango de población.")
        else:
            print("Los valores deben ser números enteros.")
            
    elif sub_opcion == "c":
        print("\n-- Rango de Superficie --")
        min_sup = input("Ingresá la superficie MÍNIMA (km²): ").strip()
        max_sup = input("Ingresá la superficie MÁXIMA (km²): ").strip()
        
        if min_sup.isdigit() and max_sup.isdigit():
            resultados = filtrar_por_rango_superficie(paises, int(min_sup), int(max_sup))
            if len(resultados) > 0:
                print(f"\nPaíses dentro del rango de superficie ({min_sup}km² - {max_sup}km²):")
                for p in resultados:
                    print(f"-> {p['nombre']} (Superficie: {p['superficie']} km²)")
            else:
                print("\nNo hay países en ese rango de superficie.")
        else:
            print("Los valores deben ser números enteros.")
    else:
        print("Opción de submenú inválida.")

#Inicia el programa
programa_principal()