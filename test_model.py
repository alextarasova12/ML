import unittest
import speech_syntese as ss
from unittest.mock import patch

class TestSpeechSyntese(unittest.TestCase):
    @patch('speech_syntese.some_external_api_call')
    def test_generate_answer(self, mock_api_call):
        answer = ss.generate_answer("Привет")
        self.assertNotEmpty(answer) 
        
        mock_api_call.assert_called_with("Привет") 

if __name__ == '__main__':
    unittest.main()
