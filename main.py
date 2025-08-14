import streamlit as st

# 🎯 페이지 기본 설정
st.set_page_config(
    page_title="🌈 MBTI 직업 추천 💼",
    page_icon="💡",
    layout="centered"
)

# 💖 MBTI별 직업 추천 데이터
mbti_jobs = {
    "INTJ": ["🧠 데이터 분석가", "📊 전략 컨설턴트", "🔬 연구원"],
    "ENTP": ["📈 마케팅 기획자", "🚀 창업가", "🎯 광고 기획자"],
    "INFJ": ["💬 심리상담가", "✍️ 작가", "🎓 교육 전문가"],
    "ESFP": ["🎭 배우", "🎉 이벤트 플래너", "🌍 여행 가이드"],
    "ISTJ": ["📚 회계사", "🏦 은행원", "⚖️ 법률가"],
    "ENFP": ["🎨 디자이너", "📢 홍보 전문가", "🎤 MC"],
    "ISFJ": ["💝 간호사", "🍳 요리사", "🏫 교사"],
    "ESTP": ["🏅 스포츠 코치", "💼 세일즈 매니저", "✈️ 항공 승무원"],
    # 나머지 MBTI 유형도 동일하게 추가 가능
}

# 🌟 제목 꾸미기
st.markdown("""
<h1 style='text-align: center; color: #ff66b3;'>
🌈 MBTI 직업 추천 💼<br>
<small>당신의 성격에 딱 맞는 직업을 찾아드립니다!</small>
</h1>
""", unsafe_allow_html=True)

st.markdown("---")

# 🎯 MBTI 선택
selected_mbti = st.selectbox("✨ MBTI를 선택하세요 ✨", list(mbti_jobs.keys()))

# 💡 추천 버튼
if st.button("💖 나에게 어울리는 직업 보기 💖"):
    st.balloons()
    st.success(f"🎉 {selected_mbti} 유형의 추천 직업 리스트 🎉")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")

    st.markdown("---")
    st.info(f"💡 **{selected_mbti}** 유형은 특별한 성향과 재능을 지닌 사람들로, "
            f"이러한 직업에서 잠재력을 최대한 발휘할 수 있습니다! ✨")

# ✨ 하단 꾸미기
st.markdown("""
<div style='text-align: center; font-size: 14px; color: gray;'>
🌟 Created with ❤️ using <b>Streamlit</b> 🌟
</div>
""", unsafe_allow_html=True)
