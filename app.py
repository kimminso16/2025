import streamlit as st

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="🧪 스마트 합금 설계 시뮬레이터 ⚙️",
    page_icon="⚙️",
    layout="centered"
)

st.title("🧪 스마트 합금 설계 시뮬레이터 ⚙️")
st.write("원소 특징을 확인하고, 합금을 만들어 특성을 예측해보세요! ✨")

# -----------------------------
# 원소 특징 데이터
# -----------------------------
elements = {
    "철(Fe)":"💪 강도 높음, 🔥 내열성 있음, ⚖️ 무거움",
    "탄소(C)":"🏗️ 강도를 증가시키는 첨가물, 🔹 경량, ⚡ 경도↑",
    "알루미늄(Al)":"⚖️ 가벼움, 🛡️ 내식성 좋음, ✈️ 항공용",
    "구리(Cu)":"⚡ 전기전도성 우수, 🛡️ 내식성, 🔶 중간 무게",
    "니켈(Ni)":"🛡️ 내식성, 🔥 내열성, 💪 강도 중간"
}

# -----------------------------
# 원소 선택
# -----------------------------
st.subheader("🧬 원소 선택 및 비율 설정")

metal1 = st.selectbox("원소 1 🔹", list(elements.keys()))
ratio1 = st.slider("비율 (%) 🔹", 0, 100, 50)

metal2 = st.selectbox("원소 2 🔸", list(elements.keys()))
ratio2 = st.slider("비율 (%) 🔸", 0, 100, 50)

# -----------------------------
# 원소 특징 출력
# -----------------------------
st.subheader("📝 선택한 원소 특징")
st.write(f"🔹 {metal1}: {elements[metal1]}")
st.write(f"🔸 {metal2}: {elements[metal2]}")

# -----------------------------
# 합금 계산 함수
# -----------------------------
def calc_properties(m1, r1, m2, r2):
    # 기본 점수 (0~1)
    score = {
        "💪 강도":0,
        "🛡️ 내식성":0,
        "⚖️ 가벼움":0
    }

    factor = {
        "철(Fe)":{"strength":0.6,"corrosion":0.2,"weight":0.2},
        "탄소(C)":{"strength":0.3,"corrosion":0.1,"weight":0.3},
        "알루미늄(Al)":{"strength":0.4,"corrosion":0.5,"weight":0.7},
        "구리(Cu)":{"strength":0.3,"corrosion":0.4,"weight":0.3},
        "니켈(Ni)":{"strength":0.5,"corrosion":0.6,"weight":0.3}
    }

    # 비율 반영
    total = r1 + r2
    score["💪 강도"] = (factor[m1]["strength"]*r1 + factor[m2]["strength"]*r2)/total*100
    score["🛡️ 내식성"] = (factor[m1]["corrosion"]*r1 + factor[m2]["corrosion"]*r2)/total*100
    score["⚖️ 가벼움"] = (factor[m1]["weight"]*r1 + factor[m2]["weight"]*r2)/total*100

    return score

# -----------------------------
# 합계 체크 및 결과 출력
# -----------------------------
if ratio1 + ratio2 != 100:
    st.warning("⚠️ 비율 합계가 100%가 되도록 조정해주세요!")
else:
    st.success("✅ 비율 합계 100%")
    scores = calc_properties(metal1, ratio1, metal2, ratio2)

    st.subheader("📊 합금 예측 결과")
    st.write(f"🔹 합금 조합: {metal1} {ratio1}% + {metal2} {ratio2}%")
    st.write(f"💪 강도: {scores['💪 강도']:.1f} / 100")
    st.write(f"🛡️ 내식성: {scores['🛡️ 내식성']:.1f} / 100")
    st.write(f"⚖️ 가벼움: {scores['⚖️ 가벼움']:.1f} / 100")

    # -----------------------------
    # Streamlit 내장 그래프 사용 (pandas 없이)
    # -----------------------------
    st.subheader("📈 특성 그래프")
    st.bar_chart(list(scores.values()), height=300)

    # -----------------------------
    # 추천 팁
    # -----------------------------
    st.subheader("💡 합금 추천 팁")
    if scores["💪 강도"] > 60 and scores["⚖️ 가벼움"] > 50:
        st.write("🚀 경량 고강도 합금 추천!")
    elif scores["🛡️ 내식성"] > 60:
        st.write("🛡️ 내식성 우수 합금 추천!")
    else:
        st.write("🔹 일반 합금, 실험을 통해 최적 조합을 찾아보세요.")
