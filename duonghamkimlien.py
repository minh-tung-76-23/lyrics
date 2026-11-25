import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = True
set_color(COLOR)
# True = tô vàng tên riêng (từ viết hoa giữa câu)
ACCENT = False
set_accent(ACCENT)

# Phát nhạc từ giây thứ START của bài
START = 0.0

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7710062834960452916.mp3'), offset=OFFSET)

LINES = [
    [('Em', 0.92), ('nói', 1.44), ('những', 1.76), ('bài', 1.92), ('nhạc', 2.06), ('anh', 2.34), ('viết', 2.62)],
    [('Em', 2.98), ('từng', 3.28), ('yêu', 3.54), ('chỉ', 3.74), ('vì', 3.9), ('nó', 4.02), ('ân', 4.34), ('cần', 4.62)],
    [('Vậy', 5.06), ('nếu', 5.48), ('như', 5.78), ('một', 5.9), ('ngày', 6.06), ('em', 6.28), ('biết', 6.56)],
    [('Baby', 6.96), ('ơi', 7.48), ('chẳng', 7.74), ('một', 7.88), ('chút', 8.06), ('chân', 8.24), ('thật', 8.58)],
    [('Anh', 9.02), ('đóng', 9.52), ('qua', 9.82), ('đường', 9.88), ('hầm', 10.04), ('Kim', 10.3), ('Liên', 10.62)],
    [('Nguyên', 10.92), ('một', 11.3), ('cây', 11.56), ('màu', 11.76), ('đen', 11.94), ('vẫn', 12.04), ('âm', 12.26), ('thầm', 12.62)],
    [('Anh', 13.18), ('muốn', 13.5), ('quay', 13.76), ('về', 13.9), ('ngày', 14.0), ('đầu', 14.3), ('tiên', 14.64)],
    [('Quay', 14.98), ('về', 15.28), ('nơi', 15.52), ('không', 15.74), ('có', 15.92), ('nỗi', 16.04), ('ân', 16.28), ('hận', 16.6)],
    [('Đứng', 17.2), ('trước', 17.48), ('lễ', 17.74), ('đường', 17.86), ('ngày', 18.04), ('hôm', 18.32), ('ấy', 18.56)],
    [('Em', 18.94), ('lộng', 19.28), ('lẫy', 19.6), ('giữa', 19.78), ('chốn', 20.0), ('đông', 20.26), ('người', 20.5)],
    [('Hai', 21.02), ('đôi', 21.44), ('mắt', 21.54), ('ta', 21.72), ('chầm', 21.88), ('chậm', 22.1), ('nhìn', 22.28), ('nhau', 22.48)],
    [('Nhưng', 22.98), ('tại', 23.26), ('sao', 23.56), ('đôi', 23.72), ('mắt', 23.86), ('ấy', 24.02), ('không', 24.24), ('cười?', 24.52)],
    [('Em', 25.06), ('hứa', 25.54), ('sẽ', 25.82), ('ở', 25.9), ('lại', 26.04), ('bên', 26.3), ('anh', 26.5)],
    [('Bây', 26.98), ('giờ', 27.32), ('đây', 27.54), ('lời', 27.76), ('hứa', 27.86), ('ấy', 28.06), ('đâu', 28.26), ('rồi?', 28.58)],
    [('Tan', 28.92), ('biến', 29.5), ('vào', 29.78), ('khoảng', 29.86), ('trời', 30.02), ('màu', 30.26), ('xanh', 30.62)],
    [('Hoa', 31.02), ('tàn', 31.32), ('phai', 31.56), ('chôn', 31.78), ('cất', 32.02), ('sau', 32.3), ('đồi', 32.6)],
    [('Nâng', 33.16), ('ly', 33.44), ('lên', 33.54), ('nói', 33.78), ('là', 33.88), ('"1,', 34.04), ('2,', 34.34), ('3"', 35.12)],
    [('Anh', 35.12), ('chỉ', 35.4), ('nghe', 35.5), ('được', 35.78), ('là', 35.9), ('1,', 36.04), ('2', 36.36), ('bar', 36.85)],
    [('Ngắm', 37.12), ('nhìn', 37.4), ('em', 37.54), ('đi', 37.74), ('cùng', 37.86), ('người', 38.02), ('em', 38.22), ('thương', 38.56)],
    [('Để', 38.74), ('lại', 38.88), ('người', 39.02), ('thương', 39.24), ('em', 39.52), ('bất', 39.8), ('chợt', 40.1), ('quay', 40.24), ('ra', 40.58)],
    [('Anh', 40.96), ('tự', 41.4), ('lấy', 41.54), ('cho', 41.72), ('mình', 41.86), ('một', 42.04), ('hợp', 42.28), ('âm', 42.6)],
    [('Anh', 43.14), ('tự', 43.34), ('viết', 43.52), ('cho', 43.74), ('mình', 43.84), ('một', 44.08), ('bài', 44.32), ('ca', 44.56)],
    [('Trên', 44.96), ('con', 45.38), ('phố', 45.52), ('đi', 45.76), ('tìm', 45.88), ('một', 46.06), ('loài', 46.3), ('hoa', 46.54)],
    [('Chấp', 46.76), ('nhận', 46.88), ('một', 47.02), ('tay', 47.3), ('buông', 47.52), ('để', 47.74), ('lại', 47.86), ('một', 48.0), ('tay', 48.28), ('ga', 48.48)],
]
ENDS = [2.98, 5.06, 6.96, 9.02, 10.92, 13.18, 14.98, 17.2, 18.94, 21.02, 22.98, 25.06, 26.98, 28.92, 30.88, 33.16, 35.22, 37.15, 38.74, 40.96, 43.14, 44.96, 46.76, 48.82]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play(start=START)

    # Em nói những bài nhạc anh viết   [typewriter: bạn chọn]
    sync_words(song, LINES[0], ENDS[0], mode='typewriter', palette='hong')
    hold(song, text(LINES[0]), LINES[1][0][1] - 0.1, shine, palette='hong')
    newline()

    # Em từng yêu chỉ vì nó ân cần   [bloom: bạn chọn]
    sync_words(song, LINES[1], ENDS[1], mode='bloom', palette='hong', indent=4)
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, heartbeat, palette='hong', indent=4)
    newline()

    # Vậy nếu như một ngày em biết   [reveal: bạn chọn]
    sync_words(song, LINES[2], ENDS[2], mode='reveal', palette='tim')
    hold(song, text(LINES[2]), LINES[3][0][1] - 0.3, breathe, palette='tim')
    gradient_fade_out('' + text(LINES[2]), 0.25, palette='tim')

    # Baby ơi chẳng một chút chân thật   [glitch: bạn chọn]
    sync_words(song, LINES[3], ENDS[3], mode='glitch', palette='tim', indent=4)
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim', indent=4)
    newline()

    # Anh đóng qua đường hầm Kim Liên   [glide: bạn chọn]
    sync_words(song, LINES[4], ENDS[4], mode='glide', palette='bien')
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.3, breathe, palette='bien')
    dissolve_out('' + text(LINES[4]), 0.25, palette='bien')

    # Nguyên một cây màu đen vẫn âm thầm   [fadein: bạn chọn]
    sync_words(song, LINES[5], ENDS[5], mode='fadein', palette='bien', indent=4)
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.3, breathe, palette='bien', indent=4)
    center_out('    ' + text(LINES[5]), 0.25, palette='bien')

    # Anh muốn quay về ngày đầu tiên   [mist: bạn chọn]
    sync_words(song, LINES[6], ENDS[6], mode='mist', palette='hoanghon')
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.1, shine, palette='hoanghon')
    newline()

    # Quay về nơi không có nỗi ân hận   [letters: bạn chọn]
    sync_words(song, LINES[7], ENDS[7], mode='letters', palette='hoanghon', indent=4)
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.1, breathe, palette='hoanghon', indent=4)
    newline()

    # Đứng trước lễ đường ngày hôm ấy   [spotlight: bạn chọn]
    sync_words(song, LINES[8], ENDS[8], mode='spotlight', palette='bac')
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.1, shine, palette='bac')
    newline()

    # Em lộng lẫy giữa chốn đông người   [sparkle: bạn chọn]
    sync_words(song, LINES[9], ENDS[9], mode='sparkle', palette='bac', indent=4)
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.1, breathe, palette='bac', indent=4)
    newline()

    # Hai đôi mắt ta chầm chậm nhìn nhau   [center: bạn chọn]
    sync_words(song, LINES[10], ENDS[10], mode='center', palette='hong')
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.1, shine, palette='hong')
    newline()

    # Nhưng tại sao đôi mắt ấy không cười?   [drop: bạn chọn]
    sync_words(song, LINES[11], ENDS[11], mode='drop', palette='hong', indent=4)
    hold(song, text(LINES[11]), LINES[12][0][1] - 0.1, breathe, palette='hong', indent=4)
    newline()

    # Em hứa sẽ ở lại bên anh   [hearts: bạn chọn]
    sync_words(song, LINES[12], ENDS[12], mode='hearts', palette='tim', indent=4)
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.1, shine, palette='tim', indent=4)
    newline()

    # Bây giờ đây lời hứa ấy đâu rồi?   [words: bạn chọn]
    sync_words(song, LINES[13], ENDS[13], mode='words', palette='tim')
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.1, breathe, palette='tim')
    newline()

    # Tan biến vào khoảng trời màu xanh   [rise: bạn chọn]
    sync_words(song, LINES[14], ENDS[14], mode='rise', palette='bien')
    hold(song, text(LINES[14]), LINES[15][0][1] - 0.1, shine, palette='bien')
    newline()

    # Hoa tàn phai chôn cất sau đồi   [karaoke: bạn chọn]
    sync_words(song, LINES[15], ENDS[15], mode='karaoke', palette='bien', indent=4)
    hold(song, text(LINES[15]), LINES[16][0][1] - 0.1, breathe, palette='bien', indent=4)
    newline()

    # Nâng ly lên nói là "1, 2, 3"   [pop: bạn chọn]
    sync_words(song, LINES[16], ENDS[16], mode='pop', palette='hoanghon')
    hold(song, text(LINES[16]), LINES[17][0][1] - 0.3, breathe, palette='hoanghon')
    sweep_out('' + text(LINES[16]), 0.25, palette='hoanghon')

    # Anh chỉ nghe được là 1, 2 bar   [shake: bạn chọn]
    sync_words(song, LINES[17], ENDS[17], mode='shake', palette='hoanghon')
    hold(song, text(LINES[17]), LINES[18][0][1] - 0.1, breathe, palette='hoanghon')
    newline()

    # Ngắm nhìn em đi cùng người em thương   [ripple: bạn chọn]
    sync_words(song, LINES[18], ENDS[18], mode='ripple', palette='bac')
    hold(song, text(LINES[18]), LINES[19][0][1] - 0.3, breathe, palette='bac')
    drift_out('' + text(LINES[18]), 0.25, palette='bac')

    # Để lại người thương em bất chợt quay ra   [swipe: bạn chọn]
    sync_words(song, LINES[19], ENDS[19], mode='swipe', palette='bac')
    hold(song, text(LINES[19]), LINES[20][0][1] - 0.3, breathe, palette='bac')
    gradient_fade_out('' + text(LINES[19]), 0.25, palette='bac')

    # Anh tự lấy cho mình một hợp âm   [wave: bạn chọn]
    sync_words(song, LINES[20], ENDS[20], mode='wave', palette='hong')
    hold(song, text(LINES[20]), LINES[21][0][1] - 0.3, breathe, palette='hong')
    dissolve_out('' + text(LINES[20]), 0.25, palette='hong')

    # Anh tự viết cho mình một bài ca   [flow: bạn chọn]
    sync_words(song, LINES[21], ENDS[21], mode='flow', palette='hong')
    hold(song, text(LINES[21]), LINES[22][0][1] - 0.3, breathe, palette='hong')
    center_out('' + text(LINES[21]), 0.25, palette='hong')

    # Trên con phố đi tìm một loài hoa   [bloom: bạn chọn]
    sync_words(song, LINES[22], ENDS[22], mode='bloom', palette='tim')
    hold(song, text(LINES[22]), LINES[23][0][1] - 0.1, shine, palette='tim')
    newline()

    # Chấp nhận một tay buông để lại một tay ga   [slide: bạn chọn]
    sync_words(song, LINES[23], ENDS[23], mode='slide', palette='tim')
    hold(song, text(LINES[23]), ENDS[23] + 1.5, heartbeat, palette='tim')
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
