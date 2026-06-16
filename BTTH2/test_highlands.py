import unittest
from pos_logic import add_to_order, calculate_total, InvalidQuantityError


class TestHighlandsPOS(unittest.TestCase):
    """Lớp kiểm thử đơn vị tự động cho các hàm xử lý logic POS."""

    def test_calculate_total(self):
        """Test Case 1: Kiểm tra tính chuẩn xác của hàm tính tổng tiền."""
        # Giả lập một giỏ hàng (Mock list) gồm 2 món P1 và 1 món F1
        mock_order = [
            {"code": "P1", "name": "Phin Sữa Đá", "price": 35000, "quantity": 2},
            {
                "code": "F1",
                "name": "Freeze Trà Xanh",
                "price": 55000,
                "quantity": 1,
            },
        ]
        # Tổng mong đợi: (35000 * 2) + (55000 * 1) = 125,000
        result = calculate_total(mock_order)
        self.assertEqual(result, 125000)

    def test_invalid_quantity(self):
        """Test Case 2: Truyền số lượng lỗi để kiểm tra InvalidQuantityError."""
        mock_order = []
        # Truyền số lượng âm vào hàm, mong đợi ném ra lỗi InvalidQuantityError
        with self.assertRaises(InvalidQuantityError):
            add_to_order(mock_order, "T1", "-1")

        # Truyền số lượng bằng 0 vào hàm, mong đợi ném ra lỗi InvalidQuantityError
        with self.assertRaises(InvalidQuantityError):
            add_to_order(mock_order, "T1", "0")


if __name__ == "__main__":
    unittest.main()