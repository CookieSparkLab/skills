# CookieSpark Skills

> 精神饱满俱乐部 · 一组开源的 **Claude Code / Codex Skill**，给 Vibe Coding 新手即插即用。
> clone 下来、丢进项目的 `.claude/skills/`，对 AI 说一句话就能用上。

## 技能清单

| Skill | 一句话 | 适用 |
|-------|--------|------|
| [`vibe-coding-saturday-style`](./vibe-coding-saturday-style) | 一键把页面换成「VIBE CODING SATURDAY」活动官网同款 neo-brutalism 风格 | 任意 HTML / React / Vue 前端 |
| [`notion-bold-diagrams`](./notion-bold-diagrams) | 把一段内容画成 Notion 风格的粗描边概念图 / 流程图 / 关系图（Pencil 或 SVG，透明背景） | 关系图 / 流程图 / 框架图 / PPT 配图 |

## 怎么用

```bash
# 1. 下载整个合集
git clone https://github.com/CookieSparkLab/skills.git

# 2. 把需要的 skill 拷进你自己的项目
cp -r skills/vibe-coding-saturday-style 你的项目/.claude/skills/
```

然后对 AI 说：「用 `vibe-coding-saturday-style` 这个 skill，把我的页面换成活动官网同款风格」即可。
每个 skill 文件夹里都有自己的 `README.md` 和 `SKILL.md`，进去看细节。

## License

[MIT](./LICENSE) —— 自由使用、修改、分发。
