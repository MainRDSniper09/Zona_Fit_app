from mysql.connector import pooling


class Conexion:
    DATABASE = 'zona_fit_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5  # El tamanio de nuestra pool de conexiones, no se recomienda un numero muy alto
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:  # Se crea el objeto pool
            try:
                cls.pool = pooling.MySQLConnectionPool(pool_name=cls.POOL_NAME,pool_size=cls.POOL_SIZE,port=cls.DB_PORT,host=cls.HOST,user=cls.USERNAME,password=cls.PASSWORD,database=cls.DATABASE)  # Creamos el objeto pool de conexiones
                print(f'Nombre del pool: {cls.POOL_NAME}')
                print(f'Size del pool: {cls.POOL_SIZE}')
                return cls.pool # retornamos el pool de conexiones
            except Exception as e:
                print(f'Ocurrio un error al obtener el pool: {e}')
        else:
            return cls.pool  # Se retorna el pool en caso de que ya se alla inicializado

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()  # Retornamos desde el metodo obtener_pool

    @classmethod
    def liberar_conexion(cls, conexion):  # Creamos la funcion liberar conexion dentro de nuestro pool
        conexion.close()

if __name__ == '__main__':
    # Creacion del objeto pool
    pool = conexion.obtener_pool()
    print(pool)  # Para ver que tenga informacion nuestro pool

    # Objeto tipo conexion
    cnx1 = conexion.obtener_conexion()  # Vemos que se crea nuestro objeto pool ya conectado a nuestra DB
    print(cnx1)
    # Liberar pool
    conexion.liberar_conexion(cnx1)
    conexion.liberar_conexion(pool)

