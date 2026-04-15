let problems = [];
let activeCategory = null;
let currentNoteContent = "";
let activeSubtag = null;

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

marked.setOptions({
  highlight: function(code, lang) {
    if (lang && hljs.getLanguage(lang)) return hljs.highlight(code, { language: lang }).value;
    return hljs.highlightAuto(code).value;
  },
  breaks: true
});

window.addEventListener("DOMContentLoaded", async () => {
  const container = document.querySelector(".container");
  const noteContainer = document.getElementById("note-container");
  const problemTableContainer = document.getElementById("problem-table-container");
  const catContainer = document.getElementById("categories");
  const searchInput = document.getElementById("search-input");

  searchInput.addEventListener("input", (e) => {
    const keyword = e.target.value.toLowerCase();
    if (!currentNoteContent) return;
    const textEl = document.getElementById("note-text");
    let html = marked.parse(currentNoteContent);
    if (keyword) {
      const regex = new RegExp(`(${keyword})`, "gi");
      html = html.replace(regex, `<mark>$1</mark>`);
    }
    textEl.innerHTML = html;
    hljs.highlightAll();
  });

  try { const pRes = await fetch("problems.json"); problems = await pRes.json(); } catch (e) {}

  for (const cat in tagStructure) {
    const div = document.createElement("span");
    div.className = "category";
    div.innerText = cat;
    div.onclick = () => toggleCategory(cat);
    catContainer.appendChild(div);
  }

  async function toggleCategory(cat) {
    document.querySelectorAll(".category, .subtag").forEach(el => el.classList.remove("active"));
    if (activeCategory === cat) { activeCategory = null; hideSubtags(); noteContainer.innerHTML = ""; clearTable(); return; }
    activeCategory = cat;
    document.querySelectorAll(".category").forEach(c => { if (c.innerText === cat) c.classList.add("active"); });
    showSubtags(cat);
    await loadNote(cat);
    clearTable();
  }

  function showSubtags(cat) {
    let subtagsDiv = document.querySelector(".subtags");
    if (!subtagsDiv) { subtagsDiv = document.createElement("div"); subtagsDiv.className = "subtags"; container.insertBefore(subtagsDiv, noteContainer); }
    subtagsDiv.innerHTML = "";
    tagStructure[cat].forEach(sub => {
      const btn = document.createElement("span");
      btn.className = "subtag";
      btn.innerText = sub;
      btn.onclick = () => {
        document.querySelectorAll(".category, .subtag").forEach(el => el.classList.remove("active"));
        btn.classList.add("active");
        document.querySelectorAll(".category").forEach(c => { if (c.innerText === cat) c.classList.add("active"); });
        filterByLeaf(sub);
      };
      subtagsDiv.appendChild(btn);
    });
    subtagsDiv.style.display = "flex";
  }

  function hideSubtags() { const st = document.querySelector(".subtags"); if (st) st.style.display = "none"; }

  async function loadNote(cat) {
    try {
      const res = await fetch(`data/${fileMap[cat]}`);
      currentNoteContent = await res.text();
      noteContainer.innerHTML = `
      <div class="note-wrapper">
        <button class="note-toggle" onclick="toggleNote()">📖 展开知识点</button>
        <div class="note-content" id="note-content" style="display:none;">
          <div class="note-text" id="note-text"></div>
          <div class="note-code" id="note-code"><p>点击 Fig 查看代码</p></div>
        </div>
      </div>`;
      renderNoteCorrect(currentNoteContent);
    } catch (e) { noteContainer.innerHTML = `<div class="note">无知识点</div>`; }
  }

  function renderNoteCorrect(content) {
    const textEl = document.getElementById("note-text");
    const codeEl = document.getElementById("note-code");
    let codeBlocks = [];
    let idx = 1;

    let processed = content.replace(/```([\s\S]*?)```/g, (match, code) => {
      const id = `fig-${idx++}`;
      codeBlocks.push({ id, code: "```" + code + "```" });
      return `<span class="fig-link" data-fig="${id}"> [Fig${idx-1}] </span>`;
    });

    textEl.innerHTML = marked.parse(processed);
    codeEl.innerHTML = "<p>点击左侧 Fig 查看代码</p>";

    document.querySelectorAll(".fig-link").forEach((link, i) => {
      link.addEventListener("click", () => {
        const id = link.dataset.fig;
        const block = codeBlocks.find(b => b.id === id);
        if (block) {
          codeEl.innerHTML = marked.parse(block.code);
          hljs.highlightAll();

          // ✅ 核心：右边代码栏 同步左边滚动位置
          setTimeout(() => {
            const codeNodes = codeEl.querySelectorAll("pre");
            if (codeNodes[i]) codeNodes[i].scrollIntoView({ behavior: "smooth", block: "start" });
          }, 0);
        }
      });
    });
    hljs.highlightAll();
  }

  window.toggleNote = function () {
    const content = document.getElementById("note-content");
    const btn = document.querySelector(".note-toggle");
    if (content.style.display === "flex") {
      content.style.display = "none";
      btn.textContent = "📖 展开知识点";
    } else {
      content.style.display = "flex";
      btn.textContent = "📕 收起知识点";
    }
  };

  function filterByLeaf(leafTag) {
    const filtered = problems.filter(p => p.tags.includes(leafTag)).sort((a, b) => a.id - b.id);
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

  function clearTable() { problemTableContainer.innerHTML = ""; }
});