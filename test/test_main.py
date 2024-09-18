import unittest
from unittest.mock import patch
from src.Main import *

class TestZombieDice(unittest.TestCase):
    def test_import_jogo():
        try:
            from src.com.jogo import Jogo
        except ImportError as e:
            assert False, f"Importação falhou: {e}"
        assert True  # O teste passa se a importação for bem-sucedida