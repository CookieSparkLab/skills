# 综艺强调特效：punch 放大 + emoji 流动排

在某一句的情绪高点（「太好用了」「绝了」「惊了」）做综艺式强调：**画面瞬间放大到 120%**，同时**一整排 emoji（😍/🔥/❤️）沿人物头部外圈弧线，从左边进、划过头顶、右边出**——传送带式流动，不是原地弹出。竖版 9:16、全屏视频场景。

## 配置

```js
// s/e = 这句起止秒；cx/cy = 弧线中心（≈人物头部中心）；ax/ay = 弧线椭圆半径
// (ax 要够大让首尾跑出画面两侧；ay 决定弧顶高度，别撞顶部章节标题)；
// count = 一排几个；gap = 相邻 emoji 在弧线上的间距(u 空间，0~1 一整条弧)
const LOVE = { s: 4.6, e: 6.0, cx: 540, cy: 560, ax: 560, ay: 380, count: 8, gap: 0.16, emoji: "😍", size: 92 };
```

## CSS

```css
#fx-layer { position: absolute; inset: 0; z-index: 44; pointer-events: none; }
.emoji { position: absolute; font-size: 96px; line-height: 1; visibility: hidden; will-change: transform;
  filter: drop-shadow(0 4px 10px rgba(0,0,0,0.35)); }
/* 全屏视频容器：给缩放原点对准脸，punch 才是「怼脸放大」 */
#person { transform-origin: 50% 44%; will-change: transform; }
```

## DOM

```html
<div id="fx-layer"></div>   <!-- 视频之上、字幕之下 -->
```

## JS（加进注册 timeline 的 script，用同一条 tl）

```js
// 1) 画面瞬间 punch 到 120%，句末快速回落
tl.set("#person", { scale: 1.2 }, LOVE.s);
tl.to("#person", { scale: 1.0, duration: 0.18, ease: "power2.out" }, LOVE.e - 0.18);

// 2) 一整排 emoji 沿头部外圈弧线，从左进→划过头顶→右出（传送带式流动）
const fxLayer = document.getElementById("fx-layer");
const emojis = [];
for (let i = 0; i < LOVE.count; i++) {
  const el = document.createElement("div");
  el.className = "emoji"; el.textContent = LOVE.emoji; el.style.fontSize = LOVE.size + "px";
  fxLayer.appendChild(el);
  gsap.set(el, { xPercent: -50, yPercent: -50, visibility: "hidden" }); // xPercent 居中，别用 CSS translate
  emojis.push(el);
}
const LOVE_SPAN = 1 + (LOVE.count - 1) * LOVE.gap + 0.3;   // 让整排首尾都跑出画面
function placeLove(p) {
  emojis.forEach((el, i) => {
    const u = p * LOVE_SPAN - 0.15 - i * LOVE.gap;         // u: 0=左侧 1=右侧
    if (u < -0.1 || u > 1.1) { el.style.visibility = "hidden"; return; }
    el.style.visibility = "visible";
    const ang = Math.PI * (1 - u);                         // π→0：左→右，弧线过头顶
    el.style.left = (LOVE.cx + LOVE.ax * Math.cos(ang)) + "px";
    el.style.top  = (LOVE.cy - LOVE.ay * Math.sin(ang)) + "px";
  });
}
const loveProxy = { p: 0 };
placeLove(0);
// 用 proxy + onUpdate 驱动：HyperFrames 每帧 seek 都会触发 onUpdate，seek-safe、确定性
tl.to(loveProxy, { p: 1, duration: LOVE.e - LOVE.s, ease: "none",
                   onUpdate: () => placeLove(loveProxy.p) }, LOVE.s);
```

弧线数学：`ang = π(1-u)`，`x = cx + ax·cos(ang)`，`y = cy − ay·sin(ang)`。u=0 在左侧(cx−ax, cy)，u=0.5 到弧顶(cx, cy−ay)，u=1 到右侧(cx+ax, cy)。整排 emoji 各差一个 `gap`，master 进度 `p` 0→1 把整排从画面左外推到右外。

## 调参速查

| 想要 | 改哪 |
|---|---|
| 放大倍数 / 怼脸位置 | `tl.set("#person",{scale:1.2})`；`#person{transform-origin}` |
| 弧顶高低 | `ay`（大→弧顶更高、更贴头顶；注意别撞顶部章节标题）|
| 进出画面幅度 | `ax`（大→首尾更靠画面外，进出更干脆）|
| 弧线整体高低 | `cy`（小→整条弧上移）|
| 一排几个 / 疏密 | `count` / `gap`（gap 小→更密集成一条连续带）|
| 流动快慢 | `LOVE.e - LOVE.s`（拉长=更慢更从容）|
| 换表情 | `emoji`（🔥惊艳 / ❤️喜欢 / 👏认可 / 😱震惊）|

## 关键点

- **emoji 居中用 `gsap.set({xPercent:-50,yPercent:-50})`**，位置用 `left/top`（不是 transform）——因为动画里没有对 emoji 做 GSAP transform，两者不冲突；千万别用 CSS `transform: translate(-50%,-50%)` 居中，会和 GSAP 冲突 / StaticGuard 报错。
- **流动用 `proxy + onUpdate`**：把一个 `{p:0}` 对象 tween 到 `{p:1}`，在 `onUpdate` 里按 `p` 重算每个 emoji 的位置。HyperFrames 渲染时逐帧 seek 会触发 onUpdate，所以确定性、可回放。**不要**用 `Math.random()`/`Date`（被禁，破坏确定性）——位置全靠下标和 `p` 算。
- **punch 只放大视频（`#person`），不要放大 `#root`**——否则字幕/进度条/水印也跟着糊。
- 弧顶 `cy − ay` 要留在顶部章节标题（~y140）下方，避免 emoji 压住标题。
```
