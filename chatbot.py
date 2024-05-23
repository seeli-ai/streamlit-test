# Code refactored from https://docs.streamlit.io/knowledge-base/tutorials/build-conversational-apps

from openai import OpenAI

import streamlit as st

with st.sidebar:
    st.title('🤖💬 OpenAI Chatbot')
    if 'OPENAI_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')
        api_key = st.secrets['OPENAI_API_KEY']
    else:
        api_key = st.text_input('Enter OpenAI API token:', type='password')
        if not (api_key.startswith('sk-') and len(api_key)==51):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        client = OpenAI(api_key=api_key)
        for response in client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[{"role": m["role"], "content": m["content"]}
                  for m in st.session_state.messages], stream=True):

            if response.choices[0].delta.content is not None:
                full_response += response.choices[0].delta.content
            else:
                full_response += ""
            
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
