from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.json
    num1 = int(data.get('num1', 0))
    num2 = int(data.get('num2', 0))
    result = num1 + num2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

