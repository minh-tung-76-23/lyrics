import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = False
set_color(COLOR)

# Phát nhạc từ giây thứ START của bài
START = 0.0

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7701676537959042305.mp3'), offset=OFFSET)

LINES = [
    [('Ký', 0.0), ('ức', 0.26), ('đôi', 0.44), ('ta', 0.76)],
    [('Là', 1.44), ('thứ', 1.84), ('anh', 2.28), ('mang', 2.62), ('cả', 3.64), ('đời', 4.06)],
    [('Này', 5.42), ('người', 5.98), ('ơi', 6.48), ('em', 6.9), ('có', 7.24), ('biết,', 7.56)],
    [('Anh', 8.22), ('vẫn', 8.48), ('ở', 8.84), ('đây', 9.22)],
    [('Vẫn', 9.62), ('muốn', 10.14), ('che', 10.58), ('chở', 10.96), ('cho', 11.28), ('em', 11.72)],
    [('Dù', 12.18), ('là', 12.72), ('khi', 13.12), ('em', 13.54), ('mắt', 13.96), ('kém', 14.18)],
    [('Hay', 14.84), ('khi', 15.12), ('mi', 15.56), ('hoen', 15.86), ('lấm', 16.32), ('lem', 17.36)],
    [('Nguyện', 18.7), ('làm', 19.3), ('ngôi', 19.8), ('sao', 20.12), ('xa', 20.54), ('xôi', 20.86)],
    [('Dẫn', 21.44), ('lối', 21.9), ('em', 22.24), ('trong', 22.52), ('đêm', 23.06), ('đông', 23.56), ('tối', 24.14), ('đèn', 24.76)],
    [('Chỉ', 26.0), ('mong', 26.4), ('em', 26.62), ('luôn', 26.86), ('yên', 27.2), ('vui', 27.6)],
    [('Thế', 28.1), ('giới', 28.62), ('với', 29.3), ('em', 29.74), ('dịu', 30.2), ('dàng', 30.66)],
    [('Thật', 31.98), ('lòng', 32.62), ('anh', 33.06), ('rất', 33.48), ('muốn', 33.82), ('biết', 34.16)],
    [('Biển', 34.88), ('người', 35.2), ('mênh', 35.58), ('mông', 35.94)],
    [('Còn', 36.54), ('có', 36.86), ('thể', 37.68), ('gặp', 37.98), ('em', 38.28), ('không?', 38.7)],
    [('Người', 39.52), ('yêu', 39.58), ('của', 39.92), ('anh', 40.22), ('nhỏ', 40.6), ('bé', 40.88)],
    [('Vắng', 41.46), ('anh', 41.94), ('ai', 42.26), ('sẽ', 42.68), ('chở', 42.94), ('che', 43.88)],
    [('Rồi', 45.46), ('mười', 45.98), ('hai', 46.48), ('mươi', 46.82), ('năm', 47.28), ('sau', 47.46)],
    [('Chẳng', 48.06), ('biết', 48.5), ('lúc', 48.92), ('đó', 49.18), ('em', 49.74), ('trông', 50.22), ('thế', 50.74), ('nào', 51.52)],
    [('Nụ', 52.66), ('cười', 53.04), ('vẫn', 53.52), ('như', 53.78), ('xưa', 54.12)],
    [('Có', 54.84), ('lẽ', 55.22), ('vẫn', 56.04), ('rất', 56.4), ('ngọt', 56.78), ('ngào', 57.24)],
]
ENDS = [1.44, 5.42, 8.02, 9.62, 12.18, 14.84, 18.7, 21.44, 26.0, 28.1, 31.98, 34.88, 36.36, 39.3, 41.46, 45.53, 48.06, 52.0, 54.82, 58.28]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play(start=START)

    # Ký ức đôi ta   [mist: từ "ký ức"]
    sync_words(song, LINES[0], ENDS[0], mode='mist', palette='hong', indent=4)
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.1, shine, palette='hong', indent=4)
    newline()

    # Là thứ anh mang cả đời   [spotlight: bạn chọn]
    sync_words(song, LINES[1], ENDS[1], mode='spotlight', palette='hong')
    trailing_dots(song, text(LINES[1]), LINES[2][0][1] - 0.1, palette='hong')
    newline()

    # Này người ơi em có biết,   [bloom: đa dạng]
    sync_words(song, LINES[2], ENDS[2], mode='bloom', palette='tim')
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.1, shine, palette='tim')
    newline()

    # Anh vẫn ở đây   [center: short]
    sync_words(song, LINES[3], ENDS[3], mode='center', palette='tim')
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.3, breathe, palette='tim')
    gradient_fade_out('' + text(LINES[3]), 0.25, palette='tim')

    # Vẫn muốn che chở cho em   [letters: đa dạng]
    sync_words(song, LINES[4], ENDS[4], mode='letters', palette='bien')
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='bien')
    newline()

    # Dù là khi em mắt kém   [mist: bạn chọn]
    sync_words(song, LINES[5], ENDS[5], mode='mist', palette='bien')
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='bien')
    newline()

    # Hay khi mi hoen lấm lem   [drop: bạn chọn]
    sync_words(song, LINES[6], ENDS[6], mode='drop', palette='hoanghon', indent=4)
    trailing_dots(song, text(LINES[6]), LINES[7][0][1] - 0.1, palette='hoanghon', indent=4)
    newline()

    # Nguyện làm ngôi sao xa xôi   [starfall: từ "ngôi sao"]
    sync_words(song, LINES[7], ENDS[7], mode='starfall', palette='hoanghon')
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.3, breathe, palette='hoanghon')
    dissolve_out('' + text(LINES[7]), 0.25, palette='hoanghon')

    # Dẫn lối em trong đêm đông tối đèn   [starfall: bạn chọn]
    sync_words(song, LINES[8], ENDS[8], mode='starfall', palette='bac')
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.3, breathe, palette='bac')
    center_out('' + text(LINES[8]), 0.25, palette='bac')

    # Chỉ mong em luôn yên vui   [letters: từ "mong"]
    sync_words(song, LINES[9], ENDS[9], mode='letters', palette='bac')
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.1, breathe, palette='bac')
    newline()

    # Thế giới với em dịu dàng   [karaoke: bạn chọn]
    sync_words(song, LINES[10], ENDS[10], mode='karaoke', palette='hong')
    trailing_dots(song, text(LINES[10]), LINES[11][0][1] - 0.1, palette='hong')
    newline()

    # Thật lòng anh rất muốn biết   [flow: bạn chọn]
    sync_words(song, LINES[11], ENDS[11], mode='flow', palette='hong')
    hold(song, text(LINES[11]), LINES[12][0][1] - 0.1, breathe, palette='hong')
    newline()

    # Biển người mênh mông   [ripple: từ "biển người"]
    sync_words(song, LINES[12], ENDS[12], mode='ripple', palette='tim', indent=4)
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.1, shine, palette='tim', indent=4)
    newline()

    # Còn có thể gặp em không?   [snow: đa dạng]
    sync_words(song, LINES[13], ENDS[13], mode='snow', palette='tim', indent=8)
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.1, breathe, palette='tim', indent=8)
    newline()

    # Người yêu của anh nhỏ bé   [hearts: từ "yêu"]
    sync_words(song, LINES[14], ENDS[14], mode='hearts', palette='bien')
    trailing_dots(song, text(LINES[14]), LINES[15][0][1] - 0.1, palette='bien')
    newline()

    # Vắng anh ai sẽ chở che   [letters: bạn chọn]
    sync_words(song, LINES[15], ENDS[15], mode='letters', palette='bien', indent=4)
    hold(song, text(LINES[15]), LINES[16][0][1] - 0.1, breathe, palette='bien', indent=4)
    newline()

    # Rồi mười hai mươi năm sau   [mist: từ "năm sau"]
    sync_words(song, LINES[16], ENDS[16], mode='mist', palette='hoanghon', indent=4)
    hold(song, text(LINES[16]), LINES[17][0][1] - 0.3, breathe, palette='hoanghon', indent=4)
    sweep_out('    ' + text(LINES[16]), 0.25, palette='hoanghon')

    # Chẳng biết lúc đó em trông thế nào   [words: long]
    sync_words(song, LINES[17], ENDS[17], mode='words', palette='hoanghon')
    hold(song, text(LINES[17]), LINES[18][0][1] - 0.3, breathe, palette='hoanghon')
    drift_out('' + text(LINES[17]), 0.25, palette='hoanghon')

    # Nụ cười vẫn như xưa   [bloom: từ "nụ cười"]
    sync_words(song, LINES[18], ENDS[18], mode='bloom', palette='bac', indent=4)
    hold(song, text(LINES[18]), LINES[19][0][1] - 0.3, breathe, palette='bac', indent=4)
    gradient_fade_out('    ' + text(LINES[18]), 0.25, palette='bac')

    # Có lẽ vẫn rất ngọt ngào   [sparkle: bạn chọn]
    sync_words(song, LINES[19], ENDS[19], mode='sparkle', palette='bac', indent=4)
    trailing_dots(song, text(LINES[19]), ENDS[19] + 3.0, palette='bac', indent=4)
    hold(song, text(LINES[19]) + '...', ENDS[19] + 4.5, heartbeat, palette='bac', indent=4)
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
