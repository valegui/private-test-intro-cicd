Descarga y Setup
================


#. Clonar el repositorio

   .. code-block:: console
    
    $ git clone ...

#. Crear virtualenvironment

   .. code-block:: console
    
    $ python -m venv .venv
    $ source .venv/bin/activate

#. Instalar requisitos

   .. code-block:: console
       
    $ pip install -r requirements.txt

#. Instalar paquete

   .. code-block:: console
    
    $ pip install -e .

#. Build docs. Para hacer el build hay dos opciones:
   
   * Opcion 1
   
   .. code-block:: console
    
    $ sphinx-build -b html docs/source/ docs/build/html

    
   * Opcion 2
   
   .. code-block:: console
    
    $ cd docs
    $ make html





