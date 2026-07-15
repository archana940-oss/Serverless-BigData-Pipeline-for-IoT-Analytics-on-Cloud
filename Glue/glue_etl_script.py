
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.dynamicframe import DynamicFrame

# Initialize Spark and Glue Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# -----------------------------
# Read CSV from Amazon S3
# -----------------------------
input_path = "s3://iot-bigdata-pipeline-archana2026/"

datasource = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [input_path]},
    format="csv",
    format_options={"withHeader": True}
)

# Convert DynamicFrame to Spark DataFrame
df = datasource.toDF()

# -----------------------------
# Data Cleaning
# -----------------------------

# Remove duplicate records
df = df.dropDuplicates()

# Remove rows containing null values
df = df.na.drop()

# -----------------------------
# Convert back to DynamicFrame
# -----------------------------
cleaned_data = DynamicFrame.fromDF(df, glueContext, "cleaned_data")

# -----------------------------
# Save Processed Data
# -----------------------------
output_path = "s3://YOUR-BUCKET-NAME/processed-data/"

glueContext.write_dynamic_frame.from_options(
    frame=cleaned_data,
    connection_type="s3",
    connection_options={"path": output_path},
    format="parquet"
)

print("ETL Job Completed Successfully.")
