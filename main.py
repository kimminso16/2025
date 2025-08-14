import streamlit as st

# MBTI별 직업 추천 데이터
mbti_jobs = {
    "INTJ": ["데이터 분석가", "전략 컨설턴트", "연구원"],
    "ENTP": ["마케팅 기획자", "창업가", "광고 기획자"],
    "INFJ": ["심리상담가", "작가", "교육 전문가"],
    "ESFP": ["배우", "이벤트 플래너", "여행 가이드"],
    # 나머지 MBTI도 추가...
}

st.set_page_config(page_title="MBTI 직업 추천", page_icon="💼", layout="centered")

st.title("💼 MBTI 기반 직업 추천")
st.write("자신의 MBTI를 선택하면 어울리는 직업을 추천해드립니다!")

# MBTI 선택
selected_mbti = st.selectbox("MBTI를 선택하세요", list(mbti_jobs.keys()))

if st.button("추천 직업 보기"):
    st.subheader(f"🔍 {selected_mbti} 유형의 추천 직업")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")

    # 선택 MBTI 상세 설명
    st.info(f"{selected_mbti} 유형은 창의성과 분석력을 활용하는 분야에서 강점을 보입니다.")

