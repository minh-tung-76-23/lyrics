import time
import sys
from animation import *

line1 = "Ngày hôm nay"  
line1a = "Trời trong xanh"  
line2 = "đẹp như tranh"  
line3 = "Mình cùng dạo vòng quanh"  
line3a = "Cả thế giới"  
line4 = "đừng vội nhanh"  
line5 = "Một hành trình"  
line5a = "nhật ký yêu thương"  
line5b = "Đời mình"  
line6 = "hát vu vơ"  
line6a = "Về "  
line6b = "tình đầu em ơi ♬"  
line7 = "Ngày hôm ấy"  
line7a = "Là cô bé "  
line7b = "tuổi đôi mươi"  
line8 = "Vậy mà giờ đã lớn"  
line8a = "Trưởng thành hơn"  
line9 = "Mặc váy cưới"  
line10 = "Chẳng điều gì dừng bước em tôi"  
line11 = "Vì"  
line11a = " người mãi kiêu sa"  
line11b = "Đẹp tuyệt vời 💕"  
line12 = "Anh ở vùng quê"  
line12a = "Khu nghèo khó đó"  
line13 = "Có"  
line13a = " trăm điều khó"  
line14 = "Muốn lên thành phố"  
line14a = " nên phải cố"  
line15 = "Sao cho bụng anh luôn no"  
line16 = "Thế rồi gặp em"  
line17 = "Những vụn vỡ đã"  
line17a = " lỡ"  
line17b = "Đêm lại nhớ"  
line18 = "Nằm mơ"  
line18a = " gọi tên em🩶..."  

time.sleep(5.5)
fade_in_from_sides(line1, .03, 10)
print()
time.sleep(.2)
fade_in_words_non_del(line1a, .01, 1)
time.sleep(.2)
show_each_letter(line2, .04)
print()

time.sleep(.5)
fade_in_from_sides(line3, .03, 10)
print()
time.sleep(.2)
fade_in_words_non_del(line3a, .01, 1)
time.sleep(.2)
show_each_letter(line4, .04)
print()
time.sleep(.5)

fade_in_words_non_del(line5, .01, 1)
time.sleep(.2)
show_each_letter(line5a, .04)
print()
time.sleep(.2)
fade_in_words_non_del(line5b, .03, 1)
time.sleep(.2)
show_each_letter(line6, .04)
print()
time.sleep(.2)

fade_in_text(line6a, .03, 10)
time.sleep(.3)
show_each_letter(line6b, .06)
time.sleep(.5)
print()

fade_in_and_move_from_right(40, line7, .02, 20)
time.sleep(.2)
fade_in_words_non_del(line7a, .01, 1)
time.sleep(.2)
show_each_letter(line7b, .04)
print()
time.sleep(.3)

fade_in_from_sides(line8, .03, 10)
time.sleep(.2)
print()
fade_in_words_non_del(line8a, .01, 1)
time.sleep(.2)
print()
fade_in_and_move_from_right(40, line9, .02, 20)

time.sleep(.3)
scroll_text(line10, .03, 15)
fade_in_text(line11, .03, 10)
time.sleep(.2)
show_each_letter(line11a, .04)
print()
time.sleep(.2)
fade_in_and_move_from_right(35, line11b, .02, 20)
time.sleep(1)

flash_line_fade_in_out_once(line12, .5)
fade_out_from_sides_left(line12a, .05, 30)
time.sleep(.2)
fade_in_text(line13, .03, 10)
time.sleep(.2)
show_each_letter(line13a, .04)
print()
time.sleep(.3)

fade_out_by_char(line14, .05, 10)
time.sleep(.5)
fade_out_from_sides_left(line14a, .05, 20)
time.sleep(.3)
show_fade_in_and_each_letter(line15, .06)
print()
time.sleep(.6)

fade_in_words_non_del(line16, .01, 1)
time.sleep(.3)
print()
bounce_text(line17, .06, 10)
time.sleep(.5)
show_each_letter(line17a, .09)
print()
time.sleep(.3)
fade_in_text(line17b, .05, 10)
print()
time.sleep(1)
fade_in_from_sides(line18, .08, 20)
time.sleep(.3)
if line18a.endswith("..."):
    main_text = line18a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)


























