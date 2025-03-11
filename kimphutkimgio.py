import time
import sys
from animation import *

line1 = "Ghim giọt lệ đằng sau mi"
line2 = "Dành một ngày cho nhau đi"
line3 = "Thật lòng là anh không cam tâm"
line4 = "Ngày mai ta không gặp lại"
line5 = "Vì mặt trời và mây lên"
line6 = "Sẽ chẳng cầm được tay em"
line7 = "Liệu bầu trời kia mưa rơi"
line8 = "Có phải đang giữ chân mình lại"
line9 = "Em muốn nắm tay anh lần cuối cùng"
line10 = "Hãy làm ngay đi"
line11 = "Cho anh được ôm em một lần cuối thôi"
line13 = "Mau ôm rồi em đi"
line14 = "Hôm nay thật ra là anh đây"
line15 = "Không dám nhắm mắt dù chỉ một lần"
line16 = "Em đi và sẽ ôm lấy"
line17 = "Những phút cuối"
line18 = "Đặt tận vào trong"
line18a = "\t\t\tlòng"
line19 = "Em cũng đâu có nói gì"
line20 = "Lặng nhìn anh đấy"
line20a = "\tAnh cứ nói đi"
line21 = "Baby I’m not crying"
line22 = "Nhưng nói ra sợ"
line23 = "Nước mắt ở trên khóe mi"
line24 = "Chẳng còn giống y như lần đầu"
line25 = "Em có muốn em như vậy đâu     "
line26 = "Không đi tiếp thôi đừng đợi"
line27 = "Đồng hồ đang quay"
line28 = "\t\tChẳng biết ngừng đâu"
line29 = "Đến giờ "
line29a = "lại đếm giờ"
line30 = "Và em không muốn giải thích"
line31 = "Cho anh thêm thời gian"
line32 = "Để rồi có lỗi"
line32a = "\t\tđó là tại mình"
line33 = "Người lặng nhìn"
line33a = "\t\tvấn vương"
line34 = "Người nặng tình"
line34a = "\t\tvẫn thương"
line35 = "Dừng lại đây là do"
line36 = "Khoảng cách hai ta"
line37 = "Mình phải chia tay thật sao?"
line38 = "Còn nhiều lời hứa từng trao "
line39 = "Giờ đây anh phải thế nào"
line40 = "Đứng nhìn em"
line40a = " cùng người ta sao?"
line41 = "Chẳng muốn phải ôm khát vọng"
line42 = "Rồi lỡ buông tay"
line43 = "Bỏ mặc em ở lại phía sau"
line44 = "Ước chi kim đồng hồ kia ngưng"
line45 = "Để ta sẽ mãi đứng im"
line46 = "Chẳng phải đuổi theo điều gì..."


fade_in_from_sides(line1, .05, 15)
time.sleep(.5)
fade_out_from_sides(line2, .04, 20)
time.sleep(.5)
fade_in_and_move_from_right(40, line3, .03, 20)
fade_in_words_non_del(line4, .01, 1)
print()

time.sleep(.5)
fade_in_from_sides(line5, .05, 15)
time.sleep(.5)
fade_out_from_sides(line6, .04, 10)
time.sleep(.5)
show_each_letter(line7,.04)
print()
scroll_text(line8, .02, 30)
random_flicker(line9, .03, 10)
print()
time.sleep(.3)
fade_in_words_non_del(line10, .01, 5)
print()
color_splash_effect(line11, .06, 10)
time.sleep(.5)
scroll_text(line13, .03, 36)
fade_in_words_non_del(line14, .01, 1)
print()
color_splash_effect(line15, .06, 10)
print()

time.sleep(.3)
fade_in_words_non_del(line16, .01, 5)
print()
time.sleep(.2)
color_splash_effect(line17, .04, 10)
print()
fade_in_and_move_from_right(40, line18, .03, 20)
time.sleep(.3)
fade_in_text(line18a, .09)
print()

time.sleep(.1)
fade_in_words(line19, .01,1)
fade_in_from_sides(line20, .04, 10)
print()
time.sleep(.2)
color_splash_effect(line20a, .04, 10)
print()
time.sleep(.1)
show_fade_in_and_each_letter(line21, .04 )
print()
fade_in_words_non_del(line22, .01, 2)
print()
fade_in_and_move_from_right(40, line23, .03, 20)
time.sleep(.3)
fade_in_text(line24, .05)
show_fade_in_and_each_letter(line25, .04 )
print()
time.sleep(.4)
fade_in_words_non_del(line26, .01, 2)
print()
show_each_letter(line27,.04)
print()
fade_in_from_sides(line28, .04, 15)

print()
time.sleep(.2)
fade_in_text(line29, .04)
time.sleep(.1)
show_each_letter(line29a,.03)
print()
time.sleep(.3)
fade_in_and_move_from_right(40, line30, .03, 20)
time.sleep(.3)

fade_in_words_non_del(line31, .01, 1)
print()
fade_in_words_non_del(line32, .01, 1)
time.sleep(.1)
fade_in_text(line32a,.04)

print()
time.sleep(.3)
fade_in_words_non_del(line33, .01, 1)
time.sleep(.3)
fade_in_text(line33a,.04)
print()
time.sleep(.1)
fade_in_words_non_del(line34, .01, 1)
time.sleep(.3)
fade_in_text(line34a,.04)
print()
time.sleep(.3)
fade_in_from_sides(line35, .03, 15)
time.sleep(.5)
fade_out_from_sides(line36, .03, 15)

print()
flash_line_fade_in_out_once(line37, 1)
time.sleep(.5)
show_fade_in_and_each_letter(line38, .06 )
print()
time.sleep(.5)
fade_out_from_sides_left(line39, .09, 30)
fade_in_words_non_del(line40, .01, 1)
show_each_letter(line40a,.06)

print()
time.sleep(.5)
fade_out_from_sides(line41, .08, 30)
time.sleep(.5)
fade_in_from_sides(line42, .05, 15)
fade_in_and_move_from_right(40, line43, .03, 20)
time.sleep(.5)
fade_in_words_non_del(line44, .01, 1)
print()
time.sleep(.3)
fade_out_from_sides_left(line45, .09, 30)
time.sleep(.5)
if line46.endswith("..."):
    main_text = line46[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05) 
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1)
    print()
