
SELECT *
FROM iot_sensor_data
LIMIT 10;

-- Count total records
SELECT COUNT(*) AS total_records
FROM iot_sensor_data;

-- Average temperature
SELECT AVG(temperature) AS average_temperature
FROM iot_sensor_data;

-- Highest temperature
SELECT MAX(temperature) AS highest_temperature
FROM iot_sensor_data;

-- Lowest temperature
SELECT MIN(temperature) AS lowest_temperature
FROM iot_sensor_data;

-- Average humidity
SELECT AVG(humidity) AS average_humidity
FROM iot_sensor_data;

-- Active devices
SELECT status, COUNT(*) AS total_devices
FROM iot_sensor_data
GROUP BY status;

-- Battery level statistics
SELECT
    AVG(battery_level) AS average_battery,
    MAX(battery_level) AS highest_battery,
    MIN(battery_level) AS lowest_battery
FROM iot_sensor_data;
