import unittest
from analytics import calculate_summary

class TestAnalytics(unittest.TestCase):
    def test_calculate_summary(self):
        sample_data = [
            {"product_name": "Laptop", "quantity_sold": 10, "revenue": 1000},
            {"product_name": "Phone", "quantity_sold": 20, "revenue": 2000},
        ]
        
        result = calculate_summary(sample_data)
        self.assertEqual(result["total_revenue"], 3000)
        self.assertEqual(result["total_quantity"], 30)

if __name__ == "__main__":
    unittest.main()