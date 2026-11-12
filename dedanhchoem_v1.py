import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = False
set_color(COLOR)

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7706420703083515156.mp3'), offset=OFFSET)

LINES = [
    [('Mùa', 1.18), ('đông', 1.78), ('ghé', 2.16), ('tới', 2.62)],
    [('Lá', 3.56), ('vàng', 4.16), ('rơi', 4.56), ('đầy', 4.88), ('rồi', 5.36), ('lại', 5.36), ('bay', 5.54), ('vèo', 5.86)],
    [('Vội', 6.24), ('lướt', 6.46), ('qua', 6.88), ('anh', 7.06)],
    [('như', 7.22), ('những', 7.3), ('cuộc', 7.5), ('tình', 7.86), ('chóng', 8.12), ('vánh', 8.6)],
    [('Cặp', 9.24), ('tình', 9.8), ('nhân', 10.08), ('nói', 10.36), ('cười', 10.74)],
    [('lượn', 11.1), ('đi', 11.44), ('đâu', 11.74), ('loanh', 12.08), ('quanh', 12.54)],
    [('Lại', 13.26), ('càng', 13.38), ('làm', 13.62), ('anh', 13.78), ('thấy', 13.9), ('ngứa', 14.04), ('mắt', 14.52), ('ghê', 14.76)],
    [('sao', 15.02), ('mình', 15.22), ('hoài', 15.42), ('không', 15.7), ('biết', 16.04), ('cách', 16.42)],
    [('À', 16.96), ('thì', 17.42), ('là', 17.56), ('vì', 17.7), ('ngoài', 17.82), ('kia', 18.0), ('còn', 18.14), ('bao', 18.36), ('người', 18.68)],
    [('Họ', 19.12), ('lãng', 19.34), ('mạn', 19.78)],
    [('Là', 20.08), ('zai', 20.4), ('đẹp,', 20.76)],
    [('Hoặc', 21.26), ('siêu', 21.38), ('giàu', 21.74)],
    [('Chẳng', 22.1), ('khó', 22.28), ('gì', 22.6), ('để', 22.78), ('tìm', 22.94), ('được', 23.16), ('một', 23.3), ('người', 23.58), ('hơn', 23.92), ('anh', 24.28)],
    [('Ngày', 25.08), ('xưa', 25.56)],
    [('anh', 25.9), ('cũng', 26.2), ('đã', 26.48), ('ngu', 26.48), ('ngơ', 26.8), ('trao', 26.94), ('đi', 27.18), ('con', 27.3), ('tim', 27.6), ('chân', 27.94), ('thành', 28.32)],
    [('Mà', 28.96), ('họ', 29.62), ('lại', 29.96), ('cứ', 30.18), ('đánh', 30.4), ('rơi', 30.58)],
    [('để', 30.74), ('hi', 30.98), ('vọng', 30.98), ('nơi', 31.34), ('anh', 31.58), ('tan', 31.92), ('tành', 32.3)],
]
ENDS = [3.56, 6.24, 7.22, 9.24, 11.1, 13.26, 15.02, 16.96, 19.12, 20.08, 21.18, 22.1, 25.08, 25.9, 28.96, 30.74, 32.9]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    signature()  # Shinn🐣
    song.play()

    # Mùa đông ghé tới
    sync_words(song, LINES[0], ENDS[0], mode='karaoke', palette='hong')
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.1, shine, palette='hong')
    newline()

    # Lá vàng rơi đầy  rồi lại bay vèo
    sync_words(song, LINES[1], ENDS[1], mode='bounce', palette='hong')
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, breathe, palette='hong')
    newline()

    # Vội lướt qua anh
    sync_words(song, LINES[2], ENDS[2], mode='slide', palette='tim')
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.1, shine, palette='tim')
    newline()

    # như những cuộc tình chóng vánh
    sync_words(song, LINES[3], ENDS[3], mode='reveal', palette='tim', indent=4)
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Cặp tình nhân nói cười
    sync_words(song, LINES[4], ENDS[4], mode='jump', palette='bien')
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='bien')
    newline()

    # lượn đi đâu loanh quanh
    sync_words(song, LINES[5], ENDS[5], mode='letters', palette='bien', indent=4)
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='bien', indent=4)
    newline()

    # Lại càng làm anh thấy ngứa mắt ghê
    sync_words(song, LINES[6], ENDS[6], mode='drop', palette='hoanghon')
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.1, shine, palette='hoanghon')
    newline()

    # sao mình hoài không biết cách
    sync_words(song, LINES[7], ENDS[7], mode='wave', palette='hoanghon', indent=8)
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.1, breathe, palette='hoanghon', indent=8)
    newline()

    # À thì là vì ngoài kia còn bao người
    sync_words(song, LINES[8], ENDS[8], mode='converge', palette='bac')
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.1, shine, palette='bac')
    newline()

    # Họ lãng mạn
    sync_words(song, LINES[9], ENDS[9], mode='typewriter', palette='bac', indent=4)
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.3, breathe, palette='bac', indent=4)
    gradient_fade_out('    ' + text(LINES[9]), 0.2, palette='bac')

    # Là zai đẹp,
    sync_words(song, LINES[10], ENDS[10], mode='pop', palette='hong', indent=4)
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.3, breathe, palette='hong', indent=4)
    gradient_fade_out('    ' + text(LINES[10]), 0.2, palette='hong')

    # Hoặc siêu giàu
    sync_words(song, LINES[11], ENDS[11], mode='pop', palette='hong', indent=4)
    hold(song, text(LINES[11]), LINES[12][0][1] - 0.1, breathe, palette='hong', indent=4)
    newline()

    # Chẳng khó gì để tìm được một người hơn anh
    sync_words(song, LINES[12], ENDS[12], mode='rainbow', palette='tim')
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.1, shine, palette='tim')
    newline()

    # Ngày xưa
    sync_words(song, LINES[13], ENDS[13], mode='flicker', palette='tim')
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.1, breathe, palette='tim')
    newline()

    # anh cũng đã ngu ngơ trao đi con tim  chân thành
    sync_words(song, LINES[14], ENDS[14], mode='karaoke', palette='bien', indent=4)
    hold(song, text(LINES[14]), LINES[15][0][1] - 0.1, shine, palette='bien', indent=4)
    newline()

    # Mà họ lại  cứ đánh rơi
    sync_words(song, LINES[15], ENDS[15], mode='bounce', palette='bien')
    hold(song, text(LINES[15]), LINES[16][0][1] - 0.1, breathe, palette='bien')
    newline()

    # để hi vọng nơi anh tan tành
    sync_words(song, LINES[16], ENDS[16], mode='slide', palette='hoanghon', indent=4)
    hold(song, text(LINES[16]), ENDS[16] + 1.5, heartbeat, palette='hoanghon', indent=4)
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
