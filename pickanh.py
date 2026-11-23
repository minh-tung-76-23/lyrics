import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = True
set_color(COLOR)

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7701846191381990677.mp3'), offset=OFFSET)

LINES = [
    [('Vì', 0.0), ('có', 0.22), ('hơn', 0.46), ('trăm', 0.58), ('lý', 0.66), ('do', 0.76), ('để', 0.88), ('cho', 1.02), ('anh', 1.1), ('yêu', 1.26), ('em', 1.38), ('quên', 1.54), ('sầu', 1.74)],
    [('Thì', 1.98), ('là', 2.16), ('vì', 2.28), ('em', 2.54), ('xinh', 2.76), ('ngoan', 3.04)],
    [('hơi', 3.28), ('gắt', 3.54), ('gỏng', 3.78)],
    [('Chu', 4.54), ('đáo', 4.78)],
    [('Yêu', 5.08), ('thương', 5.2), ('anh', 5.38), ('hết', 5.6), ('lòng', 5.84)],
    [('Ngoài', 6.04), ('cô', 6.3), ('tôi', 6.56), ('chẳng', 6.8), ('muốn', 7.12), ('phí', 7.3), ('giây', 7.62), ('nào', 7.82)],
    [('Bên', 8.12), ('một', 8.34), ('ai', 8.66), ('through', 9.08), ('the', 9.38), ('night', 9.7)],
    [('Mình', 9.9), ('dù', 10.38), ('trong', 10.62), ('túi', 10.9), ('có', 11.2), ('mỗi', 11.34), ('đôi', 11.44), ('ba', 11.68), ('đồng', 11.96)],
    [('Trao', 12.58), ('hết', 13.02), ('cho', 13.18), ('cái', 13.3), ('đôi', 13.46), ('má', 13.68), ('hồng', 13.94)],
    [('Từ', 14.22), ('trên', 14.44), ('xuống', 14.74), ('dưới', 15.0), ('peak', 15.28), ('điên', 15.46), ('như', 15.7), ('này', 15.98), ('lại', 16.26), ('còn', 16.38), ('thích', 16.4), ('em', 16.78)],
    [('Vậy', 17.38), ('không', 17.72), ('anh', 18.04), ('thì', 18.2), ('định', 18.48), ('pick', 18.84), ('ai?', 18.88)],
]
ENDS = [1.98, 3.28, 4.02, 5.08, 6.04, 8.12, 9.9, 12.2, 14.22, 17.38, 19.06]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play()

    # Vì có hơn trăm lý do để cho anh yêu em quên sầu   [scramble: từ "quên", fast]
    sync_words(song, LINES[0][0:7], LINES[0][7][1] - 0.05, mode='scramble', palette='hong')
    newline()
    sync_words(song, LINES[0][7:13], ENDS[0], mode='scramble', palette='hong', indent=8)
    hold(song, text(LINES[0][7:]), LINES[1][0][1] - 0.1, heartbeat, palette='hong', indent=8)
    newline()

    # Thì là vì em xinh ngoan   [sparkle: từ "xinh"]
    sync_words(song, LINES[1], ENDS[1], mode='sparkle', palette='hong', indent=8)
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, breathe, palette='hong', indent=8)
    newline()

    # hơi gắt gỏng   [bounce: fast, short, loud]
    sync_words(song, LINES[2], ENDS[2], mode='bounce', palette='tim', indent=12)
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.1, shine, palette='tim', indent=12)
    newline()

    # Chu đáo   [jump: fast, short]
    sync_words(song, LINES[3], ENDS[3], mode='jump', palette='tim', indent=14)
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim', indent=14)
    newline()

    # Yêu thương anh hết lòng   [hearts: từ "yêu"]
    sync_words(song, LINES[4], ENDS[4], mode='hearts', palette='bien', indent=8)
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, heartbeat, palette='bien', indent=8)
    newline()

    # Ngoài cô tôi chẳng muốn phí giây nào   [words: fast, long]
    sync_words(song, LINES[5], ENDS[5], mode='words', palette='bien')
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='bien')
    newline()

    # Bên một ai through the night   [typo: fast]
    sync_words(song, LINES[6], ENDS[6], mode='typo', palette='hoanghon', indent=4)
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.1, shine, palette='hoanghon', indent=4)
    newline()

    # Mình dù trong túi có mỗi đôi ba đồng   [sides: long, soft]
    sync_words(song, LINES[7], ENDS[7], mode='sides', palette='hoanghon', indent=2)
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.1, breathe, palette='hoanghon', indent=2)
    newline()

    # Trao hết cho cái đôi má hồng   [flicker: fast]
    sync_words(song, LINES[8], ENDS[8], mode='flicker', palette='bac', indent=6)
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.1, shine, palette='bac', indent=6)
    newline()

    # Từ trên xuống dưới peak điên như này lại còn thích em   [glitch: từ "điên", fast]
    sync_words(song, LINES[9][0:6], LINES[9][6][1] - 0.05, mode='glitch', palette='bac')
    newline()
    sync_words(song, LINES[9][6:12], ENDS[9], mode='glitch', palette='bac', indent=8)
    hold(song, text(LINES[9][6:]), LINES[10][0][1] - 0.1, breathe, palette='bac', indent=8)
    newline()

    # Vậy không anh thì định pick ai?   [typo: từ "?", fast]
    sync_words(song, LINES[10], ENDS[10], mode='typo', palette='hong', indent=8)
    hold(song, text(LINES[10]), ENDS[10] + 1.5, heartbeat, palette='hong', indent=8)
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
