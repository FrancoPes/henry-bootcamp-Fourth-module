#VIRTUAL BOX

#https://www.youtube.com/watch?v=hSJ2YmSVPpQ
#https://docs.oracle.com/en/virtualization/virtualbox/6.1/user/
#Una maquina virtual es un sofware que me permite simular un sistema operativo dentro de otro sistema operativo
# es una computadora dentro de mi compputadora
#le asigno un procesador, ram etc
#? nueva; para crear una maquina virtual
#? iniciar; 

# archivos VDI (VIRTUAL DISK IMAGE)
# CADA VEZ QUE CREAMOS UNA MAQUINA VIRTUAL, SE CREA UN VDI
#https://www.youtube.com/watch?v=8z4jcZgqJ_I
#puedo abrir un archivo ya existente. ver video

#error al abrir una maquina virtual
# https://www.youtube.com/watch?v=AO9TBc58FF4



################################################################################################################################################
#PUTTY
#https://www.youtube.com/watch?v=pWDHUlvcAsg
#https://tonyteaches.tech/putty-ssh-windows-tutorial/
# https://documentation.help/PuTTY/documentation.pdf ---> documentacion

#? QUE ES SSH?
# SSH (which stands for ‘secure shell’) is a recently designed, highsecurity protocol. It uses strong cryptography to protect your
#connection against eavesdropping, hijacking and other attacks.

#SSH and Rlogin both allow you to log in to the server without having
#to type a password.

#SSH allows you to connect to the server and automatically send a
#command, so that the server will run that command and then
#disconnect. So you can use it in automated processing.

#If the server you want to connect to doesn't
#support SSH, it might be worth trying to persuade the administrator to
#install it.

#? PUTTY
#1) When you start PuTTY, you will see a dialog box. This dialog box allows you to control everything PuTTY can do.
#2) In the ‘Host Name’ box, enter the Internet host name of the server you want to connect to.
#3) Now select a login protocol to use, from the ‘Connection type’ buttons
#4) For a login session, you should select Telnet, Rlogin or SSH. When you change the selected protocol, the number in the ‘Port’ box will change
#5) Once you have filled in the ‘Host Name’, ‘Protocol’, and possibly ‘Port’ settings, you are ready to connect.
#6) If you are using SSH to connect to a server for the first time, you will probably see a message looking something like this:
'''
The server's host key is not cached in the registry. You
have no guarantee that the server is the computer you
think it is.
The server's rsa2 key fingerprint is:
ssh-rsa 1024 7b:e5:6f:a7:f4:f9:81:62:5c:e3:1f:bf:8b:57:6c:5a
If you trust this host, hit Yes to add the key to
PuTTY's cache and carry on connecting.
If you want to carry on connecting just once, without
adding the key to the cache, hit No.
If you do not trust this host, hit Cancel to abandon the
connection.


'''

# 7) After you have connected, and perhaps verified the server's host key, you will be asked to log in, probably using a username and a password.
# Your system administrator should have provided you with these and the server should grant you access and begin your session.
# If you are using SSH, be careful not to type your username wrongly, because you will not have a chance to correct it after you press Return
#After you log in to the server, what happens next is up to the server! Most servers will print some sort of login message and then present a prompt,
#at which you can type commands which the server will carry out. Some servers will offer you on-line help; others might not

# 8) When you have finished your session, you should log out by typing the server's own logout command. This might vary between servers; if in
#doubt, try logout or exit or consult a manual or your system administrator.


################################################################################################################################################
#WINSCP
# Su función principal es facilitar la transferencia segura de archivos entre dos sistemas informáticos, el local y uno remoto que ofrezca servicios SSHNewbie.
# WinSCP se basa en la implementación del protocolo SSH de PuTTY y el protocolo FTP de FileZilla.3​ También está disponible como un complemento para el administrador de archivos Altap Salamander,4​ y existe un complemento de terceros para el administrador de archivos FAR Manager.
# WinSCP puede actuar como un editor remoto. Cuando el usuario hace clic en un archivo (texto) en el administrador de archivos remoto, transfiere el archivo a la máquina local y lo abre en el editor integrado, donde los usuarios de Windows pueden sentirse como en casa.


#? Uploading
#https://winscp.net/eng/docs/guide_upload
#Once you are connected to your account of FTP/SFTP server, you will see content of default remote directory (typically a home directory of your account) on remote file panel.
#If you want to upload the files to different directory, navigate there first.
#Now you can simply drag the local files and drop them on remote file panel. By default transfer settings dialog will appear. Typically you do not want to change any settings, so just press Copy.
################################################################################################################################################
# LINUX
# https://guias.donweb.com/como-comenzar-con-la-linea-de-comandos-de-linux/#:~:text=Las%20operaciones%20con%20archivos%20y%20directorios%20se%20llevan,como%20directorios%29%20Borrar%3A%20rm%20%28archivos%29%20y%20rmdir%20%28directorios%29
#A diferencia de otros sistemas operativos, Linux tiene solamente un árbol de directorios sin importar cuántos dispositivos de almacenamiento estén disponibles. 
# Una analogía que suele ser útil es comparar la estructura de directorios a un árbol invertido. Todo comienza con la raíz 
# y luego aparecen las ramas

#iguiendo con esta analogía, el inicio representa el directorio raíz y las ramas los demás subdirectorios del sistema.
# Cada distribución de Linux agrega algunos toques particulares, pero todas ellas siguen en mayor o menor grado el estándar
# de jerarquía del sistema de archivos. Este documento sirve de guía para entender el propósito de esta división.

# Utilizando el comando tree puedes ver el árbol de directorios (con la opción -d) hasta una profundidad dada por la opción -L. 
#sudo apt update -y && sudo apt install tree
#tree -d -L 1 /

#El estándar explica, entre otras cosas, el propósito de algunos de los directorios que observas arriba:
'''
/bin: programas (binarios ejecutables) de usuarios
/boot: archivos de arranque (incluyendo el kernel Linux)
/etc: configuraciones varias
/home: directorios personales de usuario
/tmp: archivos temporales (por lo general desaparecerán al reiniciar el sistema)
/var: datos variables (logs, por ejemplo)
'''

#Las operaciones con archivos y directorios se llevan a cabo con los comandos que aparecen a continuación:
#? Crear: touch o echo (archivos) y mkdir (directorios)
#? Cambiar el nombre: mv (tanto archivos como directorios)
#? Copiar: cp (tanto archivos como directorios)
#? Borrar: rm (archivos) y rmdir (directorios)




################################################################################################################################################
#HADOOP
#https://www.youtube.com/watch?v=aReuLtY0YMI








#https://www.youtube.com/watch?v=lRMAJwMQ0Vc
# protocolo de comunicacion de cos computadoras


#ubuntu
#https://www.youtube.com/watch?v=SDMQxLblarE
#es el sistema operativo mas importaten en la nube





#linux
#https://www.tutorialspoint.com/unix_commands/index.htm



#HADDOP
#https://www.youtube.com/watch?v=L_ikQw7ydBQ
#https://www.youtube.com/watch?v=tOB3V2iklbE

#?https://www.youtube.com/watch?v=iANBytZ26MI
#? what is hadoop
# is a framework that proces big data. de manera distribuida, y lo procesa paralelamente
# bid data >> storing >> processing >> analisung

#? componentes 
#hdfs
# es el sistema de distribucion de hadoop
# nodo master y nodos esclavos
# master or naemnode, stores the metadata, maneja y mantiene los data nodes
# slave or datanode. stores the data, performs replication as well
# distribuye los datos en bloques, ver diapositivas
#otorga seguridad, podes de soware, etc



#map reduce
#tecnica de programacion donde los datos son procesados y distribuidos en paralelo
# big data es el input, map reduce el proveso y luego tenemos el output
#data is procesed at the sale nodes
## input >> split by rows >> cuenta los datos repetidos por grupo (row) >> shuffke and sort >> reduce
# ver video min 21


#yarn
#yet another resource negociation
# its like an operative sistem. its a file sistem
#cliente >> vos en tu laptot. el cliente envia un request

'''

# Big Data

La era de los Datos.

<img src="../_src/assets/LaEraDeLosDatos.jpg"  height="400">

Es un término que hace referencia a una nueva clase de datos que no pueden ser gestionados por sistemas tradicionales.


### 3V’s de Big Data

* Volumen
* Variedad
* Velocidad

<img src="../_src/assets/BigData.jpg"  height="400">

### Casos de Uso

<img src="../_src/assets/CasosDeUso.jpg"  height="400">

### Data Lake

* Es un repositorio unificado de datos, estructurados y no estructurados.
* Está diseñado soportar las cargas de trabajo de Big Data y Machine Learning.
* Prioriza el almacenamiento de los datos en su formato original para luego ser procesados de acuerdo a la demanda.

<img src="../_src/assets/DataLake.jpg"  height="400">

### Estrategia de Procesamiento

<img src="../_src/assets/EstrategiaProcesamiento.jpg"  height="400">

### Arquitectura

<img src="../_src/assets/Arquitectura.jpg"  height="400">

## Hadoop

Es un sistema open-source diseñado para almacenar y procesar Big Data de forma distribuida utilizando un cluster de servidores.

* Características:
* Tolerancia a Fallos.
* Escalabilidad Horizontal.
* Utiliza commodity hardware.
* Desarrollado en lenguaje Java.
* Procesamiento en paralelo.

- [Sitio Oficial](https://hadoop.apache.org/)

### Ecosistema Hadoop

<img src="../_src/assets/Ecosistema_Hadoop.jpg"  height="400">

## Cluster Hadoop

<img src="../_src/assets/Cluster_Hadoop.jpg"  height="400">

## Componentes Core

### HDFS (Hadoop Distributed File System)

<img src="../_src/assets/HDFS.jpg"  height="100">

Master -> NameNode
Worker -> DataNode

Hadoop permite organizar computadoras en una relación maestro – esclavo que contribuye a conseguir una gran escalabilidad para el procesamiento.

Un Cluster Hadoop tiene dos tipos de nodos, un único “Master Node” llamado NameNode y un gran número de “Workers Nodes” llamados DataNodes.

<img src="../_src/assets/Hadoop_Nodes.jpg"  height="200">

El Masternode administra el sistema de archivos, su “namespace” y controla el acceso a los archivos por los clientes, 
conociendo qué bloques de qué archivos están en cada DataNode.
Un único MasterNode implica la necesidad de “Hot backups” para mantener la disponibilidad del servicio.

El MasterNode usa un log de transacciones para mantener un registro de cada cambio que ocurre en el sistema de archivos.

Los DataNodes almacenan los bloques de datos en el espacio de almacenamiento dirigidos por el MasterNode.

Cada DataNode típicamente contiene muchos discos para maximizar la capacidad de almacenamiento y la velocidad de acceso, 
y tienen su propio sistema de archivos local.
Los DataNodes almacenan y distribuyen bloques de datos sobre la red usando un protocolo de bloques, gestionado por el DataNode.

Los NameNodes almacenan toda la información relevante acerca de todos los DataNodes, y los archivos almacenados en los DataNodes:

* Para cada DataNode, su nombre, rack, capacidad y estado.
* Para cada archivo, su nombre, réplicas, tipo, tamaño, "timeStamp", ubicación, estado.

El NameNode trata de asegurar que los archivos se distribuyan de forma pareja entre los DataNodes del clúster, 
también optimiza el ancho de banda y balancea la carga de procesamiento y almacenamiento.

Cada pieza de datos es almacenado típicamente en tres nodos, dos en el mismo rack y uno en un rack diferente.

Si un DataNode falla, éste puede ser recreado automáticamente en otra computadora, escribiéndose 
todos los bloques de archivos desde réplicas (otros DataNodes).

Los DataNodes se comunican por medio de mensajes ("heartbeats") para conocer el estado de los nodos. 
Sin ese mensaje se considera que el nodo ha fallado, y la replicación automáticamente reemplaza el nodo fallido.

En el Sistema de Bloques ("block system"), un bloque es la unidad fundamental de almacenamiento en HDFS. 
Se almacena la información de grandes archivos distribuyendo segmentos llamados bloques para ser almacenados en diferentes computadoras.
El tamaño predeterminado de los bloques es de 64 o 128 MB dependiendo de la distribución:

hdfs getconf -confKey dfs.blocksize

Cada archivo de datos ocupa un determinado número de bloques, dependiendo de su tamaño y organizado en bloques consecutivos, 
para facilidad y velocidad de acceso.
El tamaño de bloques y el factor de replicación puede ser configurado según se requiera.

Respecto de la Integridad de los datos, Hadoop asegura que no habrá pérdida o corrupción de datos durante el procesamiento y almacenamiento.

Los datos son escritos sólo una vez y nunca actualizados en el lugar, pueden ser leídos muchas veces.

Sólo un cliente a la vez puede escribir o agregar datos al archivo, no se permiten actualizaciones concurrentes.

Si algunos datos en un DataNode se pierden o corrompen, o hay una falla en el disco que los contiene, 
una nueva réplica en buen estado es recreada automáticamente desde una réplica en otro DataNode. 
Al menos una réplica es almacenada en un DataNode en un rack diferente.

Los archivos de entrada pueden variar desde pequeños a extremadamente grandes y con diferentes estructuras.

Los archivos secuenciales ("secuence files") son una estructura especializada de datos dentro de Hadoop para manejar 
pequeños archivos en registros pequeños.

Utilizan una estructura de datos persistentes HDFS y MapReduce están diseñados para gestionar archivos de gran tamaño,
de manera que "empaquetar“ archivos pequeños en archivos secuenciales hace más eficiente su procesamiento y almacenamiento.

#### Ejemplo de escritura en HDFS

<img src="../_src/assets/Escritura_HDFS.jpg"  height="400">

### YARN (Yet Another Resource Negotiator)

<img src="../_src/assets/YARN.jpg"  height="100">

Master -> ResourceManager
Worker -> NodeManager

Es el centro de la arquitectura de Hadoop, caracterizado como un sistema Operativo distribuido para aplicaciones de Big Data.

YARN administra recursos y "workloads" en un entorno seguro mientras asegura la alta disponibilidad en múltiples clusters Hadoop.

YARN brinda flexibilidad como una plataforma común para ejecutar múltiples aplicaciones y herramientas, de consultas interactivas SQL (Hive),
de proceso de flujos en tiempo real (Spark), y procesamiento por lotes (MapReduce) para trabajar con los datos almacenados
en una plataforma HDFS.

Brinda gran escalabilidad para expandirse más allá de 1000 nodos y provee ubicación dinámica de recursos del clúster.

#### Ejemplo de ejecución de Jobs en YARN

<img src="../_src/assets/Ejemplo_YARN.jpg"  height="400">

- [YARN] (https://hadoop.apache.org/docs/stable/hadoop-yarn/hadoop-yarn-site/YARN.html)

## MapReduce

Permite procesar enormes cantidades de datos utilizando los servicios de gran cantidad de computadoras para trabajar en 
diferentes partes del trabajo ("job") simultáneamente, brindando capacidad de procesamiento en paralelo y tolerancia a fallos.

La tarea de procesamiento de los datos se divide en muchas partes, cada una procesada de forma independiente de las otras y 
luego los resultados intermedios se combinan en el resultado final.

MapReduce es un "framework" de procesamiento paralelo para acelerar el procesamiento de datos a gran escala, 
con un mínimo movimiento de los dados en el sistema de archivos distribuido del clúster Hadoop
, obteniendo resultados cercanos al tiempo real.

- [MapReduce] (https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html)


<img src="../_src/assets/Ejemplo_MapReduce.jpg"  height="400">

La función map(): se encarga del mapeo y es aplicada en paralelo para cada ítem en
la entrada de datos. Esto produce una lista de pares (k2,v2) por cada llamada.

Luego el se juntan todos los pares con la misma clave de todas las listas y los agrupa,
creando un grupo por cada una de las diferentes claves generadas.

Desde el punto de vista de la arquitectura, el nodo master toma el input, lo divide en
pequeñas piezas o problemas de menor identidad, y los distribuye a los denominados
"worker nodes".

Un "worker node" puede volver a sub-dividir, dando lugar a una estructura de árbol.

El "worker node" procesa el problema y pasa la respuesta al nodo maestro "master node".

La función reduce es aplicada en paralelo para cada grupo, produciendo una colección
de valores para cada dominio:

Reduce(k2, list (v2)) -> list(v3)

Típicamente se produce un valor v3 o una llamada vacía, 
aunque una llamada puede retornar más de un valor. El retorno de todas esas llamadas se recoge como la lista de resultado deseado.

Por lo tanto, el framework MapReduce transforma una lista de pares (clave, valor) en una lista de valores.


'''