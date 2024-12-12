from flask import Flask, jsonify, request
from database import fetch_sales_data
from analytics import calculate_summary

app = Flask(__name__)

@app.route("/sales", methods=["GET"])
def get_sales():
    data = fetch_sales_data()
    return jsonify(data)

@app.route("/analytics/summary", methods=["GET"])
def get_summary():
    data = fetch_sales_data()
    summary = calculate_summary(data)
    return jsonify(summary)

if __name__ == "__main__":
    app.run(debug=True)