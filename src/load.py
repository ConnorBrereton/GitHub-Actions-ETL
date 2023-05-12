import os
import requests
import snowflake.connector
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# Load the environment variables from the .env file.
ACCOUNT = os.getenv("ACCOUNT")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
WAREHOUSE = os.getenv("WAREHOUSE")
DATABASE = os.getenv("DATABASE")
SCHEMA = os.getenv("SCHEMA")

# Connecting to Snowflake using the default authenticator.
conn = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA
    )

# Set the warehouse, database, and schema.
conn.cursor().execute("USE warehouse COMPUTE_WH")
conn.cursor().execute("USE ETL_PIPELINE.BIKE_DATA")

# Create the temporary table.
conn.cursor().execute(
    "CREATE OR REPLACE TEMPORARY TABLE "
    "myjsontable(json_data variant)")

# Create file format JSON object.
conn.cursor().execute(
    "CREATE OR REPLACE FILE FORMAT myjsonformat type = 'JSON' "
    "strip_outer_array = TRUE")

# Putting the JSON data into the temporary table.
conn.cursor().execute(
    "PUT transformed_data.json @my_data auto_compress=true")

# Copy data into table 
conn.cursor().execute(
        "COPY INTO myjsontable FROM @my_data "
        "FILE_FORMAT = (format_name = myjsonformat) "
        "on_error='skip_file'")