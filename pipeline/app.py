from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="hannah1hannah",
        database="weather_db"
    )

@app.route("/weather", methods=["GET"])
def get_weather():
    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    query = """
    SELECT ciudad, pais, temperatura, humedad, clima, viento, fecha
    FROM weather_data
    ORDER BY fecha DESC
    LIMIT 10
    """

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)