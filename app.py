import streamlit as st
import altair as alt
import pandas as pd

# 앱 제목
st.set_page_config(page_title="⚙️ 스마트 합금 설계 시뮬레이터", page_icon="🧪")

st.title("⚙️ 스마트 합금 설계 시뮬레이터 🧪✨")
st.write("여러 원소를 선택해서 합금을 설계하고 ⚡ 특징과 활용 분야를 알아보세요!")

# 원소 데이터
elements = {
    "Fe (철)": {"특징": "강도가 높고 자기적 성질 보유 ⚡", "분야": "건축, 자동차 🚗, 기계 🛠️"},
    "Al (알루미늄)": {"특징": "가볍고 부식에 강함 🌊", "분야": "항공 ✈️, 포장재 📦, 전기 전선 ⚡"},
    "Cu (구리)": {"특징": "전기전도율이 매우 높음 🔌", "분야": "전선 ⚡, 동전 💰, 합금 (청동, 황동) 🛡️"},
    "Ni (니켈)": {"특징": "부식 저항성 🧩, 강도 향상", "분야": "스테인리스 강 🍴, 배터리 🔋"},
    "Ti (티타늄)": {"특징": "가볍고 인체 친화적 ❤️", "분야": "의료 임플란트 🦾, 항공 ✈️"},
    "Mg (마그네슘)": {"특징": "아주 가벼움 🪶", "분야": "항공 ✈️, 자동차 🚗 경량화"},
}

# 사용자 입력
selected = st.multiselect("👉 합금할 원소를 선택하세요:", list(elements.keys()))

if selected:
    st.subheader("🧾 선택한 원소의 특징")
    for el in selected:
        st.markdown(f"**{el}**")
        st.write(f"- 특징: {elements[el]['특징']}")
        st.write(f"- 활용 분야: {elements[el]['분야']}")

    # 데이터프레임 변환 (활용분야 갯수 기준 단순화)
    df = pd.DataFrame({
        "원소": selected,
        "활용 분야 개수": [len(elements[el]['분야'].split(",")) for el in selected]
    })

    # Altair 그래프 (예쁘게)
    chart = (
        alt.Chart(df)
        .mark_bar(cornerRadiusTopLeft=10, cornerRadiusTopRight=10, color="steelblue")
        .encode(
            x=alt.X("원소", sort=None, title="🔬 원소"),
            y=alt.Y("활용 분야 개수", title="📊 활용 다양성"),
            tooltip=["원소", "활용 분야 개수"]
        )
    )
    st.altair_chart(chart, use_container_width=True)

    st.subheader("📸 관련 이미지")
    if "Al (알루미늄)" in selected:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Aluminium-4.jpg/320px-Aluminium-4.jpg", caption="알루미늄 금속")
    if "Fe (철)" in selected:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Iron_electrolytic_and_1cm3_cube.jpg/320px-Iron_electrolytic_and_1cm3_cube.jpg", caption="철 금속")
    if "Cu (구리)" in selected:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Copper%28II%29_sulfate_pentahydrate_powder_sample.jpg/320px-Copper%28II%29_sulfate_pentahydrate_powder_sample.jpg", caption="구리")
else:
    st.info("👆 위에서 원소를 선택하면 결과가 표시됩니다!")
