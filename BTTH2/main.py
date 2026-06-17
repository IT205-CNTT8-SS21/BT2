import logging
from pos_logic import (
    DRINK_MENU,
    ITEM_NOT_FOUND_MSG,
    INVALID_QUANTITY_MSG,
    add_to_order,
    calculate_total,
)


def show_menu():
    """Chức năng 1: Hiển thị thực đơn Highlands Coffee."""
    print("\n--- THỰC ĐƠN HIGHLANDS COFFEE ---")
    for code, info in DRINK_MENU.items():
        print(f"[{code}] - {info['name']} - {info['price']:,} VNĐ")


def handle_add_to_order(current_order: list):
    """Chức năng 2: Điều hướng nhập liệu và bắt ngoại lệ khi thêm món."""
    print("\n--- THÊM MÓN VÀO GIỎ ---")
    drink_code = input("Nhập mã đồ uống: ")
    quantity_str = input("Nhập số lượng: ")

    try:
        add_to_order(current_order, drink_code, quantity_str)
    except KeyError as e:
        # e.args[0] lấy ra chuỗi thông báo lỗi được định nghĩa sẵn
        print(e.args[0])
    except ValueError as e:
        print(e)


def show_current_order(current_order: list):
    """Chức năng 3: Hiển thị chi tiết giỏ hàng và tổng tiền."""
    if not current_order:
        print("\nGiỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return False

    print("\n--- GIỎ HÀNG HIỆN TẠI ---")
    print(
        f"{'Mã SP':<6} | {'Tên đồ uống':<20} | {'Đơn giá':<8} | "
        f"{'Số lượng':<8} | {'Thành tiền'}"
    )
    print("-" * 64)
    for item in current_order:
        subtotal = item["price"] * item["quantity"]
        print(
            f"{item['code']:<6} | {item['name']:<20} | "
            f"{item['price']:<8,} | {item['quantity']:<8} | "
            f"{subtotal:,} VNĐ"
        )
    print("-" * 64)
    total = calculate_total(current_order)
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")
    return True


def handle_checkout(current_order: list):
    """Chức năng 4: Xác nhận thanh toán và làm rỗng giỏ hàng."""
    if not current_order:
        print("\nGiỏ hàng trống, vui lòng chọn món (Chức năng 2).")
        return

    total = calculate_total(current_order)
    print("\n--- THANH TOÁN ---")
    print(f"Tổng tiền cần thanh toán: {total:,} VNĐ")
    confirm = (
        input(f"Xác nhận thanh toán {total:,} VNĐ? (y/n): ").strip().lower()
    )

    if confirm == "y":
        print("Thanh toán thành công.")
        logging.info("Checkout successful")
        current_order.clear()
        print("Giỏ hàng đã được làm trống.")
    elif confirm == "n":
        print("Đã hủy thao tác thanh toán. Quay lại menu chính.")
    else:
        print("Lựa chọn không hợp lệ. Thanh toán đã bị hủy.")


def main():
    """Vòng lặp chính quản lý Menu CLI của hệ thống POS."""
    current_order = []

    while True:
        print("\n========== HIGHLANDS MINI POS ==========")
        print("1. Xem thực đơn")
        print("2. Thêm món vào giỏ")
        print("3. Xem giỏ hàng & Tính tổng tiền")
        print("4. Thanh toán & Xóa giỏ hàng")
        print("5. Thoát ca làm việc")
        print("========================================")

        choice = input("Chọn chức năng (1-5): ").strip()

        if choice == "1":
            show_menu()
        elif choice == "2":
            handle_add_to_order(current_order)
        elif choice == "3":
            show_current_order(current_order)
        elif choice == "4":
            handle_checkout(current_order)
        elif choice == "5":
            logging.info("Cashier logged out. System shutdown.")
            print("Đã thoát ca làm việc. Hẹn gặp lại!")
            break
        else:
            print("Chức năng không hợp lệ, vui lòng chọn lại từ 1-5!")


if __name__ == "__main__":
    main()