import unittest
from auth.service import AuthService
from auth.crypto import verify_jwt_token

class TestAuthMicroservice(unittest.TestCase):
    def setUp(self):
        self.svc = AuthService()

    def test_register_and_login_success(self):
        registered = self.svc.register("divyasree", "StrongPassword123")
        self.assertTrue(registered)
        token = self.svc.authenticate("divyasree", "StrongPassword123")
        self.assertIsNotNone(token)
        payload = verify_jwt_token(token)
        self.assertEqual(payload["sub"], "divyasree")

    def test_invalid_password_rejection(self):
        self.svc.register("alice", "ValidPass")
        token = self.svc.authenticate("alice", "WrongPass")
        self.assertIsNone(token)

if __name__ == "__main__":
    unittest.main()
