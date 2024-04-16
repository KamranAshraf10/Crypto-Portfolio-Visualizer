import requests
from collections import defaultdict
from datetime import datetime
from psycopg2 import pool
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

# from logic import BOUGHT,SOLD
from logic import format_db_row_to_transaction

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


# Database Configuration
postgreSQL_pool = pool.SimpleConnectionPool(
    1,
    100,
    dbname="exampledb",
    user="docker",
    password="docker",
    host="127.0.0.1",
    # host="localhost"
)

app.config["postgresSQL_pool"] = postgreSQL_pool


@app.route("/")
def health_check():
    return "I am healthy"


@app.route("/transactions", methods=["POST"])
def new_transaction():
    name = request.json["name"]
    symbol = request.json["symbol"]
    type = request.json["type"]
    amount = request.json["amount"]
    time_transacted = request.json["time_transacted"]
    time_created = request.json["time_created"]
    price_purchased_at = request.json["price_purchased_at"]
    no_of_coins = request.json["no_of_coins"]

    conn = postgreSQL_pool.getconn()
    cur = conn.cursor()

    # Use parameterized query to prevent SQL injection
    insert_statement = """
    INSERT INTO transaction (name, symbol, type, amount, time_transacted, time_created, price_purchased_at, no_of_coins)
    VALUES (%s, %s, %s, %s, to_timestamp(%s), to_timestamp(%s), %s, %s)
    """
    cur.execute(
        insert_statement,
        (
            name,
            symbol,
            type,
            amount,
            time_transacted,
            time_created,
            price_purchased_at,
            no_of_coins,
            coins,
        ),
    )
    conn.commit()

    # Release the connection back to the pool
    postgreSQL_pool.putconn(conn)

    return jsonify()


@app.route("/transactions")
@cross_origin()
def get_transactions():
    cur = postgreSQL_pool.getconn().cursor()
    cur.execute("SELECT * FROM TRANSACTION")
    rows = cur.fetchall()

    return jsonify([format_db_row_to_transaction(row) for row in rows])


if __name__ == "__main__":
    app.run(debug=True, port=5000)
