# ==========================================
# OOP - SHOPPING CHECKOUT
# ==========================================


class Product:

    # 1. Constructor
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # 2. Show Product Information
    def show_info(self):
        print("Product:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    # 3. Calculate Total Price
    def total_price(self):
        return self.price * self.quantity

    # 4. Calculate Discounted Price
    def discounted_price(self, discount):

        if discount < 0 or discount > 100:
            return "Invalid discount"

        total = self.total_price()
        discount_amount = total * discount / 100

        return total - discount_amount

    # 5. Update Quantity
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity


# 6. Creating Product Objects

product1 = Product("T-Shirt", 500, 2)
product2 = Product("Shoes", 2000, 1)


# 7. Product 1 Information

print("Product 1")

product1.show_info()

print("Total Price:", product1.total_price())
print("After 10% Discount:", product1.discounted_price(10))

print("--------------------")


# 8. Product 2 Information

print("Product 2")

product2.show_info()

print("Total Price:", product2.total_price())

print("--------------------")


# 9. Updating Quantity

product1.update_quantity(3)

print("Product 1 After Quantity Update")

product1.show_info()

print("New Total:", product1.total_price())

print("--------------------")


# 10. Checkout Total

checkout_total = product1.total_price() + product2.total_price()

print("Final Checkout Total:", checkout_total)