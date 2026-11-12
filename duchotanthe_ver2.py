import time
from animation import *     

line1 = "Từng cái vỗ về"
line2 = "Từng cái nắm tay"
line3 = "Từng cái nhíu mày"
line4 = "\tKhi gặp nhiều điều đắng cay"
line5 = "Và từng khóc"
line5a = " trên vai nhau"
line6 = "  Rồi cùng ngủ thiếp đi"
line6a = "\t\t\ttrong yên bình"
line7 = "Dù cho tận thế"
line8 = "\tVẫn yêu em"
line8a = ", vẫn yêu em"
line9 = "Đừng hòng"
line9a = " ai giành lấy"
line10 = "Anh không buông"
line10a = ", anh không buông"
line11 = "Dẫu"
line11a = " cho thời gian"
line12 = "Khiến anh quên lãng"
line13 = "Vẫn nhớ một mình em"
line14 = "Vì em xứng đáng 💕"
line15 = "Tận sâu tiềm thức"
line16 = "Anh yêu em"
line16a = ", luôn yêu em"
line17 = "Thật tâm"
line17a = " anh chỉ muốn"
line18 = "Em bên mình"
line18a = "\t\tmãi🩶"
line19 = "Không cho phép"
line19a = "\tEm đến"
line19b = " với một ai"
line20 = "Nếu như"
line20a = " anh vẫn tồn tại..."

time.sleep(0.5)
fade_in_from_sides(line1, .07, 20)
time.sleep(0.3)
fade_out_from_sides_left(line2, .15, 10)
time.sleep(0.5)
show_fade_in_and_each_letter(line3, .05)
print()
time.sleep(0.3)
fade_in_from_sides(line4, .09, 20)

print()
time.sleep(1.5)
fade_in_words_non_del(line5, .01, 10)
time.sleep(0.5)
show_each_letter(line5a, .08)

print()
time.sleep(0.5)
show_fade_in_and_each_letter(line6, .05)
time.sleep(0.3)
fade_in_text(line6a, .09)

print()
time.sleep(0.5)
fade_in_words_non_del(line7, .01, 10)
print()
time.sleep(0.2)
fade_in_text(line8, .06)
time.sleep(0.5)
show_each_letter(line8a, .05)

print()
time.sleep(0.5)
fade_in_words_non_del(line9, .01, 10)
time.sleep(0.2)
show_each_letter(line9a, .05)
print()
time.sleep(0.2)
fade_in_text(line10, .04)
time.sleep(0.3)
show_each_letter(line10a, .04)

print()
time.sleep(0.3)
fade_in_text(line11, .05)
time.sleep(0.5)
show_each_letter(line11a, .06)
print()
time.sleep(0.5)
fade_in_and_move_from_right(40, line12, .06, 10)

time.sleep(0.5)
fade_in_from_sides(line13, .07, 20)
time.sleep(0.3)
fade_in_words_non_del(line14, .01, 10)

print()
time.sleep(0.5)
fade_in_words_non_del(line15, .01, 10)
print()
time.sleep(0.2)
fade_in_text(line16, .06)
time.sleep(0.5)
show_each_letter(line16a, .06)

print()
time.sleep(0.5)
fade_in_words_non_del(line17, .01, 10)
time.sleep(0.2)
show_each_letter(line17a, .04)
print()
time.sleep(0.2)
fade_in_from_sides(line18, .05, 10)
time.sleep(0.2)
fade_in_text(line18a, .08)

print()
time.sleep(0.5)
fade_in_words_non_del(line19, .01, 10)
print()
time.sleep(0.2)
fade_in_text(line19a, .06)
time.sleep(0.5)
show_each_letter(line19b, .07)

print()
time.sleep(0.5)
fade_in_from_sides(line20, .07, 10)
time.sleep(0.2)
if line20a.endswith("..."):
    main_text = line20a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print()