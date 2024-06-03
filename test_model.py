import unittest
from unittest.mock import patch

import speech_syntese as ss

class TestSpeechSyntese(unittest.TestCase):
    @patch('speech_syntese.some_external_api_call') 
    def test_generate_answer(self, mock_api_call):
        mock_api_call.return_value = "Ответ от внешнего API"
        
        result = ss.generate_answer("Проверяемый запрос")
        self.assertEqual(result, "Ответ от внешнего API")

        mock_api_call.assert_called_with("Проверяемый запрос")

if __name__ == '__main__':
    unittest.main()
