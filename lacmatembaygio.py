import time
import sys
from animation import *

print()

line1 = "♪ Lạc mất em bây giờ"
line1a = "    Thì sẽ không bao giờ"
line2 = "♮ Có em trong vòng tay"
line3 = "♫ Những bước chân của ta đắm say"
line4 = "♫ Với hơi men còn đang ngất ngây"
line5 = "      ♪ Biết anh"
line5a = "\t\t như là linh hồn "
line5b = "\t\t lang bạt phương trời"
line6 = "     Nhưng em"
line6a = "Vẫn muốn cạnh bên"
line7 = "♪ Nắm tay anh cùng nhau bước qua"
line8 = "♪ Từng núi cao bão giông biển sâu"
line9 = "      ♮ Đến khi"
line9a = "\t\tchúng mình mệt nhoài"
line9b = "Hãy nghỉ chân và"
line10 = "♭ Xây đắp cho ngày mai"

show_fade_in_and_each_letter(line1, .05)
show_fade_in_and_each_letter(line1a, .05)
print()
time.sleep(.3)
fade_in_words_non_del(line2, .001, 3)
print()
time.sleep(.2)

flash_line_fade_in_out_once(line3, 2)
flash_line_fade_in_out_once(line4, 1.5)

time.sleep(.2)
show_each_letter(line5, .05)
time.sleep(.2)
show_fade_in_and_each_letter(line5a, .04)
show_fade_in_and_each_letter(line5b, .04)
print()
time.sleep(.3)

show_each_letter(line6, .04)
print()
fade_in_words_non_del(line6a, .001, 3)
print()

time.sleep(.5)
flash_line_fade_in_out_once(line7, 2)
flash_line_fade_in_out_once(line8, 1.5)

time.sleep(.2)
show_each_letter(line9, .05)
time.sleep(.2)
fade_in_text(line9a, .05)
print()
time.sleep(.2)
show_fade_in_and_each_letter(line9b, .05)
print()
time.sleep(.5)
fade_in_words_non_del(line10, .001, 3)
time.sleep(1)

