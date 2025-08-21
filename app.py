import streamlit as st

# 🎨 페이지 설정
st.set_page_config(page_title="🔬 원소 & 합금 백과사전", page_icon="⚗️", layout="wide")

st.title("⚛️ 원소 특징 + 합금 활용 백과사전")
st.write("원소들의 특성과 합금의 실제 활용 분야를 살펴보세요! 🧪")

# 🧑‍🔬 원소 데이터 (기본 특징 + 활용)
elements = {
    "철 (Fe)": {"특징": "단단하고 강도 높음 🏋️", "분야": "건축, 자동차 🚗, 철근"},
    "구리 (Cu)": {"특징": "전도성이 매우 우수 ⚡", "분야": "전선, 반도체, 동전 💰"},
    "알루미늄 (Al)": {"특징": "가볍고 내식성 우수 ✈️", "분야": "비행기, 포장재, 캔 🥫"},
    "니켈 (Ni)": {"특징": "부식에 강하고 은백색 🌟", "분야": "스테인리스강, 배터리 🔋"},
    "아연 (Zn)": {"특징": "부식 방지 효과 🛡️", "분야": "도금, 건축 자재 🏠"},
    "티타늄 (Ti)": {"특징": "가볍고 강하며 인체 친화 👩‍⚕️", "분야": "인공관절, 항공우주 🚀"},
}

# ⚒️ 합금 데이터 (조합 + 실제 분야)
alloys = {
    ("철 (Fe)", "탄소 (C)"): "🔩 강철 → 건축, 교량, 자동차 🚗",
    ("구리 (Cu)", "아연 (Zn)"): "🟡 황동 → 악기, 장식품 🎺",
    ("구리 (Cu)", "주석 (Sn)"): "🟤 청동 → 조각상, 기념비 🗿",
    ("알루미늄 (Al)", "구리 (Cu)"): "✈️ 두랄루민 → 항공기, 군수품 🛩️",
    ("철 (Fe)", "니켈 (Ni)"): "🌟 스테인리스강 → 조리도구, 건축 자재 🍴",
    ("티타늄 (Ti)", "알루미늄 (Al)"): "🚀 초경량 합금 → 항공우주, 의료기기 🏥",
}

# 🔍 원소 선택
st.header("🔍 원소 탐구")
selected_element = st.selectbox("특징을 알고 싶은 원소를 선택하세요:", list(elements.keys()))

st.subheader(f"✨ {selected_element} 의 특징")
st.write(f"**특징:** {elements[selected_element]['특징']}")
st.write(f"**활용 분야:** {elements[selected_element]['분야']}")

# 📊 합금 선택
st.header("⚒️ 합금 탐구")
col1, col2 = st.columns(2)
with col1:
    element1 = st.selectbox("첫 번째 원소 선택:", list(elements.keys()))
with col2:
    element2 = st.selectbox("두 번째 원소 선택:", list(elements.keys()))

st.subheader("🔗 합금 결과")
if (element1, element2) in alloys:
    st.success(alloys[(element1, element2)])
elif (element2, element1) in alloys:
    st.success(alloys[(element2, element1)])
else:
    st.warning("❌ 이 조합은 특별한 합금으로 잘 알려져 있지 않아요!")

# 📊 Streamlit 내장 차트 (오류 절대 없음)
st.header("📊 원소 활용도 비교")
usage_data = {
    "철 (Fe)": 90,
    "구리 (Cu)": 70,
    "알루미늄 (Al)": 85,
    "니켈 (Ni)": 60,
    "아연 (Zn)": 50,
    "티타늄 (Ti)": 40,
}
st.bar_chart(usage_data)

# 🖼️ 사진 추가 (외부 이미지 URL 사용)
st.header("🖼️ 합금 이미지 예시")
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Brass_instruments.jpg/320px-Brass_instruments.jpg",
         caption="황동 (Brass) 악기 🎺", use_column_width=True)
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Bronze_statue.jpg/320px-Bronze_statue.jpg",
         caption="청동 (Bronze) 조각상 🗿", use_column_width=True)
