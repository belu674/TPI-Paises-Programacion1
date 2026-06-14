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