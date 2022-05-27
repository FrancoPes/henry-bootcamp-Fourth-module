'''
# Virtualización

## Máquinas Virtuales

Es la versión virtual de algún recurso tecnológico, como Hardware, un sistema operativo, un dispositivo de almacenamiento o recurso de red.
Esa virtualización, es un sistema huésped que ejecuta sobre un sistema anfitrión, 
sin embargo tiene su propio sistema de archivos, que pueden tener múltiples formatos, como ser VDI, VMDK, VHD ó raw entre otros.

<img src="../_src/assets/Maquina_Virtual.jpg"  height="400">

## Docker

Utiliza contenedores, y lo que hacen es reutilizar el kernel, que es la parte mas profunda del SO de la maquina anfitriona, 
manejando de forma más óptima recursos que ya están disponibles en el SO anfitrión.
Esa containerización, trae consigo las ventajas de ser más liviana, portable, de bajo acoplamiento debido a que los contenedores son autocontenidos (no afecta a los demás para su funcionamiento), escalable y segura.

<img src="../_src/assets/Docker.jpg"  height="400">
<img src="../_src/assets/Docker2.jpg"  height="400">

Corre nativamente en Linux, por eso para otros SO levanta una máquina virtual.

Componentes del Docker Engine:
* Docker daemon: Es el centro de docker, por medio del cual, es posible la comunicación con los servicios de docker.
* REST API: Como cualquier otra API, es la que nos permite visualizar docker de forma “gráfica”.
* Cliente de docker: Permite la comunicación con el centro de docker (Docker Daemon) que por defecto es la línea de comandos.

<img src="../_src/assets/Componentes_Docker.jpg"  height="400">

Dentro de la arquitectura de Docker encontramos:
    1. Contenedores: Se encapsulan las imagenes para llevarlas a otra computadora 	o servidor, etc.
    2. Imágenes: Se puede correr una aplicación específica.
    3. Volúmenes de datos: Se puede acceder con seguridad al sistema de archivos 	de la máquina anfitrión.
    4. Redes: Permiten la comunicación entre contenedores.

Es una arquitectura cliente-servidor, se comunican mediante una API para poder gestionar el ciclo de vida de los contenedores
y así poder construir, ejecutar y distribuirlos.

### ¿Qué es un contenedor?

<img src="../_src/assets/Contenedor.jpg"  height="400">

* Agrupación de procesos.
* Entidad lógica, no tiene el límite estricto de las máquinas virtuales.
* Ejecuta sus procesos de forma nativa.
* Los procesos que se ejecutan adentro de los contenedores ven su universo como el contenedor lo define, no pueden ver mas allá del contenedor, 
a pesar de 	estar corriendo en una maquina más grande.
* No tienen forma de consumir más recursos que los que se les permite.
* Sector del disco: Cuando un contenedor es ejecutado, el daemon de docker 	    establece a qué parte puede acceder.
* Docker hace que los procesos adentro de un contenedor estén aislados del resto del sistema, no le permite ver más allá.
* Cada contenedor tiene un ID único, también tiene un nombre.

### ¿Qué es una imágen?

Se parte desde la base del SO Linux, y se agrega capas de personalización hasta obtener la imágen deseada:

Ejemplo:
    1. Distribución Debian
    2. Editor emacs
    3. Servidor Apache
    4. Permisos de escritura para la 	carpeta /var/www de Apache

    
<img src="../_src/assets/Docker_Imagen.jpg"  height="400">

### Docker Compose

* Herramienta que permite simplificar el uso de Docker a partir de archivos YAML, con los que es mas sencillo crear contendores, 
conectarlos, habilitar puertos, volumenes, etc.
* Se pueden crear diferentes contenedores y al mismo tiempo, en cada contenedor, diferentes servicios, unirlos a un volúmen común,
iniciarlos y apagarlos, etc.
* Componente fundamental para poder construir aplicaciones y microservicios.
* Permite poder instruir al Docker Engine a realizar tareas, programáticamente siendo ésta la clave: La facilidad para
dar una serie de instrucciones, y luego repetirlas en diferentes ambientes.
* Describe de forma declarativa la arquitectura de servicios necesaria en un archivo donde se declara lo que debe suceder.

Comandos:
1)	$ docker-compose up -d (crea todo lo declarado en el archivo docker-compose.yml)
2)	$ docker network ls (listo las redes)
3)	$ docker network inspect docker_default (veo la definición de la red)
4)	$ docker-compose logs (veo todos los logs)
5)	$ docker-compose logs app (solo veo el log de “app”)
6)	$ docker-compose logs -f app (hago un follow del log de app)
7)	$ docker-compose exec app bash (entro al shell del contenedor app)
8)	$ docker-compose ps (veo los contenedores generados por docker compose)
9) 	$ docker-compose down (borro todo lo generado por docker compose)
10)	$ docker-compose build (crea las imágenes)
11)	$ docker-compose up -d (crea los servicios/contenedores)

'''