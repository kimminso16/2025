import streamlit as st

# 안전한 라이브러리 임포트 처리
try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ImportError as e:
    st.error("⚠️ 필요한 라이브러리가 설치되지 않았습니다: " + str(e))
    st.stop()

# 앱 제목
st.title("🔬 합금 탐구 인터랙티브 웹앱")

# 원소 데이터 (활용분야 포함)
elements = {
    "철(Fe)": {"symbol": "Fe", "desc": "강도와 자성을 지님 🧲"},
    "구리(Cu)": {"symbol": "Cu", "desc": "전기 전도성이 뛰어남 ⚡"},
    "알루미늄(Al)": {"symbol": "Al", "desc": "가볍고 내식성이 좋음 ✈️"},
    "니켈(Ni)": {"symbol": "Ni", "desc": "내식성과 경도가 뛰어남 🛡️"},
    "주석(Sn)": {"symbol": "Sn", "desc": "산화에 강하고 부식 방지 🧪"},
    "마그네슘(Mg)": {"symbol": "Mg", "desc": "가벼우며 내열성이 있음 🔥"},
}

# 실제 합금 활용 분야 데이터
alloys = {
    ("철(Fe)", "니켈(Ni)"): {"name": "스테인리스강", "field": "내식성 필요 → 건축, 조선, 주방도구 🍴", "weight": 90},
    ("구리(Cu)", "주석(Sn)"): {"name": "청동", "field": "도구, 예술품, 동전 ⚔️", "weight": 75},
    ("알루미늄(Al)", "마그네슘(Mg)"): {"name": "알루미늄 합금", "field": "항공기, 자동차, 전자제품 🚀", "weight": 95},
    ("철(Fe)", "구리(Cu)"): {"name": "Fe-Cu 합금", "field": "전기 모터, 특수 배관 ⚡", "weight": 60},
    ("니켈(Ni)", "구리(Cu)"): {"name": "백동", "field": "악기, 장식품 🎺", "weight": 70},
}

# 사용자 입력
st.sidebar.header("⚙️ 합금 선택하기")
elem1 = st.sidebar.selectbox("첫 번째 원소 선택", list(elements.keys()))
elem2 = st.sidebar.selectbox("두 번째 원소 선택", list(elements.keys()))

# 같은 원소 선택 방지
if elem1 == elem2:
    st.warning("⚠️ 같은 원소는 선택할 수 없습니다. 다른 원소를 골라주세요!")
else:
    pair = tuple(sorted([elem1, elem2]))

    if pair in alloys:
        alloy_info = alloys[pair]

        # 정보 출력
        st.subheader(f"🔗 {alloy_info['name']}")
        st.write(f"✨ 조합: **{elem1} + {elem2}**")
        st.write(f"📖 활용 분야: {alloy_info['field']}")

        # 시각화 (활용도 그래프)
        df = pd.DataFrame({
            "합금": [alloy_info["name"]],
            "활용도(%)": [alloy_info["weight"]]
        })

        fig, ax = plt.subplots(figsize=(6, 4))
        bars = ax.bar(df["합금"], df["활용도(%)"], color="skyblue", edgecolor="black")

        # 바 위에 값 표시
        for bar in bars:
            yval = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, yval + 2, f"{yval}%", 
                    ha='center', va='bottom', fontsize=12, fontweight='bold')

        ax.set_xlabel("합금 종류", fontsize=12)
        ax.set_ylabel("활용도 (%)", fontsize=12)
        ax.set_title("📊 합금 활용도 그래프", fontsize=14, fontweight='bold')
        st.pyplot(fig)

    else:
        st.error("❌ 이 조합은 데이터베이스에 등록되지 않았습니다.")
        st.info("💡 추가하고 싶은 합금이 있다면 알려주세요!")
