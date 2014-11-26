import requests
import responses


def test_cargo_object():
    from compropago import Cargo
    c = Cargo(
        product_price = 10000.0,
        product_name = "SAMSUNG GOLD CURL",
        product_id = "SMGCURL1",
        image_url = "https =//test.amazon.com/5f4373",
        customer_name = "Alejandra Leyva",
        customer_email = "noreply@compropago.com",
        payment_type = "OXXO"
    )
    assert isinstance(c.to_dict(), dict)

def test_api_endpoint():
    from compropago import CompropagoAPI
    api = CompropagoAPI('My API Key')
    assert(api.Endpoint== 'https://api.compropago.com/v2')

@responses.activate
def test_auth():
    from compropago import CompropagoAPI
    API_KEY = '687881193b2423'
    api = API(API_KEY)
    responses.add(
        RESPONSES.GET,
        'https://api.compropago.com/v1/charges/c90870de-55a2-4b50-bd6b-9c7887787b35',
        body = """
          {
            "type":"charge.pending",
            "object":"event",
            "data": {
              "object": {
                "id": "fe92a1a5-abec-49e3-877c-5024c1464dc3",
                "object": "charge",
                "created_at": "2013-12-09T18:59:28.048Z",
                "paid": true,
                "amount": "150.00",
                "currency": "mxn",
                "refunded": false,
                "fee": "7.50",
                "fee_details": {
                  "amount": "7.50",
                  "currency": "mxn",
                  "type": "compropago_fee",
                  "description": "Honorarios de ComproPago",
                  "application": null,
                  "amount_refunded": 0,
                }
                "payment_details": {
                  "object": "cash",
                  "store": "OXXO",
                  "country": "MX",
                  "product_id": "SMGCURL1",
                  "product_price": "150.00",
                  "product_name": "SAMSUNG GOLD CURL",
                  "image_url": "https://test.amazon.com/5f4373",
                  "success_url": "",
                  "customer_name": "Alejandra Leyva",
                  "customer_email": "noreply@compropago.com",
                  "customer_phone": "2221515801",
                }
                "captured": true,
                "failure_message": null,
                "failure_code": null,
                "amount_refunded": 0,
                "description": "Estado del pago - ComproPago",
                "dispute": null,
              }
            }
          }
          """)
    resp = api.verificar_cargo
