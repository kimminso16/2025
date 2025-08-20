<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>🧪 인터랙티브 주기율표 (1~20번)</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      text-align: center;
      background: linear-gradient(135deg, #e0f7fa, #f1f8e9);
    }
    h1 {
      margin-top: 20px;
      font-size: 28px;
    }
    .table {
      display: grid;
      grid-template-columns: repeat(10, 80px);
      justify-content: center;
      gap: 8px;
      margin-top: 20px;
    }
    .element {
      background: white;
      border-radius: 12px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.2);
      padding: 10px;
      cursor: pointer;
      transition: transform 0.2s;
    }
    .element:hover {
      transform: scale(1.1);
      background: #ffe082;
    }
    .symbol {
      font-size: 20px;
      font-weight: bold;
    }
    .number {
      font-size: 12px;
      color: gray;
    }
    #info {
      margin-top: 30px;
      padding: 15px;
      max-width: 600px;
      margin-left: auto;
      margin-right: auto;
      background: #ffffffcc;
      border-radius: 15px;
      box-shadow: 0 2px 8px rgba(0,0,0,0.3);
      font-size: 16px;
      text-align: left;
    }
  </style>
</head>
<body>
  <h1>🧪 주기율표 (1~20번 원소)</h1>
  <div class="table" id="periodicTable"></div>
  <div id="info">⬆️ 원소를 클릭하면 정보가 여기에 표시됩니다!</div>

  <script>
    const elements = [
      {num:1, sym:"H", name:"수소", info:"가장 가벼운 원소 🌬️. 연료전지·우주 산업에 활용"},
      {num:2, sym:"He", name:"헬륨", info:"비활성 기체 🎈. 풍선·MRI 냉각에 사용"},
      {num:3, sym:"Li", name:"리튬", info:"가벼운 금속 🔋. 배터리·약물에 사용"},
      {num:4, sym:"Be", name:"베릴륨", info:"가볍고 단단 🛠️. 항공우주 산업에 활용"},
      {num:5, sym:"B", name:"붕소", info:"반도체 소재 💻. 유리·세라믹 강화"},
      {num:6, sym:"C", name:"탄소", info:"생명의 기본 원소 🌱. 다이아몬드·연필심"},
      {num:7, sym:"N", name:"질소", info:"공기 78% 차지 🌍. 비료·냉각제에 사용"},
      {num:8, sym:"O", name:"산소", info:"생명 유지에 필수 💨. 의료·산업 연소"},
      {num:9, sym:"F", name:"플루오린", info:"가장 반응성 높은 원소 ⚡. 치약·Teflon"},
      {num:10, sym:"Ne", name:"네온", info:"비활성 기체 💡. 네온사인에 사용"},
      {num:11, sym:"Na", name:"나트륨", info:"소금의 원소 🧂. 전해질 균형에 중요"},
      {num:12, sym:"Mg", name:"마그네슘", info:"가벼운 금속 ⚙️. 합금·소화제"},
      {num:13, sym:"Al", name:"알루미늄", info:"가볍고 내식성 🥫. 항공기·캔"},
      {num:14, sym:"Si", name:"규소", info:"반도체 산업 핵심 💻. 유리·모래 구성"},
      {num:15, sym:"P", name:"인", info:"DNA·ATP 구성 🔋. 비료·폭약에 사용"},
      {num:16, sym:"S", name:"황", info:"노란색 원소 🌋. 고무·비료·약품"},
      {num:17, sym:"Cl", name:"염소", info:"소독·표백제 🧴. PVC 플라스틱"},
      {num:18, sym:"Ar", name:"아르곤", info:"비활성 기체 🔦. 전구·용접"},
      {num:19, sym:"K", name:"칼륨", info:"신경전달 필수 ⚡. 비료·의학에 사용"},
      {num:20, sym:"Ca", name:"칼슘", info:"뼈·치아 구성 🦴. 시멘트·영양제"}
    ];

    const tableDiv = document.getElementById("periodicTable");
    const infoDiv = document.getElementById("info");

    elements.forEach(el => {
      let div = document.createElement("div");
      div.className = "element";
      div.innerHTML = `
        <div class="number">${el.num}</div>
        <div class="symbol">${el.sym}</div>
        <div>${el.name}</div>
      `;
      div.onclick = () => {
        infoDiv.innerHTML = `<b>${el.num}번 ${el.name} (${el.sym})</b><br>${el.info}`;
      };
      tableDiv.appendChild(div);
    });
  </script>
</body>
</html>
