<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>🧪 스마트 합금 설계 시뮬레이터 ⚙️</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      background: linear-gradient(120deg, #f0f9ff, #e0f7fa);
      text-align: center;
      padding: 30px;
    }
    h1 {
      color: #0d47a1;
      font-size: 2em;
    }
    .container {
      background: #fff;
      border-radius: 15px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
      padding: 20px;
      max-width: 600px;
      margin: 20px auto;
    }
    label {
      font-weight: bold;
    }
    input, select {
      margin: 5px;
      padding: 8px;
      border-radius: 8px;
      border: 1px solid #ccc;
    }
    button {
      margin-top: 15px;
      padding: 10px 20px;
      border: none;
      background: #0288d1;
      color: white;
      font-size: 1em;
      border-radius: 10px;
      cursor: pointer;
    }
    button:hover {
      background: #0277bd;
    }
    .result {
      margin-top: 20px;
      padding: 15px;
      border-radius: 12px;
      background: #f1f8e9;
      font-size: 1.1em;
    }
  </style>
</head>
<body>
  <h1>🧪 스마트 합금 설계 시뮬레이터 ⚙️</h1>
  <p>금속 원소와 비율을 선택해 📊 합금 특성을 예측해보세요!</p>

  <div class="container">
    <label>원소 1 선택 🔹</label>
    <select id="metal1">
      <option value="Fe">철(Fe)</option>
      <option value="C">탄소(C)</option>
      <option value="Al">알루미늄(Al)</option>
      <option value="Cu">구리(Cu)</option>
      <option value="Ni">니켈(Ni)</option>
    </select>
    <input type="number" id="ratio1" placeholder="비율 %" min="0" max="100">

    <br><br>

    <label>원소 2 선택 🔸</label>
    <select id="metal2">
      <option value="C">탄소(C)</option>
      <option value="Fe">철(Fe)</option>
      <option value="Al">알루미늄(Al)</option>
      <option value="Cu">구리(Cu)</option>
      <option value="Ni">니켈(Ni)</option>
    </select>
    <input type="number" id="ratio2" placeholder="비율 %" min="0" max="100">

    <br>
    <button onclick="predictAlloy()">⚡ 합금 특성 예측하기</button>

    <div id="output" class="result"></div>
  </div>

  <script>
    function predictAlloy() {
      const metal1 = document.getElementById('metal1').value;
      const ratio1 = parseInt(document.getElementById('ratio1').value) || 0;
      const metal2 = document.getElementById('metal2').value;
      const ratio2 = parseInt(document.getElementById('ratio2').value) || 0;

      const output = document.getElementById('output');

      if (ratio1 + ratio2 !== 100) {
        output.innerHTML = "⚠️ 비율의 합은 100%가 되어야 합니다!";
        return;
      }

      let result = `🔬 ${metal1} ${ratio1}% + ${metal2} ${ratio2}% → `;

      // 간단한 규칙 기반 예시
      if ((metal1 === "Fe" && metal2 === "C") || (metal1 === "C" && metal2 === "Fe")) {
        if (ratio2 <= 2) {
          result += "⚙️ 강철(높은 강도와 연성)";
        } else {
          result += "🏗️ 주철(높은 경도, 취약함)";
        }
      } else if ((metal1 === "Al" && metal2 === "Cu") || (metal1 === "Cu" && metal2 === "Al")) {
        result += "✈️ 알루미늄 합금(가볍고 강도↑, 항공기 재료)";
      } else if ((metal1 === "Ni" && metal2 === "Fe") || (metal1 === "Fe" && metal2 === "Ni")) {
        result += "🔥 니켈강(내식성↑, 내열성↑, 산업용)";
      } else {
        result += "🧩 특성이 복합적으로 변함 (실험 필요)";
      }

      output.innerHTML = result;
    }
  </script>
</body>
</html>
