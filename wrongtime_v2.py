import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = False
set_color(COLOR)

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7699048007752486162.mp3'), offset=OFFSET)

LINES = [
    [('Em', 0.0), ('quay', 0.0), ('đi', 0.32), ('ta', 0.52), ('mất', 0.74), ('nhau', 0.98)],
    [('Yêu', 1.56), ('thương', 1.78), ('kia', 1.98), ('đành', 2.2), ('cất', 2.36), ('sâu', 2.62)],
    [('Yeah', 3.36), ('con', 3.36), ('tim', 3.6), ('anh', 3.78), ('đã', 3.95), ('rất', 3.98), ('đau', 4.24)],
    [('Đi', 4.38), ('nơi', 4.6), ('đâu', 4.82), ('để', 5.0), ('có', 5.0), ('phép', 5.16), ('nhiệm', 5.4), ('màu', 5.64)],
    [('Anh', 6.36), ('không', 6.58), ('muốn', 6.86), ('phải', 7.02), ('níu', 7.26), ('đâu', 7.48)],
    [('hai', 8.18), ('ta', 8.24), ('chưa', 8.42), ('từng', 8.64), ('hiểu', 8.86), ('nhau', 9.14)],
    [('Cứ', 9.5), ('chạy', 9.88), ('đi', 10.1), ('tìm', 10.3), ('nơi', 10.3), ('mà', 10.68), ('em', 10.86), ('thấy', 11.14), ('em', 11.3), ('thuộc', 11.52), ('về', 11.7)],
    [('Mặc', 12.08), ('kệ', 12.34), ('những', 12.52), ('tiếc', 12.76), ('nuối', 12.98), ('tìm', 13.2), ('tới', 13.92), ('khi', 13.92), ('mưa', 13.92), ('cùng', 13.92), ('rơi', 14.2)],
    [('Cơn', 14.58), ('đau', 15.0), ('kia', 15.12), ('anh', 15.32), ('nhận', 15.56), ('lấy', 15.74), ('riêng', 15.94), ('anh', 16.22), ('mà', 16.36), ('thôi', 16.54)],
    [('Em', 16.8), ('đâu', 17.02), ('cần', 17.16), ('quay', 17.36), ('đầu', 17.72), ('lại', 18.06)],
    [('Và', 18.28), ('chỉ', 18.48), ('cần', 18.56), ('một', 18.7), ('lần', 18.8), ('cuối', 18.98), ('gỡ', 19.22), ('những', 19.38), ('nút', 19.58), ('thắt', 19.84), ('quên', 19.98), ('đi', 20.18), ('mắt', 20.42), ('môi', 20.86)],
    [('Ba', 21.3), ('năm', 21.62), ('mươi', 21.82), ('xé', 22.08), ('đôi', 22.52)],
    [('Cơn', 22.98), ('đau', 23.28), ('kia', 23.42), ('sẽ', 23.66), ('nguôi', 24.16)],
    [('Bởi', 24.5), ('vì', 24.64), ('anh', 24.66), ('cũng', 24.94), ('sẽ', 25.12), ('phải', 25.28), ('quên', 25.46)],
    [('Liệu', 25.88), ('không', 26.28), ('cần', 26.5), ('em', 26.74), ('ở', 26.94), ('bên', 27.18)],
    [('Nhìn', 27.48), ('mưa', 27.94), ('lao', 28.12), ('đi', 28.38), ('trong', 28.52), ('đêm', 28.76)],
    [('Rồi', 29.2), ('lại', 29.52), ('lay', 29.74), ('lắt', 29.98), ('trên', 29.98), ('bậc', 30.08), ('thềm', 30.94)],
    [('Liệu', 31.04), ('rằng', 31.12), ('mưa', 31.12), ('sẽ', 31.32), ('cuốn', 31.52), ('nàng', 31.74), ('đi', 31.92)],
    [('Hoặc', 32.63), ('là', 32.74), ('vương', 32.9), ('ngay', 33.12), ('trên', 33.12), ('đôi', 33.32), ('mi', 33.88)],
    [('Chỉ', 34.12), ('là', 34.32), ('cô', 34.44), ('đơn', 34.68), ('anh', 34.88), ('mỗi', 35.02), ('khi', 35.22)],
    [('Khua', 36.04), ('tay', 36.28), ('anh', 36.46), ('giấu', 36.7), ('đi', 36.9)],
    [('Anh', 37.22), ('chỉ', 37.48), ('anh', 37.64), ('chỉ', 37.88), ('muốn', 38.04), ('được', 38.38), ('yên', 38.48), ('bình', 38.92)],
    [('Muốn', 39.26), ('có', 39.46), ('em', 39.62), ('của', 39.88), ('riêng', 40.08), ('mình', 40.54)],
    [('Em', 40.84), ('nói', 41.08), ('anh', 41.24), ('bị', 41.46), ('điên', 41.66), ('vì', 41.9), ('sự', 42.08), ('thật', 42.3), ('giờ', 42.5), ('đây', 42.76), ('có', 42.9), ('lẽ', 43.22)],
    [('Em', 43.64), ('giờ', 43.9), ('đang', 44.14), ('ở', 44.38), ('bên', 44.58), ('một', 44.72), ('ai', 44.98), ('rồi', 45.34)],
    [('Quên', 45.76), ('đi', 45.96), ('anh', 46.16), ('là', 46.34), ('ai', 46.56), ('rồi', 46.92)],
    [('Quay', 47.42), ('bước', 47.6), ('anh', 47.8), ('rời', 48.0), ('đi', 48.16), ('anh', 48.42), ('đâu', 48.64), ('hề', 48.86), ('muốn', 49.04), ('gây', 49.26), ('khó', 49.38), ('dễ', 49.72)],
]
ENDS = [1.48, 3.6, 4.38, 6.36, 7.96, 9.5, 12.08, 14.58, 16.8, 18.28, 21.3, 22.98, 24.5, 25.88, 27.48, 29.2, 31.04, 32.52, 34.18, 35.8, 37.22, 39.26, 40.84, 43.64, 45.76, 47.3, 49.82]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play()

    # Em quay đi ta mất nhau   [splash: fast]
    sync_words(song, LINES[0], ENDS[0], mode='splash', palette='hong')
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.3, breathe, palette='hong')
    gradient_fade_out('' + text(LINES[0]), 0.25, palette='hong')

    # Yêu thương kia đành cất sâu   [sides: đa dạng]
    sync_words(song, LINES[1], ENDS[1], mode='sides', palette='hong')
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, heartbeat, palette='hong')
    newline()

    # Yeah con tim anh đã rất đau   [words: fast]
    sync_words(song, LINES[2], ENDS[2], mode='words', palette='tim')
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.3, breathe, palette='tim')
    drift_out('' + text(LINES[2]), 0.25, palette='tim')

    # Đi nơi đâu để có phép nhiệm màu   [typo: fast, long]
    sync_words(song, LINES[3], ENDS[3], mode='typo', palette='tim')
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.3, breathe, palette='tim')
    center_out('' + text(LINES[3]), 0.25, palette='tim')

    # Anh không muốn phải níu đâu   [slide: fast]
    sync_words(song, LINES[4], ENDS[4], mode='slide', palette='bien', indent=2)
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='bien', indent=2)
    newline()

    # hai ta chưa từng hiểu nhau   [hearts: từ "hai ta"]
    sync_words(song, LINES[5], ENDS[5], mode='hearts', palette='bien', indent=6)
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='bien', indent=6)
    newline()

    # Cứ chạy đi tìm nơi mà em thấy em thuộc về   [glide: từ "chạy", long]
    sync_words(song, LINES[6], ENDS[6], mode='glide', palette='hoanghon')
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.3, breathe, palette='hoanghon')
    sweep_out('' + text(LINES[6]), 0.25, palette='hoanghon')

    # Mặc kệ những tiếc nuối tìm tới khi mưa cùng rơi   [words: fast, long]
    sync_words(song, LINES[7], ENDS[7], mode='words', palette='hoanghon')
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.3, breathe, palette='hoanghon')
    drift_out('' + text(LINES[7]), 0.25, palette='hoanghon')

    # Cơn đau kia anh nhận lấy riêng anh mà thôi   [spotlight: từ "riêng anh", long]
    sync_words(song, LINES[8], ENDS[8], mode='spotlight', palette='bac')
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.1, breathe, palette='bac')
    newline()

    # Em đâu cần quay đầu lại   [flicker: fast]
    sync_words(song, LINES[9], ENDS[9], mode='flicker', palette='bac', indent=6)
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.1, breathe, palette='bac', indent=6)
    newline()

    # Và chỉ cần một lần cuối gỡ những nút thắt quên đi mắt môi   [scramble: từ "quên", fast]
    sync_words(song, LINES[10][0:7], LINES[10][7][1] - 0.05, mode='scramble', palette='hong')
    newline()
    sync_words(song, LINES[10][7:14], ENDS[10], mode='scramble', palette='hong', indent=8)
    hold(song, text(LINES[10][7:]), LINES[11][0][1] - 0.3, breathe, palette='hong', indent=8)
    gradient_fade_out('        ' + text(LINES[10][7:]), 0.25, palette='hong')

    # Ba năm mươi xé đôi   [rainbow: đa dạng]
    sync_words(song, LINES[11], ENDS[11], mode='rainbow', palette='hong', indent=6)
    hold(song, text(LINES[11]), LINES[12][0][1] - 0.3, breathe, palette='hong', indent=6)
    dissolve_out('      ' + text(LINES[11]), 0.25, palette='hong')

    # Cơn đau kia sẽ nguôi   [pop: fast]
    sync_words(song, LINES[12], ENDS[12], mode='pop', palette='tim', indent=6)
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.1, breathe, palette='tim', indent=6)
    newline()

    # Bởi vì anh cũng sẽ phải quên   [scramble: từ "quên", fast]
    sync_words(song, LINES[13], ENDS[13], mode='scramble', palette='tim', indent=4)
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Liệu không cần em ở bên   [converge: fast]
    sync_words(song, LINES[14], ENDS[14], mode='converge', palette='bien', indent=6)
    hold(song, text(LINES[14]), LINES[15][0][1] - 0.3, breathe, palette='bien', indent=6)
    center_out('      ' + text(LINES[14]), 0.25, palette='bien')

    # Nhìn mưa lao đi trong đêm   [fadein: từ "đêm"]
    sync_words(song, LINES[15], ENDS[15], mode='fadein', palette='bien', indent=6)
    hold(song, text(LINES[15]), LINES[16][0][1] - 0.3, breathe, palette='bien', indent=6)
    sweep_out('      ' + text(LINES[15]), 0.25, palette='bien')

    # Rồi lại lay lắt trên bậc thềm   [glitch: fast]
    sync_words(song, LINES[16], ENDS[16], mode='glitch', palette='hoanghon', indent=5)
    hold(song, text(LINES[16]), LINES[17][0][1] - 0.3, breathe, palette='hoanghon', indent=5)
    drift_out('     ' + text(LINES[16]), 0.25, palette='hoanghon')

    # Liệu rằng mưa sẽ cuốn nàng đi   [pop: fast, loud]
    sync_words(song, LINES[17], ENDS[17], mode='pop', palette='hoanghon', indent=5)
    hold(song, text(LINES[17]), LINES[18][0][1] - 0.3, breathe, palette='hoanghon', indent=5)
    gradient_fade_out('     ' + text(LINES[17]), 0.25, palette='hoanghon')

    # Hoặc là vương ngay trên đôi mi   [splash: fast]
    sync_words(song, LINES[18], ENDS[18], mode='splash', palette='bac', indent=7)
    hold(song, text(LINES[18]), LINES[19][0][1] - 0.3, breathe, palette='bac', indent=7)
    dissolve_out('       ' + text(LINES[18]), 0.25, palette='bac')

    # Chỉ là cô đơn anh mỗi khi   [flicker: fast, loud]
    sync_words(song, LINES[19], ENDS[19], mode='flicker', palette='bac', indent=9)
    hold(song, text(LINES[19]), LINES[20][0][1] - 0.3, breathe, palette='bac', indent=9)
    dissolve_out('         ' + text(LINES[19]), 0.25, palette='bac')

    # Khua tay anh giấu đi   [scramble: từ "giấu", fast]
    sync_words(song, LINES[20], ENDS[20], mode='scramble', palette='hong', indent=11)
    hold(song, text(LINES[20]), LINES[21][0][1] - 0.3, breathe, palette='hong', indent=11)
    sweep_out('           ' + text(LINES[20]), 0.25, palette='hong')

    # Anh chỉ anh chỉ muốn được yên bình   [glitch: fast, loud]
    sync_words(song, LINES[21], ENDS[21], mode='glitch', palette='hong', indent=2)
    hold(song, text(LINES[21]), LINES[22][0][1] - 0.1, breathe, palette='hong', indent=2)
    newline()

    # Muốn có em của riêng mình   [jump: fast]
    sync_words(song, LINES[22], ENDS[22], mode='jump', palette='tim', indent=8)
    hold(song, text(LINES[22]), LINES[23][0][1] - 0.1, shine, palette='tim', indent=8)
    newline()

    # Em nói anh bị điên vì sự thật giờ đây có lẽ   [typo: fast, long]
    sync_words(song, LINES[23][0:6], LINES[23][6][1] - 0.05, mode='typo', palette='tim', indent=2)
    newline()
    sync_words(song, LINES[23][6:12], ENDS[23], mode='typo', palette='tim', indent=10)
    hold(song, text(LINES[23][6:]), LINES[24][0][1] - 0.1, breathe, palette='tim', indent=10)
    newline()

    # Em giờ đang ở bên một ai rồi   [bounce: fast, loud]
    sync_words(song, LINES[24], ENDS[24], mode='bounce', palette='bien', indent=6)
    hold(song, text(LINES[24]), LINES[25][0][1] - 0.1, shine, palette='bien', indent=6)
    newline()

    # Quên đi anh là ai rồi   [scramble: từ "quên", fast]
    sync_words(song, LINES[25], ENDS[25], mode='scramble', palette='bien', indent=6)
    hold(song, text(LINES[25]), LINES[26][0][1] - 0.1, breathe, palette='bien', indent=6)
    newline()

    # Quay bước anh rời đi anh đâu hề muốn gây khó dễ   [letters: long, soft, finale]
    sync_words(song, LINES[26][0:6], LINES[26][6][1] - 0.05, mode='letters', palette='hoanghon')
    newline()
    sync_words(song, LINES[26][6:12], ENDS[26], mode='letters', palette='hoanghon', indent=8)
    hold(song, text(LINES[26][6:]), ENDS[26] + 1.5, heartbeat, palette='hoanghon', indent=8)
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
