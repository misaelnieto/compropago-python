compropago-python
=================

This is the Python library for ComproPago (https://compropago.com/), a Mexican
payment gateway.

Spanish from now on...

Esta es la libreria de Python para Compropago (https://compropago.com/).

ComproPago es una plataforma de pagos en efectivo que ayuda a que personas que
no cuentan con tarjeta de crédito puedan realizar transacciones en tiendas en
línea.

Los clientes finales puedan pagar sus compras de Internet en establecimientos
como 7Eleven, Oxxo, Extra, Soriana, Walmart, Coppel, Farmacia Benavides,
Bodega Aurrera y Farmacias Guadalajara entre otros.


Instalación
-----------

Con ``pip`` se instala así::

    pip install compropago-python

Si usas `zc.buildout <http://www.buildout.org/en/latest/>`_ solo necesitas
añadir ``compropago-python`` a la sección ``eggs``::

    [buildout]
    eggs =
        ...
        compropago-python

Instalación en modo desarrollo
------------------------------

En Linux
~~~~~~~~

Nota: En mac deberia funcionar de manera
parecida, pero como no tengo mac no te
puedo saber con certeza.

Debes de tener instalado pip y de preferencia virtualenv y virtualenvwrapper.

.. code-block:: bash

    mkvirtualenv ve
    workon ve
    cd compropago-python
    python setupy.py develop

Con esto se instalan las dependencias. Ahora solo necesitas correr las pruebas.

.. code-block:: bash
    nosetests

En Windoge
~~~~~~~~~~

Instala Python. Yo lo instale con chocolatey, pero puedes usar el metodo
que quieras. Chocolatey instaló python en C:\Tools\Python2.

Después de instalar Python hay que instalar pip con `get-pip.py
<https://bootstrap.pypa.io/get-pip.py>`_. [1]_

.. code-block:: msdos

    C:\Tools\Python2\python.exe get-pip.py

Despues puedes instalar virtualenv y crear tu entorno virtual.

.. code-block:: msdos

    C:\Tools\Python2\Scripts\pip.exe install virtualenv
    CD C:\Code\MyProject
    C:\Tools\Python2\Scripts\mkvirtualenv.exe ve
    ve\Scripts\activate.exe

Finalmente 
    cd compropago-python
    ..\ve\Scripts\python.exe setup.py develop
    ..\ve\Scripts\nosetests.exe


Autenticación
-------------

Crear un cargo
--------------

Verificar un cargo existente
----------------------------

Enviar instrucciones mediante SMS
---------------------------------

Errores
--------

Código  Descripción

4001    Llave no encontrada
5001    ID de pago no encontrado
5002    Tienda no encontrada
5003    El precio del producto excede el límite por transacción en el establecimiento seleccionado
6001    Hubo un problema con el proveedor de SMS y el mensaje no se envío
6002    Se ha superado el número de envios SMS, máximo 2 mensajes por orden de pago
6003    Compañia celular inválida, soportamos: TELCEL, MOVISTAR, IUSACELL, UNEFON y NEXTEL
6004    Número de celular no válido, probablemente el número contiene menos o más de 10 dígitos

