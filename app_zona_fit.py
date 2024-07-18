# Clase main
from cliente import Cliente
from cliente_dao import ClienteDAO

print('Clientes de Zona Fit (GYM)'.center(50, '-'))
opcion = None
while opcion != 5:
    print('''Menu:
    1. Listar Clientes
    2. Agregar Cliente
    3. Modificar Cliente
    4. Eliminar Cliente
    5. Salir
    ''')
    opcion = int(input('Ingresa una opcion (1-5): '))
    if opcion < 6:
        if opcion == 1:  # Listar clientes
            clientes = ClienteDAO.seleccionar()
            print('\n *** Listado de Clientes ***')
            for cliente in clientes:
                print(cliente)  # Listamos todos los clientes
            print()  # Agregamos un salto de linea
        if opcion == 2:
            nombre_var = input('Ingresa el nombre del Cliente: ')
            apellido_var = input('Ingresa el apellido del Cliente: ')
            membresia_var = input('Ingresa el membresia del Cliente: ')
            cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia= membresia_var)
            clientes_insertados = ClienteDAO.insertar(cliente)
            print(f'Clientes insertados: {clientes_insertados}')
        if opcion == 3:
            id_var = int(input('Ingresa el ID del Cliente que desea modificar: '))
            nombre_var = input('Ingresa el nombre del Cliente: ')
            apellido_var = input('Ingresa el apellido del Cliente: ')
            membresia_var = input('Ingresa el membresia del Cliente: ')
            cliente = Cliente(id=id_var,nombre=nombre_var,apellido=apellido_var,membresia= membresia_var)
            clientes_modificados = ClienteDAO.actualizar(cliente)
            print(f'Clientes modificados: {clientes_modificados}')
        if opcion == 4:
            id_var = int(input('Ingresa el ID del Cliente que desea eliminar: '))
            cliente = Cliente(id=id_var)
            clientes_eliminados = ClienteDAO.eliminar(cliente)
            print(f'Clientes eliminados: {clientes_eliminados}')
        if opcion == 5:
            print('Hasta Pronto!!'.center(50, '-'))
    else:
        print(f'La opcion {opcion} no es valida')