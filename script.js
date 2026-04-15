let problems = [];
let activeCategory = null;

// 标签结构：大类 => 小类（叶子标签）
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

// 【关键修复】提前获取所有DOM元素，避免未定义错误
const container = document.querySelector(".container");
const noteContainer = document.getElementById("note-container");
const problemTableContainer = document.getElementById("problem-table-container");
const catContainer = document.getElementById("categories");

window.addEventListener("DOMContentLoaded", async () => {
  try {
    const pRes = await fetch("problems.json");
    problems = await pRes.json();
    renderCategories();
  } catch (e) {
    console.error("加载题目数据失败:", e);
  }
});

// 渲染大类按钮
function renderCategories() {
  for (const cat in tagStructure) {
    const div = document.createElement("span");
    div.className = "category";
    div.innerText = cat;
    div.onclick = () => toggleCategory(cat);
    catContainer.appendChild(div);
  }
}

// 切换大类：展开/收起小类 + 加载知识点
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

// 【修复】显示小类：解决container未定义问题
function showSubtags(cat) {
  let subtagsDiv = document.querySelector(".subtags");
  if (!subtagsDiv) {
    subtagsDiv = document.createElement("div");
    subtagsDiv.className = "subtags";
    // 正确插入到noteContainer之前
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
  // 强制显示小类
  subtagsDiv.style.display = "flex";
}

// 隐藏小类
function hideSubtags() {
  const st = document.querySelector(".subtags");
  if (st) st.style.display = "none";
}

// 加载对应大类的知识点
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

// 清空知识点
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
    <tr>
      <th>🔥 序号</th>
      <th>📚 题目</th>
      <th>⭐️ 标签</th>
    </tr>
    ${filtered.map(p => `
    <tr>
      <td>${p.id}</td>
      <td><a href="${p.url}" target="_blank">${p.title}</a></td>
      <td>${p.tags.join(", ")}</td>
    </tr>`).join("")}
  </table>`;
}

// 清空题目表格
function clearTable() {
  problemTableContainer.innerHTML = "";
}