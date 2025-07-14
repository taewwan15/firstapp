import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 타이틀
st.title("🏁 F1 팀별 역대 우승 횟수")
st.markdown("F1 역사 속 주요 팀들의 **총 그랑프리 우승 횟수**를 시각화합니다.")

# 우승 횟수 데이터 (2024 시즌 말 기준)
data = {
    "Ferrari": 244,
    "McLaren": 183,
    "Mercedes": 125,
    "Red Bull Racing": 118,
    "Williams": 114,
    "Lotus": 79,
    "Renault": 35,
    "Brabham": 35,
    "Alpine": 1,
    "AlphaTauri": 1,
}

# 데이터프레임 생성
df = pd.DataFrame(list(data.items()), columns=["Team", "Wins"]).sort_values(by="Wins", ascending=False)

# 막대 그래프 그리기
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(df["Team"], df["Wins"], color="crimson")
ax.set_ylabel("🏆 우승 횟수")
ax.set_xlabel("F1 팀")
ax.set_title("F1 팀별 역대 우승 횟수 (1950~2024)")
ax.set_xticklabels(df["Team"], rotation=45, ha='right')

# 막대 위에 숫자 표시
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 1, int(yval), ha='center', va='bottom')

st.pyplot(fig)
