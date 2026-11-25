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

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7711598591810293000.mp3'), offset=OFFSET)

LINES = [
    [('Nhưng', 0.0), ('sẽ', 0.36), ('không', 0.72), ('thể', 1.36), ('nào', 1.6), ('xảy', 1.8), ('ra', 2.2)],
    [('Một', 2.6), ('viễn', 3.02), ('cảnh', 3.68), ('như', 4.02), ('vậy', 4.18), ('cả', 4.48)],
    [('Tụi', 4.76), ('mình', 5.0), ('đặt', 5.28), ('dấu', 5.94), ('chấm', 6.44), ('hết', 7.28), ('thôi💔', 7.72)],
    [('Bao', 8.78), ('nhiêu', 8.92), ('lâu', 9.1), ('ta', 9.3), ('bên', 9.44), ('nhau', 9.66), ('giờ', 9.9), ('đây', 10.08), ('quá', 10.18), ('đủ', 10.56), ('rồi', 10.86)],
    [('Trái', 11.32), ('tim', 11.9), ('cũng', 12.02), ('đã', 12.22), ('báo', 12.52), ('động', 12.84), ('rồi', 13.08)],
    [('Anh', 13.62), ('nghe', 14.26), ('một', 14.38), ('tin', 14.52), ('quá', 14.8), ('động', 15.12), ('trời', 15.42)],
    [('Buông', 15.88), ('tay', 16.16), ('dứt', 16.32), ('khoát', 16.58), ('chỉ', 16.82), ('vì', 17.02), ('câu', 17.16), ('nặng', 17.42), ('lời', 17.78)],
    [('Phá', 18.08), ('đi', 18.52), ('hết', 18.7), ('những', 18.82), ('đại', 19.02), ('kì', 19.2), ('công', 19.54)],
    [('Rất', 20.28), ('yêu', 20.78), ('nhưng', 20.98), ('ở', 21.1), ('lại', 21.34), ('thì', 21.52), ('không', 21.74)],
    [('Ta', 22.4), ('cứ', 23.22), ('chôn', 23.42), ('vùi', 23.58), ('tất', 23.82), ('cả', 23.9), ('năm', 24.04), ('tháng', 24.3), ('ấy', 24.64)],
    [('Chẳng', 24.96), ('ai', 25.2), ('nắm', 25.46), ('lấy', 25.72)],
    [('Vì', 26.14), ('ai?', 26.52)],
]
ENDS = [2.6, 4.76, 8.78, 11.32, 13.62, 15.88, 18.08, 20.28, 22.4, 24.96, 26.14, 26.78]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play(start=START)

    # Nhưng sẽ không thể nào xảy ra   [mist: bạn chọn]
    sync_words(song, LINES[0], ENDS[0], mode='mist', palette='hong', indent=4)
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.3, breathe, palette='hong', indent=4)
    gradient_fade_out('    ' + text(LINES[0]), 0.25, palette='hong')

    # Một viễn cảnh như vậy cả   [fadein: bạn chọn]
    sync_words(song, LINES[1], ENDS[1], mode='fadein', palette='hong', indent=8)
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, breathe, palette='hong', indent=8)
    newline()

    # Tụi mình đặt dấu chấm hết thôi💔   [typewriter: bạn chọn]
    sync_words(song, LINES[2], ENDS[2], mode='typewriter', palette='tim', indent=4)
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Bao nhiêu lâu ta bên nhau giờ đây quá đủ rồi   [karaoke: bạn chọn]
    sync_words(song, LINES[3], ENDS[3], mode='karaoke', palette='tim')
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim')
    newline()

    # Trái tim cũng đã báo động rồi   [flicker: bạn chọn]
    sync_words(song, LINES[4], ENDS[4], mode='flicker', palette='bien', indent=8)
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, heartbeat, palette='bien', indent=8)
    newline()

    # Anh nghe một tin quá động trời   [glitch: bạn chọn]
    sync_words(song, LINES[5], ENDS[5], mode='glitch', palette='bien', indent=4)
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='bien', indent=4)
    newline()

    # Buông tay dứt khoát chỉ vì câu nặng lời   [drop: bạn chọn]
    sync_words(song, LINES[6], ENDS[6], mode='drop', palette='hoanghon', indent=4)
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.1, breathe, palette='hoanghon', indent=4)
    newline()

    # Phá đi hết những đại kì công   [scramble: bạn chọn]
    sync_words(song, LINES[7], ENDS[7], mode='scramble', palette='hoanghon', indent=4)
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.1, breathe, palette='hoanghon', indent=4)
    newline()

    # Rất yêu nhưng ở lại thì không   [spotlight: bạn chọn]
    sync_words(song, LINES[8], ENDS[8], mode='spotlight', palette='bac', indent=4)
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.1, heartbeat, palette='bac', indent=4)
    newline()

    # Ta cứ chôn vùi tất cả năm tháng ấy   [sides: bạn chọn]
    sync_words(song, LINES[9], ENDS[9], mode='sides', palette='bac', indent=4)
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.1, breathe, palette='bac', indent=4)
    newline()

    # Chẳng ai nắm lấy   [center: bạn chọn]
    sync_words(song, LINES[10], ENDS[10], mode='center', palette='hong', indent=8)
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.1, shine, palette='hong', indent=8)
    newline()

    # Vì ai?   [letters: bạn chọn]
    sync_words(song, LINES[11], ENDS[11], mode='letters', palette='hong', indent=12)
    hold(song, text(LINES[11]), ENDS[11] + 1.5, heartbeat, palette='hong', indent=12)
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
