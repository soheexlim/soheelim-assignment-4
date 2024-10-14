from flask import Flask, request, render_template, jsonify
from lsa import LSA

app = Flask(__name__)
lsa_model = LSA(n_components=100)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.json['query']
    results = lsa_model.query(query)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
