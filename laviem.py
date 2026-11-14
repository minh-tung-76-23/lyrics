import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = True
set_color(COLOR)

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7696822203526024468.mp3'), offset=OFFSET)

LINES = [
    [('Hàng', 0.0), ('trăm', 0.36), ('lý', 0.56), ('do', 0.76), ('cũng', 0.76), ('chẳng', 1.06), ('thể', 1.3), ('cứu', 1.52), ('vãn', 2.16)],
    [('Biết', 2.46), ('sao', 2.82), ('hết', 3.18), ('cho', 3.46), ('vừa', 3.8)],
    [('Lòng', 4.16), ('nhau', 4.42), ('mới', 4.72), ('thấu', 5.0), ('đây', 5.18), ('em', 5.66), ('💔', 6.32)],
    [('Trái', 6.32), ('tim', 6.32), ('anh', 6.96), ('chẳng', 7.12), ('còn', 7.34), ('cần', 7.6), ('thiết', 7.98), ('nữa', 8.5)],
    [('Nói', 8.74), ('chi', 9.26), ('đến', 9.4), ('đây', 9.48), ('cũng', 9.74), ('thừa', 10.04)],
    [('Rượu', 10.4), ('vang', 10.8), ('pha', 11.1), ('với', 11.36), ('cơn', 11.92), ('mưa', 12.26)],
    [('Hàng', 12.84), ('trăm', 13.16), ('lý', 13.32), ('do', 13.52), ('cũng', 13.72), ('chẳng', 13.9), ('thể', 14.14), ('cứu', 14.32), ('vãn', 14.8)],
    [('Biết', 15.14), ('sao', 15.54), ('hết', 15.96), ('cho', 16.2), ('vừa', 16.6)],
    [('Lòng', 16.82), ('nhau', 17.16), ('mới', 17.54), ('thấu', 17.76), ('đây', 18.38), ('em', 18.66)],
    [('Dệt', 19.18), ('hàng', 19.64), ('triệu', 19.76), ('vết', 19.98), ('thương,', 20.52)],
    [('Tự', 21.1), ('vùi', 21.26), ('mình', 21.38), ('trước', 21.56), ('gương', 22.02)],
    [('Nhìn', 22.52), ('một', 22.76), ('người', 22.98), ('đã', 23.2), ('từng', 23.38), ('thương', 23.6)],
    [('Sao', 23.76), ('nay', 24.0), ('xa', 24.14), ('lạ', 24.38), ('đến', 24.64), ('bất', 24.96), ('thường', 25.34)],
    [('Cố', 25.72), ('gắng', 25.78), ('cũng', 26.16), ('chỉ', 26.4), ('bằng', 26.6), ('không', 26.86)],
    [('nước', 27.34), ('mắt', 27.78), ('ngược', 28.6), ('dòng', 28.8)],
    [('Chảy', 29.26), ('ngược', 29.66), ('tận', 29.76), ('sâu', 30.02), ('bên', 30.2), ('trong', 30.34)],
    [('nghẹn', 30.6), ('đắng', 30.94), ('nơi', 31.14), ('lồng', 31.32), ('ngực', 31.56)],
]
ENDS = [2.46, 4.16, 6.62, 8.74, 10.4, 12.84, 15.14, 16.82, 19.18, 20.9, 22.52, 23.76, 25.72, 27.34, 29.26, 30.6, 32.48]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play()

    # Hàng trăm lý do cũng chẳng thể cứu vãn
    sync_words(song, LINES[0], ENDS[0], mode='karaoke', palette='hong')
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.1, shine, palette='hong')
    newline()

    # Biết sao hết cho vừa
    sync_words(song, LINES[1], ENDS[1], mode='pop', palette='hong')
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.3, breathe, palette='hong')
    gradient_fade_out('' + text(LINES[1]), 0.25, palette='hong')

    # Lòng nhau mới thấu đây em 💔
    sync_words(song, LINES[2], ENDS[2], mode='glide', palette='tim')
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.1, shine, palette='tim')
    newline()

    newline()  # hết đoạn

    # Trái tim anh chẳng còn cần thiết nữa
    sync_words(song, LINES[3], ENDS[3], mode='sparkle', palette='bien')
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, heartbeat, palette='bien')
    newline()

    # Nói chi đến đây cũng thừa
    sync_words(song, LINES[4], ENDS[4], mode='words', palette='hoanghon', indent=4)
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='hoanghon', indent=4)
    newline()

    # Rượu vang pha với cơn mưa
    sync_words(song, LINES[5], ENDS[5], mode='jump', palette='hoanghon')
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='hoanghon')
    newline()

    # Hàng trăm lý do cũng chẳng thể cứu vãn
    sync_words(song, LINES[6], ENDS[6], mode='scramble', palette='bac')
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.1, shine, palette='bac')
    newline()

    # Biết sao hết cho vừa
    sync_words(song, LINES[7], ENDS[7], mode='sides', palette='bac')
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.1, breathe, palette='bac')
    newline()

    # Lòng nhau mới thấu đây em
    sync_words(song, LINES[8], ENDS[8], mode='drop', palette='hong', indent=4)
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.1, shine, palette='hong', indent=4)
    newline()

    # Dệt hàng triệu vết thương,
    sync_words(song, LINES[9], ENDS[9], mode='spotlight', palette='hong')
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.1, heartbeat, palette='hong')
    newline()

    # Tự vùi mình trước gương
    sync_words(song, LINES[10], ENDS[10], mode='wave', palette='tim', indent=4)
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.1, shine, palette='tim', indent=4)
    newline()

    # Nhìn một người đã từng thương
    sync_words(song, LINES[11], ENDS[11], mode='converge', palette='tim')
    hold(song, text(LINES[11]), LINES[12][0][1] - 0.1, heartbeat, palette='tim')
    newline()

    # Sao nay xa lạ đến bất thường
    sync_words(song, LINES[12], ENDS[12], mode='typo', palette='bien', indent=4)
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.1, shine, palette='bien', indent=4)
    newline()

    # Cố gắng cũng chỉ bằng không
    sync_words(song, LINES[13], ENDS[13], mode='hearts', palette='bien')
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.1, breathe, palette='bien')
    newline()

    # nước mắt ngược dòng
    sync_words(song, LINES[14], ENDS[14], mode='slide', palette='hoanghon', indent=4)
    hold(song, text(LINES[14]), LINES[15][0][1] - 0.1, shine, palette='hoanghon', indent=4)
    newline()

    # Chảy ngược tận sâu bên trong
    sync_words(song, LINES[15], ENDS[15], mode='center', palette='hoanghon')
    hold(song, text(LINES[15]), LINES[16][0][1] - 0.1, breathe, palette='hoanghon')
    newline()

    # nghẹn đắng nơi lồng ngực
    sync_words(song, LINES[16], ENDS[16], mode='rise', palette='bac', indent=8)
    hold(song, text(LINES[16]), ENDS[16] + 1.5, heartbeat, palette='bac', indent=8)
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
