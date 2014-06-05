#!/bin/bash 


#restaurar la bd en una nueva
echo Poblando la base de datos... Si se le solicita la contraseña del usuario postgres, ingresela
su postgres -c "psql -q WPMDB_prod < wpmdb.sql"

#crear directorio para descargar del git
echo Descargando proyecto de github
mkdir source
cd source
git clone https://github.com/yank07/WPM.git

#copiar settings.py modificado con la bd produccion
cd ..
cp settings.py ./source/WPM/WPM
cp jquery-1.11.0.min.js .source/WPM/WPM/static/js

#copiar al root del apache
echo Copiando al root del apache...
cd source
sudo cp -R WPM /var/www/
cd /var/www
cd ./WPM/WPM/
sudo mkdir uploaded_files
cd uploaded_files
sudo mkdir tmp
cd /var/www
sudo chown -R www-data WPM
sudo chmod -R 777 WPM
sudo mkdir .matplotlib
sudo chmod -R 757 .matplotlib


#reiniciar el apache
echo Reiniciando el servidor apache...
sudo service apache2 restart
echo Listo! Abra el navegador e ingrese la direccion especificada
