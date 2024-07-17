import tkinter as tk

# --- Hàm xử lý ---
def scan_now():
    status_label.config(text="Đang quét...")  # Cập nhật nhãn trạng thái
    # Thêm logic quét ở đây

def quick_scan():
    status_label.config(text="Quét nhanh đang diễn ra...")
    # Thêm logic quét nhanh ở đây

def full_scan():
    status_label.config(text="Đang thực hiện quét toàn bộ...")
    # Thêm logic quét toàn bộ ở đây

# --- Giao diện ---
window = tk.Tk()
window.title("AtarBals AntiVirus")
window.geometry("800x500")
window.configure(bg="#f0f0f5")  # Màu nền tùy chỉnh

# Khung chính
main_frame = tk.Frame(window, bg="#f0f0f5")
main_frame.pack(fill=tk.BOTH, expand=True)

# Thanh bên
sidebar = tk.Frame(main_frame, width=200, bg="#6495ED")
sidebar.pack(side=tk.LEFT, fill=tk.Y)

sidebar_labels = ["Trạng thái", "Cập nhật", "Cài đặt", "Gửi phản hồi", "Mua Premium", "Trợ giúp"]
for label_text in sidebar_labels:
    label = tk.Label(sidebar, text=label_text, bg="#6495ED", fg="white", font=("Arial", 12))
    label.pack(pady=10)

scan_button = tk.Button(sidebar, text="Quét Ngay", command=scan_now, bg="#00008B", fg="white", font=("Arial", 12))
scan_button.pack(pady=20)

# Khu vực chính
content_area = tk.Frame(main_frame, bg="#f0f0f5")
content_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)

title_label = tk.Label(content_area, text="Quét", font=("Arial", 24, "bold"), bg="#f0f0f5")
title_label.pack()

subtitle_label = tk.Label(content_area, text="Premium sẽ miễn phí mãi mãi. Bạn chỉ cần nhấn nút.", bg="#f0f0f5")
subtitle_label.pack(pady=10)

button_names = ["Quét Nhanh", "Bảo Vệ Web", "Khu Kéo", "Quét Toàn Bộ", "Cập Nhật Đơn Giản"]
button_commands = [quick_scan, lambda: None, lambda: None, full_scan, lambda: None]  # Các nút chưa có chức năng

for name, command in zip(button_names, button_commands):
    button = tk.Button(content_area, text=name, command=command, bg="#FF00FF", fg="white", width=15)
    button.pack(pady=5)

premium_label = tk.Label(content_area, text="Nhận Premium để Bật: (Bảo Vệ Web), (Quét Toàn Bộ), (Cập Nhật Đơn Giản)", bg="#f0f0f5")
premium_label.pack(pady=10)

# Nhãn trạng thái
status_label = tk.Label(window, text="", bg="#f0f0f5")
status_label.pack(pady=10)

window.mainloop()
