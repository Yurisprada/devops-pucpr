import unittest
from unittest.mock import patch
from src.Main import *

@patch('builtins.input', side_effect=['Alice', 'Bob'])
def test_cadastro_jogadores(self, mock_input):
    jogadores = cadastro_jogadores()
    self.assertEqual(jogadores, ['Alice', 'Bob'])
    print(jogadores)