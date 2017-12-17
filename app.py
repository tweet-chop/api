from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import Chop

app = Flask(__name__)
cors = CORS(app, ressources={r"/api/*": {"origins" : ["http://localhost:*", "https://tweet-chop.herokuapp.com*"]}})

@app.route('/api/hello')
def index():
  return jsonify({'hello': 'Hello, Flask!'})

@app.route('/api/chop', methods=['POST'])
def chop_text():
  if not request.json or not 'text' in request.json:
    abort(400)

  # chops = request.json['text'].split(",")
  chops = Chop.chop(request.json['text'], int(request.json['chars']))
  return jsonify({'chops': chops})

if __name__ == "__main__":
  app.run(debug=True)
