import time
import sys
from animation import show_each_letter, fade_in_text

# Nội dung
print("\n")
lines = [
    ("show", "Cuộc gọi nhỡ cho em hàng đêm\n", 0.04, 0.5),
    ("fade", "\t\t\t Đến tận 200 lần", 0.05, 0.7),
    ("show", "Dòng ký ức trong em về anh\n", 0.05, 0.7),
    ("fade", "\t\t\t Bây giờ đang phai dần", 0.05, 0.7),
    ("show", "Quay gót rời đi\n", 0.05, 0.7),
    ("fade", "\t\t Không để lại gì", 0.05, 1.2),
    ("show", "Bay vút qua tầm tay\n", 0.04, 0.7),
    ("fade", "\t\t\t Sao còn vương vấn để làm gì...", 0.05, 0.9),
    ("show", "Bọn mình kết thúc thật rồi\n", 0.03, 0.7),
    ("fade", "\t Hết sức thật rồi", 0.03, 0.3),
    ("fade", "\t Phải không em ơi", 0.03, 1.4),
    ("show", "Chuyện tình có khúc phải lòng\n", 0.03, 0.5),
    ("fade", "\t Có lúc phải rời", 0.03, 0.5),
    ("fade", "\t Vậy đến lúc rồi", 0.03, 1.3),
    ("show", "Và có lẽ giờ này\n", 0.03, 1.2),
    ("show", "Em đã ngủ say\n", 0.03, 1.2),
    ("show", "Còn anh thì vẫn mang\n", 0.05, 1.7),
    ("fade", "\t\t Nỗi nhớ em trong đêm thật dài", 0.05, 2.5),
    ("fade", "\t\t Thêm lý do cho anh tồn tại", 0.08, 2.5),
    ("fade", "\t\t Để lại chạm vào bờ môi ấy dịu dàng", 0.1, 2.5),
    ("show", "Lời thì thầm ngọt ngào bên tai\n", 0.06, 2.0),
    ("fade", "\t Ta mất nhau thật rồi em ơi", 0.08, 2.5),
    ("fade", "\t Tan vỡ hai cực đành chia đôi", 0.05, 3.0),
    ("fade", "\t Anh sẽ luôn ghi nhớ em", 0.1, 1.0),
    ("fade", "\t Trong từng tế bào ", 0.05, 0.3),
]

# Thực thi
for mode, text, delay, sleep_time in lines:
    if mode == "show":
        show_each_letter(text, delay=delay)
    elif mode == "fade":
        fade_in_text(text, delay=delay)
        print()  # Xuống dòng cho rõ ràng
    time.sleep(sleep_time)

# Hiển thị dòng cuối đặc biệt với 3 dấu "..."
line25 = "Vậy mà dừng lại như thế sao..."
if line25.endswith("..."):
    main_text = line25[:-3]
    for char in main_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.09)
    for dot in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(1.0)
    print()
