import os
import time
import bluetooth
import subprocess
import json
import serial
from wifi import Cell, Scheme
from typing import List

# ------------------------------- Bluetooth --------------------------------------

def scan_bluetooth():
    nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, lookup_uuids=True)
    print("Đã phát hiện các thiết bị Bluetooth: ")
    for addr, name in nearby_devices:
        print(f"Địa chỉ MAC: {addr}, Tên: {name}")
    return nearby_devices

def connect_bluetooth(address: str):
    port = 1  # Cổng mặc định của Bluetooth RFCOMM
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try:
        sock.connect((address, port))
        print(f"Đã kết nối đến {address}")
        # Gửi dữ liệu (tùy theo yêu cầu của bạn)
        sock.send("Hello from Python!")
        sock.close()
    except bluetooth.BluetoothError as e:
        print(f"Không thể kết nối: {e}")

# ------------------------------- BadUSB (giả lập) ----------------------------------

def send_badusb():
    # Tạo một thiết bị giả mạo USB (Bàn phím) và gửi các lệnh từ file `data.txt`
    try:
        with open('data.txt', 'r') as file:
            for line in file:
                print(f"Gửi lệnh: {line.strip()}")
                # Mô phỏng phím bấm (nếu dùng phần cứng như Arduino)
                # Arduino hoặc Teensy sẽ dùng lệnh tương tự để gửi phím bấm tới máy tính
                time.sleep(1)
    except FileNotFoundError:
        print("Không tìm thấy file `data.txt`")

# ------------------------------- WiFi --------------------------------------------

def scan_wifi():
    wifi_list = list(Cell.all('wlan0'))  # 'wlan0' là interface WiFi
    print("Đã quét các mạng WiFi: ")
    for network in wifi_list:
        print(f"SSID: {network.ssid}, Mã hóa: {network.encryption_type}")
    return wifi_list

def connect_wifi(ssid: str, password: str):
    try:
        scheme = Scheme.for_cell('wlan0', ssid, password)
        scheme.save()
        scheme.activate()
        print(f"Đã kết nối với WiFi {ssid}")
    except Exception as e:
        print(f"Lỗi kết nối WiFi: {e}")

# ------------------------------- NFC (Yêu cầu thiết bị hỗ trợ) ------------------

def scan_nfc():
    print("Quét NFC... (Đây là phần mô phỏng, bạn cần thiết bị hỗ trợ NFC)")
    # NFC có thể được sử dụng trên thiết bị Android thông qua các thư viện Android, không thể sử dụng trực tiếp trong Python.

# ------------------------------- IR (Infrared) ------------------

def send_ir_command(command: str):
    print(f"Gửi lệnh IR: {command}")
    # Thực hiện gửi lệnh IR nếu có phần cứng IR hỗ trợ (ví dụ như sử dụng Raspberry Pi với IR blaster)

# ------------------------------- Main Program -------------------------------------

def main():
    print("Chọn chức năng bạn muốn sử dụng:")
    print("1. Quét và kết nối Bluetooth")
    print("2. Gửi BadUSB (Giả lập bàn phím)")
    print("3. Quét và kết nối WiFi")
    print("4. Quét NFC (Thiết bị hỗ trợ NFC cần thiết)")
    print("5. Gửi lệnh IR")
    
    choice = input("Nhập lựa chọn: ")

    if choice == '1':
        devices = scan_bluetooth()
        if devices:
            address = input("Nhập địa chỉ MAC của thiết bị muốn kết nối: ")
            connect_bluetooth(address)
    elif choice == '2':
        send_badusb()
    elif choice == '3':
        wifi_list = scan_wifi()
        ssid = input("Nhập SSID WiFi muốn kết nối: ")
        password = input("Nhập mật khẩu WiFi: ")
        connect_wifi(ssid, password)
    elif choice == '4':
        scan_nfc()
    elif choice == '5':
        command = input("Nhập lệnh IR: ")
        send_ir_command(command)
    else:
        print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()