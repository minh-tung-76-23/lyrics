import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = False
set_color(COLOR)

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7707693466595167489.mp3'), offset=OFFSET)

LINES = [
    [('Người', 0.7), ('ta', 1.38), ('thường', 1.7), ('nói', 2.04)],
    [('Khi', 2.5), ('yêu', 2.86), ('đời', 3.2), ('thật', 3.52), ('nên', 3.74), ('thơ,', 4.08)],
    [('Vì', 5.68), ('say', 5.94), ('màu', 6.24), ('mắt', 6.72), ('nhau', 7.1)],
    [('Nên', 7.46), ('đời', 7.72), ('đẹp', 8.08), ('như', 8.3), ('mơ.', 8.58)],
    [('Còn', 10.3), ('em', 10.54), ('là', 10.84), ('những', 11.14), ('tương', 11.72), ('tư', 12.38)],
    [('Luôn', 12.76), ('rình', 13.12), ('tới', 13.76), ('bắt', 13.98), ('anh,', 14.24)],
    [('Để', 15.54), ('anh', 15.68), ('ngày', 16.0), ('đêm', 16.28), ('cuồng', 16.56), ('quay', 16.86), ('nhớ', 17.24), ('mong.', 17.9)],
    [('Hàng', 19.5), ('cây', 19.72), ('ngả', 19.98), ('xuống', 20.24)],
    [('Như', 20.84), ('đang', 21.12), ('cười', 21.5), ('đùa', 21.82), ('bên', 22.16), ('anh,', 22.46)],
    [('Vì', 24.06), ('em', 24.26), ('ngồi', 24.56), ('sau', 24.86)],
    [('Những', 25.36), ('nụ', 25.7), ('cười', 25.98), ('chỉ', 26.2), ('vây', 26.54), ('quanh', 26.92), ('đôi', 27.4), ('mình', 27.74), ('thôi', 28.04)],
    [('Thành', 28.62), ('phố', 29.44), ('như', 30.0), ('vô', 30.54), ('tận,', 30.92)],
    [('Tim', 31.82), ('thôi', 32.22), ('khô', 32.56), ('cằn,', 33.14)],
    [('Để', 33.84), ('những', 34.0), ('tương', 34.58), ('tư,', 35.16), ('nhớ', 35.52), ('mong', 36.1)],
    [('Luôn', 37.5), ('đong', 38.02), ('đầy', 38.32), ('theo', 39.92), ('thời', 40.24), ('gian', 40.68)],
]
ENDS = [2.5, 4.56, 7.46, 9.68, 12.76, 15.12, 18.82, 20.84, 22.86, 25.36, 28.62, 31.36, 33.84, 36.63, 41.4]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    # signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play()

    # Người ta thường nói   [sparkle: short]
    sync_words(song, LINES[0], ENDS[0], mode='sparkle', palette='hong')
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.1, shine, palette='hong')
    newline()

    # Khi yêu đời thật nên thơ,   [hearts: từ "yêu"]
    sync_words(song, LINES[1], ENDS[1], mode='hearts', palette='hong', indent=4)
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, heartbeat, palette='hong', indent=4)
    newline()

    # Vì say màu mắt nhau   [pop: đa dạng]
    sync_words(song, LINES[2], ENDS[2], mode='pop', palette='tim')
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.1, shine, palette='tim')
    newline()

    # Nên đời đẹp như mơ.   [sparkle: từ "đẹp"]
    sync_words(song, LINES[3], ENDS[3], mode='sparkle', palette='tim', indent=4)
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Còn em là những tương tư   [rise: đa dạng]
    sync_words(song, LINES[4], ENDS[4], mode='rise', palette='bien')
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='bien')
    newline()

    # Luôn rình tới bắt anh,   [fire: đa dạng]
    sync_words(song, LINES[5], ENDS[5], mode='fire', palette='bien', indent=2)
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='bien', indent=2)
    newline()

    # Để anh ngày đêm cuồng quay nhớ mong.   [letters: từ "mong", long]
    sync_words(song, LINES[6], ENDS[6], mode='letters', palette='hoanghon')
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.1, shine, palette='hoanghon')
    newline()

    # Hàng cây ngả xuống   [bounce: short]
    sync_words(song, LINES[7], ENDS[7], mode='bounce', palette='hoanghon')
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.1, breathe, palette='hoanghon')
    newline()

    # Như đang cười đùa bên anh,   [rainbow: bạn chọn]
    sync_words(song, LINES[8], ENDS[8], mode='rainbow', palette='bac', indent=4)
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.1, shine, palette='bac', indent=4)
    newline()

    # Vì em ngồi sau   [glide: bạn chọn]
    sync_words(song, LINES[9], ENDS[9], mode='glide', palette='bac')
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.1, breathe, palette='bac')
    newline()

    # Những nụ cười chỉ vây quanh đôi mình thôi   [hearts: bạn chọn]
    sync_words(song, LINES[10], ENDS[10], mode='hearts', palette='hong', indent=2)
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.1, shine, palette='hong', indent=2)
    newline()

    # Thành phố như vô tận,   [sides: slow]
    sync_words(song, LINES[11], ENDS[11], mode='sides', palette='hong')
    hold(song, text(LINES[11]), LINES[12][0][1] - 0.3, breathe, palette='hong')
    gradient_fade_out('' + text(LINES[11]), 0.25, palette='hong')

    # Tim thôi khô cằn,   [center: slow, short]
    sync_words(song, LINES[12], ENDS[12], mode='center', palette='tim', indent=2)
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.3, breathe, palette='tim', indent=2)
    dissolve_out('  ' + text(LINES[12]), 0.25, palette='tim')

    # Để những tương tư, nhớ mong   [letters: từ "mong"]
    sync_words(song, LINES[13], ENDS[13], mode='letters', palette='tim')
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.3, breathe, palette='tim')
    center_out('' + text(LINES[13]), 0.25, palette='tim')

    # Luôn đong đầy theo thời gian   [typewriter: slow, long, soft]
    sync_words(song, LINES[14], ENDS[14], mode='typewriter', palette='bien')
    hold(song, text(LINES[14]), ENDS[14] + 1.5, heartbeat, palette='bien')
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
