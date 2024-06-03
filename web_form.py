import streamlit as st
import speech_syntese as ss


def main():
    st.title("Добро пожаловать в наш чат. Спросите меня что-нибудь")
    prompt = st.text_input("Введите ваш вопрос здесь:")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.expander(f"{message['role']}"):
            st.markdown(message["content"])

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.expander("user"):
            st.markdown(prompt)

        with st.expander("assistant"):
            message_placeholder = st.empty()
            full_response = ss.generate_answer(prompt)
            message_placeholder.markdown(full_response)
        st.session_state.messages.append(
            {"role": "assistant", "content": full_response}
        )


if __name__ == "__main__":
    main()
