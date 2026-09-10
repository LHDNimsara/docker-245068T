from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_data():
    return jsonify({
        "student_id": "245068T",
        "status": "success",
        "message": "Docker API container running successfully!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)