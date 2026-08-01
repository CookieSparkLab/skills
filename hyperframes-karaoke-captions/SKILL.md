---
name: hyperframes-karaoke-captions
description: >-
  给 HyperFrames 竖版口播视频加「逐词滑动高亮」卡拉OK式字幕特效（一个荧光笔色圆角框在词间水平滑动、只高亮当前说到的词）。
  当用户在做 hyperframes / HTML→MP4 视频，想加字幕、口播字幕、卡拉OK字幕、逐词高亮、字幕特效、
  把 SRT 烧进视频、subtitle/caption animation、给竖版视频叠字幕时，使用本 skill。
  即使用户只说「给这个视频加字幕」「字幕再做个高亮特效」「把这句 SRT 做成动画字幕」，
  只要上下文是 hyperframes 合成，也应触发。不要用于纯静态海报、Pencil(.pen) 设计稿、非 hyperframes 的视频剪辑。
---

# HyperFrames 逐词滑动高亮字幕

给 HyperFrames 竖版（9:16，1080×1920）口播视频叠加卡拉OK式字幕：整句先出现，然后**一个荧光笔色的圆角高亮框在词与词之间水平滑动**，滑到哪个词、哪个词就是「正在说的词」，框宽随词宽变化。字幕用 SRT 的逐句时间戳驱动，句内每个词按时间均分。

这套效果的完整可复制代码在 `references/caption-effect.md`，把 SRT 转成时间数组的脚本在 `scripts/srt_to_cues.py`。**动手前先读 `references/caption-effect.md`** —— 里面有整段 CSS+JS、可调参数表和踩坑点。

**想在某句做「综艺强调」**（画面瞬间 punch 放大 120% + 人物轮廓外圈弹一圈 😍/🔥 emoji，句末缩回）：读 `references/variety-emphasis.md`，直接套 `LOVE` 配置。适合情绪高点（「太好用了」「绝了」「震惊」）。

## 什么时候用
- 已经在一个 hyperframes 工程里（有 `index.html` 合成、`npm run dev` 预览、`npm run render`）
- 有一段竖版口播视频 + 一份 SRT（或逐句时间），想把字幕做成会动的逐词高亮

## 三步走

1. **SRT → CUES**：用 `python3 scripts/srt_to_cues.py 你的.srt` 生成 `CUES` 数组（`[开始秒, 结束秒, "这句文字"]`）。若只做前 N 秒，加 `--end 30`；整体平移用 `--offset`。把输出粘进合成的 `<script>`。

2. **粘代码**：把 `references/caption-effect.md` 里的 CSS 段落放进 `<head><style>`，把 `#caption-layer` 容器放进 `#root`，把 JS 段落放进注册 timeline 的 `<script>`。确认视频是全屏铺底（`#person video { object-fit: cover }`），字幕 `z-index` 高于视频。

3. **校验 + 预览**：`npm run check`（0 error 即可；字幕压在视频上会有一堆「对比度 error」，那是检查器不知道视频内容的**误报**，不阻塞渲染）。再开 `npm run dev` 拖时间轴看，满意了 `npm run render`。

## 可调的几个点（细节见 reference）
- **高亮色**：`--marker`（默认荧光笔黄 `#FFD84A`）。要珊瑚红等直接改。
- **字色/描边**：默认白字 + 4px 黑描边 + 无阴影（`-webkit-text-stroke` + `paint-order: stroke`）。压在视频上最稳。
- **位置**：`.capline { bottom: … }`（下三分之一，默认 450px；往下移就减小）。
- **字号**：`.tok { font-size: … }`（竖版默认 52px）。
- **词间距**：中文词之间不加人为间隙（连贯）；原文里本来有的空格用 `.sp` 保留。

## 最容易踩的坑（reference 里有详解）
- 滑块位置靠 `tok.offsetLeft/offsetWidth` **同步测量**——所以字体要用系统字体（PingFang SC 立即可测）；若换下载字体，测量可能在字体加载前发生导致框错位。
- 别在动画元素上同时用 CSS `transform` 居中 + GSAP 动 `x`（HyperFrames StaticGuard 会报错）：`.capline` 用 `translateX(-50%)` 居中，但**不要**对它做 GSAP 的 x/scale 动画；滑动只发生在子元素 `.slider` 上。
- 字幕元素**不要**加 `class="clip"`，可见性全靠 GSAP 手动控制（`autoAlpha`），避免和 hyperframes 的 clip 生命周期打架。
