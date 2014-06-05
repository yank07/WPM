#!/bin/bash 

echo Instalando apps de django...
sudo apt-get -y install libpq-dev python-dev
sudo pip install psycopg2
sudo pip install south
sudo pip install -e git+git://github.com/mvpdev/django-eav.git#egg=django-eav
sudo pip install django-tables2
sudo pip install django-bootstrap-breadcrumbs
sudo pip install --upgrade django-crispy-forms
sudo pip install django-filter
sudo pip install django-simple-history

#desinstalar PIL 
sudo pip uninstall PIL
tar zxvf Imaging-1.1.6.tar.gz
sudo python ./Imaging-1.1.6/setup.py install

sudo pip install django-easy-pdf xhtml2pdf reportlab pisa
sudo apt-get install python-dev libjpeg-dev libfreetype6-dev zlib1g-dev
sudo ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/
sudo ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/
sudo ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/



echo Instalando libreria de grafos...
sudo apt-get -y install python-networkx

#instalar apache, mod-wsgi y activar mod-wsgi
sudo apt-get -y install apache2 libapache2-mod-wsgi apache2-utils apache2.2-common
sudo a2enmod wsgi
sudo a2enmod rewrite
echo creando base de datos...
su postgres -c "createdb -O postgres WPMDB_prod"

#configuracion de virtualhost
sudo cp wpm /etc/apache2/conf.d/ 

