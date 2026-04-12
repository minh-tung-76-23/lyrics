import time
import sys
from animation import * 

line1 = "Giá như đừng gặp gỡ"
line1a = "Thì mọi chuyện sẽ"
line1b = "không mang vết thương"
line2 = "Em đã nói"
line2a = "em chọn bỏ lỡ"
line2b = "Vì tình rồi sẽ"
line2c = " không ai vấn vương"
line3 = "Vậy thì đó"
line3a = "\tchỉ là cái cớ"
line3b = "Để tình mình chết"
line3c = "đi theo tháng năm"
line4 = "Bỏ lại anh"
line4a = "\tcùng ngàn nỗi nhớ"
line4b = "Và rùi vụt mất"
line4c = "y như khói sương💔"
line5 = "Nói anh nghe đi"
line5a = "Giờ này em đang làm gì"
line5b = "\tLiệu có còn nhớ anh không?"
line6 = "Một bài nhạc"
line6a = " thật buồn"
line6b = "\tHay nghe một đống lofi"
line7 = "Chẳng còn chờ đợi ngồi một mình"
line7a = "\tXưa em còn ngóng em trông"
line8 = "Chẳng còn gì ngoài kí ức "
line8a = "Chắc e giờ đã bên ai🩶..."

time.sleep(.5)
fade_in_from_sides(line1, .05, 10)
print()
fade_in_words_non_del(line1a, .001, 1)
print()
time.sleep(.2)
fade_in_and_move_from_right(50,line1b, 0.03, 20)    

time.sleep(.3)
fade_in_words_non_del(line2, .001, 1)
show_each_letter(line2a, .05)
print()
time.sleep(.2)
fade_in_words_non_del(line2b, .001, 1)
print()
fade_in_and_move_from_right(50,line2c, 0.03, 20)  

time.sleep(.3)
fade_in_words_non_del(line3, .001, 1)
print()
time.sleep(.2)
color_splash_effect(line3a, .04, 10)
print()
fade_in_words_non_del(line3b, .001, 1)
show_each_letter(line3c, .03)
print()

time.sleep(.2)
fade_in_words_non_del(line4, .001, 1)
print()
time.sleep(.1)
color_splash_effect(line4a, .04, 10)
print()
fade_in_words_non_del(line4b, .001, 1)
show_each_letter(line4c, .05)
print()

random_flicker(line5, .1, 4)
fade_in_words_non_del(line5a, .001, 1)
print()
time.sleep(.3)
show_each_letter(line5b, .05)
print()

time.sleep(.8)
fade_in_text(line6, .04)
time.sleep(.3)
show_each_letter(line6a, .04)
print()
time.sleep(.3)
fade_in_from_sides(line6b, 0.07, 10)
print()

time.sleep(.8)
show_fade_in_and_each_letter(line7, .04)
print()
time.sleep(.3)
fade_in_from_sides(line7a, 0.07, 10)
print()

time.sleep(.8)
bounce_text(line8, .06, 5)
print()
if line8a.endswith("..."):
    main_text = line8a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print() 
