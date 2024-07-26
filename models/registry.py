from flask import Flask, request, jsonify

app = Flask(__name__)
model_registry = {}

@app.route('/models/<model_name>', methods=['GET'])
def check_model(model_name):
    if model_name in model_registry:
        return jsonify({"available": True, "path": model_registry[model_name]})
    return jsonify({"available": False}), 404

@app.route('/models/<model_name>', methods=['POST'])
def register_model(model_name):
    data = request.json
    model_registry[model_name] = data['path']
    return jsonify({"status": "registered"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)