#https://blog.desdelinux.net/cron-crontab-explicados/

#?¿Qué es cron?
#El nombre cron viene del griego chronos que significa “tiempo”. En el sistema operativo Unix, 
# cron es un administrador regular de procesos en segundo plano (demonio) que ejecuta procesos o guiones a intervalos regulares
# (por ejemplo, cada minuto, día, semana o mes). Los procesos que deben ejecutarse y la hora en la que deben hacerlo se especifican 
# en el fichero crontab.

#?Cómo funciona
#El demonio cron inicia de /etc/rc.d/ o /etc/init.d dependiendo de la distribucion. 
# Cron se ejecuta en el background, revisa cada minuto la tabla de tareas crontab /etc/crontab o en /var/spool/cron 
# en búsqueda de tareas que se deban cumplir. Como usuario podemos agregar comandos o scripts con tareas a cron para 
# automatizar algunos procesos. Esto es util por ejemplo para automatizar la actualizacion de un sistema o un buen sistema de respaldos.


