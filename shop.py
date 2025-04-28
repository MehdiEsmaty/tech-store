class MobilePhone:
    def __init__(self, brand, model, price, stock):
        self.brand = brand
        self.model = model
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price} ({self.stock} in stock)"

class MobileStore:
    def __init__(self):
        self.phones = []
        self.sales = 0

    def add_phone(self, phone):
        self.phones.append(phone)

    def list_phones(self):
        for idx, phone in enumerate(self.phones, 1):
            print(f"{idx}. {phone}")

    def purchase_phone(self, idx, quantity):
        if 0 <= idx < len(self.phones):
            phone = self.phones[idx]
            if phone.stock >= quantity:
                phone.stock -= quantity
                self.sales += phone.price * quantity
                print(f"Purchased {quantity} x {phone.brand} {phone.model}")
            else:
                print("Not enough stock!")
        else:
            print("Invalid phone selection.")

    def view_sales(self):
        print(f"Total Sales: ${self.sales}")

def main():
    store = MobileStore()
    store.add_phone(MobilePhone("Apple", "iPhone 14", 999, 10))
    store.add_phone(MobilePhone("Samsung", "Galaxy S23", 899, 8))
    store.add_phone(MobilePhone("Google", "Pixel 7", 799, 5))

    while True:
        print("\n--- Mobile Phone Store ---")
        print("1. List Phones")
        print("2. Add Phone")
        print("3. Purchase Phone")
        print("4. View Sales")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            store.list_phones()
        elif choice == "2":
            brand = input("Brand: ")
            model = input("Model: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            store.add_phone(MobilePhone(brand, model, price, stock))
            print("Phone added!")
        elif choice == "3":
            store.list_phones()
            idx = int(input("Select phone number: ")) - 1
            quantity = int(input("Quantity: "))
            store.purchase_phone(idx, quantity)
        elif choice == "4":
            store.view_sales()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
