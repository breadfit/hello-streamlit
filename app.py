import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hello Streamlit", page_icon="🔋")
st.title("세방전지 AX 과정 첫 Streamlit 배포 🚀")

name = st.text_input("이름을 입력하세요")
if name:
    st.success(f"{name}님, 환영합니다!")

df = pd.DataFrame({
    "월": ["1월", "2월", "3월", "4월"],
    "생산량": [120, 135, 150, 142],
})
st.subheader("월별 생산량 (샘플)")
st.bar_chart(df, x="월", y="생산량")
st.dataframe(df)
