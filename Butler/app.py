import streamlit as st
import os
import openai 
from streamlit_option_menu import option_menu

selected = option_menu(
            menu_title=None,  
            options=["Home", "Intellichat", "Quick Caption", "Wizard Summarizer", "Reimaginator"],  
            icons=["house-door", "chat-left-dots", "camera-video", "card-text", "input-cursor-text"],  
            menu_icon="cast",  
            default_index=0,  
            orientation="horizontal",
        )
        
if (selected=="Home"):
    st.header("Welcome to Butler.ai!")
    st.write('''
    Are you tired of spending hours searching for answers online? Do you have a lot of content that you need to be summarized or paraphrased? Look no further than Butler.ai!
    ''')
    st.write("Our Q&A prompt uses advanced artificial intelligence to understand your questions and provide accurate and helpful answers.")
    st.write(" Plus, our video transcription service powered by Whisper AI makes it easy to quickly transcribe any video into text.")
    st.write("Need to summarize or paraphrase text? Our text summarization and paraphrasing tools are here to help. Simply provide us with your content and let us do the rest.")
    st.caption("Don't waste any more time trying to find answers or struggling to summarize and paraphrase your content. Let Butler.ai be your personal AI assistant and take care of it all for you. Try us out today!")


if (selected=="Intellichat"):
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
        
       
    



if (selected=="Quick Caption"):
    st.subheader("Do you like reading more and taking notes?")
    st.write("Quick Caption helps you generate the caption/transcript from the video very easily. The transcript generated is concise and clear. The benefits of using the Transcipter are that it saves a lot of time to take out the notes.")
    st.caption("Add your video url below and click on transcript!!!")
    

if (selected=="Wizard Summarizer"):
    st.subheader("Are you Bored?")
    st.write("Are you bored of reading a long text and wanted to cover long text in a short time or wanted to summarize the long text in the best way. Here, Bulter.ai provides you the wand and the wizard summarizer to help you out.")
    st.caption("Add your long text in the box below! and click the apply spell button")

statement=st.text_area("Add your content below!!!")
    button=st.button("Summarize")
    def response1(summ):
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
    if statement and button:
        reply=response1(statement)
        st.write(reply)
    

if (selected=="Reimaginator"):
    st.subheader("Do you want to be more clear while expressing on text?")
    st.write("Reimaginator helps you to convey your thoughts in a clear and concise manner by rephrasing your text. The Reimaginator provides you the new perspective to view the text and helps you to be expressive in a correct way.")
    st.caption("Add your text here to rephrase it, and click Reimagine!!!")
    

