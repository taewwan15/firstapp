import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# --------- 앱 제목 ---------
st.title("대한민국 지역별 에너지 사용량 시각화")

# --------- 데이터 불러오기 ---------
@st.cache_data
def load_data():
    df = pd.read_csv("에너지사용량_지역별.csv")  # CSV로 변환한 파일
    return df

df = load_data()

# --------- 사용자 입력 (연도 선택) ---------
years = df['연도'].unique()
selected_year = st.selectbox("연도를 선택하세요", sorted(years))

# --------- 선택한 연도의 데이터 필터링 ---------
filtered_df = df[df['연도'] == selected_year]

# --------- 지역 중심 좌표 정의 (간략한 예시) ---------
region_coords = {
    '서울특별시': [37.5665, 126.9780],
    '부산광역시': [35.1796, 129.0756],
    '대구광역시': [35.8714, 128.6014],
    '인천광역시': [37.4563, 126.7052],
    '광주광역시': [35.1595, 126.8526],
    '대전광역시': [36.3504, 127.3845],
    '울산광역시': [35.5384, 129.3114],
    '세종특별자치시': [36.4800, 127.2891],
    '경기도': [37.4138, 127.5183],
    '강원도': [37.8228, 128.1555],
    '충청북도': [36.6357, 127.4917],
    '충청남도': [36.5184, 126.8000],
    '전라북도': [35.7175, 127.1530],
    '전라남도': [34.8161, 126.4630],
    '경상북도': [36.4919, 128.8889],
    '경상남도': [35.4606, 128.2132],
    '제주특별자치도': [33.4996, 126.5312],
}

# --------- Folium 지도 생성 ---------
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

for _, row in filtered_df.iterrows():
    region = row['지역']
    energy = row['에너지사용량 (TJ)']
    if region in region_coords:
        lat, lon = region_coords[region]
        folium.CircleMarker(
            location=[lat, lon],
            radius=energy / 100000,  # 원 크기 조절
            popup=f"{region}\n에너지 사용량: {energy:,.0f} TJ",
            color="blue",
            fill=True,
            fill_opacity=0.6
        ).add_to(m)

# --------- 지도 출력 ---------
st.subheader(f"{selected_year}년 지역별 에너지 사용량")
st_folium(m, width=700, height=500)
