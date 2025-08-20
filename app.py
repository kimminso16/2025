import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="🧪 스마트 합금 설계 시뮬레이터 ⚙️",
    page_icon="⚙️",
    layout="centered"
)

# 제목
st.title("🧪 스마트 합금 설계 시뮬레이터 ⚙️")
st.write("원하는 성질을 선택하면 적합한 합금을 추천해드립니다! ✨")

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

    # 합금 예측 로직 (간단 예시)
    st.subheader("📊 예측 결과")
    if ("철" in metal1 and "탄소" in metal2) or ("탄소" in metal1 and "철" in metal2):
        if ratio2 <= 2:
            st.write("⚙️ 합금 유형: 강철 (높은 강도와 연성)")
        else:
            st.write("🏗️ 합금 유형: 주철 (높은 경도, 취약함)")
    elif ("알루미늄" in metal1 and "구리" in metal2) or ("구리" in metal1 and "알루미늄" in metal2):
        st.write("✈️ 알루미늄 합금 (가볍고 강도 ↑, 항공기 재료)")
    elif ("니켈" in metal1 and "철" in metal2) or ("철" in metal1 and "니켈" in metal2):
        st.write("🔥 니켈강 (내식성 ↑, 내열성 ↑, 산업용)")
    else:
        st.write("🧩 특성이 복합적으로 변함 (실험 필요)")

# 추가 팁
st.markdown("---")
st.write("💡 팁: 합금 설계 시 원소 비율과 특성을 조절하며 다양한 결과를 실험해보세요!")
