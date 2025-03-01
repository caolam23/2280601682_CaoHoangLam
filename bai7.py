def kiem_tra_nhi_phan_chia_het_cho_5(so_nhi_phan):
    try:
        # Chuyển số nhị phân sang số thập phân
        so_thap_phan = int(so_nhi_phan, 2)

        # Kiểm tra chia hết cho 5
        if so_thap_phan % 5 == 0:
            print(f"Số nhị phân {so_nhi_phan} ({so_thap_phan}) chia hết cho 5.")
        else:
            print(f"Số nhị phân {so_nhi_phan} ({so_thap_phan}) không chia hết cho 5.")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số nhị phân hợp lệ!")

# Nhập số nhị phân từ người dùng
so_nhi_phan = input("Nhập số nhị phân: ")
kiem_tra_nhi_phan_chia_het_cho_5(so_nhi_phan)
