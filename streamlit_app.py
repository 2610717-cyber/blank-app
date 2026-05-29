import streamlit as st

st.title("📁 탭으로 보는 구구단")

# 2단부터 9단까지 탭 생성
tab_titles = [f"{i}단" for i in range(2, 10)]
tabs = st.tabs(tab_titles)

for idx, tab in enumerate(tabs):
    with tab:
        i = idx + 2  # 인덱스 0이 2단이 되도록 설정
        st.write(f"### 🎯 구구단 {i}단을 외자!")
        for j in range(1, 10):
            st.write(f"**{i}** × **{j}** = **{i*j}**")