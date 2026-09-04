# 7 种版式原型

排一页之前先选原型。**选原型就是选容量** —— 定了原型，这页能放多少字就定了。

画布 1920×1080，内容框 1740 × 874。下面每种都标了实测容量，超了就删内容，别缩字号。

---

## 1 · 封面

整页居中。一个标签 + 一个大标题，最多再加一行副标题。

**容量**：标题最多两行，每行不超过 10 个汉字。

```html
<section class="slide">
  <div class="slide-inner center">
    <div class="swatches">
      <i style="background:var(--coral)"></i><i style="background:var(--blue)"></i>
      <i style="background:var(--sage)"></i><i style="background:var(--mint)"></i>
    </div>
    <div class="reveal d1 mb-5">
      <span class="pill blue" style="font-family:var(--font);font-size:44px;font-weight:700;letter-spacing:0;border-width:4px;padding:8px 24px;box-shadow:var(--sh)">
        系列名 · 副标题位
      </span>
    </div>
    <h1 class="t-display reveal d2" style="font-size:176px;line-height:1.08">
      这里写标题<br>可以换行
    </h1>
  </div>
</section>
```

---

## 2 · 标题 + N 张卡（最常用）

顶部标签和大标题，下面一行 2 到 3 张卡，底部一句结论。

**容量**：三卡并排每张宽 556px，卡内一行约 14 个汉字，正文别超过 4 行。
两卡并排每张宽 852px，一行约 23 个汉字。

**动画**：标题 `reveal`，每张卡各包一个 `step`，结论句是最后一个 `step`。

```html
<section class="slide">
  <div class="slide-inner">
    <div class="reveal d1">
      <span class="pill pink mb-3">01 · SECTION</span>
      <h2 class="t-section mb-5">这一页在讲<em>什么</em>？</h2>
    </div>

    <div class="row grow">
      <div class="step grow"><div class="card stretch">
        <h3 class="t-subhead-md mb-2">卡片标题</h3>
        <p class="t-body wrap-cn">一句话说清主要意思。</p>
        <p class="note mt-2">次要说明放这里，灰字加左竖线。</p>
      </div></div>
      <div class="step grow"><div class="card blue stretch">…</div></div>
      <div class="step grow"><div class="card coral stretch">…</div></div>
    </div>

    <div class="step mt-5">
      <p class="t-subhead-md" style="text-align:center">这一页想让观众记住的就是这一句。</p>
    </div>
  </div>
</section>
```

---

## 3 · 双栏对比

左右各一张卡，各带一个列表。适合「A 负责什么 / B 负责什么」。

**容量**：每栏最多 6 到 8 条，**每条一行写完**。超了就合并或者删。

```html
<div class="row grow">
  <div class="step grow"><div class="card stretch">
    <p class="t-subhead-lg mb-4" style="text-align:center;color:var(--ink);border-bottom:1.5px solid rgba(14,14,14,.25);padding-bottom:24px">左边负责</p>
    <ul class="list">
      <li>第一条</li>
      <li><strong>要加粗的重点</strong></li>
    </ul>
  </div></div>
  <div class="step grow"><div class="card blue stretch">…</div></div>
</div>
```

---

## 4 · 编号列表 / 清单

一行一条，每条是一张横排矮卡：左边一个编号标签，右边一句话。

**容量**：最多 5 行（含结论行）。每行的话不超过 20 个汉字。

```html
<div class="col grow" style="gap:16px">
  <div class="step"><div class="card h tight">
    <span class="pill">Q1</span>
    <h3 class="t-subhead-md">这件事你会反复做吗？</h3>
  </div></div>
  <div class="step"><div class="card h tight">…</div></div>
  <div class="step mt-2"><div class="card sage h tight">
    <span class="t-cardtitle" style="font-size:40px;line-height:1">✓</span>
    <h3 class="t-subhead-md">三个都是，那就值得做</h3>
  </div></div>
</div>
```

---

## 5 · 大字过场 / 休息页

整页居中。标签 + 巨大标题 + 副标题，下面可选三张小卡说明要做什么。

**容量**：标题一行，不超过 8 个汉字。小卡固定 460px 宽，最多三张。

```html
<div class="slide-inner center">
  <div class="reveal d1 mb-4"><span class="pill pink">BREAK · 10 MIN</span></div>
  <h1 class="t-title reveal d2 mb-3" style="font-size:132px">动手环节</h1>
  <p class="t-subhead-lg reveal d3 mb-6">先做起来，做完再回来</p>
  <div class="row" style="flex-wrap:wrap;justify-content:center;gap:30px;max-width:1700px">
    <div class="step"><div class="card tight" style="width:460px;text-align:left">
      <h3 class="t-subhead-md mb-2">1. 第一步</h3>
      <p class="t-body-sm wrap-cn">一句话说清</p>
    </div></div>
  </div>
</div>
```

---

## 6 · 单卡通栏（长内容 / 截图）

一整张大卡占满内容区。适合放一段完整的示例文本、一张截图、一张流程图。

**容量**：一行最多 30 个汉字（再长不好读），总共不超过 12 行。
放图片就用 3px 黑边 + 硬阴影，**不要圆角**。

```html
<div class="reveal d2 grow" style="display:flex">
  <div class="card stretch">
    <h3 class="t-subhead-md mb-3">示例</h3>
    <p class="t-body wrap-cn">正文…</p>
    <img src="xxx.png" alt="" style="width:100%;border:3px solid var(--ink);box-shadow:var(--sh-lg);margin-top:24px">
  </div>
</div>
```

---

## 7 · 收尾页 / Q&A

和封面同构：整页居中，一个大标题 + 一行副标题，可以再加一个标签。
**别在收尾页塞信息**，它的作用是给个停顿。

```html
<div class="slide-inner center">
  <h1 class="t-title reveal d1 mb-4" style="font-size:132px">谢谢</h1>
  <p class="t-subhead-lg reveal d2">有什么想问的？</p>
</div>
```

---

## 选不下去的时候

- 内容是**并列的几件事** → 原型 2（标题 + N 卡）
- 内容是**两方对照** → 原型 3（双栏）
- 内容是**有先后的步骤或判断** → 原型 4（编号列表）
- 内容是**一整段不好拆的东西** → 原型 6（单卡通栏）
- 只是想让节奏喘口气 → 原型 5（大字过场）

**一页只讲一件事。** 一页想讲两件事，就拆成两页。
