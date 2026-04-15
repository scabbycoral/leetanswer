let problems = [];
let activeCategory = null;

const tagStructure = {
  "contest": ["LC", "CF"],
  "bitwise": ["库函数", "XOR", "AND/OR"],
  "math": ["加法", "乘法", "模运算"],
  "binary": ["基础", "二分答案"]
};

window.addEventListener("DOMContentLoaded", async () => {
  const pRes = await fetch("problems.json");
  problems = await pRes.json();
  renderCategories();
});

function renderCategories() {
  const catContainer = document.getElementById("categories");
  for (const cat in tagStructure) {
    const div = document.createElement("div");
    div.className = "category";
    div.innerText = cat;
    div.onclick = () => toggleCategory(cat);
    catContainer.appendChild(div);
  }
}

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
  await loadAndShowNote(cat);
  clearTable();
}

function showSubtags(cat) {
  let subtagsDiv = document.querySelector(".subtags");
  if (!subtagsDiv) {
    subtagsDiv = document.createElement("div");
    subtagsDiv.className = "subtags";
    document.querySelector(".container").insertBefore(subtagsDiv, document.getElementById("note-container"));
  }

  subtagsDiv.innerHTML = "";
  tagStructure[cat].forEach(sub => {
    const btn = document.createElement("div");
    btn.className = "subtag";
    btn.innerText = sub;
    btn.onclick = () => filterProblems(`${cat}:${sub}`);
    subtagsDiv.appendChild(btn);
  });
  subtagsDiv.style.display = "flex";
}

function hideSubtags() {
  const st = document.querySelector(".subtags");
  if (st) st.style.display = "none";
}

async function loadAndShowNote(cat) {
  const noteContainer = document.getElementById("note-container");
  try {
    const res = await fetch(`data/${cat}.json`);
    const data = await res.json();
    noteContainer.innerHTML = `
      <div class="note" id="note-content">${data.content}</div>
    `;
  } catch (e) {
    noteContainer.innerHTML = `<div class="note">无知识点</div>`;
  }
}

function clearNote() {
  document.getElementById("note-container").innerHTML = "";
}

function filterProblems(tag) {
  const filtered = problems
    .filter(p => p.tags.includes(tag))
    .sort((a, b) => a.id - b.id);

  const table = `
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

  document.getElementById("problem-table-container").innerHTML = table;
}

function clearTable() {
  document.getElementById("problem-table-container").innerHTML = "";
}
