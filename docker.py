
###? QUE PROBLEMA RESUELVE DOCKER
#Cuando queremos correr algun archivo (o lo que sea) en otra maquina o en la nuestra y queremos no falle, sea la maquina que sea
#cuando quiero correr x en una maquina. necesito de alguna forma llevarme ese entorno
#cuando no quiero o puedo instalar algo para que eso me corra 

#### https://www.youtube.com/watch?v=3c-iBn73dDE
#?CONTENEDOR
#Es un paquete que trae todo lo necesario para que una app se ejecute
#es portatil
#el container vive en un repositorio
#dockerhub es un repositorio donde podes encontrar aplicaciones

#? TECNICAMENTE, UN CONTEINER
# Es una capa de imagenes stackeadas


#? como funciona un sistema operativo
# tiene 2 capas sobre el hardwar/ primero el kernel que se comunica con el harward y las aplicaciones sobre el kernel
# eso pasa con las distribuciones de linux. todas ellan usan el mismo kernel

#? diferencia entre un conteiner y una maquina virtual
#docker solo virtualiza la app, pero toma el kernel de la computadora local (por eso tengo que instalar el kernel de linux)
#en cambio una maquina virtual virtualiza el kernel y la app. emula todo el so
#! por esto las imagenes en docker son mas pequenias
#! podes 

#? DIFERENCIA ENTRE CONTAINER Y IMAGEN
# el conteiner es un entorno para la imagen (dile system, settings, etc)
# sistema de archivos virtuales

#en docker hub todos son iamgenes
# el conteiner empieza a correr cuando pongo run(seria una imagen dentro de un conteinr)

#! curiosidad >>> que es un puerto >> https://naseros.com/2020/05/29/que-es-un-puerto-y-un-socket/
#COMANDOS
#?  docker ps (LISTA DE CONTENEDORES CORRIENDO)
#?  docker ps -a (LISTA DE CONTENEDORES total)
#? docker stop id (parar un container)
#? docker start id(reiniciiar)

#otro video
# puedo correr una app dentro del container en cualquier maquina
# puedo correrlo en cualquier computadora y la app funciona igual
#es es la principal ventaja de docker

#es parecido pero no es lo mismo que una maquina virtual. la maquina virtual lo que hace es crear un sistema operativo y un kernel dentro de otra compu

# dentro de conteiner de docker, solamente tengo los requisitos minimos para hacer funcionar esa aplicacion. es decir que no tengo montado todo un  sistemas operativo
# el docker de nuestra maquina crea una pequenia maquina virtual

#IMAGEN
# docker corre un contenerdor apartir de una imagen
# ESA IMAGEN TIENE UNA DISTRIBUSION DE LINUX(UBUNTU), NUESTRO SOFWARE Y DEPENDENCIA 
#las imagenes se generan con dockerfile. es un archivo que tiene una serie de instrucciones que  indican como crear una imagen
# luego corremos un comando que es el DOCKER BUILT que genera una imagen
#Docker run para correrlo

#DESCARGAR UNA IMAGEN
#Puedo correr una imagen ya hecha por otro

#iniciar 
# voy al cmd y escribo:
# docker run -d -p 80:80 docker/getting-started
#error comun #https://docs.microsoft.com/en-us/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package

###################################################################################################################################3
#Comandos
#? docker ps (muestra los contenedores activos)

#buscar contendor
#? docker search ubuntu

#descargar
#? docker pull ubuntu
#? docker run ubuntu  #-----------> lo descarga y lo corre
#! cuando lo hago dos veces, directamente me la actualiza

#entrar al contenedor
#? docker run -it ubuntu (lo corre y entro al shell de ubuntu)
	#?	-i: interactivo
	#?	-t: abre la consola 
 
 
#! ls para ver los archivos (uso linux)
#! exit (para salirme) 
 #? empieezo a usar los comandos de linux alli 
 
 
 
 #ver el estado de los contenedores
 #? docker ps -a
 
 #encender un contenedor
 #? docker start 6c0bfb3481a4
 
 # apagar un contenedor
 #? docker stop id
 
 
 #VER LOS LOGS DEL CONTENEDOR
#? docker logs id 
#? docker logs -f

#listar todas las imagenes de la maquina

#correr
#? docker run hello-world (correr) (corro el contenedor hello-world)

'''
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

'''

# ver todos lo contenedores
#! no es lo mismo que imagenes 
#? docker ps

'''
CONTAINER ID   IMAGE             COMMAND                  CREATED          STATUS          PORTS                     NAMES
6a06cedbc269   postgres:latest   "docker-entrypoint.s…"   43 minutes ago   Up 42 minutes   0.0.0.0:49154->5432/tcp   postgres-SUR8
f95d33fe8777   postgres:latest   "docker-entrypoint.s…"   45 minutes ago   Up 45 minutes   0.0.0.0:49153->5432/tcp   postgres-t8ze

'''
#? docker ps -a (muestra todos los contenedores)

#? docker inspect <container ID> (muestra el detalle completo de un contenedor)
#? docker inspect <name> (igual que el anterior pero invocado con el nombre)
'''
[
    {
        "Id": "sha256:feb5d9fea6a5e9606aa995e879d862b825965ba48de054caab5ef356dc6b3412",
        "RepoTags": [
            "hello-world:latest"
        ],
        "RepoDigests": [
            "hello-world@sha256:10d7d58d5ebd2a652f4d93fdd86da8f265f5318c6a73cc5b6a9798ff6d2b2e67"
        ],
        "Parent": "",
        "Comment": "",
        "Created": "2021-09-23T23:47:57.442225064Z",
        "Container": "8746661ca3c2f215da94e6d3f7dfdcafaff5ec0b21c9aff6af3dc379a82fbc72",
        "ContainerConfig": {
            "Hostname": "8746661ca3c2",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "#(nop) ",
                "CMD [\"/hello\"]"
            ],
            "Image": "sha256:b9935d4e8431fb1a7f0989304ec86b3329a99a25f5efdc7f09f3f8c41434ca6d",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "DockerVersion": "20.10.7",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "Cmd": [
                "/hello"
            ],
            "Image": "sha256:b9935d4e8431fb1a7f0989304ec86b3329a99a25f5efdc7f09f3f8c41434ca6d",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": null
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 13256,
        "VirtualSize": 13256,
        "GraphDriver": {
            "Data": {
                "MergedDir": "/var/lib/docker/overlay2/52a1072543956a1ebc7dd36cc3a9d56bdc606e8cb89b19316efa114dba818c31/merged",
                "UpperDir": "/var/lib/docker/overlay2/52a1072543956a1ebc7dd36cc3a9d56bdc606e8cb89b19316efa114dba818c31/diff",
                "WorkDir": "/var/lib/docker/overlay2/52a1072543956a1ebc7dd36cc3a9d56bdc606e8cb89b19316efa114dba818c31/work"
            },
            "Name": "overlay2"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:e07ee1baac5fae6a26f30cabfe54a36d3402f96afda318fe0a96cec4ca393359"
            ]
        },
        "Metadata": {
            "LastTagTime": "0001-01-01T00:00:00Z"
        }
    }
]

'''
#reasignar nombre
#? docker run –-name hola-mundo dp hello-world (le asigno un nombre custom “hola-mundo”)






#reasignar un contenedor
#? docker container prune (borro todos lo contenedores que esten parados)
#? docker rm <ID o nombre> (borro un contenedor)










#VER IMAGENER
#? docker images

#crear un contenedor apartir de imagenes
#https://www.youtube.com/watch?v=eBRtzk0Wd6g&list=PLCTD_CpMeEKTj_n9XY0vz9n6Asi-g0kRg&index=7




#-----# #-----# #-----# #-----# #-----##-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----##-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----#

#debuggin containers
# docker logs id (veo los logs)





#-----# #-----# #-----# #-----# #-----##-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----##-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----# #-----#
#docker compose
# te permite correr varios containers a la vez
# si queres correr 10 containers  
# es un archivo, ver como se crea
# guardo ese archivo
#luego, usamos el comando docker-compose

#? docker-compose -f nombrearchivo up >>> enciende tods los container en nese archivo
#


'''
Compose is a tool for defining and running multi-container Docker applications. With Compose, 
you use a YAML file to configure your application’s services. Then, with a single command, 
you create and start all the services from your configuration. To learn more about all the features of Compose, see the list of features.

Compose works in all environments: production, staging, development, testing, as well as CI workflows. 
You can learn more about each case in Common Use Cases.

Using Compose is basically a three-step process:

Define your app’s environment with a Dockerfile so it can be reproduced anywhere.

Define the services that make up your app in docker-compose.yml so they can be run together in an isolated environment.

Run docker compose up and the Docker compose command starts and runs your entire app.
You can alternatively run docker-compose up using the docker-compose binary.

'''





