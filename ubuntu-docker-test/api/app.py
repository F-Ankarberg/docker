from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/health')
def health():
    return jsonify({"status": "ok"})

@app.route('/api/data')
def data():
    return jsonify({"message": "Hello from the API container!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
