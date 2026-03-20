CREATE DATABASE weather_db;
USE weather_db;

CREATE TABLE weather_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ciudad VARCHAR(50),
    temperatura FLOAT,
    humedad INT,
    clima VARCHAR(50),
    viento FLOAT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM weather_data;

USE weather_db;

ALTER TABLE weather_data
ADD COLUMN pais VARCHAR(10);