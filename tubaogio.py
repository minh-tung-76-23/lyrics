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

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7706185995783326997.mp3'), offset=OFFSET)

LINES = [
    [('Từ', 0.0), ('bao', 0.42), ('giờ', 0.96)],
    [('Mà', 3.06), ('con', 3.3), ('tim', 3.64), ('anh', 4.04), ('hạnh', 4.34), ('phúc', 4.64), ('nhường', 4.86), ('này?', 5.32)],
    [('Từ', 5.66), ('bao', 6.0), ('giờ', 6.54)],
    [('Mà', 8.56), ('anh', 8.82), ('không', 9.18), ('chắc', 9.6), ('có', 9.8), ('phải', 10.14), ('là', 10.46), ('mơ?', 10.8)],
    [('Từ', 11.48), ('bao', 11.54), ('giờ', 12.76)],
    [('Từng', 14.1), ('khoảng', 14.2), ('trống', 14.42), ('khẽ', 14.74), ('lấp', 15.08), ('bên', 15.34), ('trong', 15.66), ('tình', 15.92), ('yêu', 16.32)],
    [('Dần', 16.8), ('xóa', 17.2), ('nhòa', 18.14), ('cô', 19.32), ('đơn', 19.58)],
    [('Anh', 21.12), ('chưa', 21.88), ('từng', 22.22), ('khóc', 22.54)],
    [('Khi', 22.92), ('đau', 23.14), ('thương', 23.28), ('bủa', 23.56), ('vây', 23.86)],
    [('Luôn', 24.3), ('luôn', 24.66), ('thầm', 24.96), ('nghĩ', 25.34)],
    [('Sẽ', 25.66), ('không', 25.84), ('ai', 26.04), ('ở', 26.28), ('đây', 26.68)],
    [('Sẻ', 26.96), ('chia', 27.44), ('buồn', 27.82), ('vui', 28.2), ('cùng', 28.5), ('anh', 28.88)],
    [('Vượt', 29.18), ('qua', 29.6), ('chặng', 29.86), ('đường', 30.22)],
    [('đầy', 30.56), ('rẫy', 30.94), ('những', 31.26), ('chông', 31.56), ('gai', 32.08)],
    [('Nhưng', 32.44), ('em', 33.0), ('bước', 33.28), ('tới', 33.68)],
    [('Nắm', 33.96), ('lấy', 34.24), ('đôi', 34.34), ('bàn', 34.6), ('tay', 34.92)],
    [('Xua', 35.3), ('tan', 35.84), ('bóng', 36.12), ('tối', 36.58)],
    [('Ôm', 36.76), ('lấy', 37.04), ('anh', 37.12), ('thật', 37.36), ('chặt', 37.72)],
    [('Cứu', 38.66), ('lấy', 39.26), ('tâm', 39.54), ('hồn', 39.84), ('lạc', 40.32), ('lõng', 40.6), ('giữa', 41.02), ('đêm', 41.24), ('đen.', 41.58)],
]
ENDS = [2.12, 5.68, 8.04, 11.24, 13.76, 16.8, 21.12, 22.92, 24.3, 25.66, 26.96, 29.18, 30.56, 32.44, 33.96, 35.3, 36.76, 38.96, 43.18]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    # signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play(start=START)

    # Từ bao giờ   [bloom: bạn chọn]
    sync_words(song, LINES[0], ENDS[0], mode='bloom', palette='hong', indent=12)
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.3, breathe, palette='hong', indent=12)
    gradient_fade_out('            ' + text(LINES[0]), 0.25, palette='hong')

    # Mà con tim anh hạnh phúc nhường này?   [hearts: bạn chọn]
    sync_words(song, LINES[1], ENDS[1], mode='hearts', palette='hong')
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, heartbeat, palette='hong')
    newline()

    # Từ bao giờ   [center: bạn chọn]
    sync_words(song, LINES[2], ENDS[2], mode='center', palette='tim', indent=8)
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.3, breathe, palette='tim', indent=8)
    dissolve_out('        ' + text(LINES[2]), 0.25, palette='tim')

    # Mà anh không chắc có phải là mơ?   [mist: bạn chọn]
    sync_words(song, LINES[3], ENDS[3], mode='mist', palette='tim')
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim')
    newline()

    # Từ bao giờ   [letters: bạn chọn]
    sync_words(song, LINES[4], ENDS[4], mode='letters', palette='bien', indent=8)
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='bien', indent=8)
    newline()

    # Từng khoảng trống khẽ lấp bên trong tình yêu   [ripple: bạn chọn]
    sync_words(song, LINES[5], ENDS[5], mode='ripple', palette='bien')
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, heartbeat, palette='bien')
    newline()

    # Dần xóa nhòa cô đơn   [fadein: bạn chọn]
    sync_words(song, LINES[6], ENDS[6], mode='fadein', palette='hoanghon', indent=12)
    trailing_dots(song, text(LINES[6]), LINES[7][0][1] - 0.1, palette='hoanghon', indent=12)
    newline()

    # Anh chưa từng khóc   [drop: bạn chọn]
    sync_words(song, LINES[7], ENDS[7], mode='drop', palette='hoanghon')
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.1, breathe, palette='hoanghon')
    newline()

    # Khi đau thương bủa vây   [sides: bạn chọn]
    sync_words(song, LINES[8], ENDS[8], mode='sides', palette='bac', indent=4)
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.1, breathe, palette='bac', indent=4)
    newline()

    # Luôn luôn thầm nghĩ   [karaoke: bạn chọn]
    sync_words(song, LINES[9], ENDS[9], mode='karaoke', palette='bac')
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.1, breathe, palette='bac')
    newline()

    # Sẽ không ai ở đây   [center: bạn chọn]
    sync_words(song, LINES[10], ENDS[10], mode='center', palette='hong', indent=4)
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.1, shine, palette='hong', indent=4)
    newline()

    # Sẻ chia buồn vui cùng anh   [words: bạn chọn]
    sync_words(song, LINES[11], ENDS[11], mode='words', palette='hong', indent=4)
    hold(song, text(LINES[11]), LINES[12][0][1] - 0.1, breathe, palette='hong', indent=4)
    newline()

    # Vượt qua chặng đường   [glide: bạn chọn]
    sync_words(song, LINES[12], ENDS[12], mode='glide', palette='tim', indent=4)
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.1, shine, palette='tim', indent=4)
    newline()

    # đầy rẫy những chông gai   [scramble: bạn chọn]
    sync_words(song, LINES[13], ENDS[13], mode='scramble', palette='tim', indent=8)
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.1, breathe, palette='tim', indent=8)
    newline()

    # Nhưng em bước tới   [swipe: bạn chọn]
    sync_words(song, LINES[14], ENDS[14], mode='swipe', palette='bien')
    hold(song, text(LINES[14]), LINES[15][0][1] - 0.1, shine, palette='bien')
    newline()

    # Nắm lấy đôi bàn tay   [hearts: bạn chọn]
    sync_words(song, LINES[15], ENDS[15], mode='hearts', palette='bien', indent=4)
    hold(song, text(LINES[15]), LINES[16][0][1] - 0.1, breathe, palette='bien', indent=4)
    newline()

    # Xua tan bóng tối   [starfall: bạn chọn]
    sync_words(song, LINES[16], ENDS[16], mode='starfall', palette='hoanghon', indent=4)
    hold(song, text(LINES[16]), LINES[17][0][1] - 0.1, shine, palette='hoanghon', indent=4)
    newline()

    # Ôm lấy anh thật chặt   [converge: bạn chọn]
    sync_words(song, LINES[17], ENDS[17], mode='converge', palette='hoanghon', indent=4)
    hold(song, text(LINES[17]), LINES[18][0][1] - 0.1, breathe, palette='hoanghon', indent=4)
    newline()

    # Cứu lấy tâm hồn lạc lõng giữa đêm đen.   [sparkle: bạn chọn]
    sync_words(song, LINES[18], ENDS[18], mode='sparkle', palette='bac')
    hold(song, text(LINES[18]), ENDS[18] + 1.5, heartbeat, palette='bac')
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
