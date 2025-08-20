<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>🧪 인터랙티브 주기율표 (1~20번)</title>
<style>
  :root{
    --bg:#0b1220;
    --panel:#0e1730;
    --card:#111b38;
    --text:#e6eefc;
    --muted:#9fb2d9;
    --accent:#6ea8fe;
    --ring: #90caf9;
    /* 카테고리 색상 */
    --alkali:#ff8a80;            /* 알칼리 금속 */
    --alkaline:#ffd180;          /* 알칼리 토금속 */
    --nonmetal:#81c784;          /* 비금속 */
    --halogen:#f48fb1;           /* 할로젠 */
    --noble:#80deea;             /* 비활성 기체 */
    --metalloid:#ce93d8;         /* 준금속 */
    --post:#b0bec5;              /* 기타 금속 */
  }
  *{box-sizing:border-box}
  body{
    margin:0; font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, "Noto Sans KR", Arial, "Apple Color Emoji", "Segoe UI Emoji";
    color:var(--text); background: radial-gradient(1200px 700px at 10% -10%, #1a2350, #091020 60%);
  }
  header{
    padding:18px 20px; display:flex; gap:14px; align-items:center; justify-content:space-between;
    border-bottom:1px solid rgba(255,255,255,.06);
    backdrop-filter: blur(4px);
  }
  .title{
    font-size: clamp(18px, 2vw, 22px); font-weight:700; letter-spacing:.2px; display:flex; gap:10px; align-items:center;
  }
  .title .emoji{font-size: 22px}
  .legend{display:flex; flex-wrap:wrap; gap:8px; align-items:center; color:var(--muted); font-size:13px}
  .legend span{display:inline-flex; align-items:center; gap:6px; padding:6px 10px; border-radius:999px; background:rgba(255,255,255,.06);}
  .dot{width:12px; height:12px; border-radius:50%}

  main{display:grid; grid-template-columns: 1fr 360px; gap:16px; padding:16px;}
  @media (max-width: 980px){
    main{grid-template-columns: 1fr}
  }

  .board{
    background: rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.08); border-radius:18px; padding:16px; position:relative;
    box-shadow: 0 10px 30px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.04);
  }
  .grid{
    display:grid; grid-template-columns: repeat(18, minmax(36px, 1fr)); gap:8px; min-height: 420px;
  }
  .cell{
    position:relative; background:var(--card); border:1px solid rgba(255,255,255,.08); border-radius:12px; padding:6px; cursor:pointer;
    transition: transform .08s ease, box-shadow .2s ease, border-color .2s ease, background .2s ease;
    user-select:none;
  }
  .cell:hover{ transform: translateY(-1px); box-shadow:0 8px 18px rgba(0,0,0,.35); border-color: var(--ring)}
  .cell.active{ outline:2px solid var(--ring); box-shadow:0 0 0 3px rgba(144,202,249,.25) inset}
  .cell .num{font-size:10px; color:var(--muted)}
  .cell .sym{font-weight:800; font-size:18px; line-height:1.1}
  .cell .name{font-size:10px; color:var(--muted)}
  .cell .cat{position:absolute; inset:auto 6px 6px auto; width:10px; height:10px; border-radius:999px}

  /* 카테고리 색 반영 */
  .cat-alkali{background:var(--alkali)}
  .cat-alkaline{background:var(--alkaline)}
  .cat-nonmetal{background:var(--nonmetal)}
  .cat-halogen{background:var(--halogen)}
  .cat-noble{background:var(--noble)}
  .cat-metalloid{background:var(--metalloid)}
  .cat-post{background:var(--post)}

  .panel{
    background: linear-gradient(160deg, rgba(255,255,255,.05), rgba(255,255,255,.02)); border:1px solid rgba(255,255,255,.08);
    border-radius:18px; padding:18px; position:sticky; top:12px; height:fit-content;
  }
  .panel h2{margin:0 0 4px 0; display:flex; align-items:center; gap:10px; font-size:20px}
  .panel .badge{font-size:12px; color:#0b1220; background:var(--noble); border-radius:999px; padding:4px 8px; font-weight:700}
  .panel .meta{display:grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap:10px; margin:10px 0 14px}
  .meta div{background:rgba(255,255,255,.06); border:1px solid rgba(255,255,255,.08); padding:10px; border-radius:12px; font-size:13px}
  .uses{margin:10px 0 0; padding-left:18px}
  .muted{color:var(--muted)}
  .hint{font-size:13px; color:var(--muted); margin-top:6px}
  .footer{margin-top:14px; font-size:12px; color:var(--muted)}

  .searchbar{display:flex; gap:8px; margin:0 0 12px 0}
  .searchbar input{flex:1; background:rgba(255,255,255,.06); border:1px solid rgba(255,255,255,.12); color:var(--text);
    border-radius:12px; padding:10px 12px; outline:none}
  .searchbar input:focus{border-color: var(--ring)}

  .pill{display:inline-flex; align-items:center; gap:6px; padding:6px 10px; border-radius:999px; background:rgba(255,255,255,.06); font-size:12px; margin-right:6px}
</style>
</head>
<body>
  <header>
    <div class="title"><span class="emoji">🔬</span>인터랙티브 주기율표 <span class="muted">(1~20번 원소)</span></div>
    <div class="legend">
      <span><i class="dot" style="background:var(--alkali)"></i> 알칼리 금속</span>
      <span><i class="dot" style="background:var(--alkaline)"></i> 알칼리 토금속</span>
      <span><i class="dot" style="background:var(--metalloid)"></i> 준금속</span>
      <span><i class="dot" style="background:var(--nonmetal)"></i> 비금속</span>
      <span><i class="dot" style="background:var(--halogen)"></i> 할로젠</span>
      <span><i class="dot" style="background:var(--noble)"></i> 비활성 기체</span>
      <span><i class="dot" style="background:var(--post)"></i> 기타 금속</span>
    </div>
  </header>

  <main>
    <section class="board">
      <div class="searchbar">
        <input id="search" type="text" placeholder="🔎 원소 이름/기호/번호로 검색 (예: H, Hydrogen, 수소, 8)" />
      </div>
      <div id="grid" class="grid" role="grid" aria-label="Periodic table first 20 elements"></div>
      <div class="hint">💡 팁: 원소 카드를 클릭하면 우측 패널에 상세 정보가 표시됩니다.</div>
    </section>

    <aside class="panel" id="panel">
      <h2>원소를 선택해 주세요 <span class="badge">✨ Tip</span></h2>
      <div class="muted">왼쪽에서 원소를 클릭하면 여기에서 <b>성질</b>과 <b>활용 분야</b>를 확인할 수 있어요.</div>
      <ul class="uses">
        <li>예: 산소(O) — 호흡·의료용 산소 💨🩺</li>
        <li>예: 실리콘(Si) — 반도체·태양전지 🔌☀️</li>
      </ul>
      <div class="footer">ⓘ 교육용 요약 데이터입니다. 수치는 편의를 위해 반올림/간략화되어 있을 수 있어요.</div>
    </aside>
  </main>

<script>
// ===== 데이터셋 (1~20번) =====
const elements = [
  {Z:1, sym:'H', name:'Hydrogen', kr:'수소', group:1, period:1, category:'nonmetal', mass:1.008, uses:['연료전지·로켓 연료 🚀','암모니아 합성(하버-보슈) 🧪','환원 분위기 공급 🔧']},
  {Z:2, sym:'He', name:'Helium', kr:'헬륨', group:18, period:1, category:'noble', mass:4.003, uses:['MRI 자석 냉각 ❄️','기구·풍선 🎈','불활성 보호 가스 🛡️']},
  {Z:3, sym:'Li', name:'Lithium', kr:'리튬', group:1, period:2, category:'alkali', mass:6.94, uses:['리튬 이온 배터리 🔋','경량 합금 ✈️','그리스(윤활) 🛢️']},
  {Z:4, sym:'Be', name:'Beryllium', kr:'베릴륨', group:2, period:2, category:'alkaline', mass:9.0122, uses:['항공우주 합금 ✈️','X선 창 🩻','정밀 기기 스프링 ⚙️']},
  {Z:5, sym:'B', name:'Boron', kr:'붕소', group:13, period:2, category:'metalloid', mass:10.81, uses:['내열 유리(보로실리케이트) 🍳','세제·표백 🧼','반도체 도핑 💡']},
  {Z:6, sym:'C', name:'Carbon', kr:'탄소', group:14, period:2, category:'nonmetal', mass:12.011, uses:['강철·탄소섬유 🏗️','그래파이트 윤활·전극 🖊️','유기 화합물의 뼈대 🌱']},
  {Z:7, sym:'N', name:'Nitrogen', kr:'질소', group:15, period:2, category:'nonmetal', mass:14.007, uses:['비료(암모니아) 🌾','식품 포장 불활성화 🍱','실험용 냉각(액체질소) ❄️']},
  {Z:8, sym:'O', name:'Oxygen', kr:'산소', group:16, period:2, category:'nonmetal', mass:15.999, uses:['의료·호흡 보급 🩺','제강 공정 🔥','산화 반응 촉진 🧪']},
  {Z:9, sym:'F', name:'Fluorine', kr:'플루오린', group:17, period:2, category:'halogen', mass:18.998, uses:['불소수지(테플론) 🍳','우라늄 농축 UF₆ ⚛️','치아 불소화 🦷']},
  {Z:10, sym:'Ne', name:'Neon', kr:'네온', group:18, period:2, category:'noble', mass:20.180, uses:['네온사인 💡','헬륨 혼합 냉각 ❄️','가스 레이저 🔦']},
  {Z:11, sym:'Na', name:'Sodium', kr:'나트륨', group:1, period:3, category:'alkali', mass:22.990, uses:['소금·염화나트륨 🧂','나트륨 램프 🟡','유기합성 환원제 🧪']},
  {Z:12, sym:'Mg', name:'Magnesium', kr:'마그네슘', group:2, period:3, category:'alkaline', mass:24.305, uses:['경량 합금 🚗','불꽃놀이·플래시 💥','의학용 제산제 💊']},
  {Z:13, sym:'Al', name:'Aluminum', kr:'알루미늄', group:13, period:3, category:'post', mass:26.982, uses:['캔·포일 🥫','항공기 동체 ✈️','건축 자재 🏗️']},
  {Z:14, sym:'Si', name:'Silicon', kr:'규소', group:14, period:3, category:'metalloid', mass:28.085, uses:['반도체 칩 🖥️','태양전지 ☀️','유리·실리카 🧪']},
  {Z:15, sym:'P', name:'Phosphorus', kr:'인', group:15, period:3, category:'nonmetal', mass:30.974, uses:['비료 🌾','성냥(적린) 🧯','리튬인산철 배터리 🔋']},
  {Z:16, sym:'S', name:'Sulfur', kr:'황', group:16, period:3, category:'nonmetal', mass:32.06, uses:['황산 생산 🏭','고무 가황 🛞','살균·농약 🚜']},
  {Z:17, sym:'Cl', name:'Chlorine', kr:'염소', group:17, period:3, category:'halogen', mass:35.45, uses:['수처리 소독 🚿','PVC 플라스틱 🧱','표백제 🧼']},
  {Z:18, sym:'Ar', name:'Argon', kr:'아르곤', group:18, period:3, category:'noble', mass:39.948, uses:['용접 보호가스 🛡️','전구 충전 💡','3D 프린팅 분위기 🖨️']},
  {Z:19, sym:'K', name:'Potassium', kr:'칼륨', group:1, period:4, category:'alkali', mass:39.098, uses:['비료(포타시) 🌾','비누 제조 🫧','실험용 강염 시험 🔥']},
  {Z:20, sym:'Ca', name:'Calcium', kr:'칼슘', group:2, period:4, category:'alkaline', mass:40.078, uses:['시멘트·석회 🧱','제철 탈산·탈황 🏭','식품·뼈 건강 🦴']},
];

// 좌표(그룹,주기) → CSS grid 위치
const pos = {
  1:{1:[1,1], 2:[1,2], 3:[1,3], 4:[1,4]},
  2:{1:[18,1]},
  3:{2:[2,2]}, 4:{2:[2,3]}, 20:{2:[2,4]},
  5:{13:[13,2]}, 13:{3:[13,3]},
  6:{14:[14,2]}, 14:{3:[14,3]},
  7:{15:[15,2]}, 15:{3:[15,3]},
  8:{16:[16,2]}, 16:{3:[16,3]},
  9:{17:[17,2]}, 17:{3:[17,3]},
  10:{18:[18,2]}, 18:{3:[18,3]}
};
// 위 pos는 가독성을 위해 분해했으므로 아래에서 함수로 위치를 계산합니다.

const gridEl = document.getElementById('grid');
const panelEl = document.getElementById('panel');
const searchEl = document.getElementById('search');
let activeZ = null;

function categoryClass(cat){
  return {
    alkali:'cat-alkali',
    alkaline:'cat-alkaline',
    nonmetal:'cat-nonmetal',
    halogen:'cat-halogen',
    noble:'cat-noble',
    metalloid:'cat-metalloid',
    post:'cat-post'
  }[cat] || 'cat-nonmetal'
}

function gridPosition(el){
  // el: 원소 객체
  const c = el.group; const r = el.period;
  return {col: c, row: r}; // 그룹=열, 주기=행 (표준 배치)
}

function renderGrid(list){
  gridEl.innerHTML = '';
  list.forEach(el => {
    const {col, row} = gridPosition(el);
    const card = document.createElement('button');
    card.className = 'cell';
    card.setAttribute('role','gridcell');
    card.style.gridColumn = col;
    card.style.gridRow = row;
    card.dataset.z = el.Z;
    card.innerHTML = `
      <div class="num">${el.Z}</div>
      <div class="sym" aria-hidden="true">${el.sym}</div>
      <div class="name">${el.kr}</div>
      <i class="cat ${categoryClass(el.category)}"></i>
    `;
    card.addEventListener('click', () => selectElement(el.Z));
    gridEl.appendChild(card);
  });
}

function selectElement(Z){
  activeZ = Z;
  const el = elements.find(e=>e.Z===Z);
  if(!el) return;
  // active 스타일
  document.querySelectorAll('.cell').forEach(c=>c.classList.remove('active'));
  const active = [...document.querySelectorAll('.cell')].find(c=>+c.dataset.z===Z);
  if(active) active.classList.add('active');

  // 패널 렌더링
  const emojiByCat = {
    alkali:'🧯', alkaline:'🧱', nonmetal:'🌿', halogen:'🧼', noble:'🧊', metalloid:'💎', post:'🔩'
  };
  const catName = {
    alkali:'알칼리 금속', alkaline:'알칼리 토금속', nonmetal:'비금속', halogen:'할로젠', noble:'비활성 기체', metalloid:'준금속', post:'기타 금속'
  };
  panelEl.innerHTML = `
    <h2>${emojiByCat[el.category] || '🔬'} ${el.kr} <span class="muted">(${el.name}, ${el.sym})</span></h2>
    <div class="pill">#${el.Z}</div>
    <div class="pill">${catName[el.category] || ''}</div>
    <div class="meta">
      <div><b>원자번호</b><br/>${el.Z}</div>
      <div><b>원자량</b><br/>~ ${el.mass}</div>
      <div><b>주기</b><br/>${el.period}</div>
      <div><b>족(그룹)</b><br/>${el.group}</div>
    </div>
    <div><b>활용 분야 & 포인트</b></div>
    <ul class="uses">
      ${el.uses.map(u=>`<li>${u}</li>`).join('')}
    </ul>
    <div class="hint">📌 교육용 간략 설명입니다. 고급 데이터(전자배치, 융/비점 등)도 원하시면 확장 가능해요.</div>
  `;
}

function handleSearch(){
  const q = searchEl.value.trim().toLowerCase();
  const found = elements.find(e => [
    e.Z.toString(), e.sym.toLowerCase(), e.name.toLowerCase(), (e.kr||'').toLowerCase()
  ].some(t => t===q || (q && t.includes(q))));
  if(found){ selectElement(found.Z); }
}

searchEl.addEventListener('input', handleSearch);

// 초기 렌더
renderGrid(elements);
// 기본 선택: 수소
selectElement(1);
</script>
</body>
</html>
interactive_periodic.html
