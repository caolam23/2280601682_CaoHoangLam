def kiem_tra_so_nguyen():
    try:
        num = float(input("Nhập một số: "))
        if num.is_integer():  # Kiểm tra có phải số nguyên không
            print(f"Bạn đã nhập số nguyên: {int(num)}")
        else:
            print("Lỗi: Đây không phải số nguyên!")
    except ValueError:
        print("Lỗi: Vui lòng nhập một số!")

kiem_tra_so_nguyen()
