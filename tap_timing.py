"""
tap_timing.py - Gõ phím theo nhạc để đặt mốc thời gian chính xác cho từng câu.

Dùng khi máy dò lời bị lệch (nhạc nền to, whisper không nghe rõ):
    python tap_timing.py input/mp3/bai.mp3 input/lyric.txt              # bấm cho tất cả các câu
    python tap_timing.py input/mp3/bai.mp3 input/lyric.txt --only 2-4   # chỉ bấm câu 2, 3, 4
    python tap_timing.py input/mp3/bai.mp3 input/lyric.txt --start 60   # phát nhạc từ giây 60

Cách bấm: nhạc phát -> câu sắp tới hiện trên màn hình -> nhấn ENTER đúng lúc ca sĩ BẮT ĐẦU hát câu đó.
    Enter        : đánh dấu câu bắt đầu
    s + Enter    : bỏ qua câu này (giữ mốc máy dò)
    q + Enter    : dừng và lưu những câu đã bấm

Xong sẽ ghi [@giây] vào đầu các câu trong lyric.txt (có sao lưu lyric.txt.bak), rồi chạy:
    python make_lyrics.py input/mp3/bai.mp3 input/lyric.txt -o tenbai.py --reuse
"""
import argparse
import os
import re
import shutil
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

SKIP_RE = re.compile(r"^\s*(-v\d+-|\[clear\])\s*$", re.I)
AT_RE = re.compile(r"\[@\d+(?:\.\d+)?\]\s*")


def lyric_lines(raw):
    """Vị trí (số dòng trong file) và chữ của từng câu hát - bỏ dòng trống, [clear], -V2-."""
    out = []
    for n, ln in enumerate(raw):
        if not ln.strip() or SKIP_RE.match(ln):
            continue
        text = re.sub(r"\[[^\]]*\]|~", "", ln).strip()
        out.append((n, text))
    return out


def parse_only(spec, total):
    if not spec:
        return set(range(1, total + 1))
    pick = set()
    for part in spec.split(","):
        if "-" in part:
            a, b = part.split("-")
            pick |= set(range(int(a), int(b) + 1))
        else:
            pick.add(int(part))
    return pick


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mp3")
    ap.add_argument("lyrics")
    ap.add_argument("--only", help="chỉ bấm các câu này, vd 2-4 hoặc 1,3,5")
    ap.add_argument("--start", type=float, default=0.0, help="phát nhạc từ giây này")
    ap.add_argument("--react", type=float, default=0.15,
                    help="trừ thời gian phản xạ khi bấm (giây, mặc định 0.15)")
    a = ap.parse_args()

    raw = open(a.lyrics, encoding="utf-8").read().split("\n")
    lines = lyric_lines(raw)
    pick = parse_only(a.only, len(lines))

    os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")
    from animation_plus import Song
    song = Song(a.mp3)

    print("\nNhấn ENTER đúng lúc ca sĩ BẮT ĐẦU hát câu hiện trên màn hình.")
    print("  s + Enter = bỏ qua câu   |   q + Enter = dừng và lưu\n")
    input("Sẵn sàng thì nhấn Enter để phát nhạc...")
    for k in (3, 2, 1):
        print(f"  {k}...", flush=True)
        time.sleep(0.6)
    song.play(start=a.start)

    marks = {}
    for idx, (n, text) in enumerate(lines, 1):
        if idx not in pick:
            continue
        cmd = input(f"\n  câu {idx:>2}: {text}\n  -> Enter khi bắt đầu hát ").strip().lower()
        t = round(max(0.0, song.t() - a.react), 2)
        if cmd == "q":
            break
        if cmd == "s":
            print("     (bỏ qua)")
            continue
        marks[n] = t
        print(f"     ✓ {t:.2f}s")

    song._pg.mixer.music.stop()
    if not marks:
        print("\nKhông có câu nào được đánh dấu, lyric.txt giữ nguyên.")
        return

    shutil.copy(a.lyrics, a.lyrics + ".bak")
    for n, t in marks.items():
        ln = raw[n]
        body = AT_RE.sub("", ln)
        ind = body[:len(body) - len(body.lstrip())]
        raw[n] = f"{ind}[@{t:.2f}] {body.lstrip()}"
    open(a.lyrics, "w", encoding="utf-8").write("\n".join(raw))
    print(f"\nĐã ghi mốc cho {len(marks)} câu vào {a.lyrics} (bản cũ: {a.lyrics}.bak)")
    print("Giờ sinh lại file bài:")
    print(f"  .venv/bin/python make_lyrics.py {a.mp3} {a.lyrics} -o <tenbai>.py --reuse")


if __name__ == "__main__":
    main()
