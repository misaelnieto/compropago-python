#coding: utf-8
import requests

class Cargo(object):
    """ 
        product_price = 10000.0,
        product_name = "SAMSUNG GOLD CURL",
        product_id = "SMGCURL1",
        image_url = "https =//test.amazon.com/5f4373",
        customer_name = "Alejandra Leyva",
        customer_email = "noreply@compropago.com",
        payment_type = "OXXO"
    """

    def __init__(self, product_price, product_name, product_id, image_url, customer_name, customer_email, payment_type):
        self.product_price = product_price
        self.product_name = product_name
        self.product_id = product_id
        self.image_url = image_url
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.payment_type = payment_type


class CompropagoAPI(object):
    errores = {
        4001: u'Llave no encontrada',
        5001: u'ID de pago no encontrado',
        5002: u'Tienda no encontrada',
        5003: u'El precio del producto excede el límite por transacción en el establecimiento seleccionado',
        6001: u'Hubo un problema con el proveedor de SMS y el mensaje no se envío',
        6002: u'Se ha superado el número de envios SMS, máximo 2 mensajes por orden de pago',
        6003: u'Compañia celular inválida, soportamos: TELCEL, MOVISTAR, IUSACELL, UNEFON y NEXTEL',
        6004: u'Número de celular no válido, probablemente el número contiene menos o más de 10 dígitos',
    }

    def __init__(self, api_key, url_base='https://api.compropago.com'):
        self.api_key = api_key
        self.url_base = url_base

    def crear_cargo(self, cargo):
        r = requests.post('/'.join(self.url_base, '/v1/charges'))

    def verificar_cargo(self, info):
        pass

    def enviar_sms(self, **kwargs):
        pass        