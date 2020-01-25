from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = "restdb"
app.config['MONGO_URI'] = "mongodb://localhost:27017/restdb"

mongo = PyMongo(app)


@app.route("/star", methods=['POST'])
def add_star():
    star = mongo.db.stars
    name = request.json['name']
    distance = request.json['distance']
    star_id = star.insert({"name": name, "distance": distance})
    new_star = star.find_one({"_id": star_id})
    output = {"name": new_star["name"], "distance": new_star["distance"]}
    return jsonify({"result": output}), 201


if __name__ == "__main__":
    app.run(debug=True)
