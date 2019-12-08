from flask import Flask, request, jsonify
from flask_cors import CORS
from api_word import word
from api_document import document
import os 

app = Flask(__name__)
CORS(app)

app.register_blueprint(word)
app.register_blueprint(document)

