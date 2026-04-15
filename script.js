let problems = [];
let activeCategory = null;

const tagStructure = {
  "比赛": ["LC", "CF"],
  "位运算": ["库函数", "XOR", "AND/OR"],
  "数学": ["加法", "乘法", "模运算"],
  "二分": ["基础", "二分答案"]
};

// 只改这里：文件名英文
const fileMap = {
  "比赛": "contest.json",
  "位运算": "bitwise.json",
  "数学": "math.json",
  "二分": "binary.json"
};

window.addEventListener("DOMContentLoaded", async () => {
  const pRes = await fetch("problems.json");
  problems = await pRes.json();
  renderCategories();
});

// 渲染大类
function renderCategories() {
  const catContainer = document.getElementById("categories");
  for (const cat in tagStructure) {
    const div = document.createElement("span");
    div.className = "category";
    div.innerText = cat;
    div.onclick = () => toggleCategory(cat);
    catContainer.appendChild(div);
  }
}

// 切换大类
async function toggleCategory(cat) {
  if (activeCategory === cat) {
    activeCategory = null;
    hideSubtags();
    clearNote();
    clearTable();
    return;
  }

  activeCategory = cat;
  showSubtags(cat);
  await loadNote(cat);
  clearTable();
}

// 显示小类
function showSubtags(cat) {
  let subtagsDiv = document.querySelector(".subtags");
  if (!subtagsDiv) {
    subtagsDiv = document.createElement("div");
    subtagsDiv.className = "subtags";
    container.insertBefore(subtagsDiv, noteContainer);
  }

  subtagsDiv.innerHTML = "";
  tagStructure[cat].forEach(sub => {
    const btn = document.createElement("span");
    btn.className = "subtag";
    btn.innerText = sub;
    btn.onclick = () => filterByLeaf(sub);
    subtagsDiv.appendChild(btn);
  });
  subtagsDiv.style.display = "flex";
}

function hideSubtags() {
  const st = document.querySelector(".subtags");
  if (st) st.style.display = "none";
}

// 加载知识点
async function loadNote(cat) {
  const noteContainer = document.getElementById("note-container");
  try {
    const res = await fetch(`data/${fileMap[cat]}`);
    const data = await res.json();
    noteContainer.innerHTML = `<div class="note">${data.content}</div>`;
  } catch (e) {
    noteContainer.innerHTML = `<div class="note">无知识点</div>`;
  }
}

function clearNote() {
  document.getElementById("note-container").innerHTML = "";
}

// 按叶子tag筛题
function filterByLeaf(leafTag) {
  const filtered = problems
    .filter(p => p.tags.includes(leafTag))
    .sort((a, b) => a.id - b.id);

  document.getElementById("problem-table-container").innerHTML = `
  <table>
    <tr><th>🔥 序号</th><th>📚 题目</th><th>⭐️ 标签</th></tr>
    ${filtered.map(p => `
    <tr>
      <td>${p.id}</td>
      <td><a href="${p.url}" target="_blank">${p.title}</a></td>
      <td>${p.tags.join(", ")}</td>
    </tr>`).join("")}
  </table>`;
}

function clearTable() {
  document.getElementById("problem-table-container").innerHTML = "";
}