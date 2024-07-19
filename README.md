# Zona Fit App

Zona Fit App es una aplicación de gestión para gimnasios que permite administrar la información de los clientes, incluyendo su nombre, apellido y membresía. La aplicación está desarrollada en Python utilizando `tkinter` para la interfaz gráfica y un DAO para la gestión de datos.

## Características

- **Gestión de clientes**: Añadir, actualizar, eliminar y visualizar clientes.
- **Interfaz gráfica**: Interfaz amigable y fácil de usar utilizando `tkinter`.
- **Base de datos**: Gestión de datos a través de un DAO.

## Capturas de pantalla

![image](https://github.com/user-attachments/assets/e89d13e6-9659-4eee-b252-1f3febfb0166)

## Requisitos

- Python 3.x
- `tkinter` (viene incluido con Python en la mayoría de las distribuciones)

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/MainRDSniper09/Zona_Fit_app
    ```

2. Asegúrate de tener `tkinter` instalado. En la mayoría de las distribuciones de Python, viene incluido de serie. Si no, puedes instalarlo con:

    - En Debian/Ubuntu:

      ```bash
      sudo apt-get install python3-tk
      ```

    - En Windows:

      `tkinter` debería estar incluido en la instalación estándar de Python.

3. Ejecuta la aplicación:

    ```bash
    python app.py
    ```

## Uso

1. **Añadir cliente**: Rellena los campos de nombre, apellido y membresía, y haz clic en "Guardar".
2. **Actualizar cliente**: Selecciona un cliente de la tabla, edita la información en los campos y haz clic en "Guardar".
3. **Eliminar cliente**: Selecciona un cliente de la tabla y haz clic en "Eliminar".
4. **Limpiar formulario**: Haz clic en "Limpiar" para borrar los campos del formulario.

## Estructura del Proyecto

- `app.py`: Archivo principal de la aplicación.
- `cliente.py`: Definición de la clase Cliente.
- `cliente_dao.py`: Gestión de datos de clientes (DAO).
- `README.md`: Este archivo.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir:

1. Realiza un fork del proyecto.
2. Crea una rama con tu característica (`git checkout -b feature/nueva_caracteristica`).
3. Realiza un commit de tus cambios (`git commit -am 'Agrega nueva característica'`).
4. Sube a la rama (`git push origin feature/nueva_caracteristica`).
5. Crea un nuevo Pull Request.

## Creditos

Quiero agradecer al ing-ubaldo-acosta el cual me ayudo a poder desarrollar este proyecto utilizando las herramientas antes mencionadas

## Contacto

Para cualquier pregunta o sugerencia, puedes contactarme a través de [mainbarretosanchez6@gmail.com](mainbarretosanchez6@gmail.com).
