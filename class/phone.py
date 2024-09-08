class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
    def call(self, phone_number):
        print(f"{self.brand} is calling {phone_number}")

iphone = Phone("Iphone 7+", 2000000)
samsung = Phone("Samsung S21", 13000000)

print(f"call from {iphone.brand} the price is {iphone.price}")
print(f"call from {samsung.brand} the price is {samsung.price}")
samsung.call("0896362456581")