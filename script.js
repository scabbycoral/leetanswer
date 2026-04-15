let allProblems = [];
let currentSubtag = null;

// 定义多级标签结构
const tagStructure = {
  "比赛": ["LC", "CF"],
  "位运算": ["库函数", "XOR", "AND/OR"],
  "二分": ["基础", "二分答案"],
  "贪心": ["基础", "区间"],
  "DP": ["线性", "背包", "区间"]
};

// 加载 JSON（性能最高）
window.addEventListener("DOMContentLoaded", async () => {
  const res = await fetch("data/problems.json");
  allProblems = await res.json();
  renderTags();
});

// 渲染多级标签
function renderTags() {
  const container = document.getElementById("tag-container");
  container.innerHTML = "";

  for (const [main, subs] of Object.entries(tagStructure)) {
    const cat = document.createElement("div");
    cat.className = "category";
    cat.innerText = main;

    const subTagContainer = document.createElement("div");
    subTagContainer.className = "subtags";

    subs.forEach(sub => {
      const btn = document.createElement("div");
      btn.className = "subtag";
      btn.innerText = sub;
      btn.onclick = () => {
        currentSubtag = `${main}:${sub}`;
        document.querySelectorAll(".subtag").forEach(s => s.classList.remove("active"));
        btn.classList.add("active");
        filterProblems();
      };
      subTagContainer.appendChild(btn);
    });

    container.appendChild(cat);
    container.appendChild(subTagContainer);
  }
}

// 筛选题目（按题号排序）
function filterProblems() {
  const list = document.getElementById("problem-list");
  if (!currentSubtag) {
    list.innerHTML = "";
    return;
  }

  const filtered = allProblems
    .filter(p => p.tags.includes(currentSubtag))
    .sort((a, b) => a.id - b.id);

  list.innerHTML = filtered.map(p => `
    <div class="problem">
      <a href="${p.url}" target="_blank">${p.id}. ${p.title}</a>
    </div>
  `).join("");
}
