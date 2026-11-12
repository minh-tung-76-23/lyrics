import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = True
set_color(COLOR)

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7702804085438762261.mp3'), offset=OFFSET)

LINES = [
    [('Là-là-là-là', 0.0)],
    [('Lần', 0.74), ('người', 0.78), ('nói', 1.02), ('rằng', 1.36)],
    [('tình', 1.7), ('yêu', 1.94), ('này', 2.26), ('chẳng', 2.5), ('phai', 2.9)],
    [('Là-là-là-là', 3.3)],
    [('Lần', 4.14), ('người', 4.32), ('nói', 4.62)],
    [('chẳng', 4.92), ('phải', 5.26), ('anh', 5.52), ('thì', 5.82), ('chẳng', 6.14), ('ai', 6.68)],
    [('Để', 6.96), ('giờ', 7.14), ('này', 7.28), ('tình', 7.44), ('mình', 7.68)],
    [('đành', 7.92), ('vỡ', 8.22), ('tan', 8.5)],
    [('đành', 8.82), ('lỡ', 9.08), ('làng', 9.46)],
    [('đành', 9.8), ('dở', 9.98), ('dang', 10.34)],
    [('Anh', 10.6), ('ngỡ', 10.9), ('ngàng', 11.16)],
    [('để', 11.52), ('giờ', 11.74), ('đây', 12.1), ('đường', 12.4), ('về', 12.7), ('ta', 13.0), ('rẽ', 13.36), ('ngang', 13.92)],
    [('Từng', 14.38), ('ngày', 14.52), ('anh', 14.76), ('vẫn', 14.94), ('bên', 15.16), ('em,', 15.56)],
    [('Thế', 15.84), ('nhưng', 16.48), ('em', 16.68), ('vương', 17.04), ('vấn', 17.24), ('điều', 17.42), ('gì?', 17.62)],
    [('Tình', 17.98), ('yêu', 18.28), ('bấy', 18.68), ('lâu', 18.82), ('nay', 18.98)],
    [('Có', 19.36), ('khiến', 19.64), ('em', 19.96), ('thôi', 20.12), ('ngừng', 20.38), ('nghĩ', 20.58), ('suy?', 21.0)],
    [('Mỗi', 21.72), ('đêm', 22.1), ('mình', 22.3), ('anh', 22.76), ('u', 23.21), ('hoài,', 23.21)],
    [('nên', 23.36), ('dừng', 23.64), ('lại', 23.94), ('hay', 24.26), ('yêu', 24.6), ('chẳng', 24.76), ('ngần', 25.08), ('ngại?', 25.38)],
    [('Và', 26.04), ('anh', 26.34), ('cũng', 26.6), ('biết', 26.88), ('đau', 27.0), ('khi', 27.26), ('em', 27.5), ('nhạt', 27.74), ('phai', 28.26)],
    [('Chờ', 28.7), ('bao', 29.18), ('tháng', 29.32), ('năm', 29.6), ('qua', 29.82)],
    [('Vẫn', 30.51), ('mong', 30.82), ('bao', 31.06), ('yêu', 31.47), ('dấu', 31.57), ('quay', 31.66), ('lại', 32.04)],
    [('Đành', 32.32), ('buông', 32.64), ('cánh', 32.96), ('tay', 33.12), ('em', 33.28)],
    [('Khi', 33.72), ('trái', 33.96), ('tim', 34.18), ('em', 34.48), ('chẳng', 34.72), ('có', 34.98), ('anh', 35.58)],
    [('Biết', 36.08), ('đâu', 36.48), ('em', 36.6), ('cũng', 36.9), ('chấp', 37.1), ('nhận', 37.36)],
    [('không', 37.88), ('ân', 38.04), ('hận', 38.28), ('Một', 38.6), ('lần', 38.96), ('khóc', 39.16), ('cho', 39.56), ('em', 40.06)],
    [('Và', 40.4), ('quên', 40.4), ('đi', 40.9), ('tháng', 41.16), ('năm', 41.4), ('ta', 41.58), ('từng', 41.9), ('đậm', 42.22), ('sâu...', 42.66)],
]
ENDS = [0.74, 1.7, 3.3, 4.14, 4.92, 6.96, 7.92, 8.82, 9.8, 10.6, 11.52, 14.24, 15.84, 17.98, 19.36, 21.72, 23.36, 26.04, 28.7, 30.2, 32.32, 33.72, 36.08, 37.68, 40.4, 43.7]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play()

    # Là-là-là-là
    sync_words(song, LINES[0], ENDS[0], mode='karaoke', palette='hong', indent=12)
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.1, shine, palette='hong', indent=12)
    newline()

    # Lần người nói rằng
    sync_words(song, LINES[1], ENDS[1], mode='bounce', palette='hong')
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, breathe, palette='hong')
    newline()

    # tình yêu này chẳng phai
    sync_words(song, LINES[2], ENDS[2], mode='slide', palette='tim', indent=8)
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.1, shine, palette='tim', indent=8)
    newline()

    # Là-là-là-là
    sync_words(song, LINES[3], ENDS[3], mode='reveal', palette='tim', indent=12)
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim', indent=12)
    newline()

    # Lần người nói
    sync_words(song, LINES[4], ENDS[4], mode='jump', palette='bien')
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='bien')
    newline()

    # chẳng phải anh thì chẳng ai
    sync_words(song, LINES[5], ENDS[5], mode='scramble', palette='bien', indent=8)
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='bien', indent=8)
    newline()

    # Để giờ này tình mình
    sync_words(song, LINES[6], ENDS[6], mode='drop', palette='hoanghon')
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.1, shine, palette='hoanghon')
    newline()

    # đành vỡ tan
    sync_words(song, LINES[7], ENDS[7], mode='wave', palette='hoanghon', indent=4)
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.1, breathe, palette='hoanghon', indent=4)
    newline()

    # đành lỡ làng
    sync_words(song, LINES[8], ENDS[8], mode='converge', palette='bac', indent=8)
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.1, shine, palette='bac', indent=8)
    newline()

    # đành dở dang
    sync_words(song, LINES[9], ENDS[9], mode='typewriter', palette='bac', indent=12)
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.1, breathe, palette='bac', indent=12)
    newline()

    # Anh ngỡ ngàng
    sync_words(song, LINES[10], ENDS[10], mode='rise', palette='hong')
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.1, shine, palette='hong')
    newline()

    # để giờ đây đường về ta rẽ ngang
    sync_words(song, LINES[11], ENDS[11], mode='pop', palette='hong', indent=4)
    hold(song, text(LINES[11]), LINES[12][0][1] - 0.1, breathe, palette='hong', indent=4)
    newline()

    newline()  # hết đoạn

    # Từng ngày anh vẫn bên em,
    sync_words(song, LINES[12], ENDS[12], mode='rainbow', palette='bien')
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.1, shine, palette='bien')
    newline()

    # Thế nhưng  em vương vấn điều gì?
    sync_words(song, LINES[13], ENDS[13], mode='flicker', palette='bien')
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.1, breathe, palette='bien')
    newline()

    # Tình yêu bấy lâu nay
    sync_words(song, LINES[14], ENDS[14], mode='karaoke', palette='hoanghon', indent=4)
    hold(song, text(LINES[14]), LINES[15][0][1] - 0.1, shine, palette='hoanghon', indent=4)
    newline()

    # Có khiến em thôi ngừng nghĩ suy?
    sync_words(song, LINES[15], ENDS[15], mode='bounce', palette='hoanghon')
    hold(song, text(LINES[15]), LINES[16][0][1] - 0.1, breathe, palette='hoanghon')
    newline()

    # Mỗi đêm mình anh u hoài,
    sync_words(song, LINES[16], ENDS[16], mode='slide', palette='bac')
    hold(song, text(LINES[16]), LINES[17][0][1] - 0.1, shine, palette='bac')
    newline()

    # nên dừng lại  hay yêu chẳng ngần ngại?
    sync_words(song, LINES[17], ENDS[17], mode='reveal', palette='bac', indent=4)
    hold(song, text(LINES[17]), LINES[18][0][1] - 0.1, breathe, palette='bac', indent=4)
    newline()

    # Và anh  cũng biết đau khi em nhạt phai
    sync_words(song, LINES[18], ENDS[18], mode='jump', palette='hong')
    hold(song, text(LINES[18]), LINES[19][0][1] - 0.1, shine, palette='hong')
    newline()

    # Chờ bao tháng năm qua
    sync_words(song, LINES[19], ENDS[19], mode='scramble', palette='hong')
    hold(song, text(LINES[19]), LINES[20][0][1] - 0.1, breathe, palette='hong')
    newline()

    # Vẫn mong  bao yêu dấu quay lại
    sync_words(song, LINES[20], ENDS[20], mode='drop', palette='tim', indent=4)
    hold(song, text(LINES[20]), LINES[21][0][1] - 0.1, shine, palette='tim', indent=4)
    newline()

    # Đành buông cánh tay em
    sync_words(song, LINES[21], ENDS[21], mode='wave', palette='tim')
    hold(song, text(LINES[21]), LINES[22][0][1] - 0.1, breathe, palette='tim')
    newline()

    # Khi trái tim em chẳng có anh
    sync_words(song, LINES[22], ENDS[22], mode='converge', palette='bien', indent=4)
    hold(song, text(LINES[22]), LINES[23][0][1] - 0.1, shine, palette='bien', indent=4)
    newline()

    # Biết đâu em cũng chấp nhận
    sync_words(song, LINES[23], ENDS[23], mode='typewriter', palette='bien')
    hold(song, text(LINES[23]), LINES[24][0][1] - 0.1, breathe, palette='bien')
    newline()

    # không ân hận  Một lần khóc cho em
    sync_words(song, LINES[24], ENDS[24], mode='rise', palette='hoanghon', indent=8)
    hold(song, text(LINES[24]), LINES[25][0][1] - 0.1, shine, palette='hoanghon', indent=8)
    newline()

    # Và quên  đi tháng năm ta từng đậm sâu...
    sync_words(song, LINES[25], ENDS[25], mode='pop', palette='hoanghon')
    hold(song, text(LINES[25]), ENDS[25] + 1.5, heartbeat, palette='hoanghon')
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
