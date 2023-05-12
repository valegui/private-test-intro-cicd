Documentacion en Python y Sphinx
================================

Configurar Sphinx
-----------------

Documentacion de modulos
^^^^^^^^^^^^^^^^^^^^^^^^

Se usa 'sphinx.ext.napoleon' para generar documentacion de modulos a partir del docstring del codigo.
Despues de preparar Sphinx para la documentacion, se debe habilitar la extension en el 
archivo conf.py::
    
    # conf.py 
    extensions = ['sphinx.ext.napoleon']

Usar sphinx-apidoc para el build de la documentacion::

    $ sphinx-apidoc -f -o docs/source drinks

Esto genera un archivo modules.rst y un drinks.rst. Se debe hacer referencia a module.rst en algun
archivo o en compilacion habra un warning.

Una alternativa a este ultimo comando es usar la extension 'autoapi.extension'.
Para instalarla se debe ejecutar::

    $ pip install sphinx-apidoc

Luego se debe habilitar la extension en el archivo conf.py::
    
    # conf.py 
    extensions = ['sphinx.ext.napoleon', 'autoapi.extension']

Si bien la configuracion por defecto puede ser aceptable, las modificaciones pueden ser necesarias 
en caso de que se trabaje con otros lenguajes, o si se quiere tener mas control sobre la salida o 
contenidos. En particular, en la configuracion de esta documentacion se utiliza::

    # conf.py

    # Autoapi settings
    autoapi_type = 'python'
    autoapi_dirs = ['../../drinks']
    autoapi_file_patterns = ['*.py']
    autoapi_add_toctree_entry = False

La opcion 'autoapi_add_toctree_entry = False' es para que no agregue la documentacion de forma 
automatica al toctree. Para agregarlo al toctree se creo un archivo 'api.rst' que se agrega al 
toctree de index.rst, y el contenido de 'api.rst' es:

.. code-block:: rst
    
    API
    ===

    .. toctree::
       :maxdepth: 2

       autoapi/drinks/index

Snippets de codigo
^^^^^^^^^^^^^^^^^^

Se usa 'sphinx.ext.doctest' para agregar snippets de documentacion. Despues de agregarlo a conf.py
se puede ver algo como:

.. code-block:: rst

   >>> import drinks
   >>> tea = drinks.Tea()
   >>> tea.prepare_recipe()
   Boiling water
   Steeping the tea with water at 100.0°C
   Pour into cup
   Adding lemon


Documentacion dentro del codigo
-------------------------------

Python
