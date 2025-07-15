import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("지역별 에너지 사용량 지도")

@st.cache_data
def load_data():
    df = pd.read_csv("한국에너지공단_에너지사용량 통계_20231231.csv")
    return df

df = load_data()

years = sorted(df["연도"].unique())
selected_year = st.selectbox("연도를 선택하세요", years)
filtered_df = df[df["연도"] == selected_year]

region_coords = {
    '서울특별시': [37.5665, 126.9780],
    '부산광역시': [35.1796, 129.0756],
    '대구광역시': [35.8714, 128.6014],
    '인천광역시': [37.4563, 126.7052],
