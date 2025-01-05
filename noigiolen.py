import time
import sys
from animation import * 

pink = "\033[95m" 
reset = "\033[0m" 

line1 =f"🎙️  Ước mơ của anh là"
line2 =f" Kết hôn cùng em và   "
line3 =f"{pink} Sống yên bình tới già💕...{reset}"
line4 ="  ♪ Mặc kệ thôi"
line4a ="\t\tmình yêu một ai"
line5 ="Là mong gần bên"
line6 ="Khi bình minh"
line7 ="Hoàng hôn"
line7a =" đến khi đêm về"
line8 ="Mình mong được sống"
line9 ="Hạnh phúc những tháng năm dài"
line9a ="\t\tVới nhau💕..."
line10 ="Cùng trải qua"
line10a ="Buồn vui cùng nhau"
line11 ="Khi bệnh đau        "
line12 ="Mai về sau"
line12a ="Nhìn"
line12b =" con cháu ta sum vầy"
line13 ="Cùng nhìn mái tóc"
line13a ="bạc màu"
line14 ="Vẫn nhớ ngày đầu❤️ ..."

flash_line_fade_in_out_once(line1, 1)
flash_line_fade_in_out_once(line2, 1.2)
flash_line_fade_in_out_once(line3, 2)

time.sleep(.5)
fade_in_words_non_del(line4, .004, 10)
time.sleep(.5)
fade_in_text(line4a, .09)
print()

time.sleep(1)
fade_in_text(line5, .09)
print()

time.sleep(1)
show_fade_in_and_each_letter(line6, .07)
print()

time.sleep(.3)
fade_in_text(line7, .08)
time.sleep(.2)
show_each_letter(line7a, .06)
print()

time.sleep(.5)
fade_in_words_non_del(line8, .004, 10)
fade_in_and_move_from_right(40, line9, .08, 10)
time.sleep(.5)
show_each_letter(line9a, .12)
print()

time.sleep(1)
fade_in_words_non_del(line10, .004, 10)
time.sleep(.3)
flash_line_fade_in_out_once(line10a, 1.3)
flash_line_fade_in_out_once(line11, 1.3)
fade_in_text(line12, .09)
print()
time.sleep(.4)
fade_in_text(line12a, .07)
time.sleep(.2)
show_each_letter(line12b, .05)
print()

time.sleep(.5)
fade_in_words_non_del(line13, .004, 10)
time.sleep(.3)
show_each_letter(line13a, .04)
print()
time.sleep(.3)
show_fade_in_and_each_letter(line14, .15)
time.sleep(1)









