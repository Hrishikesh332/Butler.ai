import streamlit as st
import os
import openai 
from streamlit_option_menu import option_menu
st.subheader("Are you Bored?")
st.write("Are you bored of reading a long text and wanted to cover long text in a short time or wanted to summarize the long text in the best way. Here, Bulter.ai provides you the wand and the wizard summarizer to help you out.")
st.caption("Add your long text in the box below! and click the apply spell button")

statement=st.text_area("Add your content below!!!")
button1=st.button("Summarize")
def response2(statement):
    openai.api_key = st.secrets["Api"]

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Summarize anything\nQ:{statement}\nA: ",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response)
    return response.choices[0].text
if statement and button1:
        summary = response2(statement)
        st.write(summary)

