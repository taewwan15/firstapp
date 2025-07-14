import streamlit as st

st.set_page_config(page_title="F1 역사 갤러리", layout="centered")

st.title("🏁 F1 시대별 대표 차량 갤러리")
st.write("아래에서 각 시대별 F1 머신의 정보와 실물 사진을 확인하세요.")

# 차량 정보 및 이미지
f1_cars = {
    "1950s – Alfa Romeo 158": {
        "team": "Alfa Romeo",
        "driver": "Juan Manuel Fangio",
        "desc": "F1 초대 시즌 챔피언을 차지한 차량. 1938년 개발, 1950년 완전 지배.",
        "image": "https://cdn.motor1.com/images/mgl/7eXXA/s3/alfa-romeo-158.jpg"
    },
    "1960s – Lotus 49": {
        "team": "Team Lotus",
        "driver": "Jim Clark",
        "desc": "DFV 엔진과 모노코크 섀시로 레이싱 역사를 바꾼 혁신적 머신.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/42/Lotus_49_1967_Jim_Clark_Goodwood.jpg"
    },
    "1988 – McLaren MP4/4": {
        "team": "McLaren-Honda",
        "driver": "Ayrton Senna, Alain Prost",
        "desc": "16경기 중 15승, F1 역사상 가장 압도적인 퍼포먼스를 기록.",
        "image": "https://cdn-5.motorsport.com/images/mgl/0ANMMl6Y/s800/ayrton-senna-mclaren-mp4-4.jpg"
    },
    "2002 – Ferrari F2002": {
        "team": "Scuderia Ferrari",
        "driver": "Michael Schumacher",
        "desc": "미하엘 슈마허의 최강 머신, 페라리의 황금기를 상징.",
        "image": "https://cdn-8.motorsport.com/images/mgl/0a900bb2/s800/f1-spanish-gp-2002-michael-schumacher-ferrari-f2002.jpg"
    },
    "2023 – Red Bull RB19": {
        "team": "Red Bull Racing",
        "driver": "Max Verstappen",
        "desc": "현대 F1 기술의 집약체. 22경기 중 21승이라는 경이적 기록.",
        "image": "https://media.formula1.com/image/upload/f_auto/q_auto/fom-website/2023/Monaco/Saturday/Verstappen%20RB19.jpg"
    }
}

# 선택
selection = st.selectbox("시대를 선택하세요:", list(f1_cars.keys()))
car = f1_cars[selection]

# 출력
st.subheader(selection)
st.markdown(f"**🏢 팀**: {car['team']}")
st.markdown(f"**🧑‍✈️ 드라이버**: {car['driver']}")
st.markdown(f"**📝 설명**: {car['desc']}")
st.image(car['image'], caption=selection, use_container_width=True)
