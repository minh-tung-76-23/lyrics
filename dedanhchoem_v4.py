import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = True
set_color(COLOR)

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7668311562884730119.mp3'), offset=OFFSET)

LINES = [
    [('Một', 0.0), ('phần', 0.78), ('chỉ', 1.1), ('sợ', 1.48), ('đau', 2.12), ('nữa', 2.78), ('thôi', 3.4)],
    [('Phần', 4.34), ('kia', 4.76), ('lại', 5.12), ('muốn', 5.42), ('cô', 5.74), ('này', 6.14), ('phải', 6.4), ('là', 6.74), ('của', 7.06), ('tôi', 7.44)],
    [('Chơi', 8.46), ('bời', 9.06), ('chán', 9.38), ('chưa', 9.7), ('anh', 10.08), ('muốn', 10.38), ('đi', 10.68), ('đường', 11.06), ('dài?', 11.36)],
    [('Đứng', 12.8), ('đây', 13.06), ('ngóng', 13.28), ('em', 13.72), ('đón', 13.96), ('anh', 14.3), ('về', 14.6), ('tương', 14.9), ('lai', 15.32)],
    [('Đều', 15.62), ('là', 15.92), ('để', 16.26), ('dành', 16.62), ('cho', 16.84), ('em', 17.4)],
    [('Để', 19.96), ('dành', 20.64), ('cho', 20.88), ('em', 21.34)],
]
ENDS = [4.34, 8.46, 12.34, 15.62, 18.0, 22.96]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play()

    # Một phần chỉ sợ đau nữa thôi
    sync_words(song, LINES[0], ENDS[0], mode='karaoke', palette='hong', indent=4)
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.1, shine, palette='hong', indent=4)
    newline()

    newline()  # hết đoạn

    # Phần kia lại muốn cô này phải là của tôi
    sync_words(song, LINES[1], ENDS[1], mode='bounce', palette='tim')
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, breathe, palette='tim')
    newline()

    newline()  # hết đoạn

    # Chơi bời chán chưa anh muốn đi đường dài?
    sync_words(song, LINES[2], ENDS[2], mode='typo', palette='hoanghon')
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.1, shine, palette='hoanghon')
    newline()

    newline()  # hết đoạn

    # Đứng đây ngóng em đón anh về tương lai
    sync_words(song, LINES[3], ENDS[3], mode='sparkle', palette='bac')
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='bac')
    newline()

    newline()  # hết đoạn

    # Đều là để dành cho em
    sync_words(song, LINES[4], ENDS[4], mode='words', palette='tim', indent=7)
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='tim', indent=7)
    newline()

    newline()  # hết đoạn

    # Để dành cho em
    sync_words(song, LINES[5], ENDS[5], mode='jump', palette='bien', indent=9)
    trailing_dots(song, text(LINES[5]), ENDS[5] + 3.0, palette='bien', indent=9)
    hold(song, text(LINES[5]) + '...', ENDS[5] + 4.5, heartbeat, palette='bien', indent=9)
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
