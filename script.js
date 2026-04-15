let problems = [];
let activeCategory = null;
let currentNoteContent = "";

const tagStructure = {
  "比赛": ["LC", "CF"],
  "位运算": ["库函数", "XOR", "AND/OR"],
  "数学": ["加法", "乘法", "模运算"],
  "二分": ["基础", "二分答案"]
};

const fileMap = {
  "比赛": "contest.md",
  "位运算": "bitwise.md",
  "数学": "math.md",
  "二分": "binary.md"
};

window.addEventListener("DOMContentLoaded", async () => {
  const container = document.querySelector(".container");
  const noteContainer = document.getElementById("note-container");
  const problemTableContainer = document.getElementById("problem-table-container");
  const catContainer = document.getElementById("categories");
  const searchInput = document.getElementById("search-input");

  // 搜索功能
  searchInput.addEventListener("input", (e) => {
    const keyword = e.target.value.toLowerCase();
    if (!currentNoteContent) return;
    let highlighted = currentNoteContent.replace(/</g, "&lt;").replace(/>/g, "&gt;");
    if (keyword) {
      const regex = new RegExp(keyword, "gi");
      highlighted = highlighted.replace(regex, (match) => `<mark>${match}</mark>`);
    }
    document.getElementById("note-text").innerHTML = highlighted;
  });

  // 加载题目
  try {
    const pRes = await fetch("problems.json");
    problems = await pRes.json();
  } catch (e) {}

  // 渲染大类
  for (const cat in tagStructure) {
    const div = document.createElement("span");
    div.className = "category";
    div.innerText = cat;
    div.onclick = () => toggleCategory(cat);
    catContainer.appendChild(div);
  }

  // 切换大类
  async function toggleCategory(cat) {
    if (activeCategory === cat) {
      activeCategory = null;
      hideSubtags();
      noteContainer.innerHTML = "";
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

  // 加载 MD 知识点（默认折叠）
  async function loadNote(cat) {
    try {
      const res = await fetch(`data/${fileMap[cat]}`);
      currentNoteContent = await res.text();

      noteContainer.innerHTML = `
      <div class="note-wrapper">
        <button class="note-toggle" onclick="toggleNote()">📖 展开知识点</button>
        <div class="note-content" id="note-content">
          <div id="note-text"></div>
        </div>
      </div>`;

      document.getElementById("note-text").textContent = currentNoteContent;
    } catch (e) {
      noteContainer.innerHTML = `<div class="note">无知识点</div>`;
    }
  }

  // 折叠/展开知识点
  window.toggleNote = function () {
    const content = document.getElementById("note-content");
    const btn = document.querySelector(".note-toggle");
    if (content.style.display === "block") {
      content.style.display = "none";
      btn.textContent = "📖 展开知识点";
    } else {
      content.style.display = "block";
      btn.textContent = "📕 收起知识点";
    }
  };

  // 筛题
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
});