# SOFKA NAVES

Este programa nos premite crear naves espaciales y buscar (por tipo o ID) naves que se encuentran almacenadas en una base de datos.

## Cómo correr el proyecto

Hay dos formas de correr el proyecto

### Opcion 1:

Instalar todas las dependencias en tu computadora local, que son las siguientes:

- Instalar mongo usando este [link](https://www.mongodb.com/try/download/community)
- Instalar Python usando este [link](https://www.python.org/downloads/)
- Instalar las dependencias con este comando: `pip install -r requirements.txt`

Correr con el comando: `python Naves/menu.py`

### Opcion 2

Instalar docker y correr el script desde la terminal, este script es un simulador de lo que se podria hacer con un docker compose pero debido a que las librerias utilizadas tienen problema al unir las terminales , se creo el script para crear una red que permitiera conectarse con python y mongo.

## Como usar el proyecto

El programa contiene inicialmente 9 naves almacenadas en una base de datos.
Puede crear nuevas naves o buscar las existentes a traves del tipo de nave y el nro de ID, usando la interfaz por consola.
