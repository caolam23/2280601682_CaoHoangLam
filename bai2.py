import math

def tinh_dien_tich_hinh_tron(r):
    return math.pi * r ** 2

# Nhập bán kính từ người dùng
r = float(input("Nhập bán kính hình tròn: "))

if r < 0:
    print("Lỗi: Bán kính không thể là số âm!")
else:
    dien_tich = tinh_dien_tich_hinh_tron(r)
    print(f"Diện tích hình tròn có bán kính {r} là: {dien_tich:.2f}")
