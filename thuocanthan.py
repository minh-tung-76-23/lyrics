import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = True
set_color(COLOR)

# Phát nhạc từ giây thứ START của bài
START = 0.0

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7706830932493225236.mp3'), offset=OFFSET)

LINES = [
    [('Tại', 0.0), ('sao', 0.0), ('lúc', 0.0), ('vui', 0.0)],
    [('Em', 0.0), ('bao', 0.66), ('giờ', 0.94), ('cũng', 1.24), ('đang', 2.14), ('bận?', 2.58)],
    [('Lúc', 2.88), ('bên', 3.16), ('anh', 3.43), ('bao', 3.48), ('giờ', 3.76), ('cũng', 3.96)],
    [('Đang', 4.82), ('giận?', 5.18)],
    [('Nói', 5.64), ('chung', 6.02), ('anh', 6.12), ('chỉ', 6.3), ('là', 6.54)],
    [('thuốc', 7.28), ('an', 7.66), ('thần', 8.12)],
    [('Với', 8.42), ('em', 8.84), ('anh', 9.04), ('chỉ', 9.14), ('là', 9.36)],
    [('thuốc', 9.5), ('an', 10.5), ('thần', 10.98)],
    [('Nói', 11.28), ('em', 11.64), ('không', 11.76), ('nên', 11.96), ('dùng', 12.12), ('quá', 12.3), ('hai', 13.4), ('lần', 13.78)],
    [('Nói', 14.08), ('em', 14.5), ('chỉ', 14.64), ('nên', 14.82), ('dùng', 14.96), ('lúc', 15.26), ('em', 16.1), ('cần', 16.6)],
    [('Với', 16.96), ('em', 17.38), ('anh', 17.52), ('chỉ', 17.7), ('là', 17.84), ('thuốc', 18.02), ('an', 18.9), ('thần', 19.46)],
    [('Với', 19.78), ('em', 20.12), ('anh', 20.32), ('chỉ', 20.42), ('là', 20.68)],
    [('Thằng', 21.02), ('bạn', 21.74), ('thân', 22.08)],
    [('Thuốc', 22.78), ('tây', 23.38), ('cùng', 23.86), ('lá', 24.04), ('cây', 24.38)],
    [('Nó', 24.92), ('chỉ', 25.36), ('làm', 25.44), ('em', 25.66), ('quá', 25.76), ('cao', 26.18), ('để', 26.7), ('xuống', 26.88), ('đây', 27.22)],
    [('Anh', 27.52), ('chỉ', 28.14), ('mơ', 28.3), ('những', 28.48), ('đắm', 28.68), ('say,', 29.06), ('đắm', 29.24), ('say', 30.0)],
    [('Em', 30.72), ('còn', 30.92), ('không', 31.18), ('muốn', 31.32), ('nắm', 31.48), ('tay,', 31.84), ('nắm', 32.48), ('tay', 32.86)],
    [('Nói', 33.38), ('anh', 33.84), ('nghe', 33.96), ('chuyện', 34.06), ('đắng', 34.36), ('cay,', 34.62), ('đắng', 35.44), ('cay', 35.62)],
    [('Mỗi', 36.02), ('khi', 36.2), ('theo', 36.38), ('người', 36.58), ('ta', 36.74), ('đi', 36.96), ('đó', 37.28), ('đây', 37.5), ('cùng', 38.08), ('gió', 38.14), ('mây', 38.54)],
    [('Em', 38.64), ('tìm', 39.02), ('anh', 39.3), ('chỉ', 39.4), ('khi', 39.56), ('nó', 39.78), ('uống', 40.1), ('say', 40.22), ('rồi', 40.85), ('quá', 41.09), ('tay', 41.32)],
    [('Cơn', 41.64), ('giận', 41.9), ('nguôi', 42.04), ('rồi', 42.26), ('mai', 42.4), ('em', 42.58), ('sẽ', 42.76), ('bay,', 43.12), ('em', 43.64), ('sẽ', 43.8), ('bay', 44.14)],
    [('Tại', 44.43), ('sao', 44.54), ('lúc', 44.68), ('vui', 44.88), ('em', 45.12), ('bao', 45.38), ('giờ', 45.48), ('cũng', 45.58), ('đang', 46.7), ('bận?', 46.92)],
    [('Lúc', 47.34), ('bên', 47.72), ('anh', 47.88), ('bao', 48.12), ('giờ', 48.24), ('cũng', 48.36), ('đang', 49.6), ('giận?', 49.8)],
    [('Nói', 50.22), ('chung', 50.58), ('anh', 50.68), ('chỉ', 50.84), ('là', 51.06), ('thuốc', 51.26), ('an', 52.44), ('thần', 52.66)],
    [('Với', 52.98), ('em', 53.38), ('anh', 53.54), ('chỉ', 53.66), ('là', 53.9), ('thuốc', 54.02), ('an', 55.3), ('thần', 55.54)],
]
ENDS = [0.1, 2.88, 4.82, 5.64, 7.28, 8.42, 9.5, 11.28, 14.08, 16.96, 19.78, 21.02, 22.84, 24.92, 27.52, 30.3, 33.38, 36.02, 38.64, 41.64, 44.32, 47.34, 50.22, 52.98, 55.8]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play(start=START)

    # Tại sao lúc vui   [center: short, soft]
    sync_words(song, LINES[0], ENDS[0], mode='center', palette='hong', indent=4)
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.1, shine, palette='hong', indent=4)
    newline()

    # Em bao giờ cũng đang bận?   [drop: soft]
    sync_words(song, LINES[1], ENDS[1], mode='drop', palette='hong', indent=8)
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, breathe, palette='hong', indent=8)
    newline()

    # Lúc bên anh bao giờ cũng   [snow: soft]
    sync_words(song, LINES[2], ENDS[2], mode='snow', palette='tim', indent=4)
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.1, shine, palette='tim', indent=4)
    newline()

    # Đang giận?   [sparkle: short]
    sync_words(song, LINES[3], ENDS[3], mode='sparkle', palette='tim', indent=12)
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim', indent=12)
    newline()

    # Nói chung anh chỉ là   [spotlight: soft]
    sync_words(song, LINES[4], ENDS[4], mode='spotlight', palette='bien')
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='bien')
    newline()

    # thuốc an thần   [center: short, soft]
    sync_words(song, LINES[5], ENDS[5], mode='center', palette='bien', indent=12)
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.3, breathe, palette='bien', indent=12)
    gradient_fade_out('            ' + text(LINES[5]), 0.25, palette='bien')

    # Với em anh chỉ là   [sides: soft]
    sync_words(song, LINES[6], ENDS[6], mode='sides', palette='hoanghon')
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.1, shine, palette='hoanghon')
    newline()

    # thuốc an thần   [fadein: slow, soft]
    sync_words(song, LINES[7], ENDS[7], mode='fadein', palette='hoanghon', indent=8)
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.1, breathe, palette='hoanghon', indent=8)
    newline()

    # Nói em không nên dùng quá hai lần   [letters: long]
    sync_words(song, LINES[8], ENDS[8], mode='letters', palette='bac', indent=4)
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.1, shine, palette='bac', indent=4)
    newline()

    # Nói em chỉ nên dùng lúc em cần   [wave: long]
    sync_words(song, LINES[9], ENDS[9], mode='wave', palette='bac')
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.1, breathe, palette='bac')
    newline()

    # Với em anh chỉ là thuốc an thần   [karaoke: long, soft]
    sync_words(song, LINES[10], ENDS[10], mode='karaoke', palette='hong', indent=4)
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.1, shine, palette='hong', indent=4)
    newline()

    # Với em anh chỉ là   [words: fast]
    sync_words(song, LINES[11], ENDS[11], mode='words', palette='hong', indent=4)
    hold(song, text(LINES[11]), LINES[12][0][1] - 0.3, breathe, palette='hong', indent=4)
    dissolve_out('    ' + text(LINES[11]), 0.25, palette='hong')

    # Thằng bạn thân   [center: slow, short, soft]
    sync_words(song, LINES[12], ENDS[12], mode='center', palette='tim', indent=8)
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.1, shine, palette='tim', indent=8)
    newline()

    # Thuốc tây cùng lá cây   [ripple: đa dạng]
    sync_words(song, LINES[13], ENDS[13], mode='ripple', palette='tim', indent=4)
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Nó chỉ làm em quá cao để xuống đây   [sides: long]
    sync_words(song, LINES[14], ENDS[14], mode='sides', palette='bien')
    hold(song, text(LINES[14]), LINES[15][0][1] - 0.1, shine, palette='bien')
    newline()

    # Anh chỉ mơ những đắm say, đắm say   [karaoke: long]
    sync_words(song, LINES[15], ENDS[15], mode='karaoke', palette='bien')
    hold(song, text(LINES[15]), LINES[16][0][1] - 0.1, breathe, palette='bien')
    newline()

    # Em còn không muốn nắm tay, nắm tay   [spotlight: long]
    sync_words(song, LINES[16], ENDS[16], mode='spotlight', palette='hoanghon')
    hold(song, text(LINES[16]), LINES[17][0][1] - 0.1, shine, palette='hoanghon')
    newline()

    # Nói anh nghe chuyện đắng cay, đắng cay   [wave: long]
    sync_words(song, LINES[17], ENDS[17], mode='wave', palette='hoanghon')
    hold(song, text(LINES[17]), LINES[18][0][1] - 0.1, breathe, palette='hoanghon')
    newline()

    # Mỗi khi theo người ta đi đó đây cùng gió mây   [words: fast, long]
    sync_words(song, LINES[18], ENDS[18], mode='words', palette='bac')
    hold(song, text(LINES[18]), LINES[19][0][1] - 0.1, shine, palette='bac')
    newline()

    # Em tìm anh chỉ khi nó uống say rồi quá tay   [pop: fast]
    sync_words(song, LINES[19], ENDS[19], mode='pop', palette='bac')
    hold(song, text(LINES[19]), LINES[20][0][1] - 0.1, breathe, palette='bac')
    newline()

    # Cơn giận nguôi rồi mai em sẽ bay, em sẽ bay   [rise: từ "bay"]
    sync_words(song, LINES[20], ENDS[20], mode='rise', palette='hong')
    hold(song, text(LINES[20]), LINES[21][0][1] - 0.1, shine, palette='hong')
    newline()

    # Tại sao lúc vui em bao giờ cũng đang bận?   [rainbow: từ "vui"]
    sync_words(song, LINES[21], ENDS[21], mode='rainbow', palette='hong')
    hold(song, text(LINES[21]), LINES[22][0][1] - 0.1, breathe, palette='hong')
    newline()

    # Lúc bên anh bao giờ cũng đang giận?   [letters: long]
    sync_words(song, LINES[22], ENDS[22], mode='letters', palette='tim')
    hold(song, text(LINES[22]), LINES[23][0][1] - 0.1, shine, palette='tim')
    newline()

    # Nói chung anh chỉ là thuốc an thần   [glide: long]
    sync_words(song, LINES[23], ENDS[23], mode='glide', palette='tim', indent=4)
    hold(song, text(LINES[23]), LINES[24][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Với em anh chỉ là thuốc an thần   [bloom: finale]
    sync_words(song, LINES[24], ENDS[24], mode='bloom', palette='bien', indent=4)
    hold(song, text(LINES[24]), ENDS[24] + 1.5, heartbeat, palette='bien', indent=4)
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
