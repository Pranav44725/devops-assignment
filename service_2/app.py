from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Service 2 is healthy"})

@app.route('/service2')
def service2():
    return jsonify({"message": "Hello from Python service!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)

