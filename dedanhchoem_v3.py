import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = True
set_color(COLOR)

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7703131611524582664.mp3'), offset=OFFSET)

LINES = [
    [('Vì', 0.0), ('anh', 0.44), ('vẫn', 0.74), ('sẽ', 0.9), ('trao', 1.14), ('niềm', 1.28), ('tin', 1.44), ('vào', 1.6), ('em', 1.74)],
    [('Dù', 2.1), ('mong', 2.4), ('manh', 2.88)],
    [('Nhẹ', 3.68), ('tay', 4.04), ('chút', 4.36), ('nhé', 4.68)],
    [('Chân', 5.02), ('thành', 5.22), ('vẫn', 5.38), ('còn', 5.58), ('đọng', 5.78), ('lại', 6.1), ('trong', 6.32), ('anh', 6.66)],
    [('Biến', 7.42), ('nhau', 8.06), ('thành', 8.36), ('những', 8.68), ('thói', 9.66), ('quen', 10.62)],
    [('Gửi', 11.28), ('trái', 11.64), ('tim', 11.92), ('ở', 12.2), ('đó,', 12.7), ('nơi', 13.6), ('em', 14.6)],
    [('Baby', 16.48), ('em', 16.88), ('đâu', 17.12), ('òi', 17.28)],
    [('Nhanh', 17.64), ('lên', 17.8), ('anh', 17.92), ('đang', 18.06), ('đợi', 18.24)],
    [('Anh', 18.56), ('solo', 18.74), ('với', 19.06), ('đời', 19.26)],
    [('Biết', 19.64), ('bao', 19.72), ('nhiêu', 19.92), ('năm', 20.04), ('giời', 20.26)],
    [('Hôm', 20.48), ('nay', 20.74), ('anh', 20.86), ('đang', 21.04), ('ngầu', 21.18)],
    [('Trông', 21.58), ('ăn', 21.74), ('chơi', 21.79), ('quá', 21.84), ('trời', 21.88)],
    [('Trên', 22.24), ('con', 23.24), ('xe', 23.24), ('wave', 23.24), ('tàu', 23.24)],
    [('Chỉ', 23.42), ('là', 23.7), ('mình', 23.86), ('chờ', 24.02), ('gặp', 24.16), ('cô', 24.32), ('bé', 24.56)],
    [('Nói', 24.7), ('câu', 24.84), ('xin', 25.0), ('chào', 25.24)],
    [('Khóa', 25.42), ('trái', 25.7), ('tim', 25.82), ('anh', 26.02), ('lại', 26.16)],
    [('Xinh', 26.58), ('gái', 26.68), ('với', 26.8), ('đa', 26.96), ('tài', 27.2)],
    [('Nhõng', 27.42), ('nhẽo', 27.7), ('bên', 27.88), ('anh', 27.98), ('hoài', 28.16)],
    [('Còn', 28.28), ('anh', 28.46), ('có', 28.62), ('huy', 28.78), ('chương', 28.96), ('vàng', 29.12)],
    [('Bộ', 29.34), ('môn', 29.44), ('nhắn', 29.64), ('tin', 29.76), ('siêu', 29.92), ('xàm', 30.16)],
    [('Ngồi', 30.32), ('viết', 30.44), ('tiếp', 30.66), ('lên', 30.78), ('trang', 30.92), ('dài', 31.12)],
    [('Để', 31.26), ('duyên', 31.5), ('số', 31.62), ('ta', 31.72), ('an', 31.92), ('bài', 32.1)],
    [('Vì', 32.22), ('bên', 32.36), ('em', 32.6), ('anh', 32.8), ('lạc', 32.92), ('trong', 33.06), ('tình', 33.22), ('yêu', 33.42)],
    [('Mà', 33.56), ('không', 33.74), ('phải', 33.92), ('chơi', 34.1), ('vơi', 34.54)],
    [('Ông', 35.56), ('trời', 35.96), ('giấu', 36.12), ('em', 36.82), ('đi', 37.02), ('đâu', 37.16)],
    [('Sao', 37.36), ('mà', 37.52), ('giờ', 37.68), ('này', 37.88), ('mới', 38.0), ('tới', 38.44)],
    [('Vậy', 39.1), ('cớ', 39.38), ('sao', 39.6), ('em', 39.74), ('phải', 39.88), ('chần', 40.0), ('chừ', 40.28), ('mãi', 40.38)],
    [('Để', 40.76), ('dựa', 40.95), ('đầu', 41.04), ('vào', 41.18), ('vai', 41.42)],
    [('Của', 41.64), ('một', 41.86), ('chàng', 42.1), ('đẹp', 42.24), ('trai', 42.44)],
    [('Mặc', 43.72), ('kệ', 43.8), ('sự', 43.96), ('sợ', 44.14), ('hãi,', 44.4)],
    [('Everything', 44.74), ('will', 45.2), ('be', 45.7), ('alright', 45.98), ('baby', 46.6)],
    [('Hoá', 47.16), ('ra', 48.4), ('em', 48.62), ('đây', 48.62), ('rồi', 48.84)],
    [('Người', 50.76), ('chở', 51.16), ('che', 51.44), ('con', 51.78), ('tim', 52.14), ('chỉ', 52.74), ('sợ', 53.28), ('đánh', 53.8), ('mất', 54.26)],
    [('Bước', 54.46), ('ra', 55.5), ('từ', 55.82), ('trong', 56.16), ('những', 57.48), ('giấc', 57.8), ('mơ', 58.14)],
    [('Rồi', 58.4), ('lại', 58.76), ('hằn', 59.08), ('vào', 59.5), ('trí', 59.94), ('nhớ', 60.18)],
    [('Đến', 61.28), ('bao', 61.84), ('giờ?', 62.22)],
]
ENDS = [2.1, 3.68, 5.02, 7.42, 11.28, 15.4, 17.54, 18.56, 19.5, 20.48, 21.48, 22.0, 23.42, 24.7, 25.42, 26.4, 27.42, 28.28, 29.34, 30.32, 31.26, 32.22, 33.56, 35.1, 37.36, 39.1, 40.72, 41.64, 43.6, 44.74, 47.16, 50.18, 54.46, 58.4, 60.52, 62.54]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play()

    # Vì anh vẫn sẽ trao niềm tin vào em
    sync_words(song, LINES[0], ENDS[0], mode='karaoke', palette='hong')
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.3, breathe, palette='hong')
    gradient_fade_out('' + text(LINES[0]), 0.2, palette='hong')

    # Dù mong manh
    sync_words(song, LINES[1], ENDS[1], mode='pop', palette='hong', indent=8)
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.3, breathe, palette='hong', indent=8)
    gradient_fade_out('        ' + text(LINES[1]), 0.2, palette='hong')

    # Nhẹ tay chút nhé
    sync_words(song, LINES[2], ENDS[2], mode='slide', palette='tim', indent=8)
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.1, shine, palette='tim', indent=8)
    newline()

    # Chân thành vẫn còn đọng lại trong anh
    sync_words(song, LINES[3], ENDS[3], mode='reveal', palette='tim')
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim')
    newline()

    # Biến nhau thành những thói quen
    sync_words(song, LINES[4], ENDS[4], mode='jump', palette='bien')
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='bien')
    newline()

    # Gửi trái tim ở đó, nơi em
    sync_words(song, LINES[5], ENDS[5], mode='scramble', palette='bien')
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='bien')
    newline()

    # Baby em đâu òi
    sync_words(song, LINES[6], ENDS[6], mode='pop', palette='hoanghon', indent=4)
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.3, breathe, palette='hoanghon', indent=4)
    gradient_fade_out('    ' + text(LINES[6]), 0.2, palette='hoanghon')

    # Nhanh lên anh đang đợi
    sync_words(song, LINES[7], ENDS[7], mode='pop', palette='hoanghon')
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.3, breathe, palette='hoanghon')
    gradient_fade_out('' + text(LINES[7]), 0.2, palette='hoanghon')

    # Anh solo với đời
    sync_words(song, LINES[8], ENDS[8], mode='converge', palette='bac', indent=4)
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.3, breathe, palette='bac', indent=4)
    gradient_fade_out('    ' + text(LINES[8]), 0.2, palette='bac')

    # Biết bao nhiêu năm giời
    sync_words(song, LINES[9], ENDS[9], mode='typewriter', palette='bac')
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.3, breathe, palette='bac')
    gradient_fade_out('' + text(LINES[9]), 0.2, palette='bac')

    # Hôm nay anh đang ngầu
    sync_words(song, LINES[10], ENDS[10], mode='pop', palette='hong', indent=4)
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.3, breathe, palette='hong', indent=4)
    gradient_fade_out('    ' + text(LINES[10]), 0.2, palette='hong')

    # Trông ăn chơi quá trời
    sync_words(song, LINES[11], ENDS[11], mode='pop', palette='hong')
    hold(song, text(LINES[11]), LINES[12][0][1] - 0.3, breathe, palette='hong')
    gradient_fade_out('' + text(LINES[11]), 0.2, palette='hong')

    # Trên con xe wave tàu
    sync_words(song, LINES[12], ENDS[12], mode='rainbow', palette='tim')
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.1, shine, palette='tim')
    newline()

    # Chỉ là mình chờ gặp cô bé
    sync_words(song, LINES[13], ENDS[13], mode='flicker', palette='tim')
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.3, breathe, palette='tim')
    gradient_fade_out('' + text(LINES[13]), 0.2, palette='tim')

    # Nói câu xin chào
    sync_words(song, LINES[14], ENDS[14], mode='karaoke', palette='bien')
    hold(song, text(LINES[14]), LINES[15][0][1] - 0.1, shine, palette='bien')
    newline()

    # Khóa trái tim anh lại
    sync_words(song, LINES[15], ENDS[15], mode='bounce', palette='bien')
    hold(song, text(LINES[15]), LINES[16][0][1] - 0.1, breathe, palette='bien')
    newline()

    # Xinh gái với đa tài
    sync_words(song, LINES[16], ENDS[16], mode='slide', palette='hoanghon', indent=1)
    hold(song, text(LINES[16]), LINES[17][0][1] - 0.1, shine, palette='hoanghon', indent=1)
    newline()

    # Nhõng nhẽo bên anh hoài
    sync_words(song, LINES[17], ENDS[17], mode='reveal', palette='hoanghon')
    hold(song, text(LINES[17]), LINES[18][0][1] - 0.1, breathe, palette='hoanghon')
    newline()

    # Còn anh có huy chương vàng
    sync_words(song, LINES[18], ENDS[18], mode='jump', palette='bac')
    hold(song, text(LINES[18]), LINES[19][0][1] - 0.1, shine, palette='bac')
    newline()

    # Bộ môn nhắn tin siêu xàm
    sync_words(song, LINES[19], ENDS[19], mode='scramble', palette='bac', indent=4)
    hold(song, text(LINES[19]), LINES[20][0][1] - 0.1, breathe, palette='bac', indent=4)
    newline()

    # Ngồi viết tiếp lên trang dài
    sync_words(song, LINES[20], ENDS[20], mode='drop', palette='hong')
    hold(song, text(LINES[20]), LINES[21][0][1] - 0.1, shine, palette='hong')
    newline()

    # Để duyên số ta an bài
    sync_words(song, LINES[21], ENDS[21], mode='wave', palette='hong', indent=4)
    hold(song, text(LINES[21]), LINES[22][0][1] - 0.1, breathe, palette='hong', indent=4)
    newline()

    # Vì bên em anh lạc trong tình yêu
    sync_words(song, LINES[22], ENDS[22], mode='converge', palette='tim')
    hold(song, text(LINES[22]), LINES[23][0][1] - 0.1, shine, palette='tim')
    newline()

    # Mà không phải chơi vơi
    sync_words(song, LINES[23], ENDS[23], mode='typewriter', palette='tim', indent=4)
    hold(song, text(LINES[23]), LINES[24][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Ông trời giấu em đi đâu
    sync_words(song, LINES[24], ENDS[24], mode='pop', palette='bien')
    hold(song, text(LINES[24]), LINES[25][0][1] - 0.3, breathe, palette='bien')
    gradient_fade_out('' + text(LINES[24]), 0.2, palette='bien')

    # Sao mà giờ này mới tới
    sync_words(song, LINES[25], ENDS[25], mode='pop', palette='bien')
    hold(song, text(LINES[25]), LINES[26][0][1] - 0.1, breathe, palette='bien')
    newline()

    # Vậy cớ sao em phải chần chừ mãi
    sync_words(song, LINES[26], ENDS[26], mode='rainbow', palette='hoanghon')
    hold(song, text(LINES[26]), LINES[27][0][1] - 0.1, shine, palette='hoanghon')
    newline()

    # Để dựa đầu vào vai
    sync_words(song, LINES[27], ENDS[27], mode='flicker', palette='hoanghon', indent=4)
    hold(song, text(LINES[27]), LINES[28][0][1] - 0.1, breathe, palette='hoanghon', indent=4)
    newline()

    # Của một chàng đẹp trai
    sync_words(song, LINES[28], ENDS[28], mode='karaoke', palette='bac', indent=8)
    hold(song, text(LINES[28]), LINES[29][0][1] - 0.1, shine, palette='bac', indent=8)
    newline()

    # Mặc kệ sự sợ hãi,
    sync_words(song, LINES[29], ENDS[29], mode='bounce', palette='bac')
    hold(song, text(LINES[29]), LINES[30][0][1] - 0.1, breathe, palette='bac')
    newline()

    # Everything will be alright baby
    sync_words(song, LINES[30], ENDS[30], mode='slide', palette='hong', indent=4)
    hold(song, text(LINES[30]), LINES[31][0][1] - 0.1, shine, palette='hong', indent=4)
    newline()

    # Hoá ra em đây rồi
    sync_words(song, LINES[31], ENDS[31], mode='reveal', palette='hong')
    hold(song, text(LINES[31]), LINES[32][0][1] - 0.1, breathe, palette='hong')
    newline()

    # Người chở che con tim chỉ sợ đánh mất
    sync_words(song, LINES[32], ENDS[32], mode='jump', palette='tim')
    hold(song, text(LINES[32]), LINES[33][0][1] - 0.1, shine, palette='tim')
    newline()

    # Bước ra từ trong những giấc mơ
    sync_words(song, LINES[33], ENDS[33], mode='scramble', palette='tim')
    hold(song, text(LINES[33]), LINES[34][0][1] - 0.1, breathe, palette='tim')
    newline()

    # Rồi lại hằn vào trí nhớ
    sync_words(song, LINES[34], ENDS[34], mode='pop', palette='bien')
    hold(song, text(LINES[34]), LINES[35][0][1] - 0.3, breathe, palette='bien')
    gradient_fade_out('' + text(LINES[34]), 0.2, palette='bien')

    # Đến bao giờ?
    sync_words(song, LINES[35], ENDS[35], mode='pop', palette='bien', indent=8)
    hold(song, text(LINES[35]), ENDS[35] + 1.5, heartbeat, palette='bien', indent=8)
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
