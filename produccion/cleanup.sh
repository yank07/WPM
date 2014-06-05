#!/bin/bash 
# cleanup entorno produccion
# borra el directorio src en la carpeta actual,
# y borra el directorio del proyecto en el root del apache

#export PGDATA = '/var/lib/postgresql/9.1/main'

echo Borrando db...
su postgres -c "psql -q WPMDB_prod < delete_db.sql"
echo Borrando carpeta temporal...
sudo rm -R ./src
echo Borrando root del apache
sudo rm -R /var/www/WPM 

