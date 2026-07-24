# notion-bold-diagrams

> 一个开源的 **Claude Code / Codex Skill**：把一段内容画成一张 **Notion 风格的粗描边概念图**。
> 透明背景 · 近黑粗描边 · 柔和色块 · 中文粗黑标题 —— 关系图 / 流程图 / 框架图 / 概念图 / PPT 配图，一句话搞定。

核心理念：**一个想法 → 一张能读懂的图**，先保住信息，再谈好看。两种出图路径：有 **Pencil** 就出可编辑的 `.pen` + 透明 PNG；没有就直接在代码库里生成自包含 **SVG**（可选再渲染 PNG）。

---

## 安装（30 秒）

这个 skill 收在 [`CookieSparkLab/skills`](https://github.com/CookieSparkLab/skills) 合集仓库里。

### 方式 A · clone 合集，拷一个 skill 进项目（推荐）

```bash
git clone https://github.com/CookieSparkLab/skills.git
cp -r skills/notion-bold-diagrams 你的项目/.claude/skills/
```

> Codex 用户拷到 `.agents/skills/` 或你的 skills 目录下同理。

### 方式 B · 直接下载

在仓库页点 **Code → Download ZIP**，解压后把 `notion-bold-diagrams` 文件夹丢进项目的 `.claude/skills/`。

---

## 怎么用

装好后，对 AI 说一句话：

> 用 `notion-bold-diagrams` 这个 skill，把这段内容画成一张关系图。

AI 会自动：① 提炼一句话核心结论 → ② 拆成 3–7 个语义节点 → ③ 选结构（`flow` 流程 / `hub` 中心辐射 / `comparison` 对比 / `layers` 分层 / `equation` 等式 / `cards` 卡片）→ ④ 先画结构、再连线、再放框、最后写字 → ⑤ 校验排版、导出源文件与预览图。

**触发词**：画关系图 / 流程图 / 框架图 / 概念图 / 信息图 / PPT 配图 / 可视化一段内容，或点名要「粗黑线 + 柔和色块 / Pencil / SVG / 透明 PNG」。

---

## 文件说明

| 文件 | 作用 |
|------|------|
| `SKILL.md` | 给 AI 看的技能本体：输出路由、工作流、**硬性排版约束**、风格规范、自检清单。 |
| `references/style-spec.md` | 视觉语言规范（颜色、描边粗细、字号）。 |
| `references/pencil-workflow.md` | 用 Pencil 出图的完整流程。 |
| `references/svg-workflow.md` | 在代码库里生成 SVG 的流程。 |
| `scripts/validate_svg.mjs` | 校验 SVG 里连接线 / 文字有没有重叠：`node scripts/validate_svg.mjs diagram.svg`。 |
| `assets/example.svg` | 一张示例图。 |
| `agents/openai.yaml` | Agent 元信息。 |

## 风格约定

- **透明画布**、近黑描边与文字 `#111111`、描边 6–8px（按 1920×1080）。
- 柔和色块：粉 / 蓝 / 薄荷 / 红 / 暖黄；直角或微圆角（6–12px）。
- 中文粗黑标题，正文精简；**用颜色区分角色，而不是当装饰**。
- 不用渐变、玻璃拟态、霓虹、光泽 3D、细灰线、过度阴影、卡通吉祥物。
- 铁律：任何连线 / 箭头 / 图标都**不许压到文字**，放不下就删细节或拆成两张。

## License

[MIT](../LICENSE) —— 自由使用、修改、分发。
