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
st.write("원소 특징과 합금 조합, 실제 활용 분야까지 확인해보세요! ✨")

# -----------------------------
# 원소 특징 데이터
# -----------------------------
elements = {
    "철(Fe)": "💪 강도 높음(외부 힘에 강함), 🔥 내열성 있음(고온에서도 안정), ⚖️ 무거움",
    "탄소(C)": "🏗️ 강도를 증가시키는 첨가물(강철 강화), 🔹 경량, ⚡ 경도↑(단단함)",
    "알루미늄(Al)": "⚖️ 가벼움, 🛡️ 내식성 좋음(부식에 강함), ✈️ 항공용",
    "구리(Cu)": "⚡ 전기전도성 우수, 🛡️ 내식성(부식 방지), 🔶 중간 무게",
    "니켈(Ni)": "🛡️ 내식성(부식 방지), 🔥 내열성(고온 안정), 💪 강도 중간"
}

# -----------------------------
# 🔍 원소 탐구 (특징 출력 기능)
# -----------------------------
st.subheader("🔍 원소 탐구")
selected_element = st.selectbox("특징을 알고 싶은 원소를 선택하세요:", list(elements.keys()))
st.write(f"✨ {selected_element} 의 특징: {elements[selected_element]}")

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
    score = {
        "💪 강도": 0,
        "🛡️ 내식성": 0,
        "⚖️ 가벼움": 0
    }
    factor = {
        "철(Fe)": {"strength": 0.6, "corrosion": 0.2, "weight": 0.2},
        "탄소(C)": {"strength": 0.3, "corrosion": 0.1, "weight": 0.3},
        "알루미늄(Al)": {"strength": 0.4, "corrosion": 0.5, "weight": 0.7},
        "구리(Cu)": {"strength": 0.3, "corrosion": 0.4, "weight": 0.3},
        "니켈(Ni)": {"strength": 0.5, "corrosion": 0.6, "weight": 0.3}
    }
    total = r1 + r2
    score["💪 강도"] = (factor[m1]["strength"]*r1 + factor[m2]["strength"]*r2)/total*100
    score["🛡️ 내식성"] = (factor[m1]["corrosion"]*r1 + factor[m2]["corrosion"]*r2)/total*100
    score["⚖️ 가벼움"] = (factor[m1]["weight"]*r1 + factor[m2]["weight"]*r2)/total*100
    return score

# -----------------------------
# 실제 합금과 활용 분야
# -----------------------------
alloy_info = {
    ("철(Fe)", "탄소(C)"): ("강철", "🏗️ 건축 구조재, 🔩 기계부품"),
    ("알루미늄(Al)", "구리(Cu)"): ("알루미늄-구리 합금", "✈️ 항공, 🚗 자동차 부품"),
    ("철(Fe)", "니켈(Ni)"): ("스테인리스강", "🏗️ 건축, 🍴 주방용품"),
    ("알루미늄(Al)", "니켈(Ni)"): ("알루미늄-니켈 합금", "🚀 항공, ⚙️ 기계 부품"),
    ("구리(Cu)", "니켈(Ni)"): ("브라스(황동)", "💡 전기, 장신구, 배관")
}

def get_alloy_info(m1, m2):
    key = (m1, m2)
    key_rev = (m2, m1)
    if key in alloy_info:
        return alloy_info[key]
    elif key_rev in alloy_info:
        return alloy_info[key_rev]
    else:
        return ("사용자 정의 합금", "🔬 실험적 합금, 다양한 산업 분야에서 연구중")

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
    # 📈 그래프 (x축 이름 + y축 값)
    # -----------------------------
    st.subheader("📈 특성 그래프")
    chart_data = {
        "특성": list(scores.keys()),
        "값": list(scores.values())
    }
    st.bar_chart(data=chart_data, x="특성", y="값", height=300)

    # -----------------------------
    # 실제 합금 이름과 활용 분야
    # -----------------------------
    st.subheader("🏭 실제 합금 및 활용 분야")
    alloy_name, application = get_alloy_info(metal1, metal2)
    st.write(f"🔹 합금 이름: **{alloy_name}**")
    st.write(f"🔹 활용 분야: {application}")
