import unittest
from unittest.mock import patch

class TestSpeechSyntese(unittest.TestCase):
    @patch('speech_syntese.some_external_api_call')
    def test_generate_answer(self, mock_api_call):
        mock_api_call.return_value = "Ожидаемый ответ"
        
        answer = ss.generate_answer("Привет")
        self.assertEqual(answer, "Ожидаемый ответ")
        
        mock_api_call.assert_called_with("Привет")

if __name__ == '__main__':
    unittest.main()
