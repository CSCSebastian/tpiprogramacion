
def actulizapoblacion(paises):
    print("\nPaises disponibles: ")
    print([pais['nombre'] for pais in paises])

    paiseleccion = input("Elija un pais para actualizar su poblacion: ").strip().lower()

    while not paiseleccion.replace(' ', '').isalpha() or paiseleccion == '':
        print('Error: Ingreso caracteres no validos')
        paiseleccion = input("Elija un pais para actualizar su poblacion: ").strip().lower()

    encontrado = False

    for pais in paises:
        if paiseleccion == pais['nombre'].lower():
            print(f"La poblacion actual de {pais['nombre']} es: {pais['poblacion']}")

            while True:
                try:
                    nuevapoblacion = int(input("Ingrese cuantas unidades desea restar: "))
                    # Validación para no permitir números menores a 0
                    if nuevapoblacion < 0:
                        print(">> Error: el número no puede ser negativo")
                        continue  # Vuelve al inicio del while

                    break  # Si es un número válido y mayor o igual a 0, sale del ciclo
                except ValueError:
                    print(">> Error: ingrese solo números enteros")

            pais['poblacion'] = nuevapoblacion
            encontrado = True
            break

    if not encontrado:
        print(f">> Error: no se encontró el país '{paiseleccion}'")
        return None

    print("Población actualizada con exito.")
    return paises


def actualizasuperficie(paises):
    print("\nPaises disponibles: ")
    print([pais['nombre'] for pais in paises])

    paiseleccion = input("Elija un pais para actualizar su superficie: ").strip().lower()

    while not paiseleccion.replace(' ', '').isalpha() or paiseleccion == '':
        print('Error: Ingreso caracteres no validos')
        paiseleccion = input("Elija un pais para actualizar su superficie: ").strip().lower()

    encontrado = False

    for pais in paises:
        if paiseleccion == pais['nombre'].lower():
            print(f"La superficie actual de {pais['nombre']} es: {pais['superficie']}")

            while True:
                try:
                    nuevasuperficie = int(input("Ingrese la nueva superficie: "))
                    # Validación para no permitir números menores o iguales a 0
                    if nuevasuperficie <= 0:
                        print(">> Error: la superficie debe ser un número positivo")
                        continue

                    break
                except ValueError:
                    print(">> Error: ingrese solo números enteros")

            pais['superficie'] = nuevasuperficie
            encontrado = True
            break

    if not encontrado:
        print(f">> Error: no se encontró el país '{paiseleccion}'")
        return None

    print("Superficie actualizada con exito.")
    return paises


def filtrar_paises(paises):
    print("\n¿Por qué criterio desea filtrar?")
    print("1. Continente")
    print("2. Rango de población")
    print("3. Rango de superficie")

    while True:
        opcion = input("Ingrese una opción (1-3): ").strip()
        if opcion in ('1', '2', '3'):
            break
        print(">> Error: ingrese 1, 2 o 3")

    resultado = []

    if opcion == '1':
        while True:
            continente = input("Ingrese el continente: ").strip().lower()
            if continente == '' or not continente.replace(' ', '').isalpha():
                print(">> Error: ingrese solo letras")
                continue
            break
        for pais in paises:
            if pais['continente'].lower() == continente:
                resultado.append(pais)

    elif opcion == '2':
        while True:
            try:
                minimo = int(input("Ingrese la población mínima: "))
                maximo = int(input("Ingrese la población máxima: "))
                if minimo > maximo:
                    print(">> Error: el mínimo no puede ser mayor al máximo")
                    continue
                break
            except ValueError:
                print(">> Error: ingrese solo números enteros")
        for pais in paises:
            if minimo <= int(pais['poblacion']) <= maximo:
                resultado.append(pais)

    elif opcion == '3':
        while True:
            try:
                minimo = int(input("Ingrese la superficie mínima: "))
                maximo = int(input("Ingrese la superficie máxima: "))
                if minimo > maximo:
                    print(">> Error: el mínimo no puede ser mayor al máximo")
                    continue
                break
            except ValueError:
                print(">> Error: ingrese solo números enteros")
        for pais in paises:
            if minimo <= int(pais['superficie']) <= maximo:
                resultado.append(pais)

    if resultado:
        print("\nPaíses encontrados:")
        for pais in resultado:
            print(pais)
    else:
        print("No se encontraron países con ese criterio.")

    return resultado


def ordenar_paises(paises):
    print("\n¿Por qué criterio desea ordenar?")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")

    while True:
        opcion = input("Ingrese una opción (1-3): ").strip()
        if opcion in ('1', '2', '3'):
            break
        print(">> Error: ingrese 1, 2 o 3")

    print("\n¿En qué orden?")
    print("1. Ascendente")
    print("2. Descendente")

    while True:
        orden = input("Ingrese una opción (1-2): ").strip()
        if orden in ('1', '2'):
            break
        print(">> Error: ingrese 1 o 2")

    descendente = orden == '2'

    if opcion == '1':
        resultado = sorted(paises, key=lambda p: p['nombre'].lower(), reverse=descendente)  # key: p['nombre'] (en minúsculas para ignorar mayúsculas) | reverse: True=descendente, False=ascendente
    elif opcion == '2':
        resultado = sorted(paises, key=lambda p: int(p['poblacion']), reverse=descendente)  # key: p['poblacion'] (convertido a int para comparar numéricamente) | reverse: True=descendente, False=ascendente
    elif opcion == '3':
        resultado = sorted(paises, key=lambda p: int(p['superficie']), reverse=descendente)  # key: p['superficie'] (convertido a int para comparar numéricamente) | reverse: True=descendente, False=ascendente

    print("\nPaíses ordenados:")
    for pais in resultado:
        print(pais)

    return resultado

