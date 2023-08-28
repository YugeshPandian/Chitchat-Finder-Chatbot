import streamlit as st
import openai
import os
# Set your OpenAI API key


def main1():
    openai.api_key = "YOUR API KEY"
   
    # Streamlit app code
    st.header("ChitChat Finder")

    user_input = st.text_input("Type Here")

    if st.button('Search'):
        completion = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo",
                            messages=[
                    {"role": "system", "content": "Simply answer 'Yes its chitchat' if the given sentence  contains chitchat and if not means 'No Its not chitchat'"},
                    {"role": "user", "content": user_input}
                            ]
                            )
        res = completion.choices[0].message
        st.chat_message("assistant").markdown(res["content"])
        #st.text( res["content"])

if __name__=='__main__':
    main1()
