import requests
from collections import defaultdict
from datetime import datetime
from psycopg2 import pool
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

# from logic import BOUGHT,SOLD
# from logic import format_db_row_to_transaction

app = Flask(__name__)
cors = CORS(app)


# Database Configuration
postgreSQL_pool = pool.SimpleConnectionPool(
    1, 100, dbname="exampledb", user="docker", password="docker", host="0.0.0.0"
)

app.config["postgresSQL_pool"] = postgreSQL_pool


@app.route("/")
def health_check():
    return "I am healthy"


app.run(debug=True, port=5000)
