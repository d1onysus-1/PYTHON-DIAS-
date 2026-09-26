class BankAccount:
    def __init__(self, number, name, balance):
        self.number = number
        self.name = name
        self.balance = balance

    def deposit(self, money):
        if money <= 0:
            raise ValueError("Сумма должна быть больше 0")
        self.balance += money

    def withdraw(self, money):
        if money <= 0:
            raise ValueError("Сумма должна быть больше 0")

        if money <= self.balance:
            self.balance -= money
        else:
            print("Недостаточно денег")

    def show_balance(self):
        print("Баланс:", self.balance)


name = input("Введите имя: ")
account = BankAccount("061227550285", name, 0)

while True:
    print("\n1 - Пополнить")
    print("2 - Снять")
    print("3 - Посмотреть баланс")
    print("4 - Выход")

    choice = input("Выберите действие: ")

    try:
        if choice == "1":
            money = int(input("Сколько хотите пополнить? "))
            account.deposit(money)
            account.show_balance()

        elif choice == "2":
            money = int(input("Сколько хотите снять? "))
            account.withdraw(money)
            account.show_balance()

        elif choice == "3":
            account.show_balance()

        elif choice == "4":
            print("Выход из системы")
            break

        else:
            print("Неверный выбор")

    except ValueError as error:
        print("Ошибка:", error)