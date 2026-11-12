import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/2aOboRC8R0NecE8leGk6QdvysjioGd8AaVTd2deq.mp3'), offset=OFFSET)

LINES = [
    [('Là-là-là-là', 0.0), ('lần', 0.68), ('người', 0.8), ('nói', 1.02)],
    [('rằng', 1.3), ('tình', 1.66), ('yêu', 1.88), ('này', 2.2), ('chẳng', 2.44), ('phai', 2.84)],
    [('Là-là-là-là', 3.28), ('lần', 4.08), ('người', 4.28), ('nói', 4.58)],
    [('chẳng', 4.86), ('phải', 5.24), ('anh', 5.46), ('thì', 5.78), ('chẳng', 6.1), ('ai', 6.68)],
    [('Để', 6.92), ('giờ', 7.08), ('này', 7.24), ('tình', 7.4), ('mình', 7.64)],
    [('đành', 7.88), ('vỡ', 8.18), ('tan', 8.46)],
    [('đành', 8.74), ('lỡ', 9.0), ('làng', 9.38)],
    [('đành', 9.74), ('dở', 9.92), ('dang', 10.28)],
    [('Anh', 10.56), ('ngỡ', 10.82), ('ngàng', 11.14), ('để', 11.48), ('giờ', 11.7), ('đây', 12.08)],
    [('đường', 12.36), ('về', 12.6), ('ta', 12.94), ('rẽ', 13.3), ('ngang', 13.84)],
]
ENDS = [1.3, 3.28, 4.86, 6.92, 7.88, 8.74, 9.74, 10.56, 12.36, 14.18]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play()

    # Là-là-là-là lần người nói
    sync_words(song, LINES[0], ENDS[0], mode='karaoke', palette='hong')
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.1, shine, palette='hong')
    newline()

    # rằng tình yêu này chẳng phai
    sync_words(song, LINES[1], ENDS[1], mode='bounce', palette='hong', indent=24)
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, breathe, palette='hong', indent=24)
    newline()

    # Là-là-là-là lần người nói
    sync_words(song, LINES[2], ENDS[2], mode='slide', palette='tim')
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.1, shine, palette='tim')
    newline()

    # chẳng phải anh thì chẳng ai
    sync_words(song, LINES[3], ENDS[3], mode='reveal', palette='tim', indent=24)
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim', indent=24)
    newline()

    # Để giờ này tình mình
    sync_words(song, LINES[4], ENDS[4], mode='jump', palette='bien')
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='bien')
    newline()

    # đành vỡ tan
    sync_words(song, LINES[5], ENDS[5], mode='scramble', palette='bien', indent=4)
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='bien', indent=4)
    newline()

    # đành lỡ làng
    sync_words(song, LINES[6], ENDS[6], mode='drop', palette='hoanghon', indent=8)
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.1, shine, palette='hoanghon', indent=8)
    newline()

    # đành dở dang
    sync_words(song, LINES[7], ENDS[7], mode='wave', palette='hoanghon', indent=12)
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.1, breathe, palette='hoanghon', indent=12)
    newline()

    # Anh ngỡ ngàng để giờ đây
    sync_words(song, LINES[8], ENDS[8], mode='converge', palette='bac')
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.1, shine, palette='bac')
    newline()

    # đường về ta rẽ ngang
    sync_words(song, LINES[9], ENDS[9], mode='typewriter', palette='bac', indent=16)
    hold(song, text(LINES[9]), ENDS[9] + 1.5, heartbeat, palette='bac', indent=16)
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
