import streamlit as st

# 앱 제목
st.title("🏁 F1 시대별 대표 차량 갤러리")
st.markdown("각 시대를 대표하는 F1 머신들의 사진과 설명을 확인해보세요!")

# F1 차량 데이터 (사진 포함)
f1_cars = {
    "1950s – Alfa Romeo 158": {
        "team": "Alfa Romeo",
        "driver": "Juan Manuel Fangio",
        "desc": "초창기 F1을 지배한 전설의 머신. 1950년대 첫 챔피언십 우승차.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/33/Alfa_Romeo_158_Alfetta_%281949%29_%2816526443967%29.jpg"
    },
    "1960s – Lotus 49": {
        "team": "Team Lotus",
        "driver": "Jim Clark",
        "desc": "혁신적인 DFV 엔진 장착. 공기역학의 새 장을 연 차량.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Lotus_49_-_Jim_Clark_%281967%29.jpg"
    },
    "1988 – McLaren MP4/4": {
        "team": "McLaren-Honda",
        "driver": "Ayrton Senna, Alain Prost",
        "desc": "F1 역사상 가장 지배적인 머신 중 하나. 16경기 중 15승.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e9/Ayrton_Senna_McLaren_MP4-4_Honda.jpg"
    },
    "2002 – Ferrari F2002": {
        "team": "Scuderia Ferrari",
        "driver": "Michael Schumacher",
        "desc": "슈마허 전성기의 중심. 경량화와 타이어 최적화 기술 탑재.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Ferrari_F2002_front-left_2012_Monza.jpg"
    },
    "2023 – Red Bull RB19": {
        "team": "Red Bull Racing",
        "driver": "Max Verstappen",
        "desc": "현대 F1 기술의 정점. 22경기 중 21승의 압도적 퍼포먼스.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/0e/Max_Verstappen_2023_Austria_FP2.jpg"
    }
}

# 사용자 선택
selection = st.selectbox("시대를 선택하세요:", list(f1_cars.keys()))

# 선택된 데이터
car = f1_cars[selection]

# 출력
st.subheader(selection)
st.markdown(f"**팀**: {car['team']}")
st.markdown(f"**드라이버**: {car['driver']}")
st.markdown(f"**설명**: {car['desc']}")
st.image(car['image'], caption=selection, use_container_width=True)
