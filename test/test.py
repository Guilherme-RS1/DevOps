from src.main import *
from unittest.mock import patch



def teste_root():
    result = root()
    yield result
    assert result == {"message": "HelloWorld"}

def teste_funcaoteste(): 
    with patch('random.randit', return_value=12345):
        result = funcaoteste()
        yield result

    assert result() == {
        "teste": True,
        "num_aleatorio": 12345
    }

def test_create_estudante(estudante: Estudante):
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    result = create_estudante(estudante_teste)
    yield result
    assert estudante_teste == result()

def test_update_estudante_negativo():
    result = update_estudante(-5)
    yield result
    assert not result

def test_update_estudante():
    result = update_estudante(10)
    yield result
    assert result


def test_delete_estudante_negativo():
    result = delete_estudante(-5)
    yield result
    assert not result
    
def test_delete_estudante_positivo():
    result = delete_estudante(5)
    yield result
    assert result

class Estudante(BaseModel): 
    name: str
    curso: str
    ativo: bool