import streamlit as st
import matplotlib.pyplot as plt

# ==============================
# 페이지 설정
# ==============================
st.set_page_config(
    page_title="🧪 스마트 합금 설계 시뮬레이터 ⚙️",
    page_icon="⚙️",
    layout="centered"
)

st.title("🧪 스마트 합금 설계 시뮬레이터 ⚙️")
st.write("원하는 원소와 비율을 선택하면 합금 특성을 예측해드립니다! ✨")

# ==============================
# 원소 특징 데이터
# ==============================
elements = {
    "철(Fe)": {"강도": 80, "내식성": 20, "가벼움": 10, "설명": "🏗️ 강도가 높고 다양한 합금의 기본 재료"},
    "탄소(C)": {"강도": 50, "내식성": 10, "가벼움": 20, "설명": "⚡ 경화 및 강도 조절에 필수, 주로 강철에 사용"},
    "알루미늄(Al)": {"강도": 40, "내식성": 50, "가벼움": 90, "설명": "✈️ 가볍고 내식성 뛰어남, 항공기·자동차에 활용"},
    "구리(Cu)": {"강도": 30, "내식성": 60, "가벼움": 40, "설명": "💡 전기전도성이 좋고 내식성 있음"},
    "니켈(Ni)": {"강도": 50, "내식성": 80, "가벼움": 30, "설명": "🔥 내열성·내식성 우수, 스테인리스강에 사용"}
}

# ==============================
# 원소 선택
# ==============================
st.subheader("🧬 합금 원소 선택")
metal1 = st.selectbox("원소 1 🔹", list(elements.keys()))
ratio1 = st.slider("비율 (%) 🔹", 0, 100, 50)

metal2 = st.selectbox("원소 2 🔸", list(elements.keys()))
ratio2 = st.slider("비율 (%) 🔸", 0, 100, 50)

# ==============================
# 특징 표시
# ==============================
st.subheader("🔎 선택한 원소 특징")
st.write(f"{metal1}: {elements[metal1]['설명']}")
st.write(f"{metal2}: {elements[metal2]['설명']}")

# ==============================
# 합금 계산
# ==============================
if ratio1 + ratio2 != 100:
    st.warning("⚠️ 비율 합계가 100%가 되도록 조정해주세요!")
else:
    st.success("✅ 비율 합계 100%")

    # 강도, 내식성, 가벼움 계산
    strength = (elements[metal1]["강도"] * ratio1 + elements[metal2]["강도"] * ratio2) / 100
    corrosion = (elements[metal1]["내식성"] * ratio1 + elements[metal2]["내식성"] * ratio2) / 100
    weight = (elements[metal1]["가벼움"] * ratio1 + elements[metal2]["가벼움"] * ratio2) / 100

    # ==============================
    # 결과 표시
    # ==============================
    st.subheader("📊 합금 예측 특성")
    st.write(f"🔹 합금 조합: {metal1} {ratio1}% + {metal2} {ratio2}%")
    st.write(f"💪 강도: {strength:.1f} / 100")
    st.write(f"🛡️ 내식성: {corrosion:.1f} / 100")
    st.write(f"⚖️ 가벼움: {weight:.1f} / 100")

    # ==============================
    # 합금 추천 메시지
    # ==============================
    st.subheader("💡 합금 추천 메시지")
    if strength > 70 and corrosion > 50:
        st.success("🔥 강력하고 내식성 좋은 합금! 스테인리스강 느낌")
    elif weight > 70 and corrosion > 40:
        st.success("✈️ 가볍고 내식성 좋은 합금! 항공기용 알루미늄 합금")
    elif strength > 60:
        st.success("🏗️ 강도가 높아 구조용 합금에 적합")
    else:
        st.info("🧩 특성이 복합적이므로 실험 및 추가 연구 필요")

    # ==============================
    # 그래프 시각화
    # ==============================
    fig, ax = plt.subplots()
    properties = [strength, corrosion, weight]
    labels = ["💪 강도", "🛡️ 내식성", "⚖️ 가벼움"]
    colors = ["#ff6b6b", "#22c55e", "#ffd166"]
    ax.bar(labels, properties, color=colors)
    ax.set_ylim(0, 100)
    ax.set_ylabel("수치 (0~100)")
    st.pyplot(fig)

st.markdown("---")
st.write("🔧 팁: 원소와 비율을 바꾸어 다양한 합금을 실험해보세요! 🧪")
    
