import unittest
from p2p import P2PApp


class TestP2PApp(unittest.TestCase):
    def setUp(self):
        self.app = P2PApp()
        self.user_a = self.app.add_user("User A")
        self.user_b = self.app.add_user("User B")

    def test_deposit(self):
        self.app.deposit("User A", 10)
        self.assertEqual(self.app.check_balance("User A"), 10)
        self.app.deposit("User B", 20)
        self.assertEqual(self.app.check_balance("User B"), 20)

    def test_send_money(self):
        self.app.deposit("User A", 10)
        self.app.deposit("User B", 20)
        self.app.send_money(self.user_b, "User A", 15)
        self.assertEqual(self.app.check_balance("User A"), 25)
        self.assertEqual(self.app.check_balance("User B"), 5)

    def test_transfer_out(self):
        self.app.deposit("User A", 25)
        self.app.transfer_out("User A", 25)
        self.assertEqual(self.app.check_balance("User A"), 0)


if __name__ == "__main__":
    unittest.main()