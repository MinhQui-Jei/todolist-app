import tkinter as tk

# --- Hàm xử lý ---
def start_recording():
    global is_recording
    is_recording = True
    update_status()

def pause_recording():
    global is_recording
    is_recording = False
    update_status()

def end_recording():
    global is_recording
    is_recording = False
    update_status()
    # Thêm xử lý kết thúc ghi ở đây

def update_status():
    if is_recording:
        status_label.config(text="Đang ghi...")
    else:
        status_label.config(text="Recording Paused")

# --- Giao diện ---
window = tk.Tk()
window.title("Frame Recorder")
window.geometry("600x300")
window.configure(bg="#DDA0DD")  # Màu nền tùy chỉnh

# Tiêu đề
title_label = tk.Label(window, text="Frame Recorder", font=("Arial", 24), bg="#DDA0DD")
title_label.pack(pady=20)

# Nhập FPS
fps_label = tk.Label(window, text="Create an", bg="#DDA0DD")
fps_label.pack()
fps_entry = tk.Entry(window, width=5)
fps_entry.pack()
fps_unit_label = tk.Label(window, text="fps video", bg="#DDA0DD")
fps_unit_label.pack()

# Nút
button_frame = tk.Frame(window, bg="#DDA0DD")
button_frame.pack(pady=20)
pause_button = tk.Button(button_frame, text="Pause", command=pause_recording)
pause_button.pack(side=tk.LEFT, padx=5)
start_button = tk.Button(button_frame, text="Start", command=start_recording)
start_button.pack(side=tk.LEFT, padx=5)
end_button = tk.Button(button_frame, text="End", command=end_recording)
end_button.pack(side=tk.LEFT, padx=5)

# Trạng thái
status_label = tk.Label(window, text="Recording Paused", bg="#DDA0DD")
status_label.pack(pady=10)

# Biến toàn cục
is_recording = False

window.mainloop()