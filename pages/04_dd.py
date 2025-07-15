import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")
st.title("📊 지역별 에너지 사용량 지도")

@st.cache_data
def load_data():
    df = pd.read_csv("한국에너지공단_에너지사용량 통계_20231231.csv")
    return df

df = load_data()

# 확인용
if "연도" not in df.columns or "지역" not in df.columns or "에너지사용량" not in df.columns:
    st.error("❌ CSV 파일에 '연도', '지역', '에너지사용량' 열이 없습니다.")
    st.write("열 이름 목록:", df.columns.tolist())
    st.stop()

years = sorted(df["연도"].unique())
selected_year = st.selectbox("연도를 선택하세요", years)
filtered_df = df[df["연도"] == selected_year]

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

m = folium.Map(location=[36.5, 127.8], zoom_start=7)

for _, row in filtered_df.iterrows():
    region = row["지역"]
    usage = row["에너지사용량"]
    if region in region_coords:
        folium.CircleMarker(
            location=region_coords[region],
            radius=max(5, usage / 100000),  # 최소 반지름
            color='blue',
            fill=True,
            fill_opacity=0.6,
            popup=f"{region}: {usage:,.0f} TJ"
        ).add_to(m)

st_folium(m, width=800, height=550)
