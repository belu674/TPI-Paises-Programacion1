# 🌍 Sistema de Gestión de Datos de Países

## 📋 Descripción

Trabajo Práctico Integrador de Programación 1.

El sistema permite gestionar información de países almacenada en un archivo CSV.

## Funcionalidades

- Mostrar países cargados.
- Agregar países.
- Actualizar datos de un país.
- Buscar países por nombre.
- Filtrar por continente.
- Filtrar por rango de población.
- Filtrar por rango de superficie.
- Ordenar por nombre.
- Ordenar por población.
- Ordenar por superficie.
- Mostrar estadísticas.

## ▶️ Instrucciones de uso

### Requisitos

- Python 3.x instalado
- Archivo `paises.csv` en el mismo directorio que `main.py`

### Ejecución

```bash
python main.py
```

### Menú principal

Al iniciar el programa, se presenta el siguiente menú:

```
==============================================
      SISTEMA DE GESTIÓN DE DATOS DE PAÍSES
==============================================
1. Mostrar todos los países cargados
2. Agregar un nuevo país (Alta)
3. Actualizar datos de un país (Modificación)
4. Buscar un país por nombre
5. Filtrar países (Continente / Población / Superficie)
6. Ordenar países (Nombre / Población / Superficie)
7. Mostrar estadísticas globales
8. Salir y guardar
==============================================
```

> ⚠️ Los cambios realizados (altas y modificaciones) **solo se guardan en el archivo** al elegir la opción **8. Salir y guardar**.

## 🛠️ Tecnologías utilizadas

- Python 3
- Archivos CSV
- Listas
- Diccionarios
- Funciones

## 💡 Ejemplos de entradas y salidas

### Opción 3 — Actualizar datos de un país

```
Elegí una opción (1-8): 3

--- ACTUALIZAR DATOS DE UN PAÍS ---
Ingresá el nombre del país que querés modificar: argentina

País encontrado: Argentina (América del Sur)
Valores actuales -> Población: 46000000 | Superficie: 2780400 km²
--------------------------------------------------
Ingresá la NUEVA población (solo números): 47000000
Ingresá la NUEVA superficie en km² (solo números): 2780400

Los datos de Argentina fueron actualizados correctamente.
```

### Opción 7 — Estadísticas globales

```
--- ESTADÍSTICAS GLOBALES ---
País con mayor población: Brasil (214000000)
País con menor población: Egipto (109000000)
Promedio de población: 108200000.00
Promedio de superficie: 2637516.40 km²

Cantidad de países por continente:
- América del Sur: 2
- Europa: 1
- Asia: 1
- África: 1
```

## 👥 Participación de los integrantes

| Integrante             | Funciones desarrolladas                                                                                                                                                                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Belén Molina**       | Creación y carga del archivo CSV (`guardar_datos`, `cargar_datos`), menú principal (`mostrar_menu`, `programa_principal`), alta de país (`agregar_pais`), actualización de país (`actualizar_pais`), Búsqueda por nombre (`buscar_pais_por_nombre`) |
| **Facundo Avellaneda** | filtros (`ejecutar_submenu_filtros`, `filtrar_por_continente`, `filtrar_por_rango_poblacion`, `filtrar_por_rango_superficie`), ordenamiento (`ejecutar_submenu_ordenamiento`), estadísticas (`mostrar_estadisticas`), documentación del proyecto    |

## 🎬 Video demostración

[Ver video en YouTube](https://youtube.com/...)

## 📄 Documentación

[Ver documentación completa](TPI_Programación I.docx)
