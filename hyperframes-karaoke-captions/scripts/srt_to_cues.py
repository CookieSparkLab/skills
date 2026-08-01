#!/usr/bin/env python3
"""把 SRT 字幕转成逐词高亮字幕用的 CUES 数组。

用法:
    python3 srt_to_cues.py 你的.srt                # 打印全部 CUES
    python3 srt_to_cues.py 你的.srt --end 30       # 只要 0~30 秒
    python3 srt_to_cues.py 你的.srt --start 48 --end 108   # 截取一段
    python3 srt_to_cues.py 你的.srt --offset -48   # 整体时间平移(截取后归零常用)

输出形如:
    const CUES = [
      [0.066, 1.500, "我最近一周都在跟我"],
      ...
    ];
直接粘进 HyperFrames 合成的 <script>。文字保持 SRT 原样(含原有空格)。
SRT 里乱序的行会按开始时间自动排序;跨行的一条字幕会用空格拼接。
"""
import argparse, re, sys

TS = re.compile(r"(\d{2}):(\d{2}):(\d{2})[,.](\d{3})")


def to_sec(h, m, s, ms):
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000.0


def parse_srt(text):
    cues = []
    # 按空行分块
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = [l for l in block.splitlines() if l.strip() != ""]
        if not lines:
            continue
        # 找含时间轴的那一行(通常第 2 行;第 1 行是序号)
        ts_idx = next((i for i, l in enumerate(lines) if "-->" in l), None)
        if ts_idx is None:
            continue
        m = TS.findall(lines[ts_idx])
        if len(m) < 2:
            continue
        start = to_sec(*m[0])
        end = to_sec(*m[1])
        text_lines = lines[ts_idx + 1:]
        cue_text = " ".join(t.strip() for t in text_lines).strip()
        if cue_text:
            cues.append((start, end, cue_text))
    cues.sort(key=lambda c: c[0])
    return cues


def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("srt")
    ap.add_argument("--start", type=float, default=0.0, help="截取起点(秒),默认0")
    ap.add_argument("--end", type=float, default=None, help="截取终点(秒),默认到结尾")
    ap.add_argument("--offset", type=float, default=None,
                    help="整体时间平移(秒)。不填时:若 --start>0 会自动减去 start 归零")
    args = ap.parse_args()

    with open(args.srt, encoding="utf-8-sig") as f:
        cues = parse_srt(f.read())

    lo, hi = args.start, (args.end if args.end is not None else float("inf"))
    sel = [(s, e, t) for (s, e, t) in cues if e > lo and s < hi]

    offset = args.offset if args.offset is not None else (-args.start if args.start else 0.0)

    print("const CUES = [")
    for s, e, t in sel:
        s2 = max(0.0, s + offset)
        e2 = e + offset
        if args.end is not None:
            e2 = min(e2, hi + offset)
        print(f'  [{s2:.3f}, {e2:.3f}, "{esc(t)}"],')
    print("];")
    print(f"// {len(sel)} 条  (来自 {args.srt})", file=sys.stderr)


if __name__ == "__main__":
    main()
