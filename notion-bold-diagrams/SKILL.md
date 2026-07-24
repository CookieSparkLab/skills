---
name: notion-bold-diagrams
description: Create editable or code-native conceptual diagrams in a colorful Notion-like bold-outline style with transparent backgrounds. Use when the user asks to 画关系图, 流程图, 框架图, 概念图, 信息图, PPT 配图, 可视化一段内容, or requests thick black lines, pastel color blocks, hand-drawn character, Pencil output, SVG, or transparent PNG. Prefer Pencil when its editor connector is available; otherwise generate a self-contained SVG in the codebase and optionally render PNG.
---

# Notion Bold Diagrams

Turn one idea into one readable diagram. Preserve meaning before decoration.

## Output routing

1. If the user explicitly names Pencil, use Pencil.
2. Otherwise inspect available tools:
   - If Pencil is connected, create an editable `.pen` frame and export transparent PNG.
   - If Pencil is unavailable, create a self-contained SVG in the codebase. Render PNG only when a renderer is available or the user requests it.
3. Never block merely because Pencil is absent.
4. Save the final source plus a preview/export when the runtime permits.

Read the relevant path before drawing:

- Pencil: [references/pencil-workflow.md](references/pencil-workflow.md)
- SVG/codebase: [references/svg-workflow.md](references/svg-workflow.md)
- Visual language: [references/style-spec.md](references/style-spec.md)

## Workflow

1. Extract the single takeaway.
2. Convert the content into 3–7 semantic nodes.
3. Choose the structure: `flow`, `hub`, `comparison`, `layers`, `equation`, or `cards`.
4. Write a short drawing spec before creating nodes:
   - takeaway
   - node labels
   - directed relationships
   - aspect ratio
   - output route
5. Draw structure first, then connectors, then boxes, then text and icons.
6. Validate layout and visual fidelity.
7. Export and report source and preview paths.

Do not ask about choices that do not materially affect the diagram. If the content and destination imply a reasonable default, proceed.

## Hard layout constraints

Treat these as release blockers:

- No connector, arrow, icon, border, or decoration may cross text.
- Reserve a text-safe inset of at least 24 px inside every card at 1920×1080.
- Keep connectors at least 18 px away from text bounds and at least 12 px from unrelated cards.
- Route connectors through explicit whitespace channels; prefer orthogonal or simple curved paths.
- Attach connectors only to card edges or dedicated ports, never to text.
- Draw connectors behind opaque or filled nodes; draw text last.
- Place relationship labels in dedicated gaps, never on top of connector strokes.
- Do not place a label between two lines closer than 28 px.
- Keep at least 40 px vertical and 32 px horizontal gap between sibling modules.
- No clipped text, overflowing cards, hidden arrowheads, or low-contrast labels.
- If the content does not fit at readable sizes, remove detail or split the image. Never shrink body text below 24 px on a 1920×1080 slide.

After drawing, inspect the actual rendered result at least once. Structural validation alone is insufficient.

## Style invariants

- Transparent canvas by default.
- Near-black outlines and text: `#111111`.
- Thick outlines: 6–8 px at 1920×1080.
- Soft colored blocks: pink, blue, mint, red, and warm yellow.
- Squared or lightly rounded cards; corner radius 6–12 px.
- Heavy Chinese sans-serif headings; compact supporting copy.
- Simple solid icons with consistent visual weight.
- Slight human irregularity may appear in arrows or underlines, but alignment remains intentional.
- Use color to distinguish roles, not as decoration.
- Avoid gradients, glassmorphism, glossy 3D, neon, thin gray UI lines, excessive shadows, and cute character mascots.

This is an original style system. Do not copy named creators' prompt text, layouts, or proprietary visual assets.

## Content density

- Title: optional, 40–64 px.
- Node heading: 32–44 px.
- Supporting copy: 24–30 px.
- One node: one heading plus at most three short bullets.
- Prefer phrases over sentences.
- Preserve the user's terminology exactly when labels are important.

## Pencil completion check

- Run the Pencil layout-problem check.
- Inspect a screenshot of the whole frame.
- Confirm the frame fill is transparent.
- Confirm no line/text overlap visually.
- Export PNG with alpha and retain the editable `.pen`.

## SVG completion check

- Annotate node groups with `data-role="node"` and `data-bbox="x,y,w,h"`.
- Annotate connector paths with `data-role="connector"` and `data-points="x,y x,y ..."`.
- Keep connectors earlier than nodes and text in SVG paint order.
- Run:

```bash
node scripts/validate_svg.mjs path/to/diagram.svg
```

- Open or render the SVG and inspect it visually.
- Fix every reported overlap before delivery.

## Final response

Report:

- chosen route: Pencil or SVG
- editable/source file
- exported image if created
- validation performed
- any real limitation
