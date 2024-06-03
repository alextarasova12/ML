import streamlit as st
import speech_syntese as ss

def main():
    st.title("Добро пожаловать в наш чат. Спросите меня что-нибудь")
    prompt = st.text_input("Введите ваш вопрос здесь:")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        st.markdown(f"### {message['role']}")
        st.write(message["content"])

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.markdown(f"### user")
        st.write(prompt)

        response = ss.generate_answer(prompt)
        if response is not None:
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.markdown(f"### assistant")
            st.write(response)
        else:
            st.warning("Извините, в данный момент у меня возникли проблемы с генерацией ответа. Могу ли я помочь вам с чем-то еще?")

if __name__ == "__main__":
    main()
