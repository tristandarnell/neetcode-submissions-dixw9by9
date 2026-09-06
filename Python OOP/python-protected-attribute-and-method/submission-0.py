class Account:
    def __init__(self, title, balance):
        self._title = title
        self._balance = balance
    
    def display_balance(self) -> None:
        print(f"Balance: ${self._balance}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
