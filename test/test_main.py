import unittest
from unittest.mock import patch

# Suponha que a função obter_numero está no módulo my_module
from my_module import obter_numero

class TestObterNumero(unittest.TestCase):

    @patch('builtins.input', return_value='42')  # Substitui input() para sempre retornar '42'
    def test_obter_numero(self, mock_input):
        resultado = obter_numero()
        self.assertEqual(resultado, 42)  # Verifica se o retorno é 42

if __name__ == '__main__':
    unittest.main()