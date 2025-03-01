def nhap_va_in_hoa():
    print("Nhập các dòng văn bản (Nhấn Enter 2 lần để kết thúc):")
    danh_sach_dong = []

    while True:
        dong = input()  # Nhập từng dòng
        if dong == "":  # Khi gặp dòng trống thì dừng
            break
        danh_sach_dong.append(dong.upper())  # Chuyển thành chữ in hoa và lưu vào danh sách

    print("\nNội dung sau khi chuyển thành chữ in hoa:")
    for dong in danh_sach_dong:
        print(dong)

nhap_va_in_hoa()
