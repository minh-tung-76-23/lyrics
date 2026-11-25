import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = False
set_color(COLOR)
# True = tô vàng tên riêng (từ viết hoa giữa câu)
ACCENT = False
set_accent(ACCENT)

# Phát nhạc từ giây thứ START của bài
START = 0.0

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7710954743228648725.mp3'), offset=OFFSET)

LINES = [
    [('Vết', 0.45), ('thương', 0.75), ('này', 1.0), ('sao', 1.2)],
    [('Lại', 1.52), ('đau', 1.9), ('đến', 2.32), ('thế', 2.88)],
    [('Những', 3.8), ('kỷ', 4.3), ('niệm', 4.64), ('xưa', 5.0)],
    [('Chìm', 5.3), ('trong', 5.7), ('nước', 6.08), ('mắt', 6.58)],
    [('Anh', 8.3), ('mất', 8.64), ('em', 8.94), ('rồi', 9.34)],
    [('Xem', 10.2), ('như', 10.5), ('tình', 10.74), ('ta', 11.22), ('chẳng', 11.7), ('may', 12.48)],
    [('Và', 15.55), ('có', 15.88), ('lẽ', 16.2), ('tim', 16.62), ('em', 16.96)],
    [('Giờ', 17.74), ('đây', 18.1), ('cũng', 18.88), ('đã', 19.26), ('mệt', 19.96), ('rồi', 20.36), ('💔', 21.1)],
]
ENDS = [1.52, 3.8, 5.3, 8.0, 9.94, 13.98, 17.74, 21.4]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    # signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play(start=START)

    # Vết thương này sao   [drop: short]
    sync_words(song, LINES[0], ENDS[0], mode='drop', palette='hong')
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.1, breathe, palette='hong')
    newline()

    # Lại đau đến thế   [fadein: slow]
    sync_words(song, LINES[1], ENDS[1], mode='fadein', palette='hong', indent=4)
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, breathe, palette='hong', indent=4)
    newline()

    # Những kỷ niệm xưa   [mist: từ "kỷ niệm"]
    sync_words(song, LINES[2], ENDS[2], mode='mist', palette='tim')
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.1, shine, palette='tim')
    newline()

    # Chìm trong nước mắt   [drop: từ "nước mắt", short]
    sync_words(song, LINES[3], ENDS[3], mode='drop', palette='tim', indent=4)
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Anh mất em rồi   [center: short]
    sync_words(song, LINES[4], ENDS[4], mode='center', palette='bien', indent=4)
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='bien', indent=4)
    newline()

    # Xem như tình ta chẳng may   [letters: slow, long]
    sync_words(song, LINES[5], ENDS[5], mode='letters', palette='bien')
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='bien')
    newline()

    # Và có lẽ tim em   [reveal: soft]
    sync_words(song, LINES[6], ENDS[6], mode='reveal', palette='hoanghon', indent=4)
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.1, heartbeat, palette='hoanghon', indent=4)
    newline()

    # Giờ đây cũng đã mệt rồi 💔   [spotlight: slow, long, soft]
    sync_words(song, LINES[7], ENDS[7], mode='spotlight', palette='hoanghon', indent=8)
    hold(song, text(LINES[7]), ENDS[7] + 1.5, heartbeat, palette='hoanghon', indent=8)
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
