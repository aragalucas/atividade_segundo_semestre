from main import idds
def test_negativo():
    assert idds(-57) == "===numero negativo==="
    assert idds(-1) == "===numero negativo==="
def test_positivo():
    assert idds(0) == "" 
    assert idds(20) == ""