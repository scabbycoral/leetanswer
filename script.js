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
    if (lang && hljs.getLanguage(lang)) {
      return hljs.highlight(code, { language: lang }).value;
    }
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

  // 搜索
  searchInput.addEventListener("input", (e) => {
    const keyword = e.target.value.toLowerCase();
    if (!currentNoteContent) return;
    const textEl = document.getElementById("note-text");
    if (!textEl) return;
    
    let html = marked.parse(currentNoteContent);
    if (keyword) {
      const regex = new RegExp(`(${keyword})`, "gi");
      html = html.replace(regex, `<mark>$1</mark>`);
    }
    textEl.innerHTML = html;
    hljs.highlightAll();
  });

  // 加载题目
  try {
    const pRes = await fetch("problems.json");
    problems = await pRes.json();
  } catch (e) {
    console.error("加载题目失败:", e);
  }

  // 大类
  for (const cat in tagStructure) {
    const div = document.createElement("span");
    div.className = "category";
    div.innerText = cat;
    div.onclick = () => toggleCategory(cat);
    catContainer.appendChild(div);
  }

  async function toggleCategory(cat) {
    if (activeCategory === cat) {
      activeCategory = null;
      hideSubtags();
      noteContainer.innerHTML = "";
      clearTable();
      activeSubtag = null;
      document.querySelectorAll(".category, .subtag").forEach(el => el.classList.remove("active"));
      return;
    }
    document.querySelectorAll(".category, .subtag").forEach(el => el.classList.remove("active"));
    activeCategory = cat;
    document.querySelectorAll(".category").forEach(c => {
      if (c.innerText === cat) c.classList.add("active");
    });
    showSubtags(cat);
    await loadNote(cat);
    clearTable();
  }

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
      btn.onclick = () => {
        document.querySelectorAll(".category, .subtag").forEach(el => el.classList.remove("active"));
        btn.classList.add("active");
        document.querySelectorAll(".category").forEach(c => {
          if (c.innerText === cat) c.classList.add("active");
        });
        filterByLeaf(sub);
      };
      subtagsDiv.appendChild(btn);
    });
    subtagsDiv.style.display = "flex";
  }

  function hideSubtags() {
    const st = document.querySelector(".subtags");
    if (st) st.style.display = "none";
  }

  // 加载MD
  async function loadNote(cat) {
    try {
      const res = await fetch(`data/${fileMap[cat]}`);
      currentNoteContent = await res.text();

      noteContainer.innerHTML = `
      <div class="note-wrapper">
        <button class="note-toggle" onclick="toggleNote()">📖 展开知识点</button>
        <div class="note-content" id="note-content">
          <div class="note-text" id="note-text"></div>
          <div class="note-code" id="note-code">
            <p>点击左侧「Fig」查看代码</p>
          </div>
        </div>
      </div>`;

      renderNoteWithAnchors(currentNoteContent);
      hljs.highlightAll();
    } catch (e) {
      console.error("加载知识点失败:", e);
      noteContainer.innerHTML = `<div class="note">无知识点</div>`;
    }
  }

  // 渲染MD + Fig锚点
  function renderNoteWithAnchors(content) {
    const textEl = document.getElementById("note-text");
    const codeEl = document.getElementById("note-code");
    
    const blocks = content.split(/(```[\s\S]*?```)/g);
    let textHtml = "";
    let codeBlocks = [];

    blocks.forEach((block, index) => {
      if (block.startsWith("```")) {
        const lines = block.split("\n");
        const lang = lines[0].replace("```", "").trim() || "plaintext";
        const code = lines.slice(1, -1).join("\n");
        codeBlocks.push({ lang, code, id: `code-${index}` });
        textHtml += `<span class="fig-link" data-code-id="code-${index}">[Fig ${codeBlocks.length}]</span>`;
      } else {
        textHtml += marked.parse(block);
      }
    });

    textEl.innerHTML = textHtml;
    codeEl.innerHTML = `<p>点击左侧「Fig」查看代码</p>`;

    // 点击 Fig：只刷新右侧，不滚动
    document.querySelectorAll(".fig-link").forEach(link => {
      link.addEventListener("click", () => {
        const codeId = link.dataset.codeId;
        const codeBlock = codeBlocks.find(b => b.id === codeId);
        if (codeBlock) {
          codeEl.innerHTML = `
            <pre><code class="language-${codeBlock.lang}">${codeBlock.code}</code></pre>
          `;
          hljs.highlightElement(codeEl.querySelector("code"));
          // ✅ 完全删掉 scrollIntoView，不跳页
        }
      });
    });

    hljs.highlightAll();
  }

  // 折叠知识点
  window.toggleNote = function () {
    const content = document.getElementById("note-content");
    const btn = document.querySelector(".note-toggle");
    if (content.style.display === "flex") {
      content.style.display = "none";
      btn.textContent = "📖 展开知识点";
      // 折叠时隐藏代码面板
      document.querySelector(".note-code").style.display = "none";
    } else {
      content.style.display = "flex";
      btn.textContent = "📕 收起知识点";
      document.querySelector(".note-code").style.display = "block";
    }
  };

  // 筛选题目
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