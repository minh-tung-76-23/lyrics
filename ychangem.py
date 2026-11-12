import time
from animation import *  

line1 = "         🎙️   Anh      "
line1a = "💤 lang khắp cả thành phố"
line2 = "     Nhưng gặp cô nào"
line2a = "   Nhìn cũng y chang em"
line3 = "Anh đã để bản thân mình mở lòng"
line3a = "Với mọi cô gái tốt"
line4 = "Nhưng có khi thoáng quên"
line5 = "Người ta sẽ"
line5a = "     Thấy những gì họ muốn thấy"
line6 = "      Nghe những gì họ muốn nghe"
line7 = "      Quên những thứ mình cần nhớ"
line8 = "  Và luôn nhớ"
line8a = " Những thứ mình cần quên..."
line9 = "Tới cả con 🐺"
line9a = "mà anh nuôi trong nhà"
line9b = "Cũng nhìn giống"
line9c = "\t\tem y hệt"
line10 = "Cũng chỉ vì hôm đó"
line10a = "Đã có một người nhận lời nói"
line10b = "\t\t  Không ly biệt"
line11 = "Bởi vậy"
line11a = "\tlàm sao"
line11b = "\tMà anh ghét người yêu cũ được"
line12 = "Thỉnh thoảng tụi anh vẫn ngủ chung mà"
line13 = "Tên anh"
line13a = " vẫn còn nằm trong danh bạ"
line14 = "Là người yêu cũ"
line14a = "     Người yêu 'cũ khung' á..."

time.sleep(.5)
fade_in_text(line1, .02)
time.sleep(.5)
random_flicker(line1a, .06, 20)
print()
time.sleep(.2)
show_each_letter(line2, .04)
time.sleep(.2)
fade_in_words_non_del(line2a, .01, 2)
print()
time.sleep(.3)
fade_in_words_non_del(line3, .01, 1)
print()
time.sleep(.2)
fade_in_and_move_from_right(30, line3a, .03, 20)
time.sleep(.2)
bounce_text(line4, .04, 10)
print()
time.sleep(.5)

wave_text(line5, .01, 2)
print()
time.sleep(.2)
fade_in_words_non_del(line5a, .01, 2)
time.sleep(.5)
fade_in_words_non_del(line6, .01, 2)
time.sleep(.5)
fade_in_words_non_del(line7, .01, 2)
print()
time.sleep(.5)
fade_in_words_non_del(line8, .01, 2)
print()
time.sleep(.2)
fade_in_and_move_from_right(30, line8a, .04, 15)
time.sleep(.5)

fade_in_words_non_del(line9, .01, 2)
time.sleep(.2)
show_each_letter(line9a, .03)
print()
time.sleep(.1)
show_fade_in_and_each_letter(line9b, .04)
time.sleep(.2)
fade_in_words_non_del(line9c, .02,3)
print()
time.sleep(.5)

fire_text(line10, .03, 15)
print()
time.sleep(.2)
show_fade_in_and_each_letter(line10a, .04)
print()
time.sleep(.2)
fade_in_words_non_del(line10b, .02, 5)

print()
time.sleep(.5)
fade_in_text(line11, .02)
time.sleep(.1)
fade_in_text(line11a, .02)
print()
time.sleep(.1)
show_each_letter(line11b, .04)
print()
time.sleep(.5)
scroll_text(line12, .03, 10)

time.sleep(.1)
fade_in_text(line13, .02)
time.sleep(.1)
show_each_letter(line13a, .04)
print()
time.sleep(.5)
fade_in_words_non_del(line14, .01, 2)
print()
time.sleep(.5)
random_flicker(line14a, .04, 10)
time.sleep(1)


