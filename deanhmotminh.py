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

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7709109014210170130.mp3'), offset=OFFSET)

LINES = [
    [('Chúng', 0.0), ('ta', 0.18), ('đã', 0.62), ('hết', 0.8), ('cơ', 1.08), ('hội', 1.28)],
    [('Em', 1.58), ('bước', 1.82), ('trên', 1.94), ('con', 2.16), ('đường', 2.38), ('mới', 2.54)],
    [('Còn', 2.88), ('anh', 3.3), ('ở', 3.58), ('trong', 3.68), ('buồng', 3.86), ('tối', 4.08)],
    [('Gạt', 4.26), ('nước', 4.68), ('mắt,', 4.88), ('khóe', 5.06), ('môi', 5.34), ('gượng', 5.5), ('cười', 5.68)],
    [('Chẳng', 6.06), ('có', 6.68), ('ai', 6.88), ('ở', 7.12), ('trên', 7.24), ('đời', 7.56)],
    [('Vốn', 7.92), ('dĩ', 8.22), ('thuộc', 8.4), ('về', 8.64), ('nhau', 8.78), ('đâu', 9.02)],
    [('Bước', 9.6), ('đi', 9.74), ('qua', 9.94), ('niềm', 10.14), ('đau', 10.36)],
    [('Thì', 10.6), ('mới', 10.94), ('thấy', 11.12), ('được', 11.32), ('phép', 11.52), ('nhiệm', 11.68), ('màu', 11.9)],
    [('Anh', 12.16), ('vẫn', 12.32), ('cứ', 12.46), ('tin', 12.66)],
    [('Điều', 12.86), ('thần', 13.06), ('kỳ', 13.24), ('sẽ', 13.65), ('tới', 13.86)],
    [('Nhưng', 14.48), ('có', 15.14), ('lẽ', 15.26), ('định', 15.42), ('mệnh', 15.62), ('muốn', 15.76)],
    [('Hai', 16.0), ('ta', 16.2), ('phải', 16.36), ('chia', 16.56), ('hai', 16.92), ('lối', 17.64)],
    [('Chắc', 19.42), ('đây', 19.82), ('chỉ', 19.9), ('là', 20.04), ('trùng', 20.28), ('hợp', 20.48)],
    [('Bão', 20.92), ('đang', 21.0), ('kéo', 21.08), ('đến', 21.22), ('từng', 21.42), ('đợt', 21.72)],
    [('Anh', 21.92), ('luôn', 22.2), ('hy', 22.26), ('vọng', 22.42)],
    [('Rằng', 22.64), ('qua', 22.78), ('ngày', 22.98), ('mai', 23.16), ('cả', 23.3), ('hai', 23.46), ('sẽ', 23.64), ('tìm', 23.74), ('được', 23.98), ('khoảng', 24.04), ('trời', 24.2), ('mới', 24.34)],
    [('Nước', 24.84), ('mắt', 25.88), ('ơi', 25.88), ('xin', 25.88), ('hãy', 25.88), ('cứ', 26.22), ('rơi', 26.6)],
    [('Buồn', 27.34), ('một', 27.68), ('chút', 27.86), ('thôi', 28.24)],
    [('Để', 28.6), ('người', 29.2), ('khác', 29.38), ('bên', 29.76), ('em', 30.04), ('sau', 30.18), ('ngày', 30.4)],
    [('Ngày', 30.84), ('nỗi', 31.46), ('đau', 31.62), ('như', 31.8), ('dày', 31.92), ('vò', 32.2), ('trái', 32.48), ('tim', 32.96)],
    [('Anh', 33.3), ('chẳng', 33.78), ('thể', 34.12), ('tin', 34.44)],
    [('Ta', 34.88), ('đã', 35.38), ('mất', 35.64), ('nhau', 36.08), ('như', 36.42), ('vậy', 36.62)],
]
ENDS = [1.58, 2.88, 4.26, 6.06, 7.92, 9.44, 10.6, 12.16, 12.86, 14.48, 16.0, 18.46, 20.8, 21.92, 22.64, 24.84, 27.12, 28.6, 30.84, 33.3, 34.88, 37.06]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    # signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play(start=START)

    # Chúng ta đã hết cơ hội   [fadein: bạn chọn]
    sync_words(song, LINES[0], ENDS[0], mode='fadein', palette='hong', indent=2)
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.1, shine, palette='hong', indent=2)
    newline()

    # Em bước trên con đường mới   [slide: bạn chọn]
    sync_words(song, LINES[1], ENDS[1], mode='slide', palette='hong')
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, breathe, palette='hong')
    newline()

    # Còn anh ở trong buồng tối   [mist: bạn chọn]
    sync_words(song, LINES[2], ENDS[2], mode='mist', palette='tim', indent=4)
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.1, shine, palette='tim', indent=4)
    newline()

    # Gạt nước mắt, khóe môi gượng cười   [drop: bạn chọn]
    sync_words(song, LINES[3], ENDS[3], mode='drop', palette='tim')
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim')
    newline()

    # Chẳng có ai ở trên đời   [words: bạn chọn]
    sync_words(song, LINES[4], ENDS[4], mode='words', palette='bien')
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='bien')
    newline()

    # Vốn dĩ thuộc về nhau đâu   [sides: bạn chọn]
    sync_words(song, LINES[5], ENDS[5], mode='sides', palette='bien')
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='bien')
    newline()

    # Bước đi qua niềm đau   [glide: bạn chọn]
    sync_words(song, LINES[6], ENDS[6], mode='glide', palette='hoanghon', indent=4)
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.1, breathe, palette='hoanghon', indent=4)
    newline()

    # Thì mới thấy được phép nhiệm màu   [sparkle: bạn chọn]
    sync_words(song, LINES[7], ENDS[7], mode='sparkle', palette='hoanghon')
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.1, breathe, palette='hoanghon')
    newline()

    # Anh vẫn cứ tin   [spotlight: bạn chọn]
    sync_words(song, LINES[8], ENDS[8], mode='spotlight', palette='bac')
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.1, shine, palette='bac')
    newline()

    # Điều thần kỳ sẽ tới   [starfall: bạn chọn]
    sync_words(song, LINES[9], ENDS[9], mode='starfall', palette='bac', indent=4)
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.1, breathe, palette='bac', indent=4)
    newline()

    # Nhưng có lẽ định mệnh muốn   [letters: bạn chọn]
    sync_words(song, LINES[10], ENDS[10], mode='letters', palette='hong')
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.1, shine, palette='hong')
    newline()

    # Hai ta phải chia hai lối   [split: bạn chọn]
    sync_words(song, LINES[11], ENDS[11], mode='split', palette='hong', indent=4)
    hold(song, text(LINES[11]), LINES[12][0][1] - 0.1, breathe, palette='hong', indent=4)
    newline()

    # Chắc đây chỉ là trùng hợp   [reveal: bạn chọn]
    sync_words(song, LINES[12], ENDS[12], mode='reveal', palette='tim')
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.1, shine, palette='tim')
    newline()

    # Bão đang kéo đến từng đợt   [wave: bạn chọn]
    sync_words(song, LINES[13], ENDS[13], mode='wave', palette='tim')
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.1, breathe, palette='tim')
    newline()

    # Anh luôn hy vọng   [rise: bạn chọn]
    sync_words(song, LINES[14], ENDS[14], mode='rise', palette='bien', indent=4)
    hold(song, text(LINES[14]), LINES[15][0][1] - 0.1, shine, palette='bien', indent=4)
    newline()

    # Rằng qua ngày mai cả hai sẽ tìm được khoảng trời mới   [flow: bạn chọn]
    sync_words(song, LINES[15][0:6], LINES[15][6][1] - 0.05, mode='flow', palette='bien')
    newline()
    sync_words(song, LINES[15][6:12], ENDS[15], mode='flow', palette='bien', indent=8)
    hold(song, text(LINES[15][6:]), LINES[16][0][1] - 0.1, breathe, palette='bien', indent=8)
    newline()

    # Nước mắt ơi xin hãy cứ rơi   [drop: bạn chọn]
    sync_words(song, LINES[16], ENDS[16], mode='drop', palette='hoanghon')
    hold(song, text(LINES[16]), LINES[17][0][1] - 0.1, shine, palette='hoanghon')
    newline()

    # Buồn một chút thôi   [fadein: bạn chọn]
    sync_words(song, LINES[17], ENDS[17], mode='fadein', palette='hoanghon')
    hold(song, text(LINES[17]), LINES[18][0][1] - 0.1, breathe, palette='hoanghon')
    newline()

    # Để người khác bên em sau ngày   [ripple: bạn chọn]
    sync_words(song, LINES[18], ENDS[18], mode='ripple', palette='bac')
    hold(song, text(LINES[18]), LINES[19][0][1] - 0.1, shine, palette='bac')
    newline()

    # Ngày nỗi đau như dày vò trái tim   [glitch: bạn chọn]
    sync_words(song, LINES[19], ENDS[19], mode='glitch', palette='bac')
    hold(song, text(LINES[19]), LINES[20][0][1] - 0.1, breathe, palette='bac')
    newline()

    # Anh chẳng thể tin   [scramble: bạn chọn]
    sync_words(song, LINES[20], ENDS[20], mode='scramble', palette='hong')
    hold(song, text(LINES[20]), LINES[21][0][1] - 0.1, shine, palette='hong')
    newline()

    # Ta đã mất nhau như vậy   [letters: bạn chọn]
    sync_words(song, LINES[21], ENDS[21], mode='letters', palette='hong')
    trailing_dots(song, text(LINES[21]), ENDS[21] + 3.0, palette='hong')
    hold(song, text(LINES[21]) + '...', ENDS[21] + 4.5, heartbeat, palette='hong')
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
