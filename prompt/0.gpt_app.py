# Streamlit: UI를 파이썬으로 쉽게 만들 수 있게 도와주는 도구
# OpenAI : OpenAI API 도구
# pip install streamlit openai

import streamlit as st
import openai

openai.api_key = st.secrets["api_key"] # .streamlit.toml -> secrets.toml 파일 안에 개인 OpenAI API 키를 저장해 두어야 함

st.title("ChatGPT Plus DALL-E")

with st.form("form"):
    # 텍스트 인풋
    user_input = st.text_input("Prompt")
    submit = st.form_submit_button("Submit")

if submit and user_input:  # 사용자가 submit을 누르거나 적었을 때
    # st.write(user_input) # -> 단순 인풋 테스트 출력만 해볼 경우

    # 여기서부터 GPT 모델
    gpt_prompt = [{"role":"system",
                   "content":"Imagine the detail appearence of the input. Response it shortly around 20 words"
                   }]

    gpt_prompt.append({"role":"user",
                        "content":user_input
                        })
    
    with st.spinner("Waiting for ChatGPT..."):
        gpt_response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt
            )
    
    prompt = gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)