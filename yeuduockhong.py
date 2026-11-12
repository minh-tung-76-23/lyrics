import time
import sys
from animation import *

line1 = "▶ Đường xa lá rơi đón mùa thu"
line2 = "♫ Nắng âm áp nhạc ru…"
line3 = "  🩶 Nhớ em đếm từng giờ"
line3a = "\t\t\t dù trong giấc mơ"
line4 = "♪ Vờ như chẳng nhìn thấy một ai"
line5 = "𝄫 Chỉ có mỗi mình em"
line6 = "𝄞 Rồi dạo bước"
line6a = "\t♭ tay nắm thẹn thùng         "
line6b = "\t\t♮ trời mây mỉm cười"
line7 = "🎧 Tình yêu tới đôi lúc hằng đêm"
line8 = "  ♪ Ánh trăng đến mà xem"
line9 = "  ♪ Phải chăng cứ hờn ghen"
line9a = "\t\t\t là ta đã yêu💕"
line10 = "  Đừng cười với bất cứ 1 ai"
line11 = "  Dẫu anh biết là sai"
line12 = "♫ Ngại ngùng anh chỉ muốn "
line12a = "  🎼 Thể hiện tình yêu to lớn..."

# In lyrics
time.sleep(.5)
show_each_letter(line1, 0.07)
print()
time.sleep(.5)
fade_in_text(line2, 0.2)
print()

time.sleep(0.5)
show_each_letter(line3, 0.08)
time.sleep(0.3)
fade_in_text(line3a, 0.2)
print()

time.sleep(1.5)
show_fade_in_and_each_letter(line4, 0.09)  
print()
time.sleep(0.5)
fade_in_text(line5, 0.08)
print()
time.sleep(0.5)

show_each_letter(line6, 0.08)
print()
fade_in_and_move_from_right(30, line6a, .08, 10)

time.sleep(0.5)
fade_in_text(line6b, 0.2)
time.sleep(4)
print()
show_each_letter(line7, 0.08)
print()
time.sleep(1)
fade_in_text(line8, 0.2)
time.sleep(0.5)
print()
show_fade_in_and_each_letter(line9, 0.09)  
print()
fade_in_text(line9a, 0.2)
time.sleep(0.5)
print()

flash_line_fade_in_out_once(line10, 2)
flash_line_fade_in_out_once(line11, 2)
fade_in_text(line12, 0.15)
print()
if line12a.endswith("..."):
    main_text = line12a[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print() 

