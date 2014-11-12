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

