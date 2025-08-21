import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 🌟 웹앱 제목
st.title("🧪 스마트 합금 설계 시뮬레이터 ⚙️")
st.write("원소를 선택해 합금을 설계하고, 그 특성과 활용 분야를 확인해보세요! 🚀")

# 🧩 원소 데이터베이스
elements = {
    "Fe (철)": {
        "특징": "강도와 내구성이 뛰어남 💪",
        "활용": "건축물, 자동차, 선박 🏗️🚗🚢"
    },
    "Cu (구리)": {
        "특징": "전기전도성이 우수 ⚡",
        "활용": "전선, 반도체, 배터리 🔌💻🔋"
    },
    "Al (알루미늄)": {
        "특징": "가볍고 내식성이 좋음 🪶",
        "활용": "비행기, 음료 캔, 전자제품 ✈️🥫📱"
    },
    "Ni (니켈)": {
        "특징": "부식에 강하고 경도가 높음 🛡️",
        "활용": "스테인리스강, 화학 장비 🔧⚗️"
    },
    "Ti (티타늄)": {
        "특징": "가볍고 강철만큼 강함 🚀",
        "활용": "항공우주, 인공관절, 군수품 🛰️🦾"
    }
}

# 🎛️ 사용자 입력
st.sidebar.header("⚙️ 합금 원소 선택")
selected_elements = st.sidebar.multiselect("합금을 만들 원소를 선택하세요:", list(elements.keys()))

# 📊 합금 설계 결과
if len(selected_elements) >= 2:
    st.subheader("🔬 선택한 합금 정보")
    for elem in selected_elements:
        st.write(f"### {elem}")
        st.write(f"- **특징**: {elements[elem]['특징']}")
        st.write(f"- **활용 분야**: {elements[elem]['활용']}")

    # 📈 그래프로 합금 특성 표현
    st.subheader("📊 합금 특성 시각화")

    # 랜덤 특성 값 (예시: 강도, 전도성)
    np.random.seed(42)
    properties = {
        "강도 💪": np.random.randint(50, 100),
        "전도성 ⚡": np.random.randint(30, 90),
        "내식성 🛡️": np.random.randint(40, 95),
        "경량성 🪶": np.random.randint(20, 80),
    }

    categories = list(properties.keys())
    values = list(properties.values())

    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(categories, values, color=["steelblue", "orange", "green", "purple"])
    ax.set_xlabel("특성", fontsize=12)
    ax.set_ylabel("수치 (0~100)", fontsize=12)
    ax.set_title("합금 특성 분석 결과", fontsize=14)
    st.pyplot(fig)

    # 📷 합금 관련 이미지 추가
    st.subheader("🖼️ 참고 이미지")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6f/Aluminium-alloy.jpg", caption="알루미늄 합금 예시", use_container_width=True)

else:
    st.warning("⚠️ 최소 2개 이상의 원소를 선택해야 합금을 설계할 수 있습니다!")
