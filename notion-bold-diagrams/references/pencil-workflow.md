# Pencil workflow

1. Call the current-editor state with schema enabled.
2. If no file is open, create a new Pencil file and re-read editor state.
3. Load the presentation/slide guideline when the image is for a deck.
4. Use one 1920×1080 top-level frame with `clip: true`, `placeholder: true`, and transparent fill.
5. Prefer a small number of absolute-positioned major modules. Use layout frames inside modules for text.
6. Build in this order:
   - frame and major regions
   - connectors and arrowheads
   - filled modules
   - text
   - icons and minor decoration
7. Use paths for connectors. Keep each path in a reserved whitespace corridor.
8. Keep relationship captions as separate text nodes with clear space around them.
9. Remove `placeholder` only after the frame is complete.
10. Run `snapshot_layout(..., problemsOnly: true)`.
11. Take a full-frame screenshot and visually inspect:
    - every connector against every text block
    - arrowheads
    - card padding
    - Chinese wrapping
    - contrast on red/yellow fills
12. Update existing nodes to fix issues; do not rebuild the frame.
13. Export the frame as PNG at 2× scale and verify RGBA transparency.
14. Save the `.pen` source without reading or editing it through ordinary filesystem tools.

## Connector safety

For every connector, identify:

- source edge
- target edge
- route corridor
- label zone, if any

If any of those are ambiguous, move modules before drawing the line. Do not repair routing by shrinking text.
