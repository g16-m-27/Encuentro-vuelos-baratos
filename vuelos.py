# ============================================================
# SISTEMA DE ENCUENTRO DE VUELOS BARATOS
# ============================================================
# Estructura de datos utilizada:
# Lista de diccionarios
#
# Cada diccionario representa un vuelo y contiene:
# ID, Origen, Destino, Aerolínea, Fecha y Precio.
# ============================================================


# ------------------------------------------------------------
# 1. BASE DE DATOS DE VUELOS
# ------------------------------------------------------------

vuelos = [
    {
        "ID": 1,
        "Origen": "Quito",
        "Destino": "Guayaquil",
        "Aerolínea": "LATAM",
        "Fecha": "15/10/2026",
        "Precio": 65
    },
    {
        "ID": 2,
        "Origen": "Quito",
        "Destino": "Cuenca",
        "Aerolínea": "Avianca",
        "Fecha": "16/10/2026",
        "Precio": 72
    },
    {
        "ID": 3,
        "Origen": "Guayaquil",
        "Destino": "Quito",
        "Aerolínea": "LATAM",
        "Fecha": "18/10/2026",
        "Precio": 58
    },
    {
        "ID": 4,
        "Origen": "Quito",
        "Destino": "Baltra (Galápagos)",
        "Aerolínea": "Equair",
        "Fecha": "20/10/2026",
        "Precio": 115
    },
    {
        "ID": 5,
        "Origen": "Guayaquil",
        "Destino": "Cuenca",
        "Aerolínea": "Avianca",
        "Fecha": "21/10/2026",
        "Precio": 45
    },
    {
        "ID": 6,
        "Origen": "Quito",
        "Destino": "Guayaquil",
        "Aerolínea": "Avianca",
        "Fecha": "15/10/2026",
        "Precio": 70
    },
    {
        "ID": 7,
        "Origen": "Cuenca",
        "Destino": "Quito",
        "Aerolínea": "LATAM",
        "Fecha": "22/10/2026",
        "Precio": 60
    },
    {
        "ID": 8,
        "Origen": "Guayaquil",
        "Destino": "Manta",
        "Aerolínea": "Aeroregional",
        "Fecha": "25/10/2026",
        "Precio": 38
    },
    {
        "ID": 9,
        "Origen": "Quito",
        "Destino": "Loja",
        "Aerolínea": "Clic Air",
        "Fecha": "26/10/2026",
        "Precio": 85
    },
    {
        "ID": 10,
        "Origen": "Quito",
        "Destino": "Guayaquil",
        "Aerolínea": "Aeroregional",
        "Fecha": "15/10/2026",
        "Precio": 52
    }
]


# ------------------------------------------------------------
# 2. MOSTRAR LOS VUELOS
# ------------------------------------------------------------

def mostrar_vuelos(lista_vuelos):

    print("\n" + "=" * 100)
    print("LISTADO DE VUELOS")
    print("=" * 100)

    print(
        f"{'ID':<5}"
        f"{'ORIGEN':<20}"
        f"{'DESTINO':<25}"
        f"{'AEROLÍNEA':<18}"
        f"{'FECHA':<15}"
        f"{'PRECIO':<10}"
    )

    print("-" * 100)

    for vuelo in lista_vuelos:

        print(
            f"{vuelo['ID']:<5}"
            f"{vuelo['Origen']:<20}"
            f"{vuelo['Destino']:<25}"
            f"{vuelo['Aerolínea']:<18}"
            f"{vuelo['Fecha']:<15}"
            f"${vuelo['Precio']:<9.2f}"
        )

    print("=" * 100)


# ------------------------------------------------------------
# 3. BUSCAR VUELOS POR ORIGEN Y DESTINO
# ------------------------------------------------------------

def buscar_vuelos(origen, destino):

    resultados = []

    for vuelo in vuelos:

        if (
            vuelo["Origen"].lower() == origen.lower()
            and
            vuelo["Destino"].lower() == destino.lower()
        ):
            resultados.append(vuelo)

    return resultados


# ------------------------------------------------------------
# 4. FILTRAR VUELOS POR PRECIO
# ------------------------------------------------------------

def filtrar_por_precio(precio_maximo):

    resultados = []

    for vuelo in vuelos:

        if vuelo["Precio"] <= precio_maximo:
            resultados.append(vuelo)

    return resultados


# ------------------------------------------------------------
# 5. FILTRAR VUELOS POR AEROLÍNEA
# ------------------------------------------------------------

def filtrar_por_aerolinea(aerolinea):

    resultados = []

    for vuelo in vuelos:

        if vuelo["Aerolínea"].lower() == aerolinea.lower():
            resultados.append(vuelo)

    return resultados


# ------------------------------------------------------------
# 6. FILTRAR VUELOS POR FECHA
# ------------------------------------------------------------

def filtrar_por_fecha(fecha):

    resultados = []

    for vuelo in vuelos:

        if vuelo["Fecha"] == fecha:
            resultados.append(vuelo)

    return resultados


# ------------------------------------------------------------
# 7. IDENTIFICAR EL VUELO MÁS BARATO
# ------------------------------------------------------------

def encontrar_vuelo_mas_barato(lista_vuelos):

    if len(lista_vuelos) == 0:
        return None

    vuelo_mas_barato = lista_vuelos[0]

    for vuelo in lista_vuelos:

        if vuelo["Precio"] < vuelo_mas_barato["Precio"]:
            vuelo_mas_barato = vuelo

    return vuelo_mas_barato


# ------------------------------------------------------------
# 8. IDENTIFICAR EL VUELO MÁS BARATO DE UNA RUTA
# ------------------------------------------------------------

def encontrar_vuelo_mas_barato_por_ruta(origen, destino):

    resultados = buscar_vuelos(origen, destino)

    return encontrar_vuelo_mas_barato(resultados)


# ------------------------------------------------------------
# 9. ORDENAR VUELOS POR PRECIO
# ------------------------------------------------------------

def ordenar_por_precio():

    vuelos_ordenados = sorted(
        vuelos,
        key=lambda vuelo: vuelo["Precio"]
    )

    return vuelos_ordenados


# ------------------------------------------------------------
# 10. OBTENER LOS DATOS PARA LAS GRÁFICAS
# ------------------------------------------------------------
# Esta función NO genera ninguna gráfica.
# Solamente organiza los datos que pueden utilizarse
# posteriormente para elaborar las gráficas.
# ------------------------------------------------------------

def obtener_datos_grafica():

    datos = []

    for vuelo in vuelos:

        datos.append(
            {
                "ID": vuelo["ID"],
                "Precio": vuelo["Precio"],
                "Aerolínea": vuelo["Aerolínea"]
            }
        )

    return datos


# ------------------------------------------------------------
# 11. EJECUCIÓN DEL PROGRAMA
# ------------------------------------------------------------

print("\n")
print("=" * 70)
print("      SISTEMA DE ENCUENTRO DE VUELOS BARATOS")
print("=" * 70)


# Mostrar la base de datos cargada

print("\nBASE DE DATOS DE VUELOS CARGADA:")
mostrar_vuelos(vuelos)


# ------------------------------------------------------------
# BÚSQUEDA DE VUELOS
# ------------------------------------------------------------

print("\n")
print("=" * 70)
print("BÚSQUEDA DE VUELOS")
print("=" * 70)

origen = input("Ingrese la ciudad de origen: ")
destino = input("Ingrese la ciudad de destino: ")

resultados_busqueda = buscar_vuelos(origen, destino)

if len(resultados_busqueda) > 0:

    print("\nVuelos encontrados:")
    mostrar_vuelos(resultados_busqueda)

else:

    print("\nNo se encontraron vuelos para esa ruta.")


# ------------------------------------------------------------
# FILTRO POR PRECIO
# ------------------------------------------------------------

print("\n")
print("=" * 70)
print("FILTRO POR PRECIO")
print("=" * 70)

precio_maximo = float(
    input("Ingrese el precio máximo que desea pagar: $")
)

vuelos_filtrados = filtrar_por_precio(precio_maximo)

if len(vuelos_filtrados) > 0:

    print("\nVuelos encontrados dentro del precio indicado:")
    mostrar_vuelos(vuelos_filtrados)

else:

    print("\nNo existen vuelos dentro del precio indicado.")


# ------------------------------------------------------------
# VUELO MÁS BARATO DE TODA LA BASE DE DATOS
# ------------------------------------------------------------

print("\n")
print("=" * 70)
print("VUELO MÁS BARATO")
print("=" * 70)

vuelo_barato = encontrar_vuelo_mas_barato(vuelos)

print(
    f"ID: {vuelo_barato['ID']}\n"
    f"Origen: {vuelo_barato['Origen']}\n"
    f"Destino: {vuelo_barato['Destino']}\n"
    f"Aerolínea: {vuelo_barato['Aerolínea']}\n"
    f"Fecha: {vuelo_barato['Fecha']}\n"
    f"Precio: ${vuelo_barato['Precio']:.2f}"
)


# ------------------------------------------------------------
# VUELOS ORDENADOS POR PRECIO
# ------------------------------------------------------------

print("\n")
print("=" * 70)
print("VUELOS ORDENADOS DE MENOR A MAYOR PRECIO")
print("=" * 70)

vuelos_ordenados = ordenar_por_precio()

mostrar_vuelos(vuelos_ordenados)


# ------------------------------------------------------------
# DATOS PARA LAS GRÁFICAS
# ------------------------------------------------------------

datos_grafica = obtener_datos_grafica()

print("\n")
print("=" * 70)
print("DATOS PREPARADOS PARA LAS GRÁFICAS")
print("=" * 70)

for dato in datos_grafica:

    print(
        f"ID: {dato['ID']} | "
        f"Precio: ${dato['Precio']:.2f} | "
        f"Aerolínea: {dato['Aerolínea']}"
    )

print("\nPrograma finalizado.")