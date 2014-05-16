WPM
===
Para la generación de los atributos dinámicos en los modelos se utiliza la aplicación django-eav (https://github.com/mvpdev/django-eav). Asegurarse de agregar 'eav' a la lista de aplicaciones instaladas.
También esto es necesario (¿por qué?) en el settings.py: SOUTH_MIGRATION_MODULES = {'eav': 'ignore',}

Para generar el grafo de relaciones del proyecto, debe instalarse el paquete 'networkx'. Para eso, ingrese este comando en la terminal:

sudo apt-get install python-networkx
