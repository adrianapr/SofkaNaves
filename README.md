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

Instalar docker y correr el script (run: `./script.sh`) desde la terminal. Este script es un simulador de lo que se podria hacer con un docker compose pero debido a que las librerias utilizadas tienen problema al unir las terminales del contenedor con la del host, se creo el script para controlar a detalle la forma ejecucion de cada contenedor, ademas de crear una red que permitiera conectar la aplicacion con la base de datos.

## Como usar el proyecto

A traves de la interfaz de consola, usando el teclado, se podran crear nuevas naves con caracteristicas especificas, o se podra utilizar la opcion de buscar las existentes en base a lo que el usuario requiera.
Por defecto, se han almacenado 9 naves en la base de datos.

#### Video del proyecto
https://youtu.be/GKdAXEh3aiQ
