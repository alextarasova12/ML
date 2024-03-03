import speech_syntese as ss


def test_answer():
    answer = ss.generate_answer("Привет")
    assert answer != "Ура"
    assert answer is not None

def test_cleaning():
    dirty_answer = "@@ПЕРВЫЙ@@ Привет! Как дела? @@ВТОРОЙ@@ 🤡👍🏻 а как дела у тебя?😉@@ПЕРВЫЙ@@@@ПЕРВЫЙ@@"
    clean_answer  = ss.clean_answer(dirty_answer)
    assert clean_answer.find("@@ПЕРВЫЙ@@") is not True
    assert clean_answer.find("@@Второй@@") is not True