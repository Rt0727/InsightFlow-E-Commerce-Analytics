import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_sales(self):
        response = self.client.get("/sales")
        self.assertEqual(response.status_code, 200)

    def test_get_summary(self):
        response = self.client.get("/analytics/summary")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()