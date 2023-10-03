#conversor de monedas utilizando la API de un sistema financiero en tiempo real

#Pasos previos a la escritura del código
#Paso 1: registrarse en ExchangeRatesAPI.io o en una API similar que ofrezca tasas de cambio en tiempo real y obtener allí una clave de API
#Paso 2: Instalar el módulo requests

# Importamos el módulo requests
import requests

# Definimos la URL base de la API y tu clave de API
base_url = "http://api.exchangeratesapi.io/v1/latest?access_key=6a8289bd979b6fb97a50fe55ae31a102&symbols=USD,AUD,CAD,PLN,MXN&format=1"
api_key = "6a8289bd979b6fb97a50fe55ae31a102"

# Parámetros de la solicitud
params = {
    "apikey": api_key
}

# Solicitar los datos de tasas de cambio
response = requests.get(base_url, params=params)
data = response.json()

# Verificamos si la solicitud HTTP fue exitosa
if response.status_code == 200:
    # Obtenemos las tasas de cambio de la respuesta
    tasas = data["rates"]

    # Pedimos al usuario que ingrese la cantidad y las monedas
    cantidad = float(input("Ingresa la cantidad a convertir: "))
    moneda_origen = input("Ingresa la moneda de origen: ").upper()
    moneda_destino = input("Ingresa la moneda de destino: ").upper()

    if moneda_origen in tasas and moneda_destino in tasas:
        # Realizar la conversión
        tasa_origen = tasas[moneda_origen]
        tasa_destino = tasas[moneda_destino]
        resultado = cantidad * (tasa_destino / tasa_origen)
        print(f"{cantidad} {moneda_origen} equivale a {resultado} {moneda_destino}")
    else:
        print("Moneda no válida. Asegúrate de ingresar códigos de moneda válidos.")
else:
    print("Error al obtener los datos de tasas de cambio.")




#Estas son las monedas admitidas por la API utilizada (al día 25/09/23)
"""{
  "success": true,
  "timestamp": 1695653647,
  "base": "EUR",
  "date": "2023-09-25",
  "rates": {
    "USD": 1.057972,
    "AUD": 1.650938,
    "CAD": 1.426833,
    "PLN": 4.608227,
    "MXN": 18.364267
  }
}"""