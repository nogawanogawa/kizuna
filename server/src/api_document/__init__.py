from flask import Blueprint, request, jsonify
from function.mysql_access import MySQL
from function.es_access import ES
from function.neo4j_access import Neo4j
import json

document = Blueprint('document', __name__, url_prefix='/document')

@document.route('/register', methods=["POST"])
def register():
    mysql = MySQL()
    es = ES()
    neo4j = Neo4j()
    
    data = request.data.decode('utf-8')
    data = json.loads(data)

    # create node
    doc = es.register(data)
    data["_id"] = doc["_id"]
    neo4j.create_document_node(data)    

    # create rel
    words = mysql.select_all()
    # キーワードが含まれるか検査 => 含まれるキーワード一覧
    matched_list = [tag for tag in [data["title"], data["content"]] if tag in words] 

    # キーワード一覧と結合
    for word in matched_list:
        rel = {"_id": data["_id"],"word": word}
        neo4j.create_document_keyword_relation(rel)

    return jsonify(data)

@document.route('/search', methods=["GET"])
def search():
    es = ES()

    word = request.args.get('word')
    return es.search(word)

@document.route('/update/<_id>', methods=['POST'])
def update(_id):
    es = ES()
    neo4j = Neo4j()

    data = request.data.decode('utf-8')
    data = json.loads(data)

    doc = es.update(_id, document=data)
    data["_id"] = _id
    neo4j.update_document_node(data)
    return jsonify(data)

@document.route('/<_id>', methods=['DELETE'])
def delete(_id):
    es = ES()
    neo4j = Neo4j()

    es.delete(_id)
    neo4j.delete_node(_id)

    return jsonify(_id=_id)


