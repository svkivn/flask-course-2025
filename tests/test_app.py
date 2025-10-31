import unittest
from app import create_app

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        # Створюємо додаток з тестовою конфігурацією
        self.app = create_app("test")
        # Отримуємо тестовий клієнт
        self.client = self.app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    
    def test_products_page(self):
        with self.client as client: 
            response = client.get("/shop/products")
            print(response.status_code)
            self.assertEqual(response.status_code, 200)

    def test_404(self):
        response = self.client.get("/nonexistent")
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
