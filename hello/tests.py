from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse

class HelloViewTest(TestCase):
    def test_hello_view(self):
        response = self.client.get(reverse('hello'))  # 測試 /hello/
        self.assertEqual(response.status_code, 200)  # 確保回應 200
        self.assertJSONEqual(response.content, {"message": "Hello, Django!"})  # 確保 JSON 正確
        print("一階段測試 OK")
