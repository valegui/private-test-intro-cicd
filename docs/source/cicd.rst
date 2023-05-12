Integracion Continua y Entrega Continua (CI/CD)
===============================================

GitHub Actions
==============
Permite tratar la pipeline CI como codigo. Solo se necesita un archivo .yaml para la definicion del 
workflow en un directorio llamado '.github/workflows'.

No importa el nombre que se le de a los archivos porque cada archivo describe cuando se debe 
ejecutar. El "cuando" es el evento que debe ocurrir para ejecutar el job.

Una gran ventaja de GitHub Actions sobre otras herramientas CI como Circle CI, Travis CI y Jenkins, 
es que basta con crear el directorio de workflows y agregar los .yaml, no es necesario configurar el 
workflow en una pagina externa.

Conceptos
^^^^^^^^^

Un Workflow es una series de procesos automaticos que se ejecutan por GitHub Actions. En un 
repositorio pueden haber multiples workflows (ej: 1 para CI, 1 para CD, 1 para Seguridad). Cada 
workflow se compone de:

.. graphviz::

    digraph conceptos {

       "Event" [shape=box]
       "Jobs" [shape=box]
       "Runner" [shape=ellipse]
       "Steps" [shape=box]
       "Actions" [shape=box]

       { rank=same "Event" "Jobs" "Runner" "Steps" "Actions"}

       "Event" -> "Jobs" -> "Runner" -> "Steps" -> "Actions";
   }



* Event
   Evento que dice cuando debe ejecutarse un workflow, por ejemplo push, pull_request, release, fork, 
   delete. 
   Ver `GitHub Actions Events <https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows>`_.
* Jobs
   Es un conjunto de pasos en un workflow que se ejecutan en un mismo 'Runner'. En un workflow hay 1 
   o mas 'Jobs'. Cada 'Job' puede contener 1 o mas 'Steps'. Por defecto los 'Jobs' se ejecutan en 
   paralelo, menos cuando se especifica dependencia (con la keyword 'needs').
* Runner
   Servidor donde se ejecutan los 'Jobs'.
* Steps
   Es un conjunto de shell commands o acciones. Aquellos que son parte de un mismo 'Job' se ejecutan 
   en el mimsmo 'Runner', por lo que pueden compartir informacion entre ellos. Los pasos se ejecutan
   en orden y se puede tener un paso para compilar, otro para aplicar formato, otro para los tests, 
   otro que crea un contenedor de Docker.
* Actions
   Es el nivel mas bajo en un workflow. Ejecutan una sola tarea.




Configurar
^^^^^^^^^^

Runner propio
-------------

Un self-hosted runner se puede agregar a un repositorio, una organizacion o una empresa. Como 
ejemplo, para agregar un runner a un repositorio se va a Settings/Actions/Runners.
Alli estaran las instrucciones para instalar la aplicacion de GitHub Actions para configurar un 
servidor como Runner. Tambien se indica como agregarlo al workflow. Todos los Runners propios tienen
labels que permiten seleccionarlo en el .yaml.

.. code-block::

   runs-on: [self-hosted, linux, ARM64]


Costos
------

.. list-table::
   :header-rows: 1

   * - Product
     - Storage
     - Minutes (per month)
   * - GitHub Free
     - 500 MB
     - 2,000
   * - GitHub Pro
     - 1 GB
     - 3,000
   * - GitHub Free for organizations
     - 500 MB
     - 2,000
   * - GitHub Team
     - 2 GB
     - 3,000
   * - GitHub Enterprise Cloud
     - 50 GB
     - 50,000

Para mas detalles de costos y tiempos, ver 
`About billing for GitHub Actions <https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions>`_.


