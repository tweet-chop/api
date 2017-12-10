from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, ressources={r"/api/*": {"origins" : ["http://localhost:*", "https://tweet-chop.herokuapp.com*"]}})

@app.route('/api/hello')
def index():
  return jsonify({'hello': 'Hello, Flask!'})

if __name__ == "__main__":
  app.run(debug=True)
