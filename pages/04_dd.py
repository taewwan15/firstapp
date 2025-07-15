import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 페이지 설정
st.set_page_config(page_title="지역별 에너지 사용량", layout="wide")
st.title("📊 지역별 에너지 사용량 지도 (한국에너지공단 통계 기반)")

# CSV 파일 로딩 함수
@st.cache_data
def load_data():
    df = pd.read_csv("한국에너지공단_에너지사용량 통계_20231231.csv", encoding="cp949")
    return df

# 데이터 불러오기
df = load_data()

# CSV 열 이름 검증
expected_columns = ["지역", "연도", "에너지사용량"]
if not all(col in df.columns for col in expected_columns):
    st.error(f"❌ CSV 파일에 필요한 열({expected_columns})이 없습니다.")
    st.stop()

# 연도 선택
years = sorted(df["연도"].unique())
selected_year = st.selectbox("🔎 연도를 선택하세요:", years)

# 선택한 연도 기준 필터링
filtered_df = df[df["연도"] == selected_year]

# 지역 좌표 (위경도) 사전
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

# 지도 생성
m = folium.Map(location=[36.5, 127.8], zoom_start=7)

# 지역별 마커 추가
for _, row in filtered_df.iterrows():
    region = row["지역"]
    usage = row["에너지사용량"]
    if region in region_coords:
        folium.CircleMarker(
            location=region_coords[region],
            radius=max(5, usage / 100000),  # 최소 반지름 5
            color='blue',
            fill=True,
            fill_opacity=0.6,
            popup=f"{region}: {usage:,.0f} TJ"
        ).add_to(m)

# 지도 출력
st_folium(m, width=800, height=550)

# 표 출력
with st.expander("📋 데이터 표 보기"):
    st.dataframe(filtered_df)
