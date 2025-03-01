def tinh_gio_lam():
    try:
        # Nhập giờ bắt đầu và kết thúc
        gio_bat_dau = float(input("Nhập giờ bắt đầu (0-24): "))
        gio_ket_thuc = float(input("Nhập giờ kết thúc (0-24): "))

        # Kiểm tra hợp lệ
        if 0 <= gio_bat_dau <= 24 and 0 <= gio_ket_thuc <= 24:
            # Tính số giờ làm
            if gio_ket_thuc >= gio_bat_dau:
                gio_lam = gio_ket_thuc - gio_bat_dau
            else:
                # Trường hợp làm việc qua đêm (VD: 22h - 6h sáng hôm sau)
                gio_lam = (24 - gio_bat_dau) + gio_ket_thuc  

            print(f"Tổng số giờ làm: {gio_lam:.2f} giờ")
        else:
            print("Lỗi: Giờ nhập vào phải trong khoảng 0-24!")

    except ValueError:
        print("Lỗi: Vui lòng nhập số!")

tinh_gio_lam()
