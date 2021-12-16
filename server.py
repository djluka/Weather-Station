from flask import Flask, jsonify, make_response
from flask_cors import CORS, cross_origin
from db import mysql_conn, get_recent_temperature

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/temperature")
@cross_origin()
def get_temperature():
    conn = mysql_conn()
    record = get_recent_temperature(conn)
    
    return jsonify(record)

if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1')

