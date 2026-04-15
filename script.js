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

// 配置marked.js 渲染代码块
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

  // 搜索功能
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
      activeSubtag = null;
      // 清除所有高亮
      document.querySelectorAll(".category, .subtag").forEach(el => el.classList.remove("active"));
      return;
    }

    // 切换大类时清除旧高亮
    document.querySelectorAll(".category, .subtag").forEach(el => el.classList.remove("active"));
    activeCategory = cat;
    // 点亮当前大类
    document.querySelectorAll(".category").forEach(c => {
      if (c.innerText === cat) c.classList.add("active");
    });
    
    showSubtags(cat);
    await loadNote(cat);
    clearTable();
  }

  // 显示小类（核心：点击小类同时点亮大类）
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
        // 1. 清除所有高亮
        document.querySelectorAll(".category, .subtag").forEach(el => el.classList.remove("active"));
        // 2. 点亮当前小类
        btn.classList.add("active");
        // 3. 点亮所属大类
        document.querySelectorAll(".category").forEach(c => {
          if (c.innerText === cat) c.classList.add("active");
        });
        // 4. 筛选题目
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

  // 加载MD知识点（分栏布局+锚点跳转）
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
            <p>点击左侧「Fig」链接查看对应代码</p>
          </div>
        </div>
      </div>`;

      // 渲染MD + 处理锚点
      renderNoteWithAnchors(currentNoteContent);
      hljs.highlightAll();
    } catch (e) {
      console.error("加载知识点失败:", e);
      noteContainer.innerHTML = `<div class="note">无知识点</div>`;
    }
  }

  // 渲染MD + 处理Fig锚点
  function renderNoteWithAnchors(content) {
    const textEl = document.getElementById("note-text");
    const codeEl = document.getElementById("note-code");
    
    // 分割文本和代码块
    const blocks = content.split(/(```[\s\S]*?```)/g);
    let textHtml = "";
    let codeBlocks = [];

    blocks.forEach((block, index) => {
      if (block.startsWith("```")) {
        // 代码块：提取语言和代码
        const lines = block.split("\n");
        const lang = lines[0].replace("```", "").trim() || "plaintext";
        const code = lines.slice(1, -1).join("\n");
        codeBlocks.push({ lang, code, id: `code-${index}` });
        // 在文本中插入Fig链接
        textHtml += `<span class="fig-link" data-code-id="code-${index}">[Fig ${codeBlocks.length}]</span>`;
      } else {
        // 普通文本：直接渲染MD
        textHtml += marked.parse(block);
      }
    });

    textEl.innerHTML = textHtml;
    // 初始化右侧代码区
    codeEl.innerHTML = `<p>点击左侧「Fig」链接查看对应代码</p>`;

    // 绑定Fig点击事件
    document.querySelectorAll(".fig-link").forEach(link => {
      link.addEventListener("click", () => {
        const codeId = link.dataset.codeId;
        const codeBlock = codeBlocks.find(b => b.id === codeId);
        if (codeBlock) {
          codeEl.innerHTML = `
            <pre><code class="language-${codeBlock.lang}">${codeBlock.code}</code></pre>
          `;
          hljs.highlightElement(codeEl.querySelector("code"));
          // ✅ 我已经把这行【滚动代码彻底删掉】！
        }
      });
    });

    hljs.highlightAll();
  }

  // 折叠/展开知识点
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