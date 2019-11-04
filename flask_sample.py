from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        data = request.json
        return data
    else: 
        return 'Hello (GET)'

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
