import time
from animation import *     

line1 = "Anh có nỗi sợ"
line2 = "\tSợ ta mất nhau"
line3 = "Tình yêu bắt đầu"
line4 = "\tKhông phải để tìm nỗi đau"
line5 = "Sợ giây phút này"
line6 = "\tChẳng còn"
line6a = " thấy em bên anh"
line6b = " về sau🩶..."
line7 = "\tNhiều khi nóng giận"
line8 = "\tNhiều khi cãi nhau       "
line9 = "Để rồi cuối cùng"
line10 = "\tTa lại trở về với nhau"
line11 = "Đôi tay này cần "
line11a = "\t\tnâng niu"
line12 = "Vì em là người"
line12a = " anh yêu❤️ ..."

time.sleep(0.5)
fade_in_words_non_del(line1, .01, 4)
print()
time.sleep(0.5)
fade_in_text(line2, .15)
print()

time.sleep(0.5)
fade_in_words_non_del(line3, .01, 4)
print()
time.sleep(0.2)
show_fade_in_and_each_letter(line4, .07)

print()
time.sleep(1)
fade_in_words_non_del(line5, .01, 2)
print()
time.sleep(0.2)
fade_in_text(line6, .06)
time.sleep(0.5)
show_each_letter(line6a, .08)
time.sleep(0.5)
if line6b.endswith("..."):
    main_text = line6b[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.06) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print()

flash_line_fade_in_out_once(line7, 1)
time.sleep(0.3)
fade_out_from_sides_left(line8, .15, 10)
time.sleep(0.5)
show_fade_in_and_each_letter(line9, .05)

print()
time.sleep(0.2)
fade_in_from_sides(line10, .09, 20)
print()

time.sleep(1)
fade_in_words_non_del(line11, .01, 10)
time.sleep(0.2)
fade_in_text(line11a, .15)
print()

time.sleep(1)
fade_in_from_sides(line12, .07, 20)
time.sleep(0.2)
if line12a.endswith("..."):
    main_text = line12a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.07) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.6)
    print()









