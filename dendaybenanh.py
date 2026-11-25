import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = False
set_color(COLOR)
# True = tô vàng tên riêng (từ viết hoa giữa câu)
ACCENT = False
set_accent(ACCENT)

# Phát nhạc từ giây thứ START của bài
START = 0.0

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7708579900046839060.mp3'), offset=OFFSET)

LINES = [
    [('Baby', 0.0), ('girl', 0.88)],
    [('Em', 1.26), ('bước', 1.48), ('ra', 1.7), ('từ', 1.7), ('trong', 2.02), ('ngõ', 2.34)],
    [('với', 2.86), ('đôi', 3.14), ('má', 3.42), ('hồng', 3.96)],
    [('Trao', 4.74), ('cho', 5.16), ('riêng', 5.28), ('anh', 5.5)],
    [('Một', 5.82), ('nụ', 6.1), ('cười', 6.18), ('tỏa', 6.34), ('nắng', 6.7)],
    [('Con', 6.88), ('tim', 7.12), ('này', 7.38), ('rã', 7.72), ('đôngg', 8.36)],
    [('Hold', 9.24), ('me', 9.72), ('tight', 10.0), ('my', 10.18), ('tiny', 10.48), ('love', 10.88)],
    [('Anh', 11.42), ('sẽ', 11.54), ('chẳng', 11.76), ('hai', 12.12), ('lòng', 12.7)],
    [('Và', 12.86), ('sẽ', 13.06), ('chẳng', 13.24), ('để', 13.46), ('em', 13.74), ('phải', 14.02), ('dỗi', 14.26), ('hờn', 14.6)],
    [('Hỏi', 14.96), ('anh', 15.06), ('cũng', 15.36), ('nhớ', 15.62), ('em', 15.92), ('mà', 16.28), ('phải', 16.5), ('hongg', 17.0)],
    [('Anh', 17.54), ('đã', 17.68), ('nghĩ', 17.8), ('kĩ', 18.12)],
    [('Chỉ', 18.78), ('định', 19.1), ('trao', 19.18), ('con', 19.34), ('tim', 19.46), ('mà', 19.6), ('mất', 19.74), ('luôn', 19.88), ('lí', 20.04), ('trí', 20.44)],
    [('Như', 20.98), ('là', 21.26), ('ngàn', 21.36), ('bông', 21.64), ('hoa', 21.88), ('for', 22.14), ('me', 22.52)],
    [('Anh', 22.98), ('chẳng', 23.4), ('thể', 23.54), ('nào', 23.76), ('lãng', 24.06), ('quên', 24.3), ('được', 24.64), ('mùi', 24.92), ('hương', 25.2), ('này', 25.64)],
    [('Tình', 25.96), ('yêu', 26.32), ('anh', 26.52), ('qua', 26.8), ('ngày', 27.06), ('vẫn', 27.36), ('cứ', 27.62), ('lớn', 27.96), ('hơn', 28.56)],
    [('Em', 28.96), ('chính', 29.5), ('là', 29.8), ('lí', 30.12), ('do', 30.66)],
    [('Em', 31.14), ('chính', 31.64), ('là', 31.98), ('người', 32.22), ('đó❤️\u200d🩹', 32.52)],
    [('Là', 33.74), ('bởi', 33.74), ('vì', 33.74), ('đã', 34.8), ('có', 35.12), ('em', 35.54), ('bên', 35.8), ('đời', 36.1), ('rồi', 36.34)],
    [('Thì', 36.62), ('còn', 36.96), ('lắng', 37.26), ('lo', 37.54), ('chi', 37.96)],
    [('Nguyện', 38.56), ('trao', 39.16), ('hết', 39.48), ('tấm', 39.84), ('chân', 40.14), ('tình', 40.38), ('này', 40.66)],
    [('Chẳng', 40.92), ('cần', 41.22), ('đắn', 41.5), ('đo', 41.92), ('yeh', 42.44)],
    [('Người', 42.44), ('đừng', 43.12), ('đùa', 43.24), ('với', 43.36), ('cảm', 43.5), ('xúc', 43.84)],
    [('Khi', 44.2), ('em', 44.58), ('buồn', 44.8)],
    [('Thì', 45.1), ('đều', 45.34), ('chạm', 45.54), ('tới', 46.12), ('nơi', 46.28), ('anh', 46.78)],
    [('Ai', 47.16), ('cũng', 47.44), ('sẽ', 47.56), ('có', 47.72), ('những', 47.82), ('lúc', 48.1)],
    [('Hơi', 48.54), ('tiêu', 48.84), ('cực', 49.14)],
    [('Để', 49.42), ('khoảng', 49.62), ('lặng', 49.98), ('ấy', 50.26), ('trôi', 50.64), ('nhanh..', 51.04)],
]
ENDS = [1.26, 2.62, 4.24, 5.82, 6.8, 9.24, 11.3, 12.86, 14.96, 17.54, 18.78, 20.98, 22.98, 25.96, 28.96, 31.14, 33.74, 36.62, 38.56, 40.92, 42.74, 44.2, 45.1, 47.16, 48.54, 49.42, 52.6]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    # signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play(start=START)

    # Baby girl   [hearts: bạn chọn]
    sync_words(song, LINES[0], ENDS[0], mode='hearts', palette='hong', indent=4)
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.3, breathe, palette='hong', indent=4)
    gradient_fade_out('    ' + text(LINES[0]), 0.25, palette='hong')

    # Em bước ra từ trong ngõ   [swipe: bạn chọn]
    sync_words(song, LINES[1], ENDS[1], mode='swipe', palette='hong')
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.3, breathe, palette='hong')
    dissolve_out('' + text(LINES[1]), 0.25, palette='hong')

    # với đôi má hồng   [bloom: bạn chọn]
    sync_words(song, LINES[2], ENDS[2], mode='bloom', palette='tim', indent=4)
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.3, breathe, palette='tim', indent=4)
    center_out('    ' + text(LINES[2]), 0.25, palette='tim')

    # Trao cho riêng anh   [spotlight: bạn chọn]
    sync_words(song, LINES[3], ENDS[3], mode='spotlight', palette='tim')
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim')
    newline()

    # Một nụ cười tỏa nắng   [sparkle: bạn chọn]
    sync_words(song, LINES[4], ENDS[4], mode='sparkle', palette='bien', indent=4)
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='bien', indent=4)
    newline()

    # Con tim này rã đôngg   [drop: bạn chọn]
    sync_words(song, LINES[5], ENDS[5], mode='drop', palette='bien', indent=4)
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, heartbeat, palette='bien', indent=4)
    newline()

    # Hold me tight my tiny love   [converge: bạn chọn]
    sync_words(song, LINES[6], ENDS[6], mode='converge', palette='hoanghon')
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.1, shine, palette='hoanghon')
    newline()

    # Anh sẽ chẳng hai lòng   [words: bạn chọn]
    sync_words(song, LINES[7], ENDS[7], mode='words', palette='hoanghon', indent=4)
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.1, breathe, palette='hoanghon', indent=4)
    newline()

    # Và sẽ chẳng để em phải dỗi hờn   [letters: bạn chọn]
    sync_words(song, LINES[8], ENDS[8], mode='letters', palette='bac')
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.1, shine, palette='bac')
    newline()

    # Hỏi anh cũng nhớ em mà phải hongg   [typo: bạn chọn]
    sync_words(song, LINES[9], ENDS[9], mode='typo', palette='bac', indent=4)
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.1, breathe, palette='bac', indent=4)
    newline()

    # Anh đã nghĩ kĩ   [reveal: bạn chọn]
    sync_words(song, LINES[10], ENDS[10], mode='reveal', palette='hong')
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.3, breathe, palette='hong')
    sweep_out('' + text(LINES[10]), 0.25, palette='hong')

    # Chỉ định trao con tim mà mất luôn lí trí   [scramble: bạn chọn]
    sync_words(song, LINES[11], ENDS[11], mode='scramble', palette='hong')
    hold(song, text(LINES[11]), LINES[12][0][1] - 0.1, heartbeat, palette='hong')
    newline()

    # Như là ngàn bông hoa for me   [bloom: bạn chọn]
    sync_words(song, LINES[12], ENDS[12], mode='bloom', palette='tim', indent=4)
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.1, shine, palette='tim', indent=4)
    newline()

    # Anh chẳng thể nào lãng quên được mùi hương này   [flow: bạn chọn]
    sync_words(song, LINES[13], ENDS[13], mode='flow', palette='tim')
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.1, breathe, palette='tim')
    newline()

    # Tình yêu anh qua ngày vẫn cứ lớn hơn   [rise: bạn chọn]
    sync_words(song, LINES[14], ENDS[14], mode='rise', palette='bien')
    hold(song, text(LINES[14]), LINES[15][0][1] - 0.1, heartbeat, palette='bien')
    newline()

    # Em chính là lí do   [center: bạn chọn]
    sync_words(song, LINES[15], ENDS[15], mode='center', palette='bien')
    hold(song, text(LINES[15]), LINES[16][0][1] - 0.1, breathe, palette='bien')
    newline()

    # Em chính là người đó❤️‍🩹   [hearts: bạn chọn]
    sync_words(song, LINES[16], ENDS[16], mode='hearts', palette='hoanghon', indent=4)
    hold(song, text(LINES[16]), LINES[17][0][1] - 0.1, heartbeat, palette='hoanghon', indent=4)
    newline()

    # Là bởi vì đã có em bên đời rồi   [karaoke: bạn chọn]
    sync_words(song, LINES[17], ENDS[17], mode='karaoke', palette='hoanghon')
    hold(song, text(LINES[17]), LINES[18][0][1] - 0.1, breathe, palette='hoanghon')
    newline()

    # Thì còn lắng lo chi   [fadein: bạn chọn]
    sync_words(song, LINES[18], ENDS[18], mode='fadein', palette='bac', indent=5)
    hold(song, text(LINES[18]), LINES[19][0][1] - 0.1, shine, palette='bac', indent=5)
    newline()

    # Nguyện trao hết tấm chân tình này   [ripple: bạn chọn]
    sync_words(song, LINES[19], ENDS[19], mode='ripple', palette='bac')
    hold(song, text(LINES[19]), LINES[20][0][1] - 0.1, breathe, palette='bac')
    newline()

    # Chẳng cần đắn đo yeh   [pop: bạn chọn]
    sync_words(song, LINES[20], ENDS[20], mode='pop', palette='hong', indent=4)
    hold(song, text(LINES[20]), LINES[21][0][1] - 0.1, shine, palette='hong', indent=4)
    newline()

    # Người đừng đùa với cảm xúc   [wave: bạn chọn]
    sync_words(song, LINES[21], ENDS[21], mode='wave', palette='hong')
    hold(song, text(LINES[21]), LINES[22][0][1] - 0.3, breathe, palette='hong')
    drift_out('' + text(LINES[21]), 0.25, palette='hong')

    # Khi em buồn   [mist: bạn chọn]
    sync_words(song, LINES[22], ENDS[22], mode='mist', palette='tim')
    hold(song, text(LINES[22]), LINES[23][0][1] - 0.1, breathe, palette='tim')
    newline()

    # Thì đều chạm tới nơi anh   [glide: bạn chọn]
    sync_words(song, LINES[23], ENDS[23], mode='glide', palette='tim', indent=4)
    hold(song, text(LINES[23]), LINES[24][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Ai cũng sẽ có những lúc   [sides: bạn chọn]
    sync_words(song, LINES[24], ENDS[24], mode='sides', palette='bien')
    hold(song, text(LINES[24]), LINES[25][0][1] - 0.1, shine, palette='bien')
    newline()

    # Hơi tiêu cực   [glitch: bạn chọn]
    sync_words(song, LINES[25], ENDS[25], mode='glitch', palette='bien', indent=4)
    hold(song, text(LINES[25]), LINES[26][0][1] - 0.1, breathe, palette='bien', indent=4)
    newline()

    # Để khoảng lặng ấy trôi nhanh..   [slide: bạn chọn]
    sync_words(song, LINES[26], ENDS[26], mode='slide', palette='hoanghon')
    hold(song, text(LINES[26]), ENDS[26] + 1.5, heartbeat, palette='hoanghon')
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
