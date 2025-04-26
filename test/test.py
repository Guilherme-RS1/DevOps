from src.main import *
from unittest.mock import patch

def teste_root():
    assert root() == {"message": "HelloWorld"}

def teste_funcaoteste(): 
    with patch('random.randit', return_value=12345):
        result = funcaoteste()

    assert result() == {
        "teste": True,
        "num_aleatorio": 12345
    }

def test_create_estudante(estudante: Estudante):
    estudante_teste = Estudante(name="Fulano", curso="Curso 1", ativo=False)
    assert estudante_teste == create_estudante()
    return estudante


def test_update_estudante():
    assert not update_estudante(-5)


def test_update_estudante():
    assert update_estudante(10)

def test_delete_estudante_negativo():
    assert not delete_estudante(-5)
    
def test_delete_estudante_positivo():
    assert delete_estudante(5)

class Estudante(BaseModel): 
    name: str
    curso: str
    ativo: bool