from elasticsearch import Elasticsearch

class ES():

    def __init__(self):
        self.es = Elasticsearch("elasticsearch:9200")
        self.index = "document"

    def __search(self, body, size=10000):
        """検索してarray[dict]に置き換える
        
        Arguments:
            body {[type]} -- [description]
        
        Keyword Arguments:
            size {int} -- [description] (default: {10000})
        
        Returns:
            [type] -- [description]
        """
        result = []

        res = self.es.search(index=self.index, body=body, size=size)
        for doc in res['hits']['hits']:
            item = doc["_source"]
            dictionary = dict(_id=doc["_id"])
            dictionary.update(item)
            result.append(dictionary)

        return result

    def register(self, document):
        """ドキュメントを登録する
        
        Arguments:
            document {[type]} -- [description]
        """
        return self.es.index(index=self.index, doc_type=self.index, body=document)

    def search_all(self):
        """全件検索する
        
        Returns:
            [type] -- [description]
        """
        body = {"query": {"match_all": {}}}
        return self.__search(body=body)


    def search(self, word):
        """単語で検索する
        
        Returns:
            [type] -- [description]
        """
        body = {"query": {
                    "multi_match": {
                        "fields": ["title", "content"],
                        "query": word
                        }
                    }
                }
        return self.__search(body=body)


    def update(self, _id, document):
        """ドキュメントを更新する
        
        Arguments:
            _id {[type]} -- [description]
            document {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """

        return self.es.update(index=self.index, doc_type=self.index, id=_id, body={"doc":document})
    
    def delete(self, _id):
        """ドキュメントを削除する
        
        Arguments:
            _id {[type]} -- [description]
        
        Returns:
            [type] -- [description]
        """
        return self.es.delete(index=self.index, doc_type=self.index, id=_id)
