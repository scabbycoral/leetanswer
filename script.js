
// ====================== 你只需要在这里维护题目 ======================
const problems = [
  { id: 136, title: "只出现一次的数字", tag: "位运算", platform: "LC" },
  { id: 461, title: "汉明距离", tag: "位运算", platform: "LC" },
  { id: 704, title: "二分查找", tag: "二分", platform: "LC" },
  { id: 300, title: "最长上升子序列", tag: "DP", platform: "LC" },
  { id: 1, title: "Two Sum", tag: "哈希", platform: "LC" },
  { id: 42, title: "接雨水", tag: "双指针", platform: "LC" },
  { id: 123, title: "CF DP 基础", tag: "DP", platform: "CF" },
  { id: 456, title: "CF 位运算", tag: "位运算", platform: "CF" },
];
// ===================================================================

// 自动生成标签按钮
function buildTags() {
  let tags = new Set();
  problems.forEach(p => tags.add(p.tag));
  tags = Array.from(tags);

  const container = document.getElementById("tags");
  tags.forEach(tag => {
    const btn = document.createElement("button");
    btn.className = "tag-btn";
    btn.innerText = tag;
    btn.onclick = () => filterByTag(tag);
    container.appendChild(btn);
  });
}

// 显示全部题目
function showAll() {
  render(problems);
  setActive("全部");
}

// 按标签筛选
function filterByTag(tag) {
  const res = problems.filter(p => p.tag === tag);
  render(res);
  setActive(tag);
}

// 渲染题目列表
function render(list) {
  const div = document.getElementById("problem-list");
  div.innerHTML = "";

  list.forEach(p => {
    const item = document.createElement("div");
    item.className = "problem";
    item.innerHTML = `
      <span class="title">${p.id}. ${p.title}</span>
      <span class="platform">${p.platform}</span>
      <span class="tag">${p.tag}</span>
    `;
    div.appendChild(item);
  });
}

// 高亮当前选中标签
function setActive(text) {
  document.querySelectorAll(".tag-btn").forEach(btn => {
    btn.classList.remove("active");
    if (btn.innerText === text) btn.classList.add("active");
  });
}

// 初始化页面
buildTags();
showAll();
