import pdb
import pytest
from function.neo4j_access import Neo4j

@pytest.mark.parametrize('prop', [({
    "title": "title",
    "content": "content",
    "_id":"_id"
})]) 
def test_crud(prop):
    neo4j = Neo4j()

    # create
    node_label = "a"
    document = neo4j.create_document_node(prop)
    assert document[node_label]["title"] == prop["title"]
    assert document[node_label]["content"] == prop["content"]
    assert document[node_label]["_id"] == prop["_id"]

    node_id = document[node_label].id

    word = {"word" : prop["title"]}
    keyword = neo4j.create_keyword_node(word)
    assert keyword[node_label]["word"] == prop["title"]

    word_id = keyword[node_label].id

    rel = {"_id":prop["_id"], "word": prop["title"]}
    relation = neo4j.create_document_keyword_relation(rel)

    rel_id = relation["r"].id

    # update
    prop["content"] = "content_update"
    document = neo4j.update_document_node(prop)
    assert document[node_label]["title"] == prop["title"]
    assert document[node_label]["content"] == prop["content"]
    assert document[node_label]["_id"] == prop["_id"]

    # delete
    rel_result = neo4j.delete_document_keyword_relation({"id": rel_id})
    node_result = neo4j.delete_node({"id": node_id})
    key_result = neo4j.delete_node({"id": word_id})
