import unittest
from unittest.mock import patch
from database import fetch_sales_data

class TestDatabase(unittest.TestCase):
    @patch("database.connect_db")
    def test_fetch_sales_data(self, mock_connect):
        mock_connection = mock_connect.return_value
        mock_cursor = mock_connection.cursor.return_value
        
        mock_cursor.fetchall.return_value = [
            {"product_name": "Laptop", "quantity_sold": 10, "revenue": 1000}
        ]
        
        result = fetch_sales_data()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["product_name"], "Laptop")

if __name__ == "__main__":
    unittest.main()