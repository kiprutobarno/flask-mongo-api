from flask import Flask, request, jsonify, json
from flask_pymongo import PyMongo, MongoClient


app = Flask(__name__)
app.config['MONGO_DBNAME'] = "restdb"
app.config['MONGO_URI'] = "mongodb://localhost:27017/restdb"

mongo = PyMongo(app)


@app.route("/stars", methods=['POST'])
def add_star():
    data = request.get_json()
    id = mongo.db.stars.insert(data)
    cursor = mongo.db.stars.find({"_id": id})

    res = []
    for star in cursor:
        res.append({
            "_id": str(star['_id']),
            "name": star["name"],
            "distance": star["distance"]
        })
    return jsonify({"star": res}), 201


@app.route("/stars", methods=['GET'])
def get_stars():
    cursor = mongo.db.stars.find({})
    stars = []
    for star in cursor:
        stars.append({
            "_id": str(star['_id']),
            "name": star["name"],
            "distance": star["distance"]
        })
    return jsonify({"results": stars}), 200


if __name__ == "__main__":
    app.run(debug=True)
