import os
import time

# Hiển thị menu lựa chọn
print("Chọn file để gửi dữ liệu:")
print("1. pass 4 so")
print("2. pass 5 so")
print("3. pass 6 so")
print("4. pass 7 so")

# Nhận lựa chọn từ người dùng
choice = input("Nhập số tương ứng (1-4): ")

# Xác định file dựa trên lựa chọn
file_map = {
    "1": "data1.txt",
    "2": "data2.txt",
    "3": "data3.txt",
    "4": "data4.txt"
}

file_path = file_map.get(choice)

if not file_path:
    print("Lựa chọn không hợp lệ.")
    exit()

# Kiểm tra file có tồn tại không
if not os.path.exists(file_path):
    print(f"File '{file_path}' không tồn tại.")
    exit()

# Đọc từng dòng trong file và gửi qua ADB
print(f"Đang gửi dữ liệu từ file '{file_path}'...")
with open(file_path, "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()  # Xóa khoảng trắng thừa
        if line:
            # Gửi dòng qua ADB dưới dạng input text
            os.system(f"adb shell input text \"{line}\"")
            # Nhấn Enter sau mỗi dòng
            os.system("adb shell input keyevent 66")
            time.sleep(0.01)  # Độ trễ 1/100 giây

print("Hoàn thành!")