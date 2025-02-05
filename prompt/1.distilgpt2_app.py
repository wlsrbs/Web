import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 모델과 토크나이저 로드
model_name = "distilgpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

st.title("DistilGPT2 - Free Chatbot")

with st.form("form"):
    # 텍스트 인풋
    user_input = st.text_input("Prompt")
    submit = st.form_submit_button("Submit")

if submit and user_input:  # 사용자가 submit을 누르거나 적었을 때
    with st.spinner("Waiting for Chatbot..."):
        # 텍스트 인코딩
        inputs = tokenizer.encode(user_input, return_tensors="pt")

        # 모델을 사용하여 텍스트 생성
        with torch.no_grad():
            outputs = model.generate(inputs, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)

        # 결과 디코딩
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    st.write(response)
