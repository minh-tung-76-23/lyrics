import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = True
set_color(COLOR)
# True = tô vàng tên riêng (từ viết hoa giữa câu)
ACCENT = True
set_accent(ACCENT)

# Phát nhạc từ giây thứ START của bài
START = 0.0

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7709672691334237447.mp3'), offset=OFFSET)

LINES = [
    [('Em', 0.0), ('là', 0.72), ('YeaH1', 0.86)],
    [('Thì', 1.3), ('anh', 1.46), ('là', 1.64), ('Gai', 1.78), ('Con', 2.2)],
    [('Em', 2.76), ('mà', 3.08), ('uốn', 3.18), ('tóc', 3.5)],
    [('Thì', 3.62), ('anh', 3.74), ('là', 3.9), ('Salon', 4.12)],
    [('Em', 5.0), ('là', 5.4), ('Rê', 5.48), ('Mi', 5.84)],
    [('Thì', 5.92), ('anh', 6.02), ('là', 6.18), ('Fa', 6.44), ('Sol', 6.84)],
    [('Em', 7.18), ('là', 7.64), ('T1', 7.76)],
    [('Thì', 8.18), ('anh', 8.3), ('là', 8.52), ('Baron', 8.76)],
    [('Em', 9.42), ('là', 9.94), ('Bieber', 10.06)],
    [('thì', 10.46), ('anh', 10.62), ('là', 10.8), ('Baby', 10.94)],
    [('Em', 11.72), ('là', 12.2), ('thằng', 12.32), ('điên', 12.62)],
    [('thì', 12.8), ('anh', 12.9), ('là', 13.06), ('JayTee', 13.22)],
    [('Em', 14.38), ('mà', 14.5), ('lấy', 14.64), ('hơi', 14.82)],
    [('thì', 15.04), ('anh', 15.18), ('là', 15.34), ('LK', 15.46)],
    [('LadyKillah…', 16.18), ('Can', 17.11), ('you', 17.45), ('feel', 17.78), ('me?', 18.21)],
    [('Em', 18.46), ('là', 18.71), ('cô', 18.96), ('giáo', 19.22)],
    [('Thì', 19.64), ('anh', 19.76), ('sẽ', 19.92), ('lưu', 20.08), ('ban', 20.54)],
    [('Đá', 20.98), ('người', 21.38), ('yêu', 21.48), ('cũ', 21.76)],
    [('Anh', 22.0), ('là', 22.18), ('Liu', 22.34), ('Kang', 22.82)],
    [('Em', 23.1), ('là', 23.62), ('Tiến', 23.74), ('Luật', 24.1)],
    [('thì', 24.18), ('anh', 24.3), ('là', 24.48), ('Thu', 24.64), ('Trang', 25.18)],
    [('Em', 25.38), ('là', 25.7), ('ôi', 25.74), ('thôi', 26.02), ('chết', 26.06)],
    [('thì', 26.52), ('anh', 26.62), ('là', 26.84), ('Hương', 26.96), ('Giang', 27.42)],
    [('Em', 27.92), ('mà', 28.22), ('thích', 28.32), ('diss', 28.58)],
    [('thì', 28.78), ('a', 28.88), ('là', 29.08), ('YC', 29.24)],
    [('Nhà', 29.96), ('em', 30.26), ('hẻm', 30.38), ('48', 30.72)],
    [('thì', 31.04), ('anh', 31.2), ('là', 31.4), ('Wowy', 31.54)],
    [('Em', 32.18), ('là', 32.74), ('sân', 32.9), ('bay', 33.16)],
    [('thì', 33.34), ('anh', 33.46), ('là', 33.64), ('Vali', 33.84)],
    [('Em', 34.5), ('mà', 34.9), ('biểu', 35.22), ('tình', 35.42)],
    [('thì', 35.62), ('anh', 35.78), ('là', 35.98), ('Paris', 36.26)],
]
ENDS = [1.3, 2.76, 3.62, 5.0, 5.94, 7.18, 8.18, 9.42, 10.46, 11.72, 12.8, 14.38, 15.04, 16.18, 18.46, 19.64, 20.98, 22.0, 23.1, 24.2, 25.38, 26.52, 27.92, 28.78, 29.96, 31.04, 32.18, 33.34, 34.5, 35.62, 36.74]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    # signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play(start=START)

    # Em là YeaH1   [swipe: bạn chọn]
    sync_words(song, LINES[0], ENDS[0], mode='swipe', palette='hong', indent=8)
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.1, shine, palette='hong', indent=8)
    newline()

    # Thì anh là Gai Con   [shake: bạn chọn]
    sync_words(song, LINES[1], ENDS[1], mode='shake', palette='hong', indent=4)
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, breathe, palette='hong', indent=4)
    newline()

    # Em mà uốn tóc   [wave: bạn chọn]
    sync_words(song, LINES[2], ENDS[2], mode='wave', palette='tim', indent=8)
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.1, shine, palette='tim', indent=8)
    newline()

    # Thì anh là Salon   [sparkle: bạn chọn]
    sync_words(song, LINES[3], ENDS[3], mode='sparkle', palette='tim', indent=12)
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim', indent=12)
    newline()

    # Em là Rê Mi   [bounce: bạn chọn]
    sync_words(song, LINES[4], ENDS[4], mode='bounce', palette='bien', indent=8)
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='bien', indent=8)
    newline()

    # Thì anh là Fa Sol   [jump: bạn chọn]
    sync_words(song, LINES[5], ENDS[5], mode='jump', palette='bien', indent=4)
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='bien', indent=4)
    newline()

    # Em là T1   [glitch: bạn chọn]
    sync_words(song, LINES[6], ENDS[6], mode='glitch', palette='hoanghon', indent=8)
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.3, breathe, palette='hoanghon', indent=8)
    gradient_fade_out('        ' + text(LINES[6]), 0.25, palette='hoanghon')

    # Thì anh là Baron   [shake: bạn chọn]
    sync_words(song, LINES[7], ENDS[7], mode='shake', palette='hoanghon', indent=8)
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.3, breathe, palette='hoanghon', indent=8)
    dissolve_out('        ' + text(LINES[7]), 0.25, palette='hoanghon')

    # Em là Bieber   [swipe: bạn chọn]
    sync_words(song, LINES[8], ENDS[8], mode='swipe', palette='bac', indent=8)
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.3, breathe, palette='bac', indent=8)
    center_out('        ' + text(LINES[8]), 0.25, palette='bac')

    # thì anh là Baby   [hearts: bạn chọn]
    sync_words(song, LINES[9], ENDS[9], mode='hearts', palette='bac', indent=12)
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.1, breathe, palette='bac', indent=12)
    newline()

    # Em là thằng điên   [scramble: bạn chọn]
    sync_words(song, LINES[10], ENDS[10], mode='scramble', palette='hong', indent=4)
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.1, shine, palette='hong', indent=4)
    newline()

    # thì anh là JayTee   [slide: bạn chọn]
    sync_words(song, LINES[11], ENDS[11], mode='slide', palette='hong', indent=8)
    hold(song, text(LINES[11]), LINES[12][0][1] - 0.1, breathe, palette='hong', indent=8)
    newline()

    # Em mà lấy hơi   [rise: bạn chọn]
    sync_words(song, LINES[12], ENDS[12], mode='rise', palette='tim', indent=4)
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.1, shine, palette='tim', indent=4)
    newline()

    # thì anh là LK   [shake: bạn chọn]
    sync_words(song, LINES[13], ENDS[13], mode='shake', palette='tim', indent=8)
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.1, breathe, palette='tim', indent=8)
    newline()

    # LadyKillah… Can you feel me?   [showtime: bạn chọn]
    sync_words(song, LINES[14], ENDS[14], mode='showtime', palette='bien', indent=4)
    hold(song, text(LINES[14]), LINES[15][0][1] - 0.1, shine, palette='bien', indent=4)
    newline()

    song.at(LINES[15][0][1] - 0.15)
    clear_screen(keep_signature=False) # [clear] -> xoá màn hình, chạy lại từ dòng đầu

    # Em là cô giáo   [typewriter: bạn chọn]
    sync_words(song, LINES[15], ENDS[15], mode='typewriter', palette='bien', indent=8)
    hold(song, text(LINES[15]), LINES[16][0][1] - 0.1, breathe, palette='bien', indent=8)
    newline()

    # Thì anh sẽ lưu ban   [drop: bạn chọn]
    sync_words(song, LINES[16], ENDS[16], mode='drop', palette='hoanghon', indent=4)
    hold(song, text(LINES[16]), LINES[17][0][1] - 0.1, shine, palette='hoanghon', indent=4)
    newline()

    # Đá người yêu cũ   [shake: bạn chọn]
    sync_words(song, LINES[17], ENDS[17], mode='shake', palette='hoanghon', indent=4)
    hold(song, text(LINES[17]), LINES[18][0][1] - 0.3, breathe, palette='hoanghon', indent=4)
    sweep_out('    ' + text(LINES[17]), 0.25, palette='hoanghon')

    # Anh là Liu Kang   [fire: bạn chọn]
    sync_words(song, LINES[18], ENDS[18], mode='fire', palette='bac', indent=4)
    hold(song, text(LINES[18]), LINES[19][0][1] - 0.3, breathe, palette='bac', indent=4)
    drift_out('    ' + text(LINES[18]), 0.25, palette='bac')

    # Em là Tiến Luật   [swipe: bạn chọn]
    sync_words(song, LINES[19], ENDS[19], mode='swipe', palette='bac', indent=4)
    hold(song, text(LINES[19]), LINES[20][0][1] - 0.1, breathe, palette='bac', indent=4)
    newline()

    # thì anh là Thu Trang   [hearts: bạn chọn]
    sync_words(song, LINES[20], ENDS[20], mode='hearts', palette='hong', indent=8)
    hold(song, text(LINES[20]), LINES[21][0][1] - 0.1, shine, palette='hong', indent=8)
    newline()

    # Em là ôi thôi chết   [flicker: bạn chọn]
    sync_words(song, LINES[21], ENDS[21], mode='flicker', palette='hong', indent=4)
    hold(song, text(LINES[21]), LINES[22][0][1] - 0.1, breathe, palette='hong', indent=4)
    newline()

    # thì anh là Hương Giang   [sparkle: bạn chọn]
    sync_words(song, LINES[22], ENDS[22], mode='sparkle', palette='tim', indent=8)
    hold(song, text(LINES[22]), LINES[23][0][1] - 0.1, shine, palette='tim', indent=8)
    newline()

    # Em mà thích diss   [glitch: bạn chọn]
    sync_words(song, LINES[23], ENDS[23], mode='glitch', palette='tim', indent=8)
    hold(song, text(LINES[23]), LINES[24][0][1] - 0.1, breathe, palette='tim', indent=8)
    newline()

    # thì a là YC   [shake: bạn chọn]
    sync_words(song, LINES[24], ENDS[24], mode='shake', palette='bien', indent=4)
    hold(song, text(LINES[24]), LINES[25][0][1] - 0.1, shine, palette='bien', indent=4)
    newline()

    # Nhà em hẻm 48   [swipe: bạn chọn]
    sync_words(song, LINES[25], ENDS[25], mode='swipe', palette='bien', indent=4)
    hold(song, text(LINES[25]), LINES[26][0][1] - 0.1, breathe, palette='bien', indent=4)
    newline()

    # thì anh là Wowy   [rainbow: bạn chọn]
    sync_words(song, LINES[26], ENDS[26], mode='rainbow', palette='hoanghon', indent=8)
    hold(song, text(LINES[26]), LINES[27][0][1] - 0.1, shine, palette='hoanghon', indent=8)
    newline()

    # Em là sân bay   [rise: bạn chọn]
    sync_words(song, LINES[27], ENDS[27], mode='rise', palette='hoanghon')
    hold(song, text(LINES[27]), LINES[28][0][1] - 0.1, breathe, palette='hoanghon')
    newline()

    # thì anh là Vali   [slide: bạn chọn]
    sync_words(song, LINES[28], ENDS[28], mode='slide', palette='bac', indent=4)
    hold(song, text(LINES[28]), LINES[29][0][1] - 0.1, shine, palette='bac', indent=4)
    newline()

    # Em mà biểu tình   [splash: bạn chọn]
    sync_words(song, LINES[29], ENDS[29], mode='splash', palette='bac', indent=8)
    hold(song, text(LINES[29]), LINES[30][0][1] - 0.1, breathe, palette='bac', indent=8)
    newline()

    # thì anh là Paris   [starfall: bạn chọn]
    sync_words(song, LINES[30], ENDS[30], mode='starfall', palette='hong', indent=12)
    hold(song, text(LINES[30]), ENDS[30] + 1.5, heartbeat, palette='hong', indent=12)
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
