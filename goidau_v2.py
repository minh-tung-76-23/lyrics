import os
from animation_plus import *

# Chỉnh lệch toàn bài: chữ ra SỚM hơn nhạc -> tăng OFFSET (vd 0.2), TRỄ -> giảm
OFFSET = 0.0
# True = chữ màu, False = chữ trắng
COLOR = True
set_color(COLOR)

# Phát nhạc từ giây thứ START của bài
START = 159.02

song = Song(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input/mp3/7624234690135788807.mp3'), offset=OFFSET)

LINES = [
    [('Turn', 160.02), ('it', 160.46), ('up', 160.64), ('dô', 161.32)],
    [('Baby,', 161.7), ('she', 162.28), ('wants', 162.54), ('to', 162.7), ('be', 163.2), ('loved', 163.62)],
    [('This', 163.98), ('is', 164.66), ('not', 165.1), ('enough', 165.48), ('enough', 166.28)],
    [('Nên', 166.49), ('hay', 166.49), ('là', 166.7), ('kiếm', 166.94), ('chốn', 167.4), ('nào', 167.6), ('để', 167.8), ('đáp', 168.22)],
    [('Em', 168.88), ('là', 169.3), ('cây', 169.5), ('khô', 169.7), ('đang', 169.96), ('cần', 170.02), ('được', 170.24), ('tưới', 170.46), ('tắm', 170.76)],
    [('Hoa', 171.7), ('muốn', 172.32), ('nở', 172.58), ('phải', 172.84), ('có', 173.24), ('nắng', 173.64)],
    [('Nhưng', 174.14), ('em', 174.68), ('hoàn', 174.92), ('toàn', 175.2), ('trống', 175.36), ('vắng', 176.24)],
    [('Cô', 176.86), ('đơn', 177.34), ('và', 177.71), ('mong', 177.83), ('manh', 177.96)],
    [('Lao', 180.0), ('ngay', 180.0), ('vào', 180.16), ('trong', 180.42), ('anh', 180.84)],
    [('Hãy', 181.2), ('đưa', 181.2), ('em', 181.6), ('đi', 181.74), ('thật', 181.92), ('xa,', 182.08)],
    [('thật', 182.66), ('xa,', 182.76)],
    [('thật', 183.39), ('xa', 183.6), ('oh', 183.86), ('yeah,', 183.86), ('xa-ah-ah-ah-ah-ah', 183.86)],
    [('Ở', 184.18), ('một', 184.6), ('nơi', 184.74), ('chỉ', 184.82), ('còn', 185.22), ('hai', 185.52), ('ta', 185.94)],
    [('Nội', 186.74), ('tâm', 187.18), ('em', 187.4), ('đang', 187.68), ('hơi', 187.8), ('chen', 188.06), ('chúc', 188.3)],
    [('Cần', 188.68), ('được', 189.18), ('quan', 189.62), ('tâm', 189.96), ('như', 190.16), ('bông', 190.26), ('hoa', 190.88), ('cúc', 190.88)],
    [('Đôi', 191.4), ('lúc', 191.78), ('body', 192.21), ('này', 192.46), ('cần', 192.6), ('được', 192.8), ('vuốt', 192.86), ('ve', 192.96), ('một', 193.26), ('chút', 193.48)],
    [('To', 194.1), ('get', 194.42), ('her', 194.84), ('in', 195.26), ('a', 195.58), ('better', 195.79), ('mood', 196.52)],
    [('I', 197.05), ('gotta', 197.26), ('be', 197.89), ('the', 198.21), ('man', 198.63), ('I', 199.05), ('should', 199.26)],
    [('Ey', 200.0)],
    [('Oh-oh', 202.06)],
    [('Khi', 203.18), ('tình', 203.86), ('yêu', 204.18), ('của', 204.52), ('em', 204.92), ('ở', 205.28), ('bên', 205.4), ('kia', 205.7), ('cầu', 206.04)],
    [('Khi', 208.26), ('tình', 208.94), ('yêu', 209.28), ('của', 209.62), ('anh', 209.92), ('á', 210.24), ('đang', 210.44), ('gội', 210.74), ('đầu', 211.16)],
    [('Qua', 213.32), ('một', 214.0), ('đêm', 214.26), ('lại', 214.64), ('thấy', 214.9), ('mình', 215.3), ('thêm', 215.6), ('một', 215.8), ('xấu', 217.81)],
    [('Sâu', 219.46)],
    [('Oh-oh', 220.22), ('oh,', 220.98), ('oh,', 222.12), ('oh', 222.12)],
    [('Khi', 223.46), ('quả', 224.08), ('tim', 224.36), ('của', 224.74), ('em', 225.22), ('nó', 225.5), ('đang', 225.7), ('thay', 225.9), ('màu', 226.3), ('oh,', 227.15), ('oh,', 227.62), ('oh', 228.09)],
    [('Xin', 228.56), ('một', 229.18), ('hơi', 229.46), ('thật', 229.84), ('sâu', 230.08), ('trước', 230.42), ('khi', 230.76), ('bắt', 231.04), ('đầu', 231.44), ('oh,', 232.64), ('oh,', 232.82), ('oh', 233.0)],
    [('Và', 233.18), ('đưa', 233.82), ('bàn', 234.26), ('tay', 234.5), ('bạn', 234.8), ('đây', 235.14), ('làm', 235.46), ('sao', 235.68), ('phải', 235.96), ('giấu?', 236.24)],
    [('Giấu', 239.28)],
    [('uno,', 240.04), ('dos,', 240.34), ('tres,', 240.64), ('cuatro', 240.94)],
]
ENDS = [161.62, 163.98, 166.7, 168.88, 171.7, 173.88, 176.86, 180.16, 181.2, 182.5, 183.18, 184.16, 186.74, 188.68, 191.4, 194.1, 197.05, 200.0, 200.94, 202.36, 206.74, 211.74, 218.11, 220.22, 222.5, 228.39, 233.3, 236.62, 240.04, 241.24]

def text(ws):
    return ' '.join(w for w, _ in ws)


hide_cursor()
try:
    print('\n')
    signature()  # Shinn🐣 - đổi chữ ở SIGNATURE trong animation_plus.py
    song.play(start=START)

    # Turn it up dô   [splash: bạn chọn]
    sync_words(song, LINES[0][0:3], LINES[0][3][1] - 0.05, mode='splash', palette='hong')
    c = 0 + text_width(text(LINES[0][0:3])) + 1   # phần đệm
    sync_words(song, LINES[0][3:], ENDS[0], mode='fadein', palette='bac', indent=c, keep_left=True)
    song.at(LINES[1][0][1] - 0.35)
    echo_out(text(LINES[0][3:]), c, 0.3)
    newline()

    # Baby, she wants to be loved   [hearts: từ "baby"]
    sync_words(song, LINES[1], ENDS[1], mode='hearts', palette='hong', indent=4)
    hold(song, text(LINES[1]), LINES[2][0][1] - 0.1, breathe, palette='hong', indent=4)
    newline()

    # This is not enough enough   [karaoke: slow]
    sync_words(song, LINES[2][0:4], LINES[2][4][1] - 0.05, mode='karaoke', palette='tim', indent=8)
    c = 8 + text_width(text(LINES[2][0:4])) + 1   # phần đệm
    sync_words(song, LINES[2][4:], ENDS[2], mode='fadein', palette='bac', indent=c, keep_left=True)
    song.at(LINES[3][0][1] - 0.35)
    echo_out(text(LINES[2][4:]), c, 0.3)
    newline()

    # Nên hay là kiếm chốn nào để đáp   [typo: fast, long]
    sync_words(song, LINES[3], ENDS[3], mode='typo', palette='tim')
    hold(song, text(LINES[3]), LINES[4][0][1] - 0.1, breathe, palette='tim')
    newline()

    newline()  # hết đoạn

    # Em là cây khô đang cần được tưới tắm   [drop: bạn chọn]
    sync_words(song, LINES[4], ENDS[4], mode='drop', palette='hoanghon')
    hold(song, text(LINES[4]), LINES[5][0][1] - 0.1, shine, palette='hoanghon')
    newline()

    # Hoa muốn nở phải có nắng   [sparkle: bạn chọn]
    sync_words(song, LINES[5], ENDS[5], mode='sparkle', palette='hoanghon', indent=4)
    hold(song, text(LINES[5]), LINES[6][0][1] - 0.1, breathe, palette='hoanghon', indent=4)
    newline()

    # Nhưng em hoàn toàn trống vắng   [fadein: bạn chọn]
    sync_words(song, LINES[6], ENDS[6], mode='fadein', palette='bac', indent=8)
    hold(song, text(LINES[6]), LINES[7][0][1] - 0.1, shine, palette='bac', indent=8)
    newline()

    # Cô đơn và mong manh   [letters: bạn chọn]
    sync_words(song, LINES[7], ENDS[7], mode='letters', palette='bac', indent=12)
    hold(song, text(LINES[7]), LINES[8][0][1] - 0.1, breathe, palette='bac', indent=12)
    newline()

    # Lao ngay vào trong anh   [slide: bạn chọn]
    sync_words(song, LINES[8], ENDS[8], mode='slide', palette='hong')
    hold(song, text(LINES[8]), LINES[9][0][1] - 0.1, shine, palette='hong')
    newline()

    # Hãy đưa em đi thật xa,   [rise: bạn chọn]
    sync_words(song, LINES[9], ENDS[9], mode='rise', palette='hong')
    hold(song, text(LINES[9]), LINES[10][0][1] - 0.1, breathe, palette='hong')
    newline()

    # thật xa,   [glitch: fast, short]
    sync_words(song, LINES[10], ENDS[10], mode='glitch', palette='tim', indent=8)
    hold(song, text(LINES[10]), LINES[11][0][1] - 0.3, breathe, palette='tim', indent=8)
    gradient_fade_out('        ' + text(LINES[10]), 0.25, palette='tim')

    # thật xa oh yeah, xa-ah-ah-ah-ah-ah   [converge: fast]
    sync_words(song, LINES[11][0:2], LINES[11][2][1] - 0.05, mode='converge', palette='tim', indent=16)
    c = 16 + text_width(text(LINES[11][0:2])) + 1   # phần đệm
    sync_words(song, LINES[11][2:], ENDS[11], mode='fadein', palette='bac', indent=c, keep_left=True)
    hold(song, text(LINES[11][0:2]), LINES[12][0][1] - 0.3, breathe, palette='tim', indent=16)
    dissolve_out('                ' + text(LINES[11][0:2]), 0.25, palette='tim')

    # Ở một nơi chỉ còn hai ta   [hearts: bạn chọn]
    sync_words(song, LINES[12], ENDS[12], mode='hearts', palette='bien')
    hold(song, text(LINES[12]), LINES[13][0][1] - 0.1, shine, palette='bien')
    newline()

    newline()  # hết đoạn

    # Nội tâm em đang hơi chen chúc   [jump: fast]
    sync_words(song, LINES[13], ENDS[13], mode='jump', palette='hoanghon')
    hold(song, text(LINES[13]), LINES[14][0][1] - 0.1, breathe, palette='hoanghon')
    newline()

    # Cần được quan tâm như bông hoa cúc   [sparkle: bạn chọn]
    sync_words(song, LINES[14], ENDS[14], mode='sparkle', palette='bac', indent=4)
    hold(song, text(LINES[14]), LINES[15][0][1] - 0.1, shine, palette='bac', indent=4)
    newline()

    # Đôi lúc body này cần được vuốt ve một chút   [wave: bạn chọn]
    sync_words(song, LINES[15], ENDS[15], mode='wave', palette='bac')
    hold(song, text(LINES[15]), LINES[16][0][1] - 0.1, breathe, palette='bac')
    newline()

    # To get her in a better mood   [slide: đa dạng]
    sync_words(song, LINES[16], ENDS[16], mode='slide', palette='hong', indent=4)
    hold(song, text(LINES[16]), LINES[17][0][1] - 0.1, shine, palette='hong', indent=4)
    newline()

    # I gotta be the man I should   [splash: đa dạng]
    sync_words(song, LINES[17], ENDS[17], mode='splash', palette='hong', indent=8)
    hold(song, text(LINES[17]), LINES[18][0][1] - 0.1, breathe, palette='hong', indent=8)
    newline()

    # Ey   [center: slow, short]
    sync_words(song, LINES[18], ENDS[18], mode='center', palette='tim', indent=12)
    hold(song, text(LINES[18]), LINES[19][0][1] - 0.1, shine, palette='tim', indent=12)
    newline()

    newline()  # hết đoạn

    # Oh-oh   [flicker: fast, short]
    sync_words(song, LINES[19], ENDS[19], mode='flicker', palette='bien', indent=8)
    hold(song, text(LINES[19]), LINES[20][0][1] - 0.3, breathe, palette='bien', indent=8)
    center_out('        ' + text(LINES[19]), 0.25, palette='bien')

    # Khi tình yêu của em ở bên kia cầu   [letters: long, soft]
    sync_words(song, LINES[20], ENDS[20], mode='letters', palette='hoanghon')
    hold(song, text(LINES[20]), LINES[21][0][1] - 0.1, heartbeat, palette='hoanghon')
    newline()

    # Khi tình yêu của anh á đang gội đầu   [hearts: từ "yêu"]
    sync_words(song, LINES[21], ENDS[21], mode='hearts', palette='hoanghon')
    hold(song, text(LINES[21]), LINES[22][0][1] - 0.1, heartbeat, palette='hoanghon')
    newline()

    # Qua một đêm lại thấy mình thêm một xấu   [fadein: từ "đêm", slow]
    sync_words(song, LINES[22], ENDS[22], mode='fadein', palette='bac')
    hold(song, text(LINES[22]), LINES[23][0][1] - 0.1, shine, palette='bac')
    newline()

    # Sâu   [center: slow, short]
    sync_words(song, LINES[23], ENDS[23], mode='center', palette='bac', indent=16)
    hold(song, text(LINES[23]), LINES[24][0][1] - 0.1, breathe, palette='bac', indent=16)
    newline()

    # Oh-oh oh, oh, oh   [typewriter: slow]
    sync_words(song, LINES[24][0:1], LINES[24][1][1] - 0.05, mode='typewriter', palette='hong', indent=8)
    c = 8 + text_width(text(LINES[24][0:1])) + 1   # phần đệm
    sync_words(song, LINES[24][1:], ENDS[24], mode='fadein', palette='bac', indent=c, keep_left=True)
    hold(song, text(LINES[24][0:1]), LINES[25][0][1] - 0.3, breathe, palette='hong', indent=8)
    sweep_out('        ' + text(LINES[24][0:1]), 0.25, palette='hong')

    # Khi quả tim của em nó đang thay màu oh, oh, oh   [rainbow: bạn chọn]
    sync_words(song, LINES[25][0:9], LINES[25][9][1] - 0.05, mode='rainbow', palette='hong')
    c = 0 + text_width(text(LINES[25][0:9])) + 1   # phần đệm
    sync_words(song, LINES[25][9:], ENDS[25], mode='fadein', palette='bac', indent=c, keep_left=True)
    song.at(LINES[26][0][1] - 0.35)
    echo_out(text(LINES[25][9:]), c, 0.3)
    newline()

    # Xin một hơi thật sâu trước khi bắt đầu oh, oh, oh   [letters: bạn chọn]
    sync_words(song, LINES[26][0:9], LINES[26][9][1] - 0.05, mode='letters', palette='tim')
    c = 0 + text_width(text(LINES[26][0:9])) + 1   # phần đệm
    sync_words(song, LINES[26][9:], ENDS[26], mode='fadein', palette='bac', indent=c, keep_left=True)
    song.at(LINES[27][0][1] - 0.35)
    echo_out(text(LINES[26][9:]), c, 0.3)
    newline()

    # Và đưa bàn tay bạn đây làm sao phải giấu?   [typo: từ "?", long]
    sync_words(song, LINES[27], ENDS[27], mode='typo', palette='tim')
    hold(song, text(LINES[27]), LINES[28][0][1] - 0.1, breathe, palette='tim')
    newline()

    # Giấu   [scramble: từ "giấu"]
    sync_words(song, LINES[28], ENDS[28], mode='scramble', palette='bien', indent=16)
    hold(song, text(LINES[28]), LINES[29][0][1] - 0.1, shine, palette='bien', indent=16)
    newline()

    # uno, dos, tres, cuatro   [bounce: fast, short]
    sync_words(song, LINES[29], ENDS[29], mode='bounce', palette='bien', indent=20)
    trailing_dots(song, text(LINES[29]), ENDS[29] + 3.0, palette='bien', indent=20)
    hold(song, text(LINES[29]) + '...', ENDS[29] + 4.5, heartbeat, palette='bien', indent=20)
    newline()

    print('\n')
    song.wait_end()
except KeyboardInterrupt:
    pass
finally:
    show_cursor()
    print(RESET)
