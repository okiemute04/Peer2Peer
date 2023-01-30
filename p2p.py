class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def transfer(self, recipient, amount):
        self.balance -= amount
        recipient.balance += amount


class P2PApp:
    def __init__(self):
        self.users = {}

    def add_user(self, name):
        user = User(name)
        self.users[name] = user
        return user

    def deposit(self, name, amount):
        user = self.users[name]
        user.deposit(amount)
        print(f"{name} has deposited {amount}. Their current balance is {user.balance}.")

    def send_money(self, sender, recipient_name, amount):
        recipient = self.users[recipient_name]
        sender.transfer(recipient, amount)
        print(
            f"{sender.name} has sent {amount} to {recipient_name}. {sender.name}'s current balance is {sender.balance} and {recipient_name}'s current balance is {recipient.balance}.")

    def check_balance(self, name):
        balance = self.users[name].balance
        print(f"{name}'s current balance is {balance}.")
        return balance

    def transfer_out(self, name, amount):
        user = self.users[name]
        user.withdraw(amount)
        print(f"{name} has transferred out {amount}. Their current balance is {user.balance}.")


p2p_app = P2PApp()


while True:
    user_name = input("Enter user name (or 'q' to quit): ")
    if user_name == 'q':
        break
    p2p_app.add_user(user_name)

while True:

    print("\nWhat would you like to do?")
    print("1. Deposit money")
    print("2. Send money")
    print("3. Transfer out money")
    print("4. Check balance")
    print("5. Quit")
    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        user_name = input("Enter user name: ")
        deposit_amount = int(input("Enter deposit amount: "))
        p2p_app.deposit(user_name, deposit_amount)
    elif choice == 2:
        sender_name = input("Enter sender name: ")
        sender = p2p_app.users[sender_name]
        recipient_name = input("Enter recipient name: ")
        send_amount = int(input("Enter send amount: "))
        p2p_app.send_money(sender, recipient_name, send_amount)
    elif choice == 3:
        withdraw_name = input("Enter user name to transfer out: ")
        withdraw_amount = int(input("Enter transfer amount: "))
        p2p_app.transfer_out(withdraw_name, withdraw_amount)
    elif choice == 4:
        balance_name = input("Enter user name to check balance: ")
        p2p_app.check_balance(balance_name)
    elif choice == 5:
        print("Goodbye!")
        break
