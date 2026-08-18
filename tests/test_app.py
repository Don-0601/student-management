import unittest
from app import search_students

class TestSearchStudents(unittest.TestCase):

    # 1. Test trường hợp tìm thấy sinh viên
    def test_search_found(self):
        result = search_students("Nguyen")
        self.assertTrue(len(result) > 0)

    # 2. Test trường hợp không tìm thấy sinh viên
    def test_search_not_found(self):
        result = search_students("XYZ_Không_Tồn_Tại")
        self.assertEqual(len(result), 0)

    # 3. Test tìm kiếm không phân biệt hoa/thường
    def test_search_case_insensitive(self):
        result_lower = search_students("nguyen")
        result_upper = search_students("NGUYEN")
        self.assertEqual(result_lower, result_upper)

if __name__ == '__main__':
    unittest.main()
