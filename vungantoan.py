import time
import sys
from animation import * 

line1 = "Sự thật là"  
line1a = "    Vẫn chưa ai yêu anh"  
line1b = "Nhiều hơn em từng làm"  
line2 = "Và cũng sẽ chẳng có ai"  
line2a = "Có thể khiến cho nước mắt của em"  
line2b = "         rơi từng hàng"  
line3 = "Và kể cả về sau này"  
line3a = "Có trong tay biển bạc"  
line3b = "\t\t\t và rừng vàng"  
line4 = "Cũng không bao giờ có thể thay thế     "  
line4a = "  Người con gái bên cạnh"  
line4b = "\t\t\t lúc bần hàn "  
line5 = "Nhưng mà đây không phải"  
line5a = "     lời thú tội      "  
line6 = "   Anh không tới để    "  
line6a = "      nhận án      "  
line7 = "   Anh đã có    "  
line7a = "     hình phạt    "  
line7b = "Đó là nhìn em bên người xứng đáng"  
line8 = "Ta vẫn yêu và quan tâm nhau"  
line8a = "Chỉ là dùng một cách tiếp cận khác"  
line9 = "Tiếc là ta gặp nhau"  
line9a = "Vào những năm tháng anh vẫn chưa sẵn sàng"  
line10 = "Chưa sẵn sàng để"  
line10a = "\t\t đối mặt"  
line11 = "\t\t vấp ngã"  
line12 = "\t\t buông tha"  
line13 = " Chưa sẵn sàng"  
line13a = " cho tất cả  "  
line14 = "Giờ hơi thở anh"  
line14a = "đầy mùi cồn"  
line15 = "Và cổ áo anh"  
line15a = "toàn mùi thuốc lá"  
line16 = "Anh chỉ để lại đống đổ nát"  
line16a = "Tất cả những nơi"  
line16b = "    Mà anh từng bước qua🩶 ..."  

time.sleep(2)
fade_in_words_non_del(line1, .02, 2)
print()
time.sleep(.3)

fade_out_from_sides(line1a, .04, 10)
time.sleep(.2)
fade_in_and_move_from_right(30, line1b, .05, 20)
time.sleep(.3)

color_splash_effect(line2, .04, 10)
print()
time.sleep(.2)
show_fade_in_and_each_letter(line2a, .04)
time.sleep(.2)
fade_in_and_move_from_right(32, line2b, .03, 15)

time.sleep(.2)
show_fade_in_and_each_letter(line3, .04)
print()
time.sleep(.2)
fade_in_words_non_del(line3a, .01, 1)
time.sleep(.1)
fade_in_text(line3b, .04)

time.sleep(.2)
show_fade_in_and_each_letter(line4, .02)
time.sleep(.1)
fade_in_from_sides(line4a, .03, 7)
time.sleep(.1)
fade_in_text(line4b, .04)
print()
time.sleep(.2)

fade_in_words_non_del(line5, .01, 1)
time.sleep(.1)
fade_in_text(line5a, .03)
time.sleep(.1)

show_fade_in_and_each_letter(line6, .03)
time.sleep(.1)
fade_in_text(line6a, .04)
time.sleep(.1)

show_fade_in_and_each_letter(line7, .03)
time.sleep(.1)
fade_in_text(line7a, .04)
time.sleep(.2)

fade_in_from_sides(line7b, .03, 20)
print()
scroll_text(line8, .03, 25)
time.sleep(.2)
fade_in_from_sides(line8a, .03, 15)
print()
time.sleep(.2)

fade_in_words_non_del(line9, .01, 1)
print()
time.sleep(.2)
fade_out_by_char(line9a, .03, 10)
time.sleep(.2)

fade_in_words_non_del(line10, .01, 1)
time.sleep(.1)
fade_in_text(line10a, .02)
print()
time.sleep(.1)

fade_in_words_non_del(line10, .01, 1)
time.sleep(.1)
fade_in_text(line11, .02)
print()
time.sleep(.1)

fade_in_words_non_del(line10, .01, 1)
time.sleep(.1)
fade_in_text(line12, .02)
print()
time.sleep(.1)

fade_in_words_non_del(line13, .01, 1)
time.sleep(.1)
fade_in_from_sides(line13a, .03, 10)

fade_in_words_non_del(line14, .01, 1)
time.sleep(.1)
show_each_letter(line14a, .02)
print()
time.sleep(.1)

fade_in_words_non_del(line15, .01, 1)
time.sleep(.1)
show_each_letter(line15a, .02)
print()
time.sleep(.2)

fade_in_and_move_from_right(30, line16, .03, 20)
time.sleep(.1)
fade_in_words_non_del(line16a, .01, 1)
print()
time.sleep(.2)
color_splash_effect(line16b, .04, 10)






