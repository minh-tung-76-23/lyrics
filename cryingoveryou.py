import time
from animation import *     

line1 = "Sẽ có những đớn đau không thành lời"
line2 = "Sẽ có những vết thương theo một đời"
line3 = "Dù mình đã cắn"
line3a = " Thật chặt đôi môi"
line3b = " Sau bao điều mặn đắng"
line4 = "Nhưng sao hôm nay"
line4a = "Con tim anh quên rằng"
line4b = "\tAnh là người mạnh mẽ vô cùng"
line5 = "Có lẽ đã quá lâu cho một người"
line6 = "Giấu hết yếu đuối bên trong nụ cười"
line7 = "Rồi vội vàng nhắm mắt"
line7a = "\tChậm lại đôi chân"
line7b = "Đi sau thời gian"
line7c = " cùng với những vỡ tan🩶"
line8 = "I’m crying over you bei"
line8a = "I’m crying over you bei🩶"
line10 = "Khi anh chẳng thể giữ mãi"
line10a = "Những cảm xúc"
line10b = "vô tình bấy lâu"
line11 = "I’m crying over you"
line12 = "Chơ vơ đơn côi"
line12a = " bên những thứ xa xôi"

flash_line_fade_in_out_once(line1, 3)
flash_line_fade_in_out_once(line2, 4)

fade_out_by_char(line3, .05, 5)
show_fade_in_and_each_letter(line3a, .05)
print()
fade_in_and_move_from_right(40, line3b, .06, 20)
fade_out_by_char(line4, .05, 5)
fade_in_words_non_del(line4a, .01, 1)
print()
fade_in_from_sides(line4b, .06, 25)
print()

time.sleep(1)
fade_out_by_char(line5, .05, 20)
fade_out_from_sides_left(line6, .15, 30)
time.sleep(.5)
fade_in_text(line7, .05)
print()
time.sleep(.2)
show_each_letter(line7a, .08)
print()
fade_in_from_sides(line7b, .06, 15)
show_each_letter(line7c, .08)

print()
time.sleep(2)
flash_line_fade_in_out_once(line8, 2)
fade_out_by_char(line8, .05, 25)

time.sleep(2)
show_fade_in_and_each_letter(line10, .04)
print()
time.sleep(.3)
fade_in_words_non_del(line10a, .01, 1)
time.sleep(.5)
show_each_letter(line10b, .05)

print()
scroll_text(line11, .06, 10)
fade_in_words_non_del(line12, .01, 1)
print()
time.sleep(.5)
fade_in_and_move_from_right(40, line12a, .06, 10)
time.sleep(.3)
flash_line_fade_in_out_once(line8, 2)
time.sleep(.5)
fade_out_by_char(line8a, .05, 25)













