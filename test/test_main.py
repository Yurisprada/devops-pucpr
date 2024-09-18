import unittest
from unittest.mock import patch
from src.Main import *

def test_import_jogo():
    try:
        from src.com.jogo import Jogo
    except ImportError as e:
        assert False, f"Importação falhou: {e}"
    assert True  # O teste passa se a importação for bem-sucedida

def test_jogo_instanciacao():
    from src.com.jogo import Jogo
    jogo = Jogo()
    assert jogo is not None  # Verifica se a instância foi criada