from neo4j.v1 import GraphDatabase

class Neo4j:
    def __init__(self):
        self.uri = "bolt://neo4j:7687"
        self.driver = GraphDatabase.driver(
            self.uri, auth=("neo4j", "password")
        )
    
    def create_document_node(self, property):
        """ドキュメントのノードを作成する
        
        Arguments:
            property {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        node_label = "Document"
        with self.driver.session() as session:
            query = "CREATE (a:" + node_label + "{title:$title, content:$content, _id:$_id}) RETURN a;"
            result = session.run(query, title=property["title"], content= property["content"], _id=property["_id"]).single()

        return property

    def create_keyword_node(self, property):
        """キーワードのノードを作成する
        
        Arguments:
            property {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        node_label = "Keyword"
        with self.driver.session() as session:
            query = "CREATE (a:" + node_label + "{word:$word}) RETURN a;"
            result = session.run(query, word=property["word"]).single()

        return property

    def create_document_keyword_relation(self, property):
        """ドキュメント-キーワードのリレーションを作成する
        
        Arguments:
            property {[type]} -- [description]
        """
        rel_label = ""
        with self.driver.session() as session:
            query = "MATCH (a:" + "Document" + "{_id:$_id}),(b:" + "Keyword" + \
                "{word:$word})" + "CREATE (a)-[r:Rel]->(b) RETURN r;"
            result = session.run(query, _id=property["_id"] ,word=property["word"]).single()

        return property
        
    def update_document_node(self, property):
        """ドキュメントノードを更新する
        
        Arguments:
            property {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        with self.driver.session() as session:
            query = "MATCH (a:Document{_id:$_id}) SET a={title:$title, content:$content, _id:$_id} RETURN a"
            result = session.run(query, title=property["title"], content= property["content"], _id=property["_id"]).single()

        return property


    def delete_node(self, property):
        """ノードを削除する
        
        Arguments:
            property {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        with self.driver.session() as session:
            query = "MATCH (n) where id(n) = $id DELETE n RETURN n;"
            result = session.run(query, id=property["id"] ).single()
        return property


    def delete_keyword_node_by_word(self, property):
        """単語が一致するKeywordノードを削除する
        
        Arguments:
            property {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        with self.driver.session() as session:
            query = "MATCH (n: Keyword{word:$word}) DELETE n RETURN n;"
            result = session.run(query, word=property["word"] ).single()
        return property


    def delete_document_keyword_relation(self, property):
        """リレーションを削除する
        
        Arguments:
            property {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        with self.driver.session() as session:
            query = "MATCH ()-[r]-() where id(r) = $id DELETE r RETURN r;"
            result = session.run(query, id=property["id"] ).single()
        return result
        
    