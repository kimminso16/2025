<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>🧪 인터랙티브 주기율표 (1~20번)</title>
  <style>
    body { font-family: Arial, sans-serif; text-align: center; }
    h1 { margin: 20px; }
    .grid { display: grid; grid-template-columns: repeat(10, 80px); gap: 10px; justify-content: center; }
    .element {
      border: 2px solid #333; border-radius: 10px;
      padding: 10px; cursor: pointer;
      background: linear-gradient(145deg, #e6e6e6, #ffffff);
      transition: transform 0.2s, background 0.2s;
    }
    .element:hover { transform: scale(1.1); background: #f0f8ff; }
    #infoBox {
      margin-top: 30px; padding: 20px; border: 2px solid #555;
      border-radius: 10px; max-width: 600px; margin-left: auto; margin-right: auto;
      background: #fafafa;
    }
  </style>
</head>
<body>
  <h1>🧪 인터랙티브 주기율표 (1~20번)</h1>
  <div class="grid" id="periodicTable"></div>

  <div id="infoBox">⬆️ 원소를 클릭하면 성질과 활용을 볼 수 있어요!</div>

  <script>
    const elements = [
      {symbol:"H", name:"수소", info:"가장 가벼운 원소 ⚡ / 연료전지·암모니아 합성에 사용"},
      {symbol:"He", name:"헬륨", info:"불활성 기체 🎈 / 풍선, 냉각재로 활용"},
      {symbol:"Li", name:"리튬", info:"가벼운 금속 🔋 / 이차전지에 사용"},
      {symbol:"Be", name:"베릴륨", info:"단단하고 가벼움 🛡 / 합금, 원자로켓 소재"},
      {symbol:"B", name:"붕소", info:"반도체 성질 💡 / 유리, 세라믹 강화"},
      {symbol:"C", name:"탄소", info:"생명체의 기본 원소 🌱 / 다이아몬드, 연료"},
      {symbol:"N", name:"질소", info:"대기의 78% 🌬 / 비료, 냉각제"},
      {symbol:"O", name:"산소", info:"호흡에 필수 💨 / 의료, 용접"},
      {symbol:"F", name:"플루오린", info:"반응성이 매우 큼 ⚠ / 불소수지, 치약"},
      {symbol:"Ne", name:"네온", info:"불활성 기체 💡 / 네온사인"},
      {symbol:"Na", name:"나트륨", info:"활발한 금속 🧂 / 소금, 고압등"},
      {symbol:"Mg", name:"마그네슘", info:"가벼운 금속 ✈ / 합금, 폭죽"},
      {symbol:"Al", name:"알루미늄", info:"가볍고 내식성 🥤 / 캔, 비행기"},
      {symbol:"Si", name:"규소", info:"반도체 원소 💻 / 전자기기, 유리"},
      {symbol:"P", name:"인", info:"생명체 필수 원소 🧬 / 비료, 불꽃"},
      {symbol:"S", name:"황", info:"노란색 비금속 🌋 / 화약, 의약품"},
      {symbol:"Cl", name:"염소", info:"살균 작용 🧼 / 소독제, PVC"},
      {symbol:"Ar", name:"아르곤", info:"불활성 기체 💡 / 전구, 용접"},
      {symbol:"K", name:"칼륨", info:"생체 필수 이온 ❤️ / 비료, 유리"},
      {symbol:"Ca", name:"칼슘", info:"뼈·치아 구성 🦴 / 시멘트, 제강"},
    ];

    const container = document.getElementById("periodicTable");
    const infoBox = document.getElementById("infoBox");

    elements.forEach(el => {
      const div = document.createElement("div");
      div.className = "element";
      div.innerHTML = `<strong>${el.symbol}</strong><br>${el.name}`;
      div.onclick = () => {
        infoBox.innerHTML = `🔎 <b>${el.symbol} (${el.name})</b><br>${el.info}`;
      };
      container.appendChild(div);
    });
  </script>
</body>
</html>
