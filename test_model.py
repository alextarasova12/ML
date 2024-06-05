import speech_syntese as ss

def test_answer():
    answer = ss.generate_answer("Привет")
    
    assert answer != "Ура"
    assert answer != ""
    assert "Привет" not in answer
    assert answer is not None
