import streamlit as st

st.title("Hello Streamlit 👋")

name = st.text_input("이름을 입력하세요")

if st.button("확인"):
    st.write(f"{name}님 반갑습니다!")
