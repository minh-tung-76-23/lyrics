import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = False
set_color(COLOR)

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7702342256983952648.mp3'), offset=OFFSET)

LINES = [
    [('Đã', 0.0), ('không', 0.6), ('còn', 0.88), ('những', 1.16), ('phút', 1.36), ('giây', 1.62)],
    [('Mình', 1.78), ('từng', 2.0), ('đắm', 2.26), ('say', 2.54)],
    [('Ngày', 2.66), ('còn', 2.92), ('nắm', 3.16), ('tay', 3.34)],
    [('Giờ', 3.58), ('ôm', 3.86), ('đắng', 4.08), ('cay', 4.32)],
    [('Mọi', 4.46), ('lời', 4.76), ('hứa', 4.94), ('trôi', 5.12), ('theo', 5.36), ('gió', 5.74), ('bay', 5.98)],
    [('Chỉ', 6.62), ('còn', 7.42), ('những', 7.66), ('đêm', 8.06), ('dài', 8.46)],
    [('Mình', 8.92), ('anh', 9.18), ('cứ', 9.52), ('ngóng', 9.64), ('trông', 9.94), ('em', 10.08), ('hoài', 10.44)],
    [('Chẳng', 10.74), ('thể', 10.96), ('nào', 11.22)],
    [('Níu', 11.54), ('giữ', 11.88), ('bước', 12.14), ('chân', 12.4), ('em', 12.74), ('lại', 13.34)],
    [('Là', 13.66), ('là', 14.48), ('là', 14.48), ('là', 14.48)],
    [('Lần', 14.48), ('người', 14.6), ('nói', 14.8), ('rằng', 15.14), ('tình', 15.42), ('yêu', 15.66), ('này', 16.0), ('chẳng', 16.22), ('phai', 16.64)],
    [('Là', 17.02), ('là', 17.38), ('là', 17.54), ('là', 17.68)],
    [('Lần', 17.86), ('người', 18.06), ('nói', 18.38), ('chẳng', 18.66), ('phải', 19.02), ('anh', 19.3), ('thì', 19.54), ('chẳng', 19.9), ('ai', 20.42)],
    [('Để', 20.7), ('giờ', 20.9), ('này', 21.04), ('tình', 21.22), ('mình', 21.44)],
    [('đành', 21.66), ('vỡ', 21.92), ('tan', 22.28)],
    [('đành', 22.56), ('lỡ', 22.8), ('làng', 23.2)],
    [('đành', 23.54), ('dở', 23.72), ('dang', 24.08)],
    [('Anh', 24.36), ('ngỡ', 24.64), ('ngàng', 24.92)],
    [('để', 25.26), ('giờ', 25.52), ('đây', 25.86)],
    [('đường', 26.16), ('về', 26.42), ('ta', 26.74), ('rẽ', 27.12), ('ngang', 27.66)],
    [('Từng', 27.98), ('ngày', 27.98), ('anh', 27.98), ('vẫn', 28.64), ('bên', 28.96), ('em', 29.38)],
    [('Thế', 29.82), ('nhưng', 30.0), ('em', 30.4), ('vương', 30.78), ('vấn', 31.14), ('điều', 31.14), ('gì?', 31.36)],
    [('Tình', 31.74), ('yêu', 32.02), ('bấy', 32.4), ('lâu', 32.54), ('nay', 32.72)],
    [('Có', 33.12), ('khiến', 33.42), ('em', 33.7), ('thôi', 33.94), ('ngừng', 34.14), ('nghĩ', 34.36), ('suy?', 34.82)],
    [('Mỗi', 35.52), ('đêm', 35.86), ('mình', 36.06), ('anh', 36.26), ('u', 36.58), ('hoài', 36.58)],
    [('Nên', 37.04), ('dừng', 37.36), ('lại', 37.7), ('hay', 38.04), ('yêu', 38.34)],
    [('Chẳng', 38.52), ('ngần', 38.84), ('ngại?', 39.16)],
    [('Và', 40.02), ('anh', 40.12), ('cũng', 40.4), ('biết', 40.62), ('đau', 40.74), ('khi', 41.0), ('em', 41.3), ('nhạt', 41.54), ('phai', 42.02)],
    [('Chờ', 42.56), ('bao', 42.88), ('tháng', 43.04), ('năm', 43.34), ('qua', 43.58)],
    [('Vẫn', 43.96), ('mong', 44.38), ('bao', 44.38), ('yêu', 45.02), ('dấu', 45.2), ('quay', 45.38), ('lại', 45.8)],
    [('Đành', 46.08), ('buông', 46.38), ('cánh', 46.6), ('tay', 46.86), ('em', 47.14)],
    [('khi', 47.5), ('trái', 47.72), ('tim', 47.96), ('em', 48.24), ('chẳng', 48.44), ('có', 48.64), ('anh', 49.42)],
    [('Biết', 49.82), ('đâu', 50.2), ('em', 50.4), ('cũng', 50.64), ('chấp', 50.86), ('nhận', 51.1)],
    [('Không', 51.42), ('ân', 51.78), ('hận', 52.02)],
    [('Một', 52.36), ('lần', 52.68), ('khóc', 52.88), ('cho', 53.32), ('em', 53.84)],
    [('Và', 54.16), ('quên', 54.16), ('đi', 54.66), ('tháng', 54.9), ('năm', 55.18)],
    [('Ta', 55.34), ('từng', 55.64), ('đậm', 55.96), ('sâu', 56.32)],
]
ENDS = [1.78, 2.66, 3.58, 4.46, 6.62, 8.92, 10.74, 11.54, 13.66, 14.58, 17.02, 17.86, 20.7, 21.66, 22.56, 23.54, 24.36, 25.26, 26.16, 27.98, 29.64, 31.74, 33.12, 35.52, 37.04, 38.52, 40.02, 42.56, 43.96, 46.08, 47.5, 49.82, 51.42, 52.36, 54.16, 55.34, 56.82]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    signature()  # Shinn🐣 
    song.play()

    # Đã không còn những phút giây
    sync_words(song, LINES[0], ENDS[0], mode='karaoke', palette='hong')
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.3, breathe, palette='hong')
    gradient_fade_out('' + text(LINES[0]), 0.25, palette='hong')

    # Mình từng đắm say
    sync_words(song, LINES[1], ENDS[1], mode='pop', palette='hong')
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, breathe, palette='hong')
    newline()

    # Ngày còn nắm tay
    sync_words(song, LINES[2], ENDS[2], mode='glide', palette='tim')
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.3, breathe, palette='tim')
    dissolve_out('' + text(LINES[2]), 0.25, palette='tim')

    # Giờ ôm đắng cay
    sync_words(song, LINES[3], ENDS[3], mode='pop', palette='tim', indent=4)
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Mọi lời hứa trôi theo gió bay
    sync_words(song, LINES[4], ENDS[4], mode='words', palette='bien')
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='bien')
    newline()

    # Chỉ còn những đêm dài
    sync_words(song, LINES[5], ENDS[5], mode='jump', palette='bien')
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='bien')
    newline()

    # Mình anh cứ ngóng trông em hoài
    sync_words(song, LINES[6], ENDS[6], mode='scramble', palette='hoanghon')
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.1, shine, palette='hoanghon')
    newline()

    # Chẳng thể nào
    sync_words(song, LINES[7], ENDS[7], mode='sides', palette='hoanghon')
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.1, breathe, palette='hoanghon')
    newline()

    # Níu giữ bước chân em lại
    sync_words(song, LINES[8], ENDS[8], mode='drop', palette='bac', indent=4)
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.1, shine, palette='bac', indent=4)
    newline()

    # Là là là là
    sync_words(song, LINES[9], ENDS[9], mode='spotlight', palette='bac', indent=8)
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.1, breathe, palette='bac', indent=8)
    newline()

    # Lần người nói rằng tình yêu này chẳng phai
    sync_words(song, LINES[10], ENDS[10], mode='wave', palette='hong')
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.1, heartbeat, palette='hong')
    newline()

    # Là là là là
    sync_words(song, LINES[11], ENDS[11], mode='converge', palette='hong', indent=8)
    hold(song, text(LINES[11]), LINES[12][0][1] - 0.1, breathe, palette='hong', indent=8)
    newline()

    # Lần người nói chẳng phải anh thì chẳng ai
    sync_words(song, LINES[12], ENDS[12], mode='typo', palette='tim')
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.1, shine, palette='tim')
    newline()

    # Để giờ này tình mình
    sync_words(song, LINES[13], ENDS[13], mode='pop', palette='tim')
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.3, breathe, palette='tim')
    center_out('' + text(LINES[13]), 0.25, palette='tim')

    # đành vỡ tan
    sync_words(song, LINES[14], ENDS[14], mode='slide', palette='bien', indent=4)
    hold(song, text(LINES[14]), LINES[15][0][1] - 0.3, breathe, palette='bien', indent=4)
    sweep_out('    ' + text(LINES[14]), 0.25, palette='bien')

    # đành lỡ làng
    sync_words(song, LINES[15], ENDS[15], mode='center', palette='bien', indent=8)
    hold(song, text(LINES[15]), LINES[16][0][1] - 0.3, breathe, palette='bien', indent=8)
    drift_out('        ' + text(LINES[15]), 0.25, palette='bien')

    # đành dở dang
    sync_words(song, LINES[16], ENDS[16], mode='pop', palette='hoanghon', indent=12)
    hold(song, text(LINES[16]), LINES[17][0][1] - 0.3, breathe, palette='hoanghon', indent=12)
    gradient_fade_out('            ' + text(LINES[16]), 0.25, palette='hoanghon')

    # Anh ngỡ ngàng
    sync_words(song, LINES[17], ENDS[17], mode='splash', palette='hoanghon')
    hold(song, text(LINES[17]), LINES[18][0][1] - 0.1, breathe, palette='hoanghon')
    newline()

    # để giờ đây
    sync_words(song, LINES[18], ENDS[18], mode='glitch', palette='bac', indent=4)
    hold(song, text(LINES[18]), LINES[19][0][1] - 0.1, shine, palette='bac', indent=4)
    newline()

    # đường về ta rẽ ngang
    sync_words(song, LINES[19], ENDS[19], mode='fire', palette='bac', indent=8)
    hold(song, text(LINES[19]), LINES[20][0][1] - 0.1, breathe, palette='bac', indent=8)
    newline()

    newline()  # hết đoạn

    # Từng ngày anh vẫn bên em
    sync_words(song, LINES[20], ENDS[20], mode='reveal', palette='tim')
    hold(song, text(LINES[20]), LINES[21][0][1] - 0.1, shine, palette='tim')
    newline()

    # Thế nhưng em vương vấn điều gì?
    sync_words(song, LINES[21], ENDS[21], mode='fadein', palette='tim', indent=4)
    hold(song, text(LINES[21]), LINES[22][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Tình yêu bấy lâu nay
    sync_words(song, LINES[22], ENDS[22], mode='typewriter', palette='bien')
    hold(song, text(LINES[22]), LINES[23][0][1] - 0.1, heartbeat, palette='bien')
    newline()

    # Có khiến em thôi ngừng nghĩ suy?
    sync_words(song, LINES[23], ENDS[23], mode='snow', palette='bien', indent=4)
    hold(song, text(LINES[23]), LINES[24][0][1] - 0.1, breathe, palette='bien', indent=4)
    newline()

    # Mỗi đêm mình anh u hoài
    sync_words(song, LINES[24], ENDS[24], mode='pop', palette='hoanghon')
    hold(song, text(LINES[24]), LINES[25][0][1] - 0.1, shine, palette='hoanghon')
    newline()

    # Nên dừng lại hay yêu
    sync_words(song, LINES[25], ENDS[25], mode='rainbow', palette='hoanghon', indent=4)
    hold(song, text(LINES[25]), LINES[26][0][1] - 0.1, heartbeat, palette='hoanghon', indent=4)
    newline()

    # Chẳng ngần ngại?
    sync_words(song, LINES[26], ENDS[26], mode='flicker', palette='bac', indent=12)
    hold(song, text(LINES[26]), LINES[27][0][1] - 0.1, shine, palette='bac', indent=12)
    newline()

    # Và anh cũng biết đau khi em nhạt phai
    sync_words(song, LINES[27], ENDS[27], mode='letters', palette='bac')
    hold(song, text(LINES[27]), LINES[28][0][1] - 0.1, breathe, palette='bac')
    newline()

    # Chờ bao tháng năm qua
    sync_words(song, LINES[28], ENDS[28], mode='karaoke', palette='hong')
    hold(song, text(LINES[28]), LINES[29][0][1] - 0.3, breathe, palette='hong')
    dissolve_out('' + text(LINES[28]), 0.25, palette='hong')

    # Vẫn mong bao yêu dấu quay lại
    sync_words(song, LINES[29], ENDS[29], mode='pop', palette='hong', indent=4)
    hold(song, text(LINES[29]), LINES[30][0][1] - 0.1, heartbeat, palette='hong', indent=4)
    newline()

    # Đành buông cánh tay em
    sync_words(song, LINES[30], ENDS[30], mode='glide', palette='tim')
    hold(song, text(LINES[30]), LINES[31][0][1] - 0.3, breathe, palette='tim')
    center_out('' + text(LINES[30]), 0.25, palette='tim')

    # khi trái tim em chẳng có anh
    sync_words(song, LINES[31], ENDS[31], mode='pop', palette='tim', indent=4)
    hold(song, text(LINES[31]), LINES[32][0][1] - 0.1, heartbeat, palette='tim', indent=4)
    newline()

    # Biết đâu em cũng chấp nhận
    sync_words(song, LINES[32], ENDS[32], mode='words', palette='bien')
    hold(song, text(LINES[32]), LINES[33][0][1] - 0.3, breathe, palette='bien')
    sweep_out('' + text(LINES[32]), 0.25, palette='bien')

    # Không ân hận
    sync_words(song, LINES[33], ENDS[33], mode='pop', palette='bien', indent=4)
    hold(song, text(LINES[33]), LINES[34][0][1] - 0.3, breathe, palette='bien', indent=4)
    drift_out('    ' + text(LINES[33]), 0.25, palette='bien')

    # Một lần khóc cho em
    sync_words(song, LINES[34], ENDS[34], mode='scramble', palette='hoanghon', indent=8)
    hold(song, text(LINES[34]), LINES[35][0][1] - 0.3, breathe, palette='hoanghon', indent=8)
    gradient_fade_out('        ' + text(LINES[34]), 0.25, palette='hoanghon')

    # Và quên đi tháng năm
    sync_words(song, LINES[35], ENDS[35], mode='sides', palette='hoanghon')
    hold(song, text(LINES[35]), LINES[36][0][1] - 0.1, breathe, palette='hoanghon')
    newline()

    # Ta từng đậm sâu
    sync_words(song, LINES[36], ENDS[36], mode='drop', palette='bac', indent=4)
    trailing_dots(song, text(LINES[36]), ENDS[36] + 3.0, palette='bac', indent=4)
    hold(song, text(LINES[36]) + '...', ENDS[36] + 4.5, heartbeat, palette='bac', indent=4)
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
