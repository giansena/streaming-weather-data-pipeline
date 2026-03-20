import requests
import mysql.connector
import time

api_key = "----"

cities = [
    "Cordoba,AR",
    "Buenos Aires,AR",
    "Rio de Janeiro,BR",
    "New York,US",
    "Los Angeles,US"
]

while True:
    for city in cities:
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()

                ciudad = data["name"]
                temperatura = data["main"]["temp"]
                humedad = data["main"]["humidity"]
                clima = data["weather"][0]["description"]
                viento = data["wind"]["speed"]

                conexion = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="hannah1hannah",
                    database="weather_db"
                )

                cursor = conexion.cursor()

                query = """
                INSERT INTO weather_data (ciudad, temperatura, humedad, clima, viento)
                VALUES (%s, %s, %s, %s, %s)
                """

                values = (ciudad, temperatura, humedad, clima, viento)

                cursor.execute(query, values)
                conexion.commit()

                print(f"{ciudad}: {temperatura}°C guardado")

                cursor.close()
                conexion.close()

            else:
                print(f"Error API con {city}")

        except Exception as e:
            print(f"Error con {city}: {e}")

    print("Esperando 60 segundos...\n")
    time.sleep(60)