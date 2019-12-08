from flask import Blueprint, request
from function.mysql_access import MySQL
from function.es_access import ES
from function.neo4j_access import Neo4j
import json

word = Blueprint('word', __name__, url_prefix='/word')

@word.route('/register', methods=['POST'])
def insert():
    """単語の登録
    
    Returns:
        [type] -- [description]
    """
    mysql = MySQL()
    neo4j = Neo4j()
    es = ES()

    data = request.data.decode('utf-8')
    data = json.loads(data)
    word = str(data['word'])

    result = {}

    # 1. 既存のkeywordに同一のものがないか確認
    exist = mysql.check_existance(word)

    # 2. 同一のものがなければ、RDBとNeo4jにinsert
    if exist != True:
        rdb = mysql.insert(word)
        node = neo4j.create_keyword_node({"word": word})
        result["rdb"] = rdb
        result["node"] = node
                
        # 3. Elasticsearchの全ドキュメントに対して該当keywordを使用して検索
        docs = es.search(word)

        # 4. 検索されたドキュメントidを持つノードとkeywordノードの間にエッジを構築
        rels = []
        for doc in docs:
            rel = neo4j.create_document_keyword_relation({"_id": doc["_id"], "word": word})
            rels.append(rel)
        result["rel"] = rels

    return result

@word.route('/', methods=['DELETE'])
def delete():
    """単語を削除する
    
    Returns:
        [type] -- [description]

    Note:
        クエリパラメータで削除するするものを指定する
    """
    mysql = MySQL()
    neo4j = Neo4j()

    data = request.data.decode('utf-8')
    data = json.loads(data)
    word = str(data['key'])

    result = {}

    # 1. 既存のkeywordに同一のものがないか確認
    exist = mysql.check_existance(word)

    # 2. 同一のものがあれば、RDBとNeo4jからレコードを削除
    if exist:
        rdb = mysql.delete(word)
        node = neo4j.delete_keyword_node_by_word({"word":word})
        result["rdb"] = rdb
        result["node"] = node

    return result

    @word.route('/search_all', methods=['GET'])
    def search_all():
        """単語の全件取得
        
        Returns:
            [type] -- [description]
        """
        mysql = MySQL()
        return mysql.select_all()

    @word.route('/search', methods=['GET'])
    def search():
        """単語の存在有無取得
        
        Returns:
            [type] -- [description]
        """
        mysql = MySQL()
        word = request.args.get('word')

        return "search_all"

