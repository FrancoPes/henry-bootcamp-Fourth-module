# en el archivo docker compose yml esta la configuracion del cluster
# 1) en el servidor, primero instalamos docker compose ; 
# 2) descargamos la carpeta dsm4hive
# 3) ejecutamos el cluster (sudo dockerp-compose up)
#4) entramos a la interfaz de hue simplemente usando la ip del servidor  
#! hue es una herramienta de big data, sea usame con otras herramientas tambien(r, spark etc)
#! por defecto la bd se llama default
# abajo en la izquierda puedo cambiar y configurar los usuarios
# TENGO QUE SUBIR LA CARPETA DATA (LA CUAL TIENE 3 CARPETAS ADENTRO). Vamos a #? ARCHIVO >>> NUEVO >>> DIRECTORIO >> le pongo DATA
# dentro del directorio data creo 3 carpetas igual que las de la practica (de todas formas puedo arrastrarlas)
# luego para cargar los archivos dentro de los directorios correspondientes voy a #? CARGAR >> Arrastro

#5) Nos ubicamos dentro del contenedor namenode #? sudo docker exec -it dsm4huehive_namenode_1 bash  >> 
# ahora estoy dentro del contenedor namenode#
#para ver hdfs >> hdfs dfs -ls/   >>> veo usuarios de hive, etc
# si quiero puedo eliminar archivos con un rm >> es como usar hue

#6) para entrar a la consola de hive #? >>> sudo docker exec -it xxx_hive-server_1 bash   
# estoy dentro de hive y puedo hacer consultas desde ahi

#7) levantamos el json
# vamos a documents, toco los 3 puntos, importar

#! por defecto, las tablas son MANAGED. el EXTERNAL va despues de CREATE


#8) crear particiones #? >> create table ..... partitioned by (year int) location (path)



















