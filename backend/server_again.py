import requests
from datetime import datetime
from collections import defaultdict
from psycopg2 import pool
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

# from logic import BOUGHT, SOLD


app = Flask(__name__)
cors = CORS(app)

postgreSQL_pool = pool.SimpleConnectionPool(
    1, 100, database="exampledb", user="docker", password="docker", host="localhost"
)
app.config["postgresSQL_pool"] = postgreSQL_pool


@app.route("/")
def health_check():
    return "I am healthy!"


app.run(debug=True, port=5000)
