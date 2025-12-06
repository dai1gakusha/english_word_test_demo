import streamlit as st
import random
from utils import load_words

st.title("英単語テスト（デモ版）")

# CSV読み込み
df = load_words()

# 初期化
if "current" not in st.session_state:
    st.session_state.current = random.randint(0, len(df)-1)

# 現在の問題
word = df.iloc[st.session_state.current]

st.subheader("日本語の意味を見て英単語を入力してください")

st.write("【意味】", word["meaning"])

user_answer = st.text_input("英単語を入力", "")

# 回答処理
if st.button("回答する"):
    if user_answer.lower().strip() == word["word"].lower().strip():
        st.success("正解！")
    else:
        st.error(f"不正解… 正しくは {word['word']} です。")

    # 次の問題へ
    st.session_state.current = random.randint(0, len(df)-1)
    st.experimental_rerun()