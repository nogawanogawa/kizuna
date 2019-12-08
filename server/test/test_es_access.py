import pytest
import time
import json
from function.es_access import ES


@pytest.mark.parametrize('body', [
    (
        {"title": "test_title", "content": "test_content"}
    )
]) 
def test_crud(body):
    es = ES()

    result = es.register(body)
    shards = result["_shards"]
    assert shards["successful"] == 1

    _id = result["_id"]

    time.sleep(3)
    
    result = es.search_all()
    assert len(result) > 0

    content_ = "test_update"
    result = es.update(_id=_id, document={"content": content_})
    shards = result["_shards"]
    assert shards["successful"] == 1

    time.sleep(3)

    result = es.delete(_id=_id)
    assert result["result"] == "deleted"
