import logging

# Cấu hình logging cơ bản hiển thị ra màn hình Terminal theo yêu cầu
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Thực đơn mặc định của Highlands Coffee
DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000},
}

# Thay vì tạo Class ngoại lệ, ta định nghĩa các chuỗi mã lỗi (Custom Error Messages)
# Điều này giúp code thuần túy xử lý chuỗi dựa trên Exception gốc của Python
ITEM_NOT_FOUND_MSG = "Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!"
INVALID_QUANTITY_MSG = "Số lượng phải lớn hơn 0!"


def calculate_total(order_list: list) -> int:
    """Tính tổng số tiền của toàn bộ đơn hàng trong giỏ.

    Args:
        order_list (list): Danh sách các món ăn trong giỏ hàng hiện tại.

    Returns:
        int: Tổng giá trị đơn hàng.
    """
    total = 0
    for item in order_list:
        total += item["price"] * item["quantity"]
    return total


def add_to_order(order_list: list, drink_code: str, quantity_str: str):
    """Xử lý nghiệp vụ kiểm tra và thêm món ăn vào giỏ hàng.

    Raises:
        ValueError: Nếu số lượng không phải số nguyên hoặc nhỏ hơn hoặc bằng 0.
        KeyError: Nếu mã đồ uống không nằm trong DRINK_MENU.
    """
    # Chuẩn hóa chuỗi nhập: viết hoa và xóa khoảng trắng thừa
    code = drink_code.strip().upper()

    # Bẫy 1: Kiểm tra số lượng có phải là số nguyên không
    try:
        quantity = int(quantity_str)
    except ValueError:
        logging.error("ValueError - Invalid quantity input")
        raise ValueError("Vui lòng nhập số lượng là một số nguyên!")

    # Bẫy 2: Kiểm tra mã đồ uống tồn tại bằng KeyError (Lỗi có sẵn của Python)
    if code not in DRINK_MENU:
        logging.warning(f"ItemNotFoundError - Code: {code}")
        raise KeyError(ITEM_NOT_FOUND_MSG)

    # Bẫy 3: Kiểm tra số lượng hợp lệ (> 0) bằng ValueError
    if quantity <= 0:
        logging.warning(f"InvalidQuantityError - Quantity: {quantity}")
        raise ValueError(INVALID_QUANTITY_MSG)

    # Nếu tất cả hợp lệ, tiến hành thêm vào giỏ hàng
    drink_info = DRINK_MENU[code]
    order_list.append(
        {
            "code": code,
            "name": drink_info["name"],
            "price": drink_info["price"],
            "quantity": quantity,
        }
    )
    logging.info(f"Added {quantity} of {code} to order")
    print(f"Đã thêm {quantity} x {drink_info['name']} vào giỏ hàng.")