let problems = [];
let activeCategory = null;

// 标签结构：大类 => 小类（叶子）
const tagStructure = {
  "比赛": ["LC", "CF"],
  "位运算": ["库函数", "XOR", "AND/OR"],
  "数学": ["加法", "乘法", "模运算"],
  "二分": ["基础", "二分答案"]
};

// 大类 → 英文知识点文件名（中文内容保留）
const fileMap = {
  "比赛": "contest.json",
  "位运算": "bitwise.json",
  "数学": "math.json",
  "二分": "binary.json"
};

// 全局获取DOM元素（修复变量未定义问题）
const container = document.querySelector(".container");
const noteContainer = document.getElementById("note-container");
const problemTableContainer = document.getElementById("problem-table-container");

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
    // 修复事件绑定：用箭头函数确保作用域正确
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

// 显示小类（修复变量+DOM操作）
function showSubtags(cat) {
  let subtagsDiv = document.querySelector(".subtags");
  if (!subtagsDiv) {
    subtagsDiv = document.createElement("div");
    subtagsDiv.className = "subtags";
    // 修复：正确插入到noteContainer之前
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
  // 强制显示：解决display:none不生效问题
  subtagsDiv.style.display = "flex";
}

function hideSubtags() {
  const st = document.querySelector(".subtags");
  if (st) st.style.display = "none";
}

// 加载知识点（修复模板字符串语法）
async function loadNote(cat) {
  try {
    const res = await fetch(`data/${fileMap[cat]}`);
    const data = await res.json();
    noteContainer.innerHTML = `<div class="note">${data.content}</div>`;
  } catch (e) {
    console.error("加载知识点失败:", e);
    noteContainer.innerHTML = `<div class="note">无知识点</div>`;
  }
}

function clearNote() {
  noteContainer.innerHTML = "";
}

// 按叶子标签筛选题目
function filterByLeaf(leafTag) {
  const filtered = problems
    .filter(p => p.tags.includes(leafTag))
    .sort((a, b) => a.id - b.id);

  problemTableContainer.innerHTML = `
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
  problemTableContainer.innerHTML = "";
}