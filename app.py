a import streamlit as st

# 제목
st.set_page_config(page_title="🧪 스마트 합금 설계 시뮬레이터 ⚙️", layout="wide")

st.title("🧪 스마트 합금 설계 시뮬레이터 ⚙️")
st.write("원소를 선택해서 합금을 만들고, 특징과 활용 분야를 확인해보세요! 🚀")

# 원소 데이터
elements = {
    "Al(알루미늄)": {
        "특징": "가볍고 부식에 강함 💨",
        "활용": "항공기✈️, 자동차🚗, 건축🏢"
    },
    "Fe(철)": {
        "특징": "강도가 높음 💪",
        "활용": "교량🌉, 빌딩🏗️, 철강재료⚙️"
    },
    "Cu(구리)": {
        "특징": "전기전도율이 높음 ⚡",
        "활용": "전선🔌, 전자기기📱, 배관🚰"
    },
    "Ni(니켈)": {
        "특징": "내열·내식성 우수 🔥",
        "활용": "배터리🔋, 터빈엔진🛞, 화학기계⚗️"
    },
    "Ti(티타늄)": {
        "특징": "강도 대비 가벼움 🪶",
        "활용": "의료 임플란트🦴, 항공우주🚀, 스포츠 장비🎾"
    }
}

# 사용자 입력
col1, col2 = st.columns(2)
with col1:
    e1 = st.selectbox("첫 번째 원소 선택", list(elements.keys()))
with col2:
    e2 = st.selectbox("두 번째 원소 선택", list(elements.keys()))

# 합금 결과 출력
if e1 and e2 and e1 != e2:
    st.subheader("🔬 합금 결과")

    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**{e1} 특징:** {elements[e1]['특징']}")
        st.write(f"**{e1} 주요 활용 분야:** {elements[e1]['활용']}")
    with col2:
        st.write(f"**{e2} 특징:** {elements[e2]['특징']}")
        st.write(f"**{e2} 주요 활용 분야:** {elements[e2]['활용']}")

    st.markdown("---")

    # 실제 합금 활용 분야 (단순 매핑)
    applications = {
        frozenset(["Al(알루미늄)", "Cu(구리)"]): "⚡ 전기·열 교류 장치, 방열판, 항공기 부품",
        frozenset(["Fe(철)", "C(탄소)"]): "⚙️ 강철(철강 산업 전반)",
        frozenset(["Ni(니켈)", "Cu(구리)"]): "🔋 전기저항 합금, 화폐, 배터리",
        frozenset(["Ti(티타늄)", "Al(알루미늄)"]): "🚀 항공우주, 인공위성, 스포츠 장비",
        frozenset(["Fe(철)", "Ni(니켈)"]): "🔥 내열합금, 발전소 터빈, 원자로"
    }

    combo = frozenset([e1, e2])
    if combo in applications:
        st.success(f"✨ **{e1} + {e2} 합금은 실제로 → {applications[combo]} 에 활용됩니다!**")
    else:
        st.info("💡 이 조합은 특성이 연구 중이거나 활용도가 낮습니다!")

    # 간단한 그래프 (강도 vs 밀도 예시)
    st.subheader("📊 합금 성질 비교")
    chart_data = {
        "원소": [e1, e2],
        "강도(상대적)": [len(elements[e1]["특징"]), len(elements[e2]["특징"])],
        "밀도(상대적)": [len(elements[e1]["활용"]), len(elements[e2]["활용"])]
    }

    import pandas as pd
    df = pd.DataFrame(chart_data)
    st.bar_chart(df.set_index("원소"))

    # 대표 합금 이미지 (Unsplash 무료 이미지 사용)
    st.subheader("🖼️ 대표 합금 이미지")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Aluminium-foil.jpg/640px-Aluminium-foil.jpg",
             caption="예시: 알루미늄 합금", use_container_width=True)

else:
    st.warning("👆 두 개의 다른 원소를 선택해주세요!")
