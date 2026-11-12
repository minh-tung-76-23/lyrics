import time
from animation import * 

line1 = " ♫  Vì anh biết" 
line1a = "\t\tvắng anh" 
line1b = "              Phố quen rất buồn   " 
line2 = "Vắng anh"
line2a = "\t em vắng một bờ vai..."
linea = "      ●─ 🩶   ─●"
line3 = "   ♪ Anh đâu muốn xa"
line3a = "\tCon phố"
line3b = "\t\tta đã yêu"
line4 = "Nơi ấy hẹn hò"
line4a = " \t Đôi ta"
line4b = "\t\tchuyện trò"
line5 = "Nơi ấy đã từng"
line5a = "  Đón đưa"
line5b = " em từng chiều"
line5c = "\t\t\ttới trường"
line6 = " Khi ấy"
line6a = "\tem"
line6b = " còn tóc xanh..."
line7 = "Bóng dáng"
line7a = "\tg anh yêu thương"
line8 = "Đôi vai hao gầy"
line8a = "\t\tmỏng manh"
line8b = "\t\t\th tâm hồn"
line9 = "  Anh hứa sẽ về"
line9a = "\t\tvới em"
line9b = "    Như lời hứa"
line9c = "\t\tanh từng"
line10 = "  Xin em"
line10a = "\t hãy"
line10b = " chờ anh về..."

# show_fade_in_and_each_letter(line1, .06)
# time.sleep(.5)
# fade_in_text(line1a, .06)
# time.sleep(.5)
# print()
# fade_in_from_sides(line1b, .09, 30)
# print()
# time.sleep(.7)

# fade_in_words_non_del(line2, .05, 5)
# time.sleep(.5)
# fade_in_text(line2a, .2)
# print()
# time.sleep(.5)
# flash_line_fade_in_out_once(linea, 3)
# time.sleep(.5)

# fade_in_words_non_del(line3, .02, 4)
# print()
# time.sleep(.5)
# show_fade_in_and_each_letter(line3a, .08)
# time.sleep(.5)
# fade_in_text(line3b, .2)
# print()
# time.sleep(.5)

# show_fade_in_and_each_letter(line4, .06)
# print()
# time.sleep(.5)
# fade_in_words_non_del(line4a, .02, 5)
# time.sleep(.5)
# fade_in_text(line4b, .2)
# print()
# time.sleep(.8)

# fade_in_words_non_del(line5, .02, 5)
# print()
# time.sleep(.5)
# fade_in_text(line5a, .15)
# time.sleep(.5)
# show_each_letter(line5b, .06)
# time.sleep(.5)
# fade_in_text(line5c, .15)
# print()
# time.sleep(.5)

# show_fade_in_and_each_letter(line6, .06)
# time.sleep(.5)
# fade_in_text(line6a, .09)
# time.sleep(.5)
# show_each_letter(line6b, .08)
# print()
time.sleep(.5)

fade_in_words_non_del(line3, .02, 4)
print()
time.sleep(.5)
show_fade_in_and_each_letter(line7, .08)
time.sleep(.5)
fade_in_text(line7a, .2)
print()
time.sleep(.5)

show_fade_in_and_each_letter(line8, .08)
time.sleep(.5)
fade_in_text(line8a, .1)
time.sleep(.5)
fade_in_text(line8b, .15)
print()
time.sleep(.5)

fade_in_words_non_del(line9, .02, 4)
time.sleep(.5)
fade_in_text(line9a, .1)
print()
time.sleep(.5)
show_fade_in_and_each_letter(line9b, .08)
time.sleep(.5)
fade_in_text(line9c, .1)
print()
time.sleep(.5)

show_fade_in_and_each_letter(line10, .06)
time.sleep(.5)
fade_in_text(line10a, .09)
time.sleep(.5)
if line10b.endswith("..."):
    main_text = line10b[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.6)
    print()

