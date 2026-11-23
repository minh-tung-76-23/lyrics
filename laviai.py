import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = True
set_color(COLOR)

# Phát nhạc từ giây thứ START của bài
START = 0.0

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7613558514182622485.mp3'), offset=OFFSET)

LINES = [
    [('Là', 0.8), ('vì', 1.1), ('ai?', 1.48)],
    [('Nỗi', 3.02), ('cô', 3.46), ('đơn', 3.88), ('này', 4.08), ('là', 4.3), ('vì', 4.48), ('ai?', 4.84)],
    [('Em', 6.22), ('nói', 6.42), ('anh', 6.86), ('nghe', 7.22), ('anh', 7.46), ('làm', 7.72), ('gì', 7.84), ('sai?', 8.1)],
    [('Quá', 9.86), ('khứ', 10.4), ('kia', 10.4), ('giờ', 10.9), ('nhạt', 11.36), ('phai', 11.44)],
    [('Một', 14.0), ('thằng', 14.52), ('ngu', 14.74)],
    [('Cuối', 15.86), ('cùng', 16.72), ('chỉ', 17.12), ('là', 17.42), ('một', 17.58), ('thằng', 17.9), ('ngu', 18.04)],
    [('Em', 19.3), ('đưa', 19.8), ('anh', 20.06), ('lên', 20.46), ('rồi', 20.76), ('đạp', 21.02), ('anh', 21.16), ('xuống', 21.44)],
    [('Đó', 22.92), ('có', 23.44), ('phải', 23.92), ('điều', 24.08), ('em', 24.3), ('mong', 24.48), ('muốn?', 24.7)],
    [('Đó-đó', 26.16), ('có', 27.02), ('phải', 27.32), ('điều', 27.46), ('em', 27.68), ('mong', 27.9), ('muốn', 28.08)],
    [('Là', 28.76), ('anh', 28.88), ('phải', 29.08), ('đi', 29.28), ('khỏi', 29.5), ('đây?', 29.76)],
    [('Anh', 30.22), ('cũng', 30.76), ('chẳng', 31.0), ('thể', 31.2), ('giữ', 31.4), ('nữa', 31.8)],
    [('Khi', 32.16), ('anh', 32.46), ('đang', 32.64), ('mỏi', 32.82), ('tay,', 33.1), ('yeah', 34.1)],
    [('Con', 34.52), ('tim', 34.84), ('giờ', 34.84), ('trống', 35.18), ('rỗng', 35.18)],
    [('Cố', 35.52), ('tỏ', 35.84), ('ra', 36.0), ('thờ', 36.24), ('ơ', 36.6)],
    [('Em', 37.16), ('bây', 37.44), ('giờ', 37.72), ('không', 37.84), ('giống', 38.08), ('ngày', 38.28), ('xưa', 38.5), ('nên', 38.66)],
    [('I', 38.88), ("can't", 39.1), ('feel', 39.38), ('the', 39.68), ('love', 39.68)],
    [('Cứ', 40.08), ('bước', 40.34), ('tiếp', 40.56), ('đi', 40.74), ('anh', 41.02), ('không', 41.16), ('níu', 41.42), ('đâu', 41.78)],
    [('Anh', 42.28), ('biết', 42.44), ('đau', 42.64), ('mà', 42.9)],
    [('You', 43.04), ('know', 43.54)],
    [('Sống', 43.72), ('như', 44.08), ('khi', 44.26), ('anh', 44.54), ('chưa', 44.72), ('gặp', 44.9), ('em', 45.16)],
    [('Như', 45.36), ('hai', 45.54), ('ta', 45.76), ('chưa', 45.98), ('từng', 46.18), ('thiếu', 46.42), ('nhau', 46.78)],
    [('Chưa', 47.12), ('bao', 47.44), ('giờ', 47.7), ('anh', 47.84), ('chán', 48.12), ('em', 48.54)],
    [('Đây', 48.86), ('đâu', 49.1), ('phải', 49.36), ('là', 49.54), ('ván', 49.78), ('game', 50.22)],
    [('Câu', 50.56), ('yêu', 50.78), ('thương', 50.98), ('này', 51.2), ('quá', 51.38), ('quen', 51.74)],
    [('Em', 52.42), ('đoán', 52.64), ('xem', 53.02)],
    [('Giờ', 54.0), ('lại', 54.54), ('ngồi', 54.7), ('ở', 55.0), ('trong', 55.18), ('phòng', 55.38), ('thu', 55.54)],
    [('Và', 55.78), ('anh', 56.0), ('lại', 56.16), ('cuốn', 56.4)],
    [('Dặn', 56.82), ('lòng', 57.1), ('rằng', 58.02), ('phải', 58.2), ('giữ', 58.42), ('tỉnh', 58.64), ('táo', 58.94)],
    [('Nên', 59.1), ('anh', 59.3), ('phải', 59.46), ('uống', 59.68)],
    [('Bật', 60.86), ('bài', 61.16), ('nhạc', 61.34), ('em', 61.64), ('thích', 61.74), ('ngày', 61.98), ('xưa', 62.16)],
    [('Cảm', 62.38), ('xúc', 62.66), ('lại', 62.84), ('tuôn', 63.02)],
    [('Tự', 64.28), ('hỏi', 64.5), ('bản', 64.68), ('thân', 64.94), ('sao', 65.1), ('ngày', 65.36), ('đó', 65.5)],
    [('Tay', 65.72), ('em', 65.96), ('lại', 66.22), ('buông', 66.38)],
]
ENDS = [2.82, 5.94, 9.26, 13.42, 15.86, 19.3, 22.92, 26.16, 28.56, 30.22, 32.16, 34.34, 35.52, 36.82, 38.88, 40.08, 42.08, 43.04, 43.72, 45.36, 47.12, 48.8, 50.56, 52.24, 54.0, 55.78, 56.82, 59.1, 60.0, 62.38, 64.28, 65.72, 66.72]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play(start=START)

    # Là vì ai?   [reveal: slow]
    sync_words(song, LINES[0], ENDS[0], mode='reveal', palette='hong', indent=8)
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.3, breathe, palette='hong', indent=8)
    dissolve_out('        ' + text(LINES[0]), 0.25, palette='hong')

    # Nỗi cô đơn này là vì ai?   [mist: bạn chọn]
    sync_words(song, LINES[1], ENDS[1], mode='mist', palette='hong', indent=2)
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, breathe, palette='hong', indent=2)
    newline()

    # Em nói anh nghe anh làm gì sai?   [glitch: từ "sai"]
    sync_words(song, LINES[2], ENDS[2], mode='glitch', palette='tim')
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.1, shine, palette='tim')
    newline()

    # Quá khứ kia giờ nhạt phai   [typewriter: slow, long]
    sync_words(song, LINES[3], ENDS[3], mode='typewriter', palette='tim', indent=4)
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Một thằng ngu   [fadein: slow]
    sync_words(song, LINES[4], ENDS[4], mode='fadein', palette='bien', indent=8)
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.3, breathe, palette='bien', indent=8)
    drift_out('        ' + text(LINES[4]), 0.25, palette='bien')

    # Cuối cùng chỉ là một thằng ngu   [glitch: bạn chọn]
    sync_words(song, LINES[5], ENDS[5], mode='glitch', palette='bien')
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='bien')
    newline()

    # Em đưa anh lên rồi đạp anh xuống   [rise: bạn chọn]
    sync_words(song, LINES[6], ENDS[6], mode='rise', palette='hoanghon')
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.3, breathe, palette='hoanghon')
    center_out('' + text(LINES[6]), 0.25, palette='hoanghon')

    # Đó có phải điều em mong muốn?   [letters: từ "mong", long, finale]
    sync_words(song, LINES[7], ENDS[7], mode='letters', palette='hoanghon')
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.1, breathe, palette='hoanghon')
    newline()

    newline()  # hết đoạn

    # Đó-đó có phải điều em mong muốn   [typo: bạn chọn]
    sync_words(song, LINES[8], ENDS[8], mode='typo', palette='hong')
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.3, breathe, palette='hong')
    sweep_out('' + text(LINES[8]), 0.25, palette='hong')

    # Là anh phải đi khỏi đây?   [words: fast]
    sync_words(song, LINES[9], ENDS[9], mode='words', palette='hong', indent=4)
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.1, breathe, palette='hong', indent=4)
    newline()

    # Anh cũng chẳng thể giữ nữa   [mist: đa dạng]
    sync_words(song, LINES[10], ENDS[10], mode='mist', palette='tim')
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.1, shine, palette='tim')
    newline()

    # Khi anh đang mỏi tay, yeah   [drop: bạn chọn]
    sync_words(song, LINES[11], ENDS[11], mode='drop', palette='tim', indent=4)
    hold(song, text(LINES[11]), LINES[12][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Con tim giờ trống rỗng   [scramble: fast]
    sync_words(song, LINES[12], ENDS[12], mode='scramble', palette='bien')
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.1, breathe, palette='bien')
    newline()

    # Cố tỏ ra thờ ơ   [ripple: đa dạng]
    sync_words(song, LINES[13], ENDS[13], mode='ripple', palette='bien', indent=12)
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.1, breathe, palette='bien', indent=12)
    newline()

    # Em bây giờ không giống ngày xưa nên   [words: fast, long]
    sync_words(song, LINES[14], ENDS[14], mode='words', palette='hoanghon')
    hold(song, text(LINES[14]), LINES[15][0][1] - 0.1, shine, palette='hoanghon')
    newline()

    # I can't feel the love   [pop: fast]
    sync_words(song, LINES[15], ENDS[15], mode='pop', palette='hoanghon', indent=4)
    hold(song, text(LINES[15]), LINES[16][0][1] - 0.1, breathe, palette='hoanghon', indent=4)
    newline()

    # Cứ bước tiếp đi anh không níu đâu   [words: bạn chọn]
    sync_words(song, LINES[16], ENDS[16], mode='words', palette='bac')
    hold(song, text(LINES[16]), LINES[17][0][1] - 0.1, breathe, palette='bac')
    newline()

    # Anh biết đau mà   [drop: short]
    sync_words(song, LINES[17], ENDS[17], mode='drop', palette='bac', indent=4)
    hold(song, text(LINES[17]), LINES[18][0][1] - 0.3, breathe, palette='bac', indent=4)
    dissolve_out('    ' + text(LINES[17]), 0.25, palette='bac')

    # You know   [center: short]
    sync_words(song, LINES[18], ENDS[18], mode='center', palette='hong', indent=8)
    hold(song, text(LINES[18]), LINES[19][0][1] - 0.1, shine, palette='hong', indent=8)
    newline()

    # Sống như khi anh chưa gặp em   [slide: fast]
    sync_words(song, LINES[19], ENDS[19], mode='slide', palette='hong')
    hold(song, text(LINES[19]), LINES[20][0][1] - 0.1, breathe, palette='hong')
    newline()

    # Như hai ta chưa từng thiếu nhau   [flow: đa dạng]
    sync_words(song, LINES[20], ENDS[20], mode='flow', palette='tim', indent=4)
    hold(song, text(LINES[20]), LINES[21][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Chưa bao giờ anh chán em   [spotlight: đa dạng]
    sync_words(song, LINES[21], ENDS[21], mode='spotlight', palette='tim')
    hold(song, text(LINES[21]), LINES[22][0][1] - 0.1, breathe, palette='tim')
    newline()

    # Đây đâu phải là ván game   [karaoke: đa dạng]
    sync_words(song, LINES[22], ENDS[22], mode='karaoke', palette='bien', indent=4)
    hold(song, text(LINES[22]), LINES[23][0][1] - 0.1, shine, palette='bien', indent=4)
    newline()

    # Câu yêu thương này quá quen   [hearts: từ "yêu"]
    sync_words(song, LINES[23], ENDS[23], mode='hearts', palette='bien')
    hold(song, text(LINES[23]), LINES[24][0][1] - 0.1, heartbeat, palette='bien')
    newline()

    # Em đoán xem   [scramble: bạn chọn]
    sync_words(song, LINES[24], ENDS[24], mode='scramble', palette='hoanghon', indent=8)
    trailing_dots(song, text(LINES[24]), LINES[25][0][1] - 0.1, palette='hoanghon', indent=8)
    newline()

    # Giờ lại ngồi ở trong phòng thu   [pop: fast, loud]
    sync_words(song, LINES[25], ENDS[25], mode='pop', palette='hoanghon')
    hold(song, text(LINES[25]), LINES[26][0][1] - 0.3, breathe, palette='hoanghon')
    gradient_fade_out('' + text(LINES[25]), 0.25, palette='hoanghon')

    # Và anh lại cuốn   [glitch: fast, short]
    sync_words(song, LINES[26], ENDS[26], mode='glitch', palette='bac', indent=4)
    hold(song, text(LINES[26]), LINES[27][0][1] - 0.1, shine, palette='bac', indent=4)
    newline()

    # Dặn lòng rằng phải giữ tỉnh táo   [sides: đa dạng]
    sync_words(song, LINES[27], ENDS[27], mode='sides', palette='bac')
    hold(song, text(LINES[27]), LINES[28][0][1] - 0.3, breathe, palette='bac')
    dissolve_out('' + text(LINES[27]), 0.25, palette='bac')

    # Nên anh phải uống   [drop: short]
    sync_words(song, LINES[28], ENDS[28], mode='drop', palette='hong', indent=4)
    hold(song, text(LINES[28]), LINES[29][0][1] - 0.1, shine, palette='hong', indent=4)
    newline()

    # Bật bài nhạc em thích ngày xưa   [mist: từ "ngày xưa"]
    sync_words(song, LINES[29], ENDS[29], mode='mist', palette='hong')
    hold(song, text(LINES[29]), LINES[30][0][1] - 0.3, breathe, palette='hong')
    center_out('' + text(LINES[29]), 0.25, palette='hong')

    # Cảm xúc lại tuôn   [wave: đa dạng]
    sync_words(song, LINES[30], ENDS[30], mode='wave', palette='tim', indent=4)
    hold(song, text(LINES[30]), LINES[31][0][1] - 0.1, shine, palette='tim', indent=4)
    newline()

    # Tự hỏi bản thân sao ngày đó   [scramble: fast]
    sync_words(song, LINES[31], ENDS[31], mode='scramble', palette='tim', indent=4)
    hold(song, text(LINES[31]), LINES[32][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Tay em lại buông   [letters: finale]
    sync_words(song, LINES[32], ENDS[32], mode='letters', palette='bien', indent=8)
    trailing_dots(song, text(LINES[32]), ENDS[32] + 3.0, palette='bien', indent=8)
    hold(song, text(LINES[32]) + '...', ENDS[32] + 4.5, heartbeat, palette='bien', indent=8)
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
