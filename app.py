import json
from flask import Flask, jsonify, request, send_from_directory
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root',
                         password='pass',
                        authSource="admin")
    db = client["chiottes_db"]
    return db

@app.route('/')
def ping_server():
    return send_from_directory('.', 'api_documentation.html')

@app.route('/chiottes')
def get_stored_chiottes():
    db = get_db()
    chiottes = db.chiottes.find()
    result = []
    for chiotte in chiottes:
        result.append({
            'titre': chiotte['titre'],
            'ref': chiotte['ref'],
            'dimension': chiotte['dimension'],
            'couleur': chiotte['couleur']
        })
    return jsonify(result)

@app.route('/chiottes/add_all', methods=['POST'])
def add_all_chiottes():
    with open('data.json') as f:
        data = json.load(f)
    if data and isinstance(data, list):
        db = get_db()
        db.chiottes.insert_many(data)
        return jsonify({'status': 'success', 'message': 'All products added.'}), 201
    else:
        return jsonify({'status': 'error', 'message': 'Invalid data format.'}), 400

@app.route('/chiottes/delete_all', methods=['DELETE'])
def delete_all_chiottes():
    db = get_db()
    db.chiottes.delete_many({})
    return jsonify({'status': 'success', 'message': 'All products deleted.'}), 200

@app.route('/chiottes/add', methods=['POST'])
def add_chiotte():
    data = request.get_json()
    if data and isinstance(data, dict):
        db = get_db()
        result = db.chiottes.insert_one(data)
        return jsonify({'status': 'success', 'message': 'Product added.', 'id': str(result.inserted_id)}), 201
    else:
        return jsonify({'status': 'error', 'message': 'Invalid data format.'}), 400
    
@app.route('/chiottes/update/<chiotte_id>', methods=['PUT'])
def update_chiotte(chiotte_id):
    data = request.get_json()
    if data and isinstance(data, dict):
        db = get_db()
        result = db.chiottes.update_one({'_id': ObjectId(chiotte_id)}, {'$set': data})
        if result.modified_count > 0:
            return jsonify({'status': 'success', 'message': 'Product updated.'}), 200
        else:
            return jsonify({'status': 'error', 'message': 'Product not found.'}), 404
    else:
        return jsonify({'status': 'error', 'message': 'Invalid data format.'}), 400

@app.route('/chiottes/delete/<chiotte_id>', methods=['DELETE'])
def delete_chiotte(chiotte_id):
    db = get_db()
    result = db.chiottes.delete_one({'_id': ObjectId(chiotte_id)})
    if result.deleted_count > 0:
        return jsonify({'status': 'success', 'message': 'Product deleted.'}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Product not found.'}), 404

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)