import time
import sys
from animation import *

pink = "\033[95m"  # Mã màu hồng (màu tím nhạt)
reset = "\033[0m"  # Reset màu về mặc định

line1 = f"{pink}♪ Tình yêu đến ngọt ngào{reset}"
line2 = "  Yêu áng mây trên cao   "
line3 = f"{pink}♪ Tình yêu khẽ thì thầm{reset}"
line4 = "  Anh thích em ra sao    "
line5 = f"{pink}♪ Tình yêu muốn nồng nàn{reset}"
line6 = "  Như sóng xô dạt dào   "
line6a = "\tKhắp muôn nơi💕"

line7 = "♪ Từng ngày cô đơn"
line7a = "\t\tơn xé đôi "
line7b = "Hạ thu đông"
line7c = " khẽ trôi"
line8 = "♪ Cạnh bên em"
line8a = "Anh sẽ thôi u sầu"
line9 = "♪ Lại làm cho anh"
line9a = "Càng thấy yêu em"
line9b = "hơn ngày qua💕..."
print("\n\n\n")
time.sleep(.5)
fade_in_text(line1, .09)
time.sleep(.2)
show_fade_in_and_each_letter(line2, .06)
print()

time.sleep(.5)
fade_in_text(line3, .09)
time.sleep(.2)
show_fade_in_and_each_letter(line4, .06)
print()

time.sleep(.3)
fade_in_text(line5, .09)
time.sleep(.2)
show_fade_in_and_each_letter(line6, .06)
print()
flash_line_fade_in_out_once(line6a, 2)

time.sleep(.8)
show_fade_in_and_each_letter(line7, .055)
fade_in_text(line7a, .06)
print()

time.sleep(.3)
fade_in_text(line7b, .06)
show_each_letter(line7c, .06)
print()

time.sleep(.3)
fade_in_words_non_del(line8, .001, 5)
print()
time.sleep(.2)
fade_in_and_move_from_right(40, line8a, .06, 10)

time.sleep(.5)
show_each_letter(line9, .06)
print()
fade_in_words_non_del(line9a, .001, 5)
time.sleep(.3)
if line9b.endswith("..."):
    main_text = line9b[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print() 



