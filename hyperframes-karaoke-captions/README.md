# HyperFrames 逐词滑动高亮字幕（卡拉OK字幕特效）

给 **HyperFrames** 竖版（9:16, 1080×1920）口播视频叠加卡拉OK式字幕：整句先出现，然后**一个荧光笔黄的圆角高亮框在词与词之间水平滑动**，滑到哪个词、哪个词就是「正在说的词」，框宽随词宽变化。字幕由 SRT 的逐句时间戳驱动，句内按词均分。

> 只用于 HyperFrames / HTML→MP4 合成里的字幕特效，不是通用视频剪辑工具。

## 安装

```bash
# 方式一：skills CLI
npx skills add CookieSparkLab/skills@hyperframes-karaoke-captions

# 方式二：手动拷进项目
cp -r hyperframes-karaoke-captions 你的项目/.claude/skills/
```

然后在一个 HyperFrames 工程里对 AI 说：「用 `hyperframes-karaoke-captions` 给这个视频加逐词高亮字幕」。

## 三步走

1. **SRT → CUES**：`python3 scripts/srt_to_cues.py 你的.srt`（`--start/--end/--offset` 可截取平移）→ 得到 `[开始秒, 结束秒, "文字"]` 数组，粘进合成的 `<script>`。
2. **粘代码**：把 `references/caption-effect.md` 的 CSS / DOM / JS 三块分别放进合成的 `<style>` / `#root` / timeline `<script>`。
3. **校验预览**：`npm run check`（字幕压视频上的对比度报错是误报）→ `npm run dev` 拖时间轴 → `npm run render`。

完整可复制代码 + 可调参数 + 踩坑点见 [`references/caption-effect.md`](references/caption-effect.md)。想给某句做「综艺 punch 强调」见 [`references/variety-emphasis.md`](references/variety-emphasis.md)。

## 可调

| 想改 | 改哪 | 默认 |
|---|---|---|
| 高亮框颜色 | CSS `--marker` | 荧光笔黄 `#FFD84A` |
| 字色 / 描边 | `.tok { color / -webkit-text-stroke }` | 白字 + 4px 黑描边 |
| 字号 | `.tok { font-size }` | 52px（竖版）|
| 竖直位置 | `.capline { bottom }` | 450px |
| 高亮框留白 | JS `PAD` | 10px |
| 滑动手感 | slider tween `duration` / `ease` | 0.16s / power2.inOut |

## License

[MIT](../LICENSE) — CookieSpark Lab（精神饱满俱乐部）
