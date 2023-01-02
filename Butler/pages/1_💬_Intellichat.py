import streamlit as st
import os
import openai 
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Intellichat", page_icon="💬")
st.subheader("You're at the right place to get the answer of any question in this whole universe!!!")
st.write('''
IntelliChat: This name highlights the intelligence and chat capabilities of ChatGPT3, making it clear that it's a smart and capable AI chatbot.
    ''')
question=st.text_area("Add your question below!!!")
button=st.button("Answer")
def response1(ques):
    openai.api_key = st.secrets["Api"]

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Ask me anything\nQ:{question}\nA: ",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response)
    return response.choices[0].text
if question and button:
    reply=response1(question)
    st.write(reply)
    
    