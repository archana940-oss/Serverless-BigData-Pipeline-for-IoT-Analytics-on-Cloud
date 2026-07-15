

CREATE EXTERNAL TABLE IF NOT EXISTS iot_sensor_data (
    sensor_id STRING,
    timestamp STRING,
    temperature DOUBLE,
    humidity DOUBLE,
    pressure DOUBLE,
    battery_level DOUBLE,
    status STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES (
    "separatorChar" = ",",
    "quoteChar" = "\""
)
LOCATION 's3://iot-bigdata-pipeline-archana2026/'
TBLPROPERTIES (
    'skip.header.line.count'='1'
);
