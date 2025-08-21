import streamlit as st
import sys
import subprocess

# 🔧 필요한 라이브러리 자동 설치
def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = __import__(package)

install_and_import("pandas")
install_and_import("matplotlib")

import pandas as pd
import matplotlib.pyplot as plt

# 🎉 제목
st.title("🧪 스마트 합금 설계 & 활용 분야 시뮬레이터 ⚙️")

# 🧑‍🔬 원소 데이터
elements = {
    "Fe": {"특징": "강철의 주성분, 높은 강도 💪", "활용": "건축 자재 🏗️, 자동차 🚗"},
    "Cu": {"특징": "우수한 전기 전도성 ⚡", "활용": "전선 🔌, 전자기기 📱"},
    "Al": {"특징": "가볍고 내식성 🪶", "활용": "항공기 ✈️, 캔 🥫"},
    "Ni": {"특징": "내열·내식성 🔥", "활용": "터빈 엔진 ✈️, 화학 장비 ⚗️"},
    "Ti": {"특징": "강도 높고 가벼움 🏋️", "활용": "의료용 임플란트 🦾, 항공 우주 🚀"},
    "Zn": {"특징": "부식 방지 🛡️", "활용": "도금 철강 🏭"},
    "Mg": {"특징": "초경량 합금 🚴", "활용": "자전거 🚲, 전자제품 💻"}
}

# 🌟 선택 UI
st.header("⚙️ 합금 원소 선택")
col1, col2 = st.columns(2)
with col1:
    elem1 = st.selectbox("첫 번째 원소 선택", list(elements.keys()))
with col2:
    elem2 = st.selectbox("두 번째 원소 선택", list(elements.keys()))

if elem1 and elem2 and elem1 != elem2:
    st.subheader(f"🔬 선택한 합금: **{elem1}-{elem2} 합금**")

    # 특징 및 활용 설명
    st.write(f"**{elem1} 특징:** {elements[elem1]['특징']}")
    st.write(f"**{elem2} 특징:** {elements[elem2]['특징']}")

    st.success(f"✅ 이 합금은 주로 **{elements[elem1]['활용']}** 및 **{elements[elem2]['활용']}** 분야에서 응용됩니다!")

    # 📊 데이터프레임 생성
    data = pd.DataFrame({
        "원소": [elem1, elem2],
        "특징": [elements[elem1]["특징"], elements[elem2]["특징"]],
        "활용 분야": [elements[elem1]["활용"], elements[elem2]["활용"]],
        "가상 강도": [len(elements[elem1]["특징"]) * 10, len(elements[elem2]["특징"]) * 10],
        "내식성": [len(elements[elem1]["활용"]) * 5, len(elements[elem2]["활용"]) * 5]
    })

    st.dataframe(data)

    # 📈 그래프 시각화
    st.subheader("📊 합금 성질 시각화")
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(data["가상 강도"], data["내식성"], s=300, c="orange", alpha=0.7, edgecolors="black")

    for i, txt in enumerate(data["원소"]):
        ax.annotate(txt, (data["가상 강도"][i] + 2, data["내식성"][i] + 2))

    ax.set_xlabel("가상 강도 💪")
    ax.set_ylabel("내식성 🛡️")
    ax.set_title(f"{elem1}-{elem2} 합금 성질 그래프")
    st.pyplot(fig)
else:
    st.warning("⚠️ 서로 다른 두 원소를 선택해주세요!")
