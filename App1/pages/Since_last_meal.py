import streamlit as st
from datetime import datetime, timedelta
import tkinter as tk
from datetime import datetime, timedelta

st.title("経過時間計算アプリ")

# ユーザーが日付と時間を入力
# Date input
# selected_date = st.date_input("Select a date", datetime.now().date())
yesterday = datetime.now() - timedelta(days=1)

# Time input
selected_time = st.time_input("Select a time")

# 現在の日時を取得
now = datetime.now()

selected_datetime = datetime.combine(yesterday.date(), selected_time)

# 経過時間を計算
elapsed_time = now - selected_datetime
time_after_16_hours = elapsed_time + timedelta(hours=16)

days = elapsed_time.days
hours, remainder = divmod(elapsed_time.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

tdays = time_after_16_hours.days
thours, treminder = divmod(time_after_16_hours.seconds, 3600)
tminutes, tseconds = divmod(treminder, 60)


st.subheader("経過時間")
st.write(f"{days}日 {hours}時間 {minutes}分 {seconds}秒")

st.subheader("残り時間")
st.write(f"{tdays}日 {thours}時間 {tminutes}分 {tseconds}秒")


