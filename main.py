# =====================================================================
# BLOQUE 1: CREACIÓN DEL ARCHIVO
# =====================================================================
# Usamos modo 'w' para crear el archivo desde cero con los encabezados y algunos países de ejemplo.
# with open("paises.csv", "w", encoding="utf-8") as archivo_inicial:
#     archivo_inicial.write("nombre,continente,poblacion,superficie,pbi\n")
#     archivo_inicial.write("Argentina,América del Sur,46000000,2780400,490000\n")
#     archivo_inicial.write("Brasil,América del Sur,214000000,8515767,1600000\n")
#     archivo_inicial.write("España,Europa,47000000,505990,1400000\n")
#     archivo_inicial.write("Japón,Asia,125000000,377975,4900000\n")
#     archivo_inicial.write("Egipto,África,109000000,1002450,400000\n")

# print("Archivo 'paises.csv' creado con éxito.")

#Al haberse creado una vez, no hace falta volver a crear el archivo.
# =====================================================================
# BLOQUE 1.2: GUARDAR DATOS EN ARCHIVO CSV
# =====================================================================
def guardar_datos(archivo, lista_paises):
    try:
        #Abrimos con 'w' (write) para reescribir el archivo con todo lo nuevo
        with open(archivo, "w", encoding="utf-8") as f:
            for pais in lista_paises:
                #Armamos la línea pegando los datos separados por coma. Convertimos los números a str() para poder unirlos
                linea = f"{pais['nombre']},{pais['continente']},{pais['poblacion']},{pais['superficie']},{pais['pbi']}\n"
                f.write(linea)
        print("\nArchivo CSV actualizado correctamente.")
    except Exception as e:
        print(f"\nNo se pudo guardar en el archivo: {e}")

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
    continentes=["América del Sur","América del Norte","Europa","Asia","África","Oceanía"]
    
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción (1-8): ")
        
        if opcion == "1":
            print("\n--- LISTADO TOTAL DE PAÍSES ---")
            for p in paises:
                print(f"País: {p['nombre']:<12} | Continente: {p['continente']:<16} | Población: {p['poblacion']:<10} | Superficie: {p['superficie']:<10} km² | PBI: {p['pbi']}")
        
        elif opcion == "2":
            #Llamamos a la función de alta pasándole nuestra lista de países
            agregar_pais(paises,continentes)
            
        elif opcion == "3":
            #Llamamos a la función de modificación pasándole la lista
            actualizar_pais(paises)
            
        elif opcion == "4":
            #Llamamos a la función de búsqueda pasándole el dataset
            buscar_pais_por_nombre(paises)
            
        elif opcion == "5":
            #Llamamos a la función encargada de gestionar los filtros
            ejecutar_submenu_filtros(paises,continentes)

        elif opcion == "6":
            ejecutar_submenu_ordenamiento(paises)
            
        elif opcion == "7":
            mostrar_estadisticas(paises)
            
        elif opcion == "8":
            guardar_datos(archivo_datos, paises)
            print("\nSe guardaron los cambios con éxito. Se finaliza el programa.")
            break
        else:
            print("\nOpción inválida. Por favor, ingresá un número del 1 al 8.")

# =====================================================================
# BLOQUE 5: FUNCIÓN PARA AGREGAR UN PAÍS (ALTA)
# =====================================================================
def agregar_pais(lista_paises,continentes):
    print("\n--- REGISTRAR NUEVO PAÍS ---")
    
    #Validamos que el nombre no sea vacío
    nombre = input("Ingresá el nombre del país: ").strip()
    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Ingresá el nombre del país: ").strip()
        
    #Solicitamos al usuario que elija el continente
    while True:
        print("\nSeleccioná el continente:")
        for i, c in enumerate(continentes, 1):
            print(f"{i}. {c}")
        try:
            opcion = int(input("Opción (1-6): "))
            if 1 <= opcion <= len(continentes):
                continente = continentes[opcion - 1]
                break
            else:
                print("Opción inválida. Elige un número del 1 al 6.")
        except ValueError:
            print("Entrada no válida. Debes ingresar un número.")

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
# FUNCION DE ORDENAMIENTO
# =====================================================================
def obtener_nombre(pais): #función para ordenar por nombre
    return pais["nombre"]

def obtener_poblacion(pais):#función para ordenar por población
    return pais["poblacion"]

def obtener_superficie(pais):#función para ordenar por superficie con opciones de orden ascendente y descendente
    return pais['superficie']

def ejecutar_submenu_ordenamiento(paises):
    print("\n--- SUBMENÚ DE ORDENAMIENTO ---")
    print("a. Ordenar por Nombre")
    print("b. Ordenar por Población")
    print("c. Ordenar por Superficie")

    sub_opcion = input("Elegí una opción de ordenamiento (a, b o c): ").strip().lower()

    if sub_opcion == "a":
        paises_ordenados = sorted(paises, key=obtener_nombre)

        print("\n--- PAÍSES ORDENADOS POR NOMBRE ---")
        for pais in paises_ordenados: #recorre la lista y obtiene el valor "nombre" en cada recorrido
            print(f"{pais['nombre']} | {pais['continente']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']}")

    elif sub_opcion=="b":
        paises_ordenados=sorted(paises,key=obtener_poblacion) #recorre la lista y obtiene el valor "población" en cada recorrido
        print("\n--- PAÍSES ORDENADOS POR POBLACIÓN ---")
        for pais in paises_ordenados:
            print(f"{pais['nombre']} | {pais['continente']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']}")
    elif sub_opcion == "c":
        orden = input(
            "¿Cómo desea ordenar la superficie?\n"
            "a. Ascendente\n"
            "b. Descendente\n"
            "Opción: "
        ).strip().lower()
        
        if orden == "a":
            paises_ordenados = sorted(paises, key=obtener_superficie) #recorre la lista y obtiene el valor "superficie" en cada recorrido
            print("\n--- PAÍSES ORDENADOS POR SUPERFICIE ASCENDENTE ---")
            
        elif orden == "b":
            paises_ordenados = sorted(paises, key=obtener_superficie, reverse=True) #reverse=True es para hacerlo descendente.
            print("\n--- PAÍSES ORDENADOS POR SUPERFICIE DESCENDENTE ---")

        else:
            print("Opción inválida.")
            return

        for pais in paises_ordenados:
            print(f"{pais['nombre']} | {pais['continente']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']}")
    else:
        print("Opción inválida.")

# =====================================================================
# BLOQUE 5: SUBMENÚ DE FILTROS
# =====================================================================
def ejecutar_submenu_filtros(paises,continentes):
    print("\n--- SUBMENÚ DE FILTROS ---")
    print("a. Filtrar por Continente")
    print("b. Filtrar por Rango de Población")
    print("c. Filtrar por Rango de Superficie")
    sub_opcion = input("Elegí una opción de filtrado (a, b o c): ").strip().lower()
    
    if sub_opcion == "a":
        while True:
            try:
                print("Ingresá la opción correspondiente al continente:")
                for i, c in enumerate(continentes, 1):
                    print(f"{i}. {c}")
                
                continente_elegido = int(input("Opción: "))
                if 1 <= continente_elegido <= len(continentes):
                    continente = continentes[continente_elegido - 1]
                    break # Salimos del bucle si es correcto
                else:
                    print("Opción inválida, debe estar entre 1 y 6.")
            except ValueError as e:
                print(f"Error: {e}, ingrese un dato válido")
        
        resultados = filtrar_por_continente(paises, continente)
        if len(resultados) > 0:
            print(f"\nPaíses en {continente}:")
            for p in resultados:
                print(f"-> {p['nombre']} (Población: {p['poblacion']})")
        else:
                print(f"\nNo se encontraron países en '{continente}'.")

            
    elif sub_opcion == "b":
        print("\n-- Rango de Población --")
        min_pob = input("Ingresá la población MÍNIMA: ").strip()
        max_pob = input("Ingresá la población MÁXIMA: ").strip()

        if min_pob.isdigit() and max_pob.isdigit():

            if int(min_pob) > int(max_pob):
                print("La población mínima no puede ser mayor que la máxima.")
                return

            resultados = filtrar_por_rango_poblacion(
                paises,
                int(min_pob),
                int(max_pob)
            )

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

            if int(min_sup) > int(max_sup):
                print("La superficie mínima no puede ser mayor que la máxima.")
                return

            resultados = filtrar_por_rango_superficie(
                paises,
                int(min_sup),
                int(max_sup)
            )

            if len(resultados) > 0:
                print(f"\nPaíses dentro del rango de superficie ({min_sup} km² - {max_sup} km²):")
                for p in resultados:
                    print(f"-> {p['nombre']} (Superficie: {p['superficie']} km²)")
            else:
                print("\nNo hay países en ese rango de superficie.")
        else:
            print("Los valores deben ser números enteros.")
    else:
        print("Opción de submenú inválida.")
# =====================================================================
# FUNCIONES DE MÉTRICAS
# =====================================================================

def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("No hay países cargados para calcular estadísticas.")
        return

    pais_mayor_poblacion = paises[0] #se le asigna el primer registro para poder comparar después.
    pais_menor_poblacion = paises[0] #se le asigna el primer registro para poder comparar después.

    suma_poblacion = 0
    suma_superficie = 0

    cantidad_por_continente = {}

    for pais in paises: #se comparan los valores dentro del ciclo for
        if pais["poblacion"] > pais_mayor_poblacion["poblacion"]: 
            pais_mayor_poblacion = pais # la variable va a tomar el mayor valor

        if pais["poblacion"] < pais_menor_poblacion["poblacion"]:
            pais_menor_poblacion = pais # la variable va a tomar el menor valor

        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        continente = pais["continente"]

        if continente in cantidad_por_continente:
            cantidad_por_continente[continente] += 1 #en caso de encontrar el nombre del continente, se suma al valor
        else:
            cantidad_por_continente[continente] = 1 #por defecto va a tomar el valor de 1

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    print("\n--- ESTADÍSTICAS GLOBALES ---")
    print(f"País con mayor población: {pais_mayor_poblacion['nombre']} ({pais_mayor_poblacion['poblacion']})")
    print(f"País con menor población: {pais_menor_poblacion['nombre']} ({pais_menor_poblacion['poblacion']})")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f} km²")

    print("\nCantidad de países por continente:")
    for continente in cantidad_por_continente:
        print(f"- {continente}: {cantidad_por_continente[continente]}")
        
#Inicia el programa
programa_principal()