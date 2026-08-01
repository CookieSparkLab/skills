# 逐词滑动高亮字幕 —— 完整代码

把下面三块（CSS / DOM / JS）粘进一个 HyperFrames 合成（`index.html`）。这套代码经过实拍口播视频验证：整句先出现，一个荧光笔色圆角框在词间水平滑动、只高亮当前词，框宽随词宽变化。

## 1) CSS —— 放进 `<head><style>`

```css
:root { --marker: #FFD84A; }              /* 高亮框颜色（荧光笔黄）*/

#caption-layer { position: absolute; inset: 0; z-index: 45; }

/* 一句字幕。用 translateX 居中——不要对它做 GSAP x/scale 动画（会和 StaticGuard 冲突）*/
.capline {
  position: absolute; left: 50%; bottom: 450px; transform: translateX(-50%);
  white-space: nowrap; visibility: hidden;
}

/* 滑动的高亮框：绝对定位在 .capline 内，靠 GSAP 动 x + width 滑动 */
.slider {
  position: absolute; top: 4px; height: calc(100% - 8px); left: 0; width: 0;
  background: var(--marker); border-radius: 12px; z-index: 0;
}

/* 每个词。白字 + 黑描边 + 无阴影，压在视频上最清晰 */
.tok {
  position: relative; z-index: 1; display: inline-block;
  font-size: 52px; font-weight: 900;
  font-family: "PingFang SC", "Inter", sans-serif;   /* 系统字体：offset 可同步测量 */
  color: #fff; line-height: 1.3; padding: 6px 0;
  -webkit-text-stroke: 4px #000; paint-order: stroke; /* 描边画在字后面，字形不被吃 */
}

/* 原文里本来就有的空格（如 "Image2 和 Claude"）；中文词之间不加，保持连贯 */
.sp { display: inline-block; width: 0.3em; }
```

## 2) DOM —— 放进 `#root`（字幕层，空容器，JS 会填充）

```html
<div id="caption-layer"></div>
```

假设视频是全屏铺底的：

```html
<div id="person" style="position:absolute; inset:0; z-index:1; background:#000">
  <video id="talking-video" class="clip" src="media/talking.mp4"
         data-start="0" data-duration="30" data-track-index="1"
         data-has-audio="true" playsinline
         style="width:100%; height:100%; object-fit:cover; display:block"></video>
</div>
```

## 3) JS —— 放进注册 timeline 的 `<script>`

```js
// ==== 每句字幕：[开始秒, 结束秒, "文字"]。用 scripts/srt_to_cues.py 从 SRT 生成 ====
const CUES = [
  [0.000, 1.600, "这是一句示例字幕"],
  [1.600, 3.400, "换成你自己的 SRT 就行"],
  [3.400, 5.200, "高亮框会逐词滑过去"],
  // ...
];

window.__timelines = window.__timelines || {};
const tl = window.__timelines["main"] || gsap.timeline({ paused: true });

// 分词：中文按 2 字一组、英文/数字整词、标点跟随前一词、原文空格转成 .sp
function buildTokens(line, text) {
  const latin = c => /[A-Za-z0-9]/.test(c);
  const cjk   = c => /[一-鿿]/.test(c);
  const toks = []; let i = 0;
  while (i < text.length) {
    const c = text[i];
    if (c === " ") { const sp = document.createElement("span"); sp.className = "sp"; line.appendChild(sp); i++; continue; }
    let word;
    if (latin(c)) { let j = i; while (j < text.length && latin(text[j])) j++; word = text.slice(i, j); i = j; }
    else if (cjk(c)) { word = c; i++; if (i < text.length && cjk(text[i])) { word += text[i]; i++; } }
    else { if (toks.length) { toks[toks.length-1].appendChild(document.createTextNode(c)); i++; continue; } word = c; i++; }
    const tok = document.createElement("span");
    tok.className = "tok"; tok.appendChild(document.createTextNode(word));
    line.appendChild(tok); toks.push(tok);
  }
  return toks;
}

const capLayer = document.getElementById("caption-layer");
const PAD = 10; // 高亮框比词左右各多出的像素

CUES.forEach(([s, e, text]) => {
  const line = document.createElement("div"); line.className = "capline";
  const slider = document.createElement("div"); slider.className = "slider";
  line.appendChild(slider);
  const toks = buildTokens(line, text);
  capLayer.appendChild(line);

  // 整句只在 [s, e] 期间可见（用 autoAlpha，不要用 class="clip"）
  gsap.set(line, { autoAlpha: 0 });
  tl.set(line, { autoAlpha: 1 }, s);
  tl.set(line, { autoAlpha: 0 }, e);

  // 高亮框：起点落在第一个词；之后每个词按时间均分，滑过去（x + width 一起动 = 横移）
  const n = toks.length, dur = e - s, first = toks[0];
  gsap.set(slider, { x: first.offsetLeft - PAD, width: first.offsetWidth + PAD * 2 });
  toks.forEach((tok, i) => {
    if (i === 0) return;
    const ts = s + (i / n) * dur;
    tl.to(slider, { x: tok.offsetLeft - PAD, width: tok.offsetWidth + PAD * 2,
                    duration: 0.16, ease: "power2.inOut" }, ts);
  });
});

window.__timelines["main"] = tl;
```

> 若合成里还有别的动画（人物、进度条等），共用同一条 `tl` 即可——上面用 `window.__timelines["main"] || gsap.timeline(...)` 兼容已存在的 timeline，最后再 `window.__timelines["main"] = tl`。

## 可调参数速查

| 想改 | 改哪 | 默认 |
|---|---|---|
| 高亮框颜色 | `--marker` | 荧光笔黄 `#FFD84A`（珊瑚红 `#FF5A36` 也常用）|
| 字色 | `.tok { color }` | 白 `#fff` |
| 描边粗细/色 | `.tok { -webkit-text-stroke }` | `4px #000` |
| 字号 | `.tok { font-size }` | 52px（竖版）|
| 竖直位置 | `.capline { bottom }` | 450px（往下移就减小）|
| 高亮框留白 | JS 里 `PAD` | 10px |
| 滑动速度/手感 | slider tween 的 `duration`/`ease` | 0.16s / power2.inOut |
| 每词高亮时长 | 按句时长均分（`dur / n`）| —— |

## 踩坑点（都验证过）

1. **滑块靠同步测量定位**：`tok.offsetLeft/offsetWidth` 在脚本执行时读取。系统字体（PingFang SC 用 `src: local(...)`）立即可测，所以框位置准。**若换成需要下载的字体**（webfont），测量可能发生在字体就绪前，导致框和字错位——这时要么改用系统字体，要么把测量与建 tween 放进 `document.fonts.ready.then(...)`。

2. **别让 CSS transform 撞上 GSAP**：`.capline` 用 `transform: translateX(-50%)` 居中，但**不要**对 `.capline` 做 GSAP 的 `x`/`scale` 动画（GSAP 会覆盖整个 transform，居中丢失，HyperFrames StaticGuard 也会直接报 invalid）。滑动只加在子元素 `.slider` 上（它没有 CSS transform，随便动 x）。

3. **字幕不加 `class="clip"`**：可见性完全用 GSAP `autoAlpha` 在 `[s,e]` 控制。加了 clip 会和 hyperframes 的 clip 可见性生命周期打架。

4. **`npm run check` 的对比度报错是误报**：字幕直接压在视频上，检查器不知道视频像素，会按最坏情况判低对比度、报一堆 error。只要没有别的结构性 error，**照常渲染**即可（`npm run render` 默认不因 lint 失败而中止，除非加 `--strict`）。真实可读性以预览/成片为准——白字+黑描边在实拍画面上通常很清晰。

5. **字体要有 @font-face 声明**：系统中文字体也要在 CSS 里声明一次，否则 hyperframes 渲染时可能回退：
   ```css
   @font-face { font-family: 'PingFang SC'; src: local('PingFang SC'); }
   ```

## 想要「逐词打字机」而不是「滑动框」？

上面是「整句先出现 + 框滑动」。若想改成词逐个淡入（打字机感），去掉 slider，改成每个 `.tok` 起始 `opacity:0`，在它的 `ts` 用 `tl.to(tok,{opacity:1,duration:0.05}, ts)`，当前词另给一个短暂高亮。两种风格按需二选一。
