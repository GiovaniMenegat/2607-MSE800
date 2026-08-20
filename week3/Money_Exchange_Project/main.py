from database import create_table
from managers.customer_manager import Customer
from managers.currency_manager import Currency
from managers.exchange_rate_manager import ExchangeRate
from managers.exchange_manager import Exchange

def menu():
    print("\n==== Money Exchange Manager ====")
    print("1. Add Customer")
    print("2. Add Currency")
    print("3. Create Exchange Rate")
    print("4. Create Exchange")
    print("5. List Exchange")
    print("6. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            c = Customer(name, email, address)
            c.create_customer()
        elif choice == '2':
           name = input("Enter name: ")
           country = input("Enter country: ")
           c = Currency(name, country)
           c.create_currency()
        elif choice == '3':
            rate = float(input("Enter rate: "))
            date = input("Enter date: ")
            print(Currency.view_currency())
            from_currency_id = int(input("Enter from_currency_id (see list above): "))
            to_currency_id = int(input("Enter to_currency_id (see list above): "))
            e = ExchangeRate(rate, date, from_currency_id, to_currency_id)
            e.create_exchange_rate()
        elif choice == '4':
            original_amount = float(input("Enter original_amount: "))
            final_amount = float(input("Enter final_amount: "))
            date = input("Enter date: ")
            print(ExchangeRate.view_exchange_rate())
            exchange_rate_id = int(input("Enter exchange_rate_id (see list above): "))
            print(Customer.view_customer())
            customer_id = int(input("Enter customer_id (see list above): "))
            e = Exchange(original_amount, final_amount, date, exchange_rate_id, customer_id)
            e.create_exchange()
        elif choice == '5':
            id = input("Enter exchange id to search: ")
            print(Exchange.search_exchange_by_id(id))
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
