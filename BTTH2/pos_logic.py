import logging

# Cấu hình logging cơ bản hiển thị ra màn hình Terminal
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

# Thực đơn mặc định của Highlands Coffee
DRINK_MENU = {
    "P1": {"name": "Phin Sữa Đá", "price": 35000},
    "F1": {"name": "Freeze Trà Xanh", "price": 55000},
    "T1": {"name": "Trà Sen Vàng", "price": 45000},
}


class ItemNotFoundError(Exception):
    """Ngoại lệ xảy ra khi mã đồ uống không tồn tại trong thực đơn."""

    pass


class InvalidQuantityError(Exception):
    """Ngoại lệ xảy ra khi số lượng nhập vào nhỏ hơn hoặc bằng 0."""

    pass


def calculate_total(order_list: list) -> float:
    """Tính tổng số tiền của toàn bộ đơn hàng trong giỏ.

    Args:
        order_list (list): Danh sách các món ăn trong giỏ hàng hiện tại.

    Returns:
        float: Tổng giá trị đơn hàng.
    """
    total = 0
    for item in order_list:
        total += item["price"] * item["quantity"]
    return total


def add_to_order(order_list: list, drink_code: str, quantity_str: str):
    """Xử lý nghiệp vụ kiểm tra và thêm món ăn vào giỏ hàng.

    Args:
        order_list (list): Giỏ hàng hiện tại cần thêm món.
        drink_code (str): Mã đồ uống do người dùng nhập.
        quantity_str (str): Chuỗi số lượng do người dùng nhập.

    Raises:
        ValueError: Nếu số lượng không phải số nguyên hợp lệ.
        ItemNotFoundError: Nếu mã đồ uống không nằm trong DRINK_MENU.
        InvalidQuantityError: Nếu số lượng <= 0.
    """
    # Chuẩn hóa chuỗi nhập: viết hoa và xóa khoảng trắng thừa
    code = drink_code.strip().upper()

    # Bẫy 1: Kiểm tra số lượng có phải là số nguyên không
    try:
        quantity = int(quantity_str)
    except ValueError:
        logging.error("ValueError - Invalid quantity input")
        raise ValueError("Vui lòng nhập số lượng là một số nguyên!")

    # Bẫy 2: Kiểm tra mã đồ uống tồn tại
    if code not in DRINK_MENU:
        logging.warning(f"ItemNotFoundError - Code: {code}")
        raise ItemNotFoundError(
            "Mã đồ uống không hợp lệ, vui lòng kiểm tra lại thực đơn!"
        )

    # Bẫy 3: Kiểm tra số lượng hợp lệ (> 0)
    if quantity <= 0:
        logging.warning(f"InvalidQuantityError - Quantity: {quantity}")
        raise InvalidQuantityError("Số lượng phải lớn hơn 0!")

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