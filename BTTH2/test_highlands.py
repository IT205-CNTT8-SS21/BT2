import unittest
from pos_logic import add_to_order, calculate_total, INVALID_QUANTITY_MSG


class TestHighlandsPOS(unittest.TestCase):
    """Lớp kiểm thử đơn vị tự động cho các hàm xử lý logic POS."""

    def test_calculate_total(self):
        """Test Case 1: Kiểm tra tính chuẩn xác của hàm tính tổng tiền."""
        mock_order = [
            {"code": "P1", "name": "Phin Sữa Đá", "price": 35000, "quantity": 2},
            {
                "code": "F1",
                "name": "Freeze Trà Xanh",
                "price": 55000,
                "quantity": 1,
            },
        ]
        result = calculate_total(mock_order)
        self.assertEqual(result, 125000)

    def test_invalid_quantity(self):
        """Test Case 2: Kiểm tra ValueError khi truyền số lượng không hợp lệ."""
        mock_order = []
        
        # Kiểm tra khi nhập số âm, hàm phải ném ra ValueError với nội dung thông báo chuẩn
        with self.assertRaises(ValueError) as context:
            add_to_order(mock_order, "T1", "-1")
        self.assertEqual(str(context.exception), INVALID_QUANTITY_MSG)

        # Kiểm tra khi nhập bằng 0, hàm phải ném ra ValueError
        with self.assertRaises(ValueError) as context:
            add_to_order(mock_order, "T1", "0")
        self.assertEqual(str(context.exception), INVALID_QUANTITY_MSG)


if __name__ == "__main__":
    unittest.main()