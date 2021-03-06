from flask import Flask,render_template, request, jsonify
""" from flask-cors import CORS """
from chat import get_response
import os

client = Flask(__name__)
""" CORS(app) """

@client.get("/")
def index_get():
    return render_template("base.html")


@client.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    client.run(host='0.0.0.0', port=port,debug=True)