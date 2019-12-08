import pytest
from function.mysql_access import MySQL

@pytest.mark.parametrize('word', [("test")])
def test_crud(word):
    mysql = MySQL()
    result = mysql.insert(word)
    assert result["word"] == word
    assert result["success"] == True

    result = mysql.select_all()
    assert len(result) > 0

    result = mysql.delete(word)
    assert result["word"] == word
    assert result["success"] == True

