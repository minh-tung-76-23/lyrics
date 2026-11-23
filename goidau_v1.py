import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = True
set_color(COLOR)

# Phát nhạc từ giây thứ START của bài
START = 65.42

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7624234690135788807.mp3'), offset=OFFSET)

LINES = [
    [('Để', 66.42), ('lại', 66.82), ('một', 66.92), ('ly', 67.1)],
    [('Margarita', 67.32), ('Martini', 68.08), ('cho', 68.48), ('señorita', 68.62)],
    [('đang', 69.34), ('bên', 69.42), ('ta', 69.42)],
    [('Rồi', 69.78), ('pha', 69.92), ('thêm', 70.06)],
    [('Piña', 70.9), ('Colada', 71.02), ('khi', 71.02), ('cô', 71.16), ('ta', 71.38), ('đang', 71.5), ('đưa', 71.73), ('tao', 71.82), ('đi', 71.96), ('xa', 72.16)],
    [('Ooh,', 72.36), ('mama', 72.36), ('feels', 72.72), ('so', 72.86), ('good,', 73.26)],
    [('Dù', 73.52), ('nàng', 73.76), ('là', 73.9), ('người', 74.02), ('tình', 74.2), ('cũ', 74.42)],
    [('Mà', 74.74), ('mình', 74.94), ('vòng', 75.14), ('lại', 75.3), ('một', 75.48), ('chút', 75.68)],
    [('Để', 76.04), ('mình', 76.2), ('giúp', 76.42), ('một', 76.58), ('tay', 76.86)],
    [('Anh', 77.14), ('không', 77.48), ('quan', 77.64), ('tâm', 77.86)],
    [('Em', 78.0), ('đi', 78.3), ('đâu', 78.44), ('khi', 78.68), ('em', 78.88), ('sober', 79.06)],
    [('Xem', 79.54), ('trên', 79.84), ('video', 80.06)],
    [('Đang', 80.74), ('đi', 80.8), ('show', 81.0), ('hay', 81.28), ('đi', 81.46), ('đâu', 81.6), ('nhờ?', 81.94)],
    [('Quen', 82.12), ('em', 82.52), ('từ', 82.7), ('lâu', 82.88), ('nên', 83.26)],
    [('I', 83.4), ('know', 83.58), ('it′s', 83.68), ('never', 83.92), ('over', 84.18)],
    [('Trong', 84.6), ('studio', 84.9), ('đêm', 85.74), ('thâu,', 86.12), ('đêm', 86.32), ('thâu', 86.7), ('ta', 86.88), ('lại', 87.02)],
    [('Ngồi', 88.5), ('tới', 89.04), ('ba', 89.04), ('giờ', 89.04), ('thấy', 89.48)],
    [('Lời', 89.96), ('rót', 90.6), ('ra', 91.12), ('tờ', 91.46), ('giấy', 92.16)],
    [('Mùi', 92.52), ('Vodka', 93.22)],
    [('Mười', 94.82), ('shot', 95.72), ('không', 96.04), ('pha', 96.58)],
    [('Lại', 97.36), ('lướt', 98.14), ('qua', 98.52), ('người', 99.1), ('ấy', 99.62)],
    [('Người', 100.04), ('thướt', 100.66), ('tha', 101.1), ('tà', 101.68), ('váy', 102.12)],
    [('Hoạ', 102.52), ('tiết', 103.28), ('hoa', 103.54)],
    [('Nhưng', 104.62), ('nhìn', 104.98), ('vẫn', 105.52), ('xuyên', 105.96), ('qua', 106.74)],
    [('Nhìn', 107.32), ('vẫn', 107.96), ('shh', 108.64)],
    [('Oh-oh', 108.64), ('oh,', 108.64), ('oh,', 109.68), ('oh', 110.04)],
    [('Khi', 112.18), ('tình', 112.86), ('yêu', 113.26), ('của', 113.58), ('em', 113.98), ('ở', 114.32), ('bên', 114.48), ('kia', 114.72), ('cầu', 115.04), ('oh,', 115.96), ('oh,', 116.4), ('oh', 116.84)],
    [('Khi', 117.28), ('tình', 117.96), ('yêu', 118.36), ('của', 118.68), ('anh', 119.02), ('á', 119.47), ('đang', 119.56), ('gội', 119.82), ('đầu', 120.22), ('oh,', 121.02), ('oh,', 121.48), ('oh', 121.94)],
    [('Qua', 122.4), ('một', 123.08), ('đêm', 123.36), ('lại', 123.7), ('thấy', 123.98), ('mình', 124.34), ('thêm', 124.6), ('một', 125.09), ('xấu', 125.09)],
    [('Show', 125.32)],
    [('Oh-oh', 128.1), ('oh,', 129.6), ('oh,', 129.6), ('oh', 130.16)],
    [('Khi', 132.48), ('quả', 133.16), ('tim', 133.46), ('của', 133.78), ('em', 134.26), ('nó', 134.67), ('đang', 134.74), ('thay', 135.08), ('màu', 135.32), ('oh,', 136.13), ('oh,', 136.6), ('oh', 137.07)],
    [('Xin', 137.54), ('một', 138.18), ('hơi', 138.56), ('thật', 138.9), ('sâu', 139.14), ('trước', 139.46), ('khi', 139.78), ('bắt', 140.1), ('đầu', 140.44), ('oh,', 141.19), ('oh,', 141.62), ('oh', 142.04)],
    [('Và', 142.47), ('đưa', 142.9), ('bàn', 143.32), ('tay', 143.56), ('bạn', 143.96), ('đây', 144.18), ('làm', 144.52), ('sao', 144.78), ('phải', 145.02), ('giấu?', 145.36), ('cạn', 146.78), ('ly', 147.46), ('yeah', 148.14)],
    [('Giấu', 148.82)],
    [('Yeah', 149.46), ('đêm', 150.34), ('nay', 150.7), ('sao', 150.98), ('lại', 151.34), ('say', 151.6), ('say?', 151.72), ('uầy', 151.73), ('say', 151.73), ('vãi', 151.74)],
    [('Cái', 151.74), ('đầu', 153.14), ('sao', 153.22), ('mà', 153.42), ('nó', 153.6), ('lại', 153.94), ('quay', 154.18), ('quay?', 154.86), ('huh', 155.38)],
    [('Hai', 155.38), ('bàn', 155.74), ('tay', 156.2), ('lại', 156.36), ('loay', 156.68), ('hoay', 157.24), ('em', 157.8), ('ê', 158.02)],
    [('Gọi', 158.02), ('thêm', 158.02), ('hai', 158.62), ('ly', 158.84), ('Tequila', 158.92), ('cho', 158.92), ('mình', 159.18), ('bay', 159.52), ('bay', 160.0)],
]
ENDS = [67.32, 69.34, 69.66, 70.42, 72.36, 73.52, 74.74, 76.04, 77.14, 78.0, 79.54, 80.56, 82.12, 83.4, 84.6, 87.28, 89.96, 92.52, 93.9, 97.36, 100.04, 102.52, 104.62, 107.32, 109.68, 110.52, 117.14, 122.24, 125.32, 128.1, 130.86, 137.37, 142.34, 148.44, 149.46, 152.04, 155.68, 158.32, 160.3]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play(start=START)

    # Để lại một ly   [flicker: fast, short, loud]
    sync_words(song, LINES[0], ENDS[0], mode='flicker', palette='hong')
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.1, shine, palette='hong')
    newline()

    # Margarita Martini cho señorita   [flow: bạn chọn]
    sync_words(song, LINES[1], ENDS[1], mode='flow', palette='hong', indent=4)
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, breathe, palette='hong', indent=4)
    newline()

    # đang bên ta   [glitch: fast, short]
    sync_words(song, LINES[2], ENDS[2], mode='glitch', palette='tim', indent=12)
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.3, breathe, palette='tim', indent=12)
    gradient_fade_out('            ' + text(LINES[2]), 0.25, palette='tim')

    # Rồi pha thêm   [converge: fast, short]
    sync_words(song, LINES[3], ENDS[3], mode='converge', palette='tim')
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim')
    newline()

    # Piña Colada khi cô ta đang đưa tao đi xa   [typo: fast, long]
    sync_words(song, LINES[4], ENDS[4], mode='typo', palette='bien', indent=4)
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='bien', indent=4)
    newline()

    # Ooh, mama feels so good,   [rainbow: bạn chọn]
    sync_words(song, LINES[5], ENDS[5], mode='rainbow', palette='bien')
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.3, breathe, palette='bien')
    dissolve_out('' + text(LINES[5]), 0.25, palette='bien')

    # Dù nàng là người tình cũ   [pop: fast]
    sync_words(song, LINES[6], ENDS[6], mode='pop', palette='hoanghon', indent=4)
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.3, breathe, palette='hoanghon', indent=4)
    center_out('    ' + text(LINES[6]), 0.25, palette='hoanghon')

    # Mà mình vòng lại một chút   [words: fast]
    sync_words(song, LINES[7], ENDS[7], mode='words', palette='hoanghon', indent=4)
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.3, breathe, palette='hoanghon', indent=4)
    sweep_out('    ' + text(LINES[7]), 0.25, palette='hoanghon')

    # Để mình giúp một tay   [slide: fast]
    sync_words(song, LINES[8], ENDS[8], mode='slide', palette='bac', indent=4)
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.1, shine, palette='bac', indent=4)
    newline()

    # Anh không quan tâm   [jump: fast, short, loud]
    sync_words(song, LINES[9], ENDS[9], mode='jump', palette='bac')
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.1, breathe, palette='bac')
    newline()

    # Em đi đâu khi em sober   [splash: fast]
    sync_words(song, LINES[10], ENDS[10], mode='splash', palette='hong', indent=8)
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.1, shine, palette='hong', indent=8)
    newline()

    # Xem trên video   [drop: short]
    sync_words(song, LINES[11], ENDS[11], mode='drop', palette='hong')
    hold(song, text(LINES[11]), LINES[12][0][1] - 0.1, breathe, palette='hong')
    newline()

    # Đang đi show hay đi đâu nhờ?   [typo: từ "?", fast]
    sync_words(song, LINES[12], ENDS[12], mode='typo', palette='tim', indent=8)
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.1, shine, palette='tim', indent=8)
    newline()

    # Quen em từ lâu nên   [scramble: fast]
    sync_words(song, LINES[13], ENDS[13], mode='scramble', palette='tim')
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.1, breathe, palette='tim')
    newline()

    # I know it′s never over   [bounce: fast]
    sync_words(song, LINES[14], ENDS[14], mode='bounce', palette='bien', indent=8)
    hold(song, text(LINES[14]), LINES[15][0][1] - 0.1, shine, palette='bien', indent=8)
    newline()

    # Trong studio đêm thâu, đêm thâu ta lại   [words: bạn chọn]
    sync_words(song, LINES[15], ENDS[15], mode='words', palette='bien')
    hold(song, text(LINES[15]), LINES[16][0][1] - 0.1, breathe, palette='bien')
    newline()

    newline()  # hết đoạn

    # Ngồi tới ba giờ thấy   [flow: bạn chọn]
    sync_words(song, LINES[16], ENDS[16], mode='flow', palette='bac')
    hold(song, text(LINES[16]), LINES[17][0][1] - 0.1, shine, palette='bac')
    newline()

    # Lời rót ra tờ giấy   [flow: bạn chọn]
    sync_words(song, LINES[17], ENDS[17], mode='flow', palette='bac', indent=4)
    hold(song, text(LINES[17]), LINES[18][0][1] - 0.1, breathe, palette='bac', indent=4)
    newline()

    # Mùi Vodka   [flow: bạn chọn]
    sync_words(song, LINES[18], ENDS[18], mode='flow', palette='hong', indent=12)
    hold(song, text(LINES[18]), LINES[19][0][1] - 0.1, shine, palette='hong', indent=12)
    newline()

    # Mười shot không pha   [flow: bạn chọn]
    sync_words(song, LINES[19], ENDS[19], mode='flow', palette='hong', indent=8)
    hold(song, text(LINES[19]), LINES[20][0][1] - 0.1, breathe, palette='hong', indent=8)
    newline()

    # Lại lướt qua người ấy   [flow: bạn chọn]
    sync_words(song, LINES[20], ENDS[20], mode='flow', palette='tim')
    hold(song, text(LINES[20]), LINES[21][0][1] - 0.1, shine, palette='tim')
    newline()

    # Người thướt tha tà váy   [flow: bạn chọn]
    sync_words(song, LINES[21], ENDS[21], mode='flow', palette='tim', indent=4)
    hold(song, text(LINES[21]), LINES[22][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Hoạ tiết hoa   [flow: bạn chọn]
    sync_words(song, LINES[22], ENDS[22], mode='flow', palette='bien', indent=12)
    hold(song, text(LINES[22]), LINES[23][0][1] - 0.1, shine, palette='bien', indent=12)
    newline()

    # Nhưng nhìn vẫn xuyên qua   [flow: bạn chọn]
    sync_words(song, LINES[23], ENDS[23], mode='flow', palette='bien', indent=8)
    hold(song, text(LINES[23]), LINES[24][0][1] - 0.1, breathe, palette='bien', indent=8)
    newline()

    # Nhìn vẫn shh   [flow: bạn chọn]
    sync_words(song, LINES[24], ENDS[24], mode='flow', palette='hoanghon', indent=16)
    hold(song, text(LINES[24]), LINES[25][0][1] - 0.1, shine, palette='hoanghon', indent=16)
    newline()

    newline()  # hết đoạn

    # Oh-oh oh, oh, oh   [center: short, soft]
    sync_words(song, LINES[25][0:1], LINES[25][1][1] - 0.05, mode='center', palette='bac', indent=8)
    c = 8 + text_width(text(LINES[25][0:1])) + 1   # phần đệm
    sync_words(song, LINES[25][1:], ENDS[25], mode='fadein', palette='bac', indent=c, keep_left=True)
    hold(song, text(LINES[25][0:1]), LINES[26][0][1] - 0.3, breathe, palette='bac', indent=8)
    drift_out('        ' + text(LINES[25][0:1]), 0.25, palette='bac')

    # Khi tình yêu của em ở bên kia cầu oh, oh, oh   [sides: long]
    sync_words(song, LINES[26][0:9], LINES[26][9][1] - 0.05, mode='sides', palette='hong')
    c = 0 + text_width(text(LINES[26][0:9])) + 1   # phần đệm
    sync_words(song, LINES[26][9:], ENDS[26], mode='fadein', palette='bac', indent=c, keep_left=True)
    song.at(LINES[27][0][1] - 0.35)
    echo_out(text(LINES[26][9:]), c, 0.3)
    newline()

    # Khi tình yêu của anh á đang gội đầu oh, oh, oh   [hearts: từ "yêu"]
    sync_words(song, LINES[27][0:9], LINES[27][9][1] - 0.05, mode='hearts', palette='hong')
    c = 0 + text_width(text(LINES[27][0:9])) + 1   # phần đệm
    sync_words(song, LINES[27][9:], ENDS[27], mode='fadein', palette='bac', indent=c, keep_left=True)
    song.at(LINES[28][0][1] - 0.35)
    echo_out(text(LINES[27][9:]), c, 0.3)
    newline()

    # Qua một đêm lại thấy mình thêm một xấu   [fadein: từ "đêm"]
    sync_words(song, LINES[28], ENDS[28], mode='fadein', palette='tim')
    hold(song, text(LINES[28]), LINES[29][0][1] - 0.1, shine, palette='tim')
    newline()

    # Show   [wave: slow]
    sync_words(song, LINES[29], ENDS[29], mode='wave', palette='tim', indent=16)
    trailing_dots(song, text(LINES[29]), LINES[30][0][1] - 0.1, palette='tim', indent=16)
    newline()

    # Oh-oh oh, oh, oh   [center: slow, short]
    sync_words(song, LINES[30][0:1], LINES[30][1][1] - 0.05, mode='center', palette='bien', indent=8)
    c = 8 + text_width(text(LINES[30][0:1])) + 1   # phần đệm
    sync_words(song, LINES[30][1:], ENDS[30], mode='fadein', palette='bac', indent=c, keep_left=True)
    hold(song, text(LINES[30][0:1]), LINES[31][0][1] - 0.3, breathe, palette='bien', indent=8)
    gradient_fade_out('        ' + text(LINES[30][0:1]), 0.25, palette='bien')

    # Khi quả tim của em nó đang thay màu oh, oh, oh   [rainbow: bạn chọn]
    sync_words(song, LINES[31][0:9], LINES[31][9][1] - 0.05, mode='rainbow', palette='bien')
    c = 0 + text_width(text(LINES[31][0:9])) + 1   # phần đệm
    sync_words(song, LINES[31][9:], ENDS[31], mode='fadein', palette='bac', indent=c, keep_left=True)
    song.at(LINES[32][0][1] - 0.35)
    echo_out(text(LINES[31][9:]), c, 0.3)
    newline()

    # Xin một hơi thật sâu trước khi bắt đầu oh, oh, oh   [letters: bạn chọn]
    sync_words(song, LINES[32][0:9], LINES[32][9][1] - 0.05, mode='letters', palette='hoanghon')
    c = 0 + text_width(text(LINES[32][0:9])) + 1   # phần đệm
    sync_words(song, LINES[32][9:], ENDS[32], mode='fadein', palette='bac', indent=c, keep_left=True)
    song.at(LINES[33][0][1] - 0.35)
    echo_out(text(LINES[32][9:]), c, 0.3)
    newline()

    # Và đưa bàn tay bạn đây làm sao phải giấu? cạn ly yeah   [scramble: từ "giấu", loud]
    sync_words(song, LINES[33][0:10], LINES[33][10][1] - 0.05, mode='scramble', palette='hoanghon')
    c = 0 + text_width(text(LINES[33][0:10])) + 1   # phần đệm
    sync_words(song, LINES[33][10:], ENDS[33], mode='fadein', palette='bac', indent=c, keep_left=True)
    song.at(LINES[34][0][1] - 0.35)
    echo_out(text(LINES[33][10:]), c, 0.3)
    newline()

    # Giấu   [sparkle: short, finale]
    sync_words(song, LINES[34], ENDS[34], mode='sparkle', palette='bac', indent=16)
    hold(song, text(LINES[34]), LINES[35][0][1] - 0.1, shine, palette='bac', indent=16)
    newline()

    newline()  # hết đoạn

    # Yeah đêm nay sao lại say say? uầy say vãi   [wave: bạn chọn]
    sync_words(song, LINES[35][0:7], LINES[35][7][1] - 0.05, mode='wave', palette='hong')
    c = 0 + text_width(text(LINES[35][0:7])) + 1   # phần đệm
    sync_words(song, LINES[35][7:], ENDS[35], mode='fadein', palette='bac', indent=c, keep_left=True)
    song.at(LINES[36][0][1] - 0.35)
    echo_out(text(LINES[35][7:]), c, 0.3)
    newline()

    # Cái đầu sao mà nó lại quay quay? huh   [jump: bạn chọn]
    sync_words(song, LINES[36][0:8], LINES[36][8][1] - 0.05, mode='jump', palette='tim', indent=4)
    c = 4 + text_width(text(LINES[36][0:8])) + 1   # phần đệm
    sync_words(song, LINES[36][8:], ENDS[36], mode='fadein', palette='bac', indent=c, keep_left=True)
    song.at(LINES[37][0][1] - 0.35)
    echo_out(text(LINES[36][8:]), c, 0.3)
    newline()

    # Hai bàn tay lại loay hoay em ê   [bounce: bạn chọn]
    sync_words(song, LINES[37][0:6], LINES[37][6][1] - 0.05, mode='bounce', palette='tim', indent=8)
    c = 8 + text_width(text(LINES[37][0:6])) + 1   # phần đệm
    sync_words(song, LINES[37][6:], ENDS[37], mode='fadein', palette='bac', indent=c, keep_left=True)
    song.at(LINES[38][0][1] - 0.35)
    echo_out(text(LINES[37][6:]), c, 0.3)
    newline()

    # Gọi thêm hai ly Tequila cho mình bay bay   [rise: bạn chọn]
    sync_words(song, LINES[38], ENDS[38], mode='rise', palette='bien')
    hold(song, text(LINES[38]), ENDS[38] + 1.5, heartbeat, palette='bien')
    newline()

    print('\n')
    song.at(161.9)
    song.stop(1.5)  # hết đoạn -> giảm dần rồi tắt nhạc
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
