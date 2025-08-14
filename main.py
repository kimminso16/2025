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
    "E
