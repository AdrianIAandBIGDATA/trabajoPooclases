import requests
import json
url0= "https://v6.exchangerate-api.com/v6/b63c2f0eb7f960cee32fc1db/codes"
response1 = requests.get(url0)
datos1 = response1.json()
codigos = datos1["supported_codes"]

for codigo, nombre in codigos:
    print(f"Código: {codigo}, Nombre: {nombre}")
moneda1 = input("Ingresa la moneda que tengas: ")
moneda1=moneda1.upper()
moneda2 = input("Ingresa la moneda que quieras: ")
moneda2= moneda2.upper()
cantidad = input("Ingresa la cantidad que quieras convertir: ")

#url = "https://v6.exchangerate-api.com/v6/b63c2f0eb7f960cee32fc1db/latest/EUR"
url = "https://v6.exchangerate-api.com/v6/b63c2f0eb7f960cee32fc1db/pair/"+moneda1+"/"+moneda2+"/"+cantidad
response = requests.get(url)


if response.status_code == 200:
   
    datos = response.json()
    conversion_rate = datos["conversion_rate"]
    conversion_result = datos["conversion_result"]
    print("El porcentaje de conversion es:", conversion_rate)
    print("La cantidad sera:", conversion_result)
    #print("Datos obtenidos:", datos)
else:
    print("Error en la solicitud. Código de estado:", response.status_code)
    print("Texto de respuesta:", response.text)



