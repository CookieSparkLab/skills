# SVG/codebase workflow

Create a self-contained SVG when Pencil is unavailable.

## Required structure

```xml
<svg viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
  <defs>...</defs>
  <g id="connectors">...</g>
  <g id="nodes">...</g>
  <g id="labels">...</g>
</svg>
```

Do not add an opaque full-canvas rectangle. Transparency must remain visible.

## Machine-checkable annotations

Every semantic card group must carry its bounding rectangle:

```xml
<g data-role="node" data-bbox="170,610,700,270">
```

Every connector must record its polyline route, even if the visible path uses rounded curves:

```xml
<path
  data-role="connector"
  data-points="520,520 520,570 470,570 470,610"
  d="M520 520 L520 570 L470 570 L470 610"
/>
```

The validator expands each unrelated node box by the safety gap and checks connector segments against it.

## Text

- Use `<text>` and `<tspan>` rather than foreignObject.
- Set `font-family` with Chinese fallbacks.
- Set explicit font sizes and weights.
- Keep a minimum 24 px internal inset from the node bbox.
- Wrap text manually into short lines.

## Layering

Paint in this order:

1. connectors
2. local masks only when necessary
3. filled node shapes
4. icons
5. text

This prevents lines from appearing through text or translucent cards.

## PNG rendering

Use the runtime's available SVG renderer. Prefer, in order:

1. a project-provided render command
2. an existing browser automation tool
3. `sharp` if already installed
4. platform-native conversion

Do not add a heavy dependency solely to render PNG unless the user approves. The SVG is already a valid image deliverable.

## Validation

Run the bundled validator using its path relative to this Skill:

```bash
node {baseDir}/scripts/validate_svg.mjs diagram.svg
```

Then inspect the rendered SVG. Static checks cannot detect every font-metric or visual collision.
