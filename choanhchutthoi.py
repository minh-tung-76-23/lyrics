import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = True
set_color(COLOR)
# True = tô vàng tên riêng (từ viết hoa giữa câu)
ACCENT = False
set_accent(ACCENT)

# Phát nhạc từ giây thứ START của bài
START = 0.0

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7692991862784724230.mp3'), offset=OFFSET)

LINES = [
    [('Giáng', 0.0), ('sinh', 1.14), ('chẳng', 1.72), ('giống', 2.1), ('giáng', 2.68), ('sinh', 3.34)],
    [('Chỉ', 4.3), ('có', 4.53), ('em', 4.76), ('một', 4.99), ('mình', 5.22)],
    [('Chờ', 5.45), ('anh', 5.78), ('chút', 6.1), ('thôi', 6.42)],
    [('Khi', 6.75), ('mùa', 7.13), ('đông', 7.51), ('vừa', 7.88), ('sang', 8.26)],
    [('Xếp', 8.64), ('lại', 9.28), ('hết', 9.5), ('ngổn', 9.82), ('ngang', 10.36)],
    [('Chờ', 10.76), ('chút', 11.1), ('thôi', 11.6)],
    [('Rồi', 12.44), ('anh', 12.82), ('sẽ', 13.14), ('tìm', 13.44), ('tới', 14.08)],
    [('Chờ', 15.18), ('anh', 15.8), ('chút', 16.06), ('thôi', 16.72)],
    [('Đã', 17.34), ('phiền', 17.74), ('em', 18.12), ('phải', 18.38), ('đợi', 18.82)],
    [('Có', 19.36), ('anh', 19.84), ('ở', 20.06), ('đây', 20.3), ('rồi', 20.62)],
    [('Vẫn', 21.3), ('gần', 21.92), ('em', 22.16), ('thôi', 22.52)],
    [('Dù', 22.98), ('xa', 23.28), ('cách', 23.62), ('khung', 23.88), ('trời ♥️', 24.34)],
]
ENDS = [4.3, 5.45, 6.75, 8.64, 10.76, 12.44, 15.18, 17.34, 19.36, 21.3, 22.98, 25.28]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    # signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play(start=START)

    # Giáng sinh chẳng giống giáng sinh   [xmas: từ "giáng sinh"]
    sync_words(song, LINES[0], ENDS[0], mode='xmas', palette='hong', indent=4)
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.3, breathe, palette='hong', indent=4)
    gradient_fade_out('    ' + text(LINES[0]), 0.25, palette='hong')

    # Chỉ có em một mình   [fadein: từ "một mình"]
    sync_words(song, LINES[1], ENDS[1], mode='fadein', palette='hong', indent=8)
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, breathe, palette='hong', indent=8)
    newline()

    # Chờ anh chút thôi   [letters: từ "chờ"]
    sync_words(song, LINES[2], ENDS[2], mode='letters', palette='tim', indent=4)
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.1, shine, palette='tim', indent=4)
    newline()

    # Khi mùa đông vừa sang   [snow: từ "mùa đông"]
    sync_words(song, LINES[3], ENDS[3], mode='snow', palette='tim', indent=4)
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Xếp lại hết ngổn ngang   [reveal: soft]
    sync_words(song, LINES[4], ENDS[4], mode='reveal', palette='bien', indent=4)
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='bien', indent=4)
    newline()

    # Chờ chút thôi   [center: slow, short, soft]
    sync_words(song, LINES[5], ENDS[5], mode='center', palette='bien', indent=8)
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='bien', indent=8)
    newline()

    # Rồi anh sẽ tìm tới   [glide: bạn chọn]
    sync_words(song, LINES[6], ENDS[6], mode='glide', palette='hoanghon', indent=12)
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.1, shine, palette='hoanghon', indent=12)
    newline()

    # Chờ anh chút thôi   [letters: từ "chờ", slow]
    sync_words(song, LINES[7], ENDS[7], mode='letters', palette='hoanghon', indent=4)
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.1, breathe, palette='hoanghon', indent=4)
    newline()

    # Đã phiền em phải đợi   [wave: đa dạng]
    sync_words(song, LINES[8], ENDS[8], mode='wave', palette='bac', indent=8)
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.1, shine, palette='bac', indent=8)
    newline()

    # Có anh ở đây rồi   [ripple: đa dạng]
    sync_words(song, LINES[9], ENDS[9], mode='ripple', palette='bac', indent=16)
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.1, breathe, palette='bac', indent=16)
    newline()

    # Vẫn gần em thôi   [drop: short]
    sync_words(song, LINES[10], ENDS[10], mode='drop', palette='hong', indent=8)
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.1, shine, palette='hong', indent=8)
    newline()

    # Dù xa cách khung trời   [snow: từ "khung trời"]
    sync_words(song, LINES[11], ENDS[11], mode='snow', palette='hong', indent=4)
    hold(song, text(LINES[11]), ENDS[11] + 1.5, heartbeat, palette='hong', indent=4)
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
