import mysql

from cliente import Cliente
from conexion import Conexion


class ClienteDAO:
    # Se crea las sentencias sql
    SELECCIONAR = 'SELECT * FROM cliente'
    INSERTAR = 'INSERT INTO cliente (nombre, apellido, membresia) VALUES (%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    # Se crean las funciones basicas de sql
    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)  # Ejecuta el Quary de select
            registros = cursor.fetchall()  # Nos regresa todos los registros
            # Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)  # Anexiona los objetos de tipo cliente a nuestra lista cliente
            return clientes
        except Exception as e:
            print(f'Ocurrio un error: {e}')
        finally:
            if conexion is not None:
                cursor.close()  # Se cierra la conexion
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.get_nombre(), cliente.get_apellido(), cliente.get_membresia())
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.get_nombre(), cliente.get_apellido(), cliente.get_membresia(), cliente.get_id())
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount  # Cuantos registros se actualizaron
        except Exception as e:
            print(f'Ocurrio un error: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id, )
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':
# Insertar un registro
#     cliente_uno = Cliente(nombre='Nicolas',apellido='Sanchez',membresia=300)
#     clientes_insertados = ClienteDAO.insertar(cliente_uno)
#     print(f'Clientes insertados: {clientes_insertados}')

# Actualizar
#     cliente_actualizar = Cliente(3, 'Alexa', 'Gomez', 600)
#     clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
#     print(f'Clientes actualizados: {clientes_actualizados}')

# Eliminar
#     cliente_eliminar = Cliente(id=3)
#     clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
#     print(f'Clientes eliminados: {clientes_eliminados}')

# Seleccionar clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)




