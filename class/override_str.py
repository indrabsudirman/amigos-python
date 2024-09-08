class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
    def call(self, phone_number):
        print(f"{self.brand} is calling {phone_number}")
    
    #override the string method
    def __str__(self) -> str:
        return f"Brand {self.brand} Price {self.price}"
    
    

iphone = Phone("Iphone 7+", 2000000)
samsung = Phone("Samsung S21", 13000000)

print(iphone)
print(samsung)