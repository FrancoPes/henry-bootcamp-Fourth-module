#1) bajo el archivo de la consigna y lo abro. es una maquina virtual que simula ser el servidor asws o el quen sea
#me registro en el servidor, ubuntu, password ubuntu


#2) me conecto a winscp 

#3) conecto mi maquina local con el servidor a traves de putty
# tutorial de putty

#4) manejo el 'servidor' de manera remota, simulando un entorno de trabajo

'''
Se puede instalar Hadoop en un clúster de computadoras "on premise" o utilizar servicios en la nube: Azure, IBMCloud, AWS.
Requiere una instalación de Java y está escrito en ese lenguaje.
Para instalaciones locales es útil contar con una interfaz gráfica como Cloudera Resouces 
Manager que permite la instalación de Hadoop y componentes relacionados, como YARN, HBase, Pig.
Si se instala desde la línea de comandos, se debe descargar Hadoop de algunos de
los "mirrors" de Apache. 
La instalación en la nube es más sencilla que instalar Java Virtual Machines en computadoras locales.
HDFS tiene una interfase de línea de comandos "UNIX-like".
Use el "shell" sh para comunicarse con Hadoop.


'''

# probamos si funbciona docker desde el servidor: sudo docker run hello-world

#cd DS(tab)  >>> entro a la carpeta del cluster

#? nano start-conteiner.sh  >>>> es basicamente una interfaz grafica
#? otra interfaz es vi

# le damos permiso de ejecucion a start conteiner con;
#? chmod 777 start-container.sh
# luego ls -ll >> ahora aparece el verde

#creamos una red virtual> sudo docker create network --driver=bridge hadoop
#! https://docs.docker.com/engine/reference/commandline/network_create/

# luego ejecutamos el cluster con > sudo ./start-container.sh    >>>>> dentro de la master 
#  lo que hacemos es ejecutar un cluster hadoop en el servidos, las cuales son 3 maquinas de docker
#son 3 maquinas empaquetadas
#? luego de ejecutar el cluster, estoy adentro de la master, la cual es un container de docker
#sudo docker ps -a >> veo los contenedores activos

#  ejecuto el archivo start hadop (enciendo yarn y hdfs) >> ./start-hadoop.sh

#? ver las metricas del cluster> escribo la ip en el buscador y me lleva a una interfaz donde veo info del cluster

# descargo el txt de la odisea desde el nudo master, para usar map reduce.
#? >> wget https://raw.githubusercontent.com/uracilo/testdata/master/odisea.txt
#? >> ls -ll >> ahora tengo el archivo en el nodo master

#? creo un directorio con>>> mkdir input
#? comprimo el archivo con la instruccion tar de linux >> tar -czvf input/odisea.tar.gz odisea.txt
#? ls -flarts input >> veo tamanio de direnctorio

#entro al cluster
#? hdfs dfs -ls /  >>> cuanto escribo hdfs estoy en el cluster
# para crear un directorio EN en cluster, que se llama test: 
#? hdfs dfs -mkdir -p test
### notar que test ESTA DENTRO DE HDFS
# ponemos la carpeta input dentro de hdfs 
#? hdfs dfs -put input 
# chequeo que inout este en el cluster 

# el comando cat enlista un contenido de un archivo de texto
# si hago cat start-hadoop.sh veo lo que hay adentro de ese archivo
#? cat odisea.txt

#luego en el homework borramos el archivo con -rm (ver)

#ejecutamos al final un map reduce en hadoop (los 3 containers estan trabajando)


# para apagar todo 
#? sudo docker ps -a
#? sudo docker stop id de los 3 contenedores
#! aca simulamos el servidos y las maquinas de los clusteres en docker








#---------------------------# #---------------------------# #---------------------------# #---------------------------# #---------------------------#
#comandos de linux en la maquina virtual
#https://www.hostinger.es/tutoriales/linux-comandos#:~:text=1%20comando%20pwd.%20Usa%20el%20comando%20pwd%20para,6%20comando%20mv.%20...%207%20comando%20mkdir.%20
#? pwd (veo el directorio actual)
#? exit (cerrar cesion)
#? help (todas las ordenes del sistema)
#? ip a list (ver tu ip)
#? cd .. (con dos puntos) para ir un directorio hacia arriba
#? cd para ir directamente a la carpeta de inicio
#? cd- (con un guión) para ir al directorio anterior

#? ls -R también listará todos los archivos en los subdirectorios
#? ls -a mostrará los archivos ocultos
#? ls -al listará los archivos y directorios con información detallada como los permisos, el tamaño, el propietario, etc.

#? cat > nombredearchivo crea un nuevo archivo.
#? cat nombredearchivo1 nombredearchivo2>nombredearchivo3 une dos archivos (1 y 2) y almacena la salida de ellos en un nuevo archivo (3)
#? convertir un archivo a mayúsculas o minúsculas, cat nombredearchivo | tr a-z A-Z> salida.txt

#? cp copia archivos del directorio actual a un directorio diferent
#>  Por ejemplo, el comando cp escenario.jpg /home/nombredeusuario/Imagenes crearía una copia de escenario.jpg (desde tu directorio actual) en el directorio de Imagenes.

#?  mv es mover archivos, aunque también se puede usar para cambiar el nombre de los archivos
#> Por ejemplo: mv archivo.txt /home/nombredeusuario/Documentos.

#? mkdir para crear un nuevo directorio
#> mkdir Musica, creará un directorio llamado Musica. Para generar un nuevo directorio dentro de otro directorio, usa este comando básico de Linux mkdir Musica/Nuevoarchivo

#? rmdir borra un directorio que este vacio

#?  rm se usa para eliminar directorios y el contenido dentro de ellos. Si solo deseas eliminar el directorio, como alternativa a rmdir, usa rm -r.

#? touch te permite crear un nuevo archivo en blanco a través de la línea de comando de Linux.
#> touch /home/nombredeusuario/Documentos/Web.html para crear un archivo HTML titulado Web en el directorio Documentos

#? locate -i escuela*nota buscará cualquier archivo que contenga la palabra «escuela» y «nota», ya sea en mayúsculas o minúsculas

#? find también buscas archivos y directorios. La diferencia es que usas el comando find para ubicar archivos dentro de un directorio dado.

#? sudo este comando te permite realizar tareas que requieren permisos administrativos o raíz

#? df para obtener un informe sobre el uso del espacio en disco del sistema

#? du erificar cuánto espacio ocupa un archivo o un directorio

#?  history es particularmente útil si deseas revisar los comandos que ingresaste anteriormente

#? man tail se mostrarán las instrucciones manuales del comando tail.
#---------------------------# #---------------------------# #---------------------------# #---------------------------# #---------------------------#
