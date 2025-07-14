import streamlit as st

# 앱 타이틀
st.title("🏎️ F1 역사 속 전설적인 차량들")
st.write("F1의 각 시대를 대표한 차량과 드라이버를 소개합니다!")

# 시대별 데이터 정의
f1_data = {
    "1950s": {
        "car": "Alfa Romeo 158",
        "team": "Alfa Romeo",
        "driver": "Juan Manuel Fangio",
        "desc": "F1 첫 챔피언십 우승 차량. 1938년 설계, 1950년 압도적인 우승.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/33/Alfa_Romeo_158_Alfetta_%281949%29_%2816526443967%29.jpg"
    },
    "1960s": {
        "car": "Lotus 49",
        "team": "Team Lotus",
        "driver": "Jim Clark",
        "desc": "DFV 엔진 첫 탑재, 공기역학 혁신의 상징.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Lotus_49_-_Jim_Clark_%281967%29.jpg"
    },
    "1988": {
        "car": "McLaren MP4/4",
        "team": "McLaren-Honda",
        "driver": "Ayrton Senna & Alain Prost",
        "desc": "16경기 중 15승, F1 역사상 가장 지배적인 머신 중 하나.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e9/Ayrton_Senna_McLaren_MP4-4_Honda.jpg"
    },
    "2002": {
        "car": "Ferrari F2002",
        "team": "Scuderia Ferrari",
        "driver": "Michael Schumacher",
        "desc": "슈마허를 위한 경량화, 브리지스톤 타이어 최적화.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/f/f0/Ferrari_F2002_front-left_2012_Monza.jpg"
    },
    "2023": {
        "car": "Red Bull RB19",
        "team": "Red Bull Racing",
        "driver": "Max Verstappen",
        "desc": "22경기 중 21승, 현대 F1 기술의 정점.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/0e/Max_Verstappen_2023_Austria_FP2.jpg"
    }
}

# 사이드바에서 시대 선택
era = st.sidebar.selectbox("시대를 선택하세요:", list(f1_data.keys()))

# 선택된 시대의 정보 불러오기
data = f1_data[era]

# 메인 정보 표시
st.subheader(f"{era} - {data['car']}")
st.markdown(f"**팀**: {data['team']}")
st.markdown(f"**드라이버**: {data['driver']}")
st.markdown(f"**설명**: {data['desc']}")

# 이미지 출력 (최신 방식)
st.image(data['image'], caption=data['car'], use_container_width=True)
