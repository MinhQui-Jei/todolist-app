import tkinter as tk
from tkinter import messagebox

def submit_data():
    # Lấy dữ liệu từ các trường nhập liệu
    ho = ho_entry.get()
    ten = ten_entry.get()
    title = title_var.get()
    tuoi = tuoi_var.get()
    quoc_tich = quoc_tich_entry.get()
    da_dang_ky = da_dang_ky_var.get()
    so_khoa_hoc = so_khoa_hoc_var.get()
    so_hoc_ky = so_hoc_ky_var.get()
    chap_nhan_dieukhoan = dieukhoan_var.get()

    # Kiểm tra xem các điều khoản đã được chấp nhận chưa
    if not chap_nhan_dieukhoan:
        messagebox.showerror("Lỗi", "Vui lòng chấp nhận các điều khoản và điều kiện.")
        return

    # Hiển thị thông báo xác nhận (hoặc gửi dữ liệu đi xử lý)
    message = f"Dữ liệu đã được gửi:\n" \
              f"  Họ: {ho}\n" \
              f"  Tên: {ten}\n" \
              f"  Chức danh: {title}\n" \
              f"  Tuổi: {tuoi}\n" \
              f"  Quốc tịch: {quoc_tich}\n" \
              f"  Đã đăng ký: {da_dang_ky}\n" \
              f"  Số khóa học đã hoàn thành: {so_khoa_hoc}\n" \
              f"  Số học kỳ: {so_hoc_ky}"
    messagebox.showinfo("Thành công", message)

# Tạo cửa sổ chính
window = tk.Tk()
window.title("Biểu mẫu nhập liệu")
window.geometry("500x400")

# Khung thông tin người dùng
user_info_frame = tk.LabelFrame(window, text="Thông tin người dùng")
user_info_frame.pack(padx=10, pady=10)

ho_label = tk.Label(user_info_frame, text="Họ:")
ho_label.grid(row=0, column=0, padx=5, pady=5)
ho_entry = tk.Entry(user_info_frame)
ho_entry.grid(row=0, column=1, padx=5, pady=5)

ten_label = tk.Label(user_info_frame, text="Tên:")
ten_label.grid(row=1, column=0, padx=5, pady=5)
ten_entry = tk.Entry(user_info_frame)
ten_entry.grid(row=1, column=1, padx=5, pady=5)

title_label = tk.Label(user_info_frame, text="Chức danh:")
title_label.grid(row=2, column=0, padx=5, pady=5)
title_var = tk.StringVar(value="Ông")  # Giá trị mặc định
title_options = ["Ông", "Bà", "Tiến sĩ", "Giáo sư"]
title_dropdown = tk.OptionMenu(user_info_frame, title_var, *title_options)
title_dropdown.grid(row=2, column=1, padx=5, pady=5)

tuoi_label = tk.Label(user_info_frame, text="Tuổi:")
tuoi_label.grid(row=3, column=0, padx=5, pady=5)
tuoi_var = tk.IntVar(value=18)  # Giá trị mặc định
tuoi_spinbox = tk.Spinbox(user_info_frame, from_=18, to=120, textvariable=tuoi_var)
tuoi_spinbox.grid(row=3, column=1, padx=5, pady=5)

quoc_tich_label = tk.Label(user_info_frame, text="Quốc tịch:")
quoc_tich_label.grid(row=4, column=0, padx=5, pady=5)
quoc_tich_entry = tk.Entry(user_info_frame)
quoc_tich_entry.grid(row=4, column=1, padx=5, pady=5)

# Khung trạng thái đăng ký
registration_frame = tk.LabelFrame(window, text="Trạng thái đăng ký")
registration_frame.pack(padx=10, pady=10)

da_dang_ky_var = tk.BooleanVar()
da_dang_ky_check = tk.Checkbutton(registration_frame, text="Hiện đang đăng ký", variable=da_dang_ky_var)
da_dang_ky_check.grid(row=0, column=0, sticky="w")

so_khoa_hoc_label = tk.Label(registration_frame, text="# Khóa học đã hoàn thành:")
so_khoa_hoc_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
so_khoa_hoc_var = tk.IntVar()
so_khoa_hoc_spinbox = tk.Spinbox(registration_frame, from_=0, to=100, textvariable=so_khoa_hoc_var)
so_khoa_hoc_spinbox.grid(row=1, column=1, padx=5, pady=5)

so_hoc_ky_label = tk.Label(registration_frame, text="# Học kỳ:")
so_hoc_ky_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
so_hoc_ky_var = tk.IntVar()
so_hoc_ky_spinbox = tk.Spinbox(registration_frame, from_=0, to=20, textvariable=so_hoc_ky_var)
so_hoc_ky_spinbox.grid(row=2, column=1, padx=5, pady=5)

# Khung điều khoản và điều kiện
terms_frame = tk.LabelFrame(window, text="Điều khoản và điều kiện")
terms_frame.pack(padx=10, pady=10)

dieukhoan_var = tk.BooleanVar()
dieukhoan_check = tk.Checkbutton(terms_frame, text="Tôi chấp nhận các điều khoản và điều kiện.", variable=dieukhoan_var)
dieukhoan_check.pack(anchor="w")

# Nút gửi
submit_button = tk.Button(window, text="Nhập dữ liệu", command=submit_data)
submit_button.pack(pady=10)

window.mainloop()
