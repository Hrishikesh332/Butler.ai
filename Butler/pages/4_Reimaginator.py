import streamlit as st
import os
import openai 
from streamlit_option_menu import option_menu
st.subheader("Do you want to be more clear while expressing on text?")
st.write("Reimaginator helps you to convey your thoughts in a clear and concise manner by rephrasing your text. The Reimaginator provides you the new perspective to view the text and helps you to be expressive in a correct way.")
st.caption("Add your text here to rephrase it, and click Reimagine!!!")
statement1=st.text_area("Add your content below!!!")
button2=st.button("Paraphrase It")
def response3(statement1):
    openai.api_key = st.secrets["Api"]

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Rephrase the provided statement\nQ:{statement1}\nA: ",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response)
    return response.choices[0].text
if statement1 and button2:
        reimagine = response3(statement1)
        st.write(reimagine)

