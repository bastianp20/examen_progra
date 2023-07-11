datos_personales = []
A = 3800 
B = 3000 
C = 2800 
D = 3500 
def matriz(): 
    print(" departamento -- A  B  C  D ")
    print("     piso                   ")
    print("       |                    ")
    print("      10         *  *  *  * ")
    print("       9         *  *  *  * ")
    print("       8         *  *  *  * ")
    print("       7         *  *  *  * ")
    print("       6         *  *  *  * ")
    print("       5         *  *  *  * ")
    print("       4         *  *  *  * ")
    print("       3         *  *  *  * ")
    print("       2         *  *  *  * ")
    print("       1         *  *  *  * ")


def comprar_departamento(): 
    matriz()
    while True: 
        piso = int(input("ingrese el piso que comprará: "))
        departamento = int(input("ingrese el departamento que comprará [1 = A], [2 = B], [3 = C], [4 =D]: ")) 
        contador = 0
        if piso < 5:
            if departamento == 1:
                contador = contador + 3800
                print("usted escogio el departamento A " + "que está en el piso: "+ str(piso) + " y tiene un precio de: "+ '$' + str(contador) + ' expresado en UF ')
                print(contador)
                break
            elif departamento == 2:
                contador = contador + 3000
                print("usted escogio el departamento B " + "que está en el piso: "+ str(piso) + " y tiene un precio de: "+ '$' + str(contador) + ' expresado en UF ')
                print(contador)
                break
            elif departamento == 3: 
                contador = contador + 2800
                print("usted escogio el departamento C " + "que está en el piso: "+ str(piso) + " y tiene un precio de: "+ '$' + str(contador) + ' expresado en UF ')
                break
            elif departamento == 4: 
                contador = contador + 3500
                print("usted escogio el departamento D " + "que está en el piso: "+ str(piso) + " y tiene un precio de: "+ '$' + str(contador) + ' expresado en UF ')
                break
            else: 
                print("error")
                break 
        
def compradores(): 
    nombre = input("ingrese su nombre: ")
    rut = int(input("ingrese su rut: "))
    datos = nombre, rut
    print("!accion exitosa¡")
    datos_personales.append(datos)
    print(datos_personales)


while True: 
    menu = int(input("ingrese la opcion a elegir [1] comprar departamento [2] ver los compradores: " ))
    if menu ==1:
        comprar_departamento()
    elif menu == 2: 
        compradores()

