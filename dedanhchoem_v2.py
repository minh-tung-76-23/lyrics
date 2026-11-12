import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = True
set_color(COLOR)

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7692046376548502791.mp3'), offset=OFFSET)

LINES = [
    [('Và', 0.0), ('điều', 0.82), ('khó', 1.08), ('nhất', 1.54)],
    [('Một', 2.64), ('mình', 2.78), ('thì', 2.98), ('hơi', 3.2), ('côi', 3.56)],
    [('Hà', 4.3), ('Nội', 4.9), ('gió', 5.06), ('bấc', 5.52)],
    [('Do', 5.86), ('you', 6.04), ('wanna', 6.16), ('dựa', 6.4), ('đầu', 6.78), ('vào', 6.94), ('nơi', 7.14), ('tôi?', 7.44)],
    [('Điều', 7.82), ('gì', 7.94), ('phiền', 8.06), ('muộn', 8.24), ('nói', 8.42), ('nhau', 8.82), ('nghe', 9.06), ('đi', 9.42), ('nào', 9.76)],
    [('Xem', 10.02), ('là', 10.26), ('hôm', 10.44), ('nay', 10.76), ('sao', 11.0), ('rồi', 11.32)],
    [('Mình', 12.04), ('cất', 12.44), ('lên', 12.8), ('câu', 13.04), ('"xin', 13.36), ('chào"', 13.7)],
    [('anh', 14.06), ('đã', 14.26), ('sợ', 14.48), ('ngày', 14.66), ('phải', 14.9), ('xa', 15.12), ('rời', 15.46)],
    [('Ngồi', 16.2), ('sau', 16.74), ('xe', 17.0), ('anh', 17.38)],
    [('Và', 17.9), ('đừng', 18.66), ('né', 18.98), ('tránh', 19.36)],
    [('Tình', 20.04), ('yêu', 20.64), ('ở', 20.82), ('đấy', 21.06), ('đó', 21.32)],
    [('Nên', 21.64), ('anh', 21.9), ('mong', 22.04), ('là', 22.1), ('em', 22.3), ('sẽ', 22.58), ('thấy', 22.9), ('nó', 23.24)],
    [('Vì', 23.96), ('anh', 24.56), ('lại', 24.94), ('ngốc', 25.2), ('nghếch', 25.4)],
    [('Trao', 25.68), ('đi', 25.74), ('cho', 25.9), ('em', 26.06), ('con', 26.22), ('tim', 26.54), ('chân', 26.82), ('thành', 27.18)],
    [('Nó', 27.48), ('chỉ', 27.84), ('muốn', 28.14), ('được', 28.54), ('yêu', 28.9), ('thươnggg', 29.38)],
    [('À', 31.4), ('hóa', 32.22), ('ra', 32.76), ('em', 32.92), ('đây', 33.24), ('rồi', 33.82)],
    [('Người', 35.9), ('chở', 36.1), ('che', 36.62), ('con', 36.78), ('tim', 37.14), ('chỉ', 37.7), ('sợ', 38.14), ('đánh', 38.68), ('mất', 39.16)],
    [('Bước', 39.94), ('ra', 40.36), ('từ', 40.68), ('trong', 41.12)],
    [('Những', 42.24), ('giấc', 42.7), ('mơ', 43.06), ('rồi', 43.34), ('lại', 43.74), ('hằn', 44.0), ('vào', 44.38), ('trí', 44.88), ('nhớ', 45.12)],
    [('Đến', 46.18), ('bao', 46.72), ('giờ?', 46.96)],
    [('Một', 47.8), ('phần', 48.32), ('chỉ', 48.54), ('sợ', 48.92), ('đau', 49.62), ('nữa', 50.26), ('thôi', 50.86)],
    [('Phần', 51.74), ('kia', 52.22), ('lại', 52.6), ('muốn', 52.92), ('cô', 53.22), ('này', 53.64), ('phải', 53.88), ('là', 54.26), ('của', 54.56), ('tôi', 54.92)],
    [('Chơi', 56.58), ('bời', 56.58), ('chán', 56.82), ('chưa', 57.22)],
    [('anh', 57.62), ('muốn', 57.9), ('đi', 58.2), ('đường', 58.58), ('dài?', 58.84)],
    [('Đứng', 59.88), ('đây', 60.54), ('ngóng', 60.82), ('em', 61.24), ('đón', 61.5), ('anh', 61.84), ('về', 62.18), ('tương', 62.48), ('lai', 62.84)],
    [('Đều', 63.22), ('là', 63.52), ('để', 64.01), ('dành', 64.18), ('cho', 64.4), ('em', 64.96)],
]
ENDS = [2.16, 4.3, 5.86, 7.76, 10.02, 12.04, 14.06, 16.2, 17.9, 20.04, 21.64, 23.96, 25.68, 27.48, 29.94, 34.94, 39.94, 42.24, 46.18, 47.8, 51.74, 55.94, 57.62, 59.88, 63.22, 65.62]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play()

    # Và điều khó nhất
    sync_words(song, LINES[0], ENDS[0], mode='karaoke', palette='hong')
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.1, shine, palette='hong')
    newline()

    # Một mình thì hơi côi
    sync_words(song, LINES[1], ENDS[1], mode='bounce', palette='hong')
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, breathe, palette='hong')
    newline()

    # Hà Nội gió bấc
    sync_words(song, LINES[2], ENDS[2], mode='slide', palette='tim')
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.1, shine, palette='tim')
    newline()

    # Do you wanna dựa đầu vào nơi tôi?
    sync_words(song, LINES[3], ENDS[3], mode='reveal', palette='tim', indent=4)
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Điều gì phiền muộn nói nhau nghe đi nào
    sync_words(song, LINES[4], ENDS[4], mode='jump', palette='bien')
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='bien')
    newline()

    # Xem là hôm nay sao rồi
    sync_words(song, LINES[5], ENDS[5], mode='scramble', palette='bien', indent=4)
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='bien', indent=4)
    newline()

    # Mình cất lên câu "xin chào"
    sync_words(song, LINES[6], ENDS[6], mode='drop', palette='hoanghon')
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.1, shine, palette='hoanghon')
    newline()

    # anh đã sợ ngày phải xa rời
    sync_words(song, LINES[7], ENDS[7], mode='wave', palette='hoanghon', indent=8)
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.1, breathe, palette='hoanghon', indent=8)
    newline()

    # Ngồi sau xe anh
    sync_words(song, LINES[8], ENDS[8], mode='converge', palette='bac')
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.3, breathe, palette='bac')
    gradient_fade_out('' + text(LINES[8]), 0.2, palette='bac')

    # Và đừng né tránh
    sync_words(song, LINES[9], ENDS[9], mode='typewriter', palette='bac')
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.3, breathe, palette='bac')
    gradient_fade_out('' + text(LINES[9]), 0.2, palette='bac')

    # Tình yêu ở đấy đó
    sync_words(song, LINES[10], ENDS[10], mode='pop', palette='hong')
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.3, breathe, palette='hong')
    gradient_fade_out('' + text(LINES[10]), 0.2, palette='hong')

    # Nên anh mong là em sẽ thấy nó
    sync_words(song, LINES[11], ENDS[11], mode='pop', palette='hong')
    hold(song, text(LINES[11]), LINES[12][0][1] - 0.3, breathe, palette='hong')
    gradient_fade_out('' + text(LINES[11]), 0.2, palette='hong')

    # Vì anh lại ngốc nghếch
    sync_words(song, LINES[12], ENDS[12], mode='rainbow', palette='tim')
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.1, shine, palette='tim')
    newline()

    # Trao đi cho em con tim chân thành
    sync_words(song, LINES[13], ENDS[13], mode='flicker', palette='tim')
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.1, breathe, palette='tim')
    newline()

    # Nó chỉ muốn được yêu thươnggg
    sync_words(song, LINES[14], ENDS[14], mode='karaoke', palette='bien', indent=4)
    hold(song, text(LINES[14]), LINES[15][0][1] - 0.1, shine, palette='bien', indent=4)
    newline()

    # À hóa ra em đây rồi
    sync_words(song, LINES[15], ENDS[15], mode='bounce', palette='bien')
    hold(song, text(LINES[15]), LINES[16][0][1] - 0.1, breathe, palette='bien')
    newline()

    # Người chở che con tim chỉ sợ đánh mất
    sync_words(song, LINES[16], ENDS[16], mode='slide', palette='hoanghon')
    hold(song, text(LINES[16]), LINES[17][0][1] - 0.1, shine, palette='hoanghon')
    newline()

    # Bước ra từ trong
    sync_words(song, LINES[17], ENDS[17], mode='reveal', palette='hoanghon', indent=4)
    hold(song, text(LINES[17]), LINES[18][0][1] - 0.1, breathe, palette='hoanghon', indent=4)
    newline()

    # Những giấc mơ rồi lại hằn vào trí nhớ
    sync_words(song, LINES[18], ENDS[18], mode='jump', palette='bac')
    hold(song, text(LINES[18]), LINES[19][0][1] - 0.1, shine, palette='bac')
    newline()

    # Đến bao giờ?
    sync_words(song, LINES[19], ENDS[19], mode='scramble', palette='bac', indent=12)
    hold(song, text(LINES[19]), LINES[20][0][1] - 0.1, breathe, palette='bac', indent=12)
    newline()

    # Một phần chỉ sợ đau nữa thôi
    sync_words(song, LINES[20], ENDS[20], mode='pop', palette='hong', indent=4)
    hold(song, text(LINES[20]), LINES[21][0][1] - 0.3, breathe, palette='hong', indent=4)
    gradient_fade_out('    ' + text(LINES[20]), 0.2, palette='hong')

    # Phần kia lại muốn cô này phải là của tôi
    sync_words(song, LINES[21], ENDS[21], mode='pop', palette='hong')
    hold(song, text(LINES[21]), LINES[22][0][1] - 0.1, breathe, palette='hong')
    newline()

    # Chơi bời chán chưa
    sync_words(song, LINES[22], ENDS[22], mode='converge', palette='tim')
    hold(song, text(LINES[22]), LINES[23][0][1] - 0.1, shine, palette='tim')
    newline()

    # anh muốn đi đường dài?
    sync_words(song, LINES[23], ENDS[23], mode='typewriter', palette='tim', indent=4)
    hold(song, text(LINES[23]), LINES[24][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Đứng đây ngóng em đón anh về tương lai
    sync_words(song, LINES[24], ENDS[24], mode='rise', palette='bien')
    hold(song, text(LINES[24]), LINES[25][0][1] - 0.1, shine, palette='bien')
    newline()

    # Đều là để dành cho em
    sync_words(song, LINES[25], ENDS[25], mode='pop', palette='bien', indent=8)
    trailing_dots(song, text(LINES[25]), ENDS[25] + 3.0, palette='bien', indent=8)
    hold(song, text(LINES[25]) + '...', ENDS[25] + 4.5, heartbeat, palette='bien', indent=8)
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
