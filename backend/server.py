import requests
from collections import defaultdict
from datetime import datetime
import pysopg2 import pool
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from logic import BOUGHT,SOLD
from logic import format_db_row_to_transaction

app = Flask(__name__)