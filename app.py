import streamlit as st
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(
    page_title="🧪 스마트 합금 설계 시뮬레이터 ⚙️",
    page_icon="⚙️",
    layout="centered"
)

st.title("🧪 스마트 합금 설계 시뮬레이터 ⚙️")
st.write("원하는 성질을 선택하면 합금 특성을 시각적으로 예측해드립니다! ✨")

# 합금 원소 선택
st.subheader("🧬 합금 원소 선택")
metal_options = ["철(Fe)", "탄소(C)", "알루미늄(Al)", "구리(Cu)", "니켈(Ni)"]

metal1 = st.selectbox("원소 1 🔹", metal_options)
ratio1 = st.slider("비율 (%) 🔹", 0, 100, 50)

metal2 = st.selectbox("원소 2 🔸", metal_options)
ratio2 = st.slider("비율 (%) 🔸", 0, 100, 50)

# 합계 체크
if ratio1 + ratio2 != 100:
    st.warning("⚠️ 비율 합계가 100%가 되도록 조정해주세요!")
else:
    st.success("✅ 비율 합계 100%")

    # 합금 특성 계산 (간단 예시)
    def calc_properties(m1, r1, m2, r2):
        # 기본 값
        strength = 0
        corrosion = 0
        weight = 0

        # 강도
        if "철" in [m1, m2]:
            strength += 0.6
        if "탄소" in [m1, m2]:
            strength += 0.3
        if "알루미늄" in [m1, m2]:
            strength += 0.4
        if "니켈" in [m1, m2]:
            strength += 0.5
        if "구리" in [m1, m2]:
            strength += 0.3

        # 내식성
        if "니켈" in [m1, m2]:
            corrosion += 0.6
        if "구리" in [m1, m2]:
            corrosion += 0.4
        if "알루미늄" in [m1, m2]:
            corrosion += 0.5
        if "철" in [m1, m2]:
            corrosion += 0.2
        if "탄소" in [m1, m2]:
            corrosion += 0.1

        # 가벼움
        if "알루미늄" in [m1, m2]:
            weight += 0.7
        if "탄소" in [m1, m2]:
            weight += 0.3
        if "철" in [m1, m2]:
            weight += 0.2
        if "니켈" in [m1, m2]:
            weight += 0.3
        if "구리" in [m1, m2]:
            weight += 0.3

        # 비율 반영
        total = r1 + r2
        s = (strength * r1 + strength * r2) / total * 100
        c = (corrosion * r1 + corrosion * r2) / total * 100
        w = (weight * r1 + weight * r2) / total * 100
        return s, c, w

    strength, corrosion, weight = calc_properties(metal1, ratio1, metal2, ratio2)

    # 결과 표시
    st.subheader("📊 합금 예측 특성")
    st.write(f"🔹 합금 조합: {metal1} {ratio1}% + {metal2} {ratio2}%")
    st.write(f"💪 강도: {strength:.1f} / 100")
    st.write(f"🛡️ 내식성: {corrosion:.1f} / 100")
    st.write(f"⚖️ 가벼움: {weight:.1f} / 100")

    # 그래프 표시
    fig, ax = plt.subplots()
    ax.bar(["강도 💪", "내식성 🛡️", "가벼움 ⚖️"], [strength, corrosion, weight], color=["#ff6b6b","#22c55e","#ffd166"])
    ax.set_ylim(0, 100)
    ax.set_ylabel("수치 (0~100)")
    st.pyplot(fig)

st.markdown("---")
st.write("💡 팁: 원소와 비율을 바꾸어 다양한 합금 특성을 실험해보세요!")
