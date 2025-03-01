def loc_so_nhi_phan_chia_het_cho_5():
    # Nhập chuỗi số nhị phân, cách nhau bởi dấu phẩy
    chuoi_nhi_phan = input("Nhập các số nhị phân, cách nhau bởi dấu phẩy: ")

    # Tách các số nhị phân thành danh sách
    danh_sach_nhi_phan = chuoi_nhi_phan.split(",")

    # Danh sách lưu các số chia hết cho 5
    ket_qua = []

    for so_nhi_phan in danh_sach_nhi_phan:
        try:
            # Chuyển số nhị phân sang số thập phân
            so_thap_phan = int(so_nhi_phan, 2)

            # Kiểm tra chia hết cho 5
            if so_thap_phan % 5 == 0:
                ket_qua.append(so_nhi_phan)  # Thêm số nhị phân vào danh sách kết quả
        except ValueError:
            print(f"Lỗi: {so_nhi_phan} không phải số nhị phân hợp lệ!")

    # In kết quả
    if ket_qua:
        print("Các số nhị phân chia hết cho 5:", ",".join(ket_qua))
    else:
        print("Không có số nhị phân nào chia hết cho 5.")

# Gọi hàm
loc_so_nhi_phan_chia_het_cho_5()
