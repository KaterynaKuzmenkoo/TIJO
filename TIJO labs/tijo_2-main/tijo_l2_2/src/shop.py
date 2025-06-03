class ShoppingCart:
    def __init__(self):
        self.items = []
        self.discount_applied = 0.0

    def add_product(self, product_name: str, price: int, quantity: int) -> bool:
        product = (product_name, price, quantity)
        self.items.append(product)
        return True

    def remove_product(self, product_name: str) -> bool:
        for product in self.items:
            if product[0] == product_name:
                self.items.remove(product)
                return True
        return False

    def update_quantity(self, product_name: str, new_quantity: int) -> bool:
        for i, product in enumerate(self.items):
            if product[0] == product_name:
                self.items[i] = (product_name, product[1], new_quantity)
                return True
        return False

    def get_products(self):
         return [product[0] for product in self.items]

    def count_products(self) -> int:
        return sum(product[2] for product in self.items)

    def get_total_price(self) -> int:
        total = sum(product[1] * product[2] for product in self.items)
        return total * (1 - self.discount_applied)

    def apply_discount_code(self, discount_code: str) -> bool:
        DISCOUNT_CODES = {
            "PROMO10": 0.10,
            "PROMO20": 0.20,
            "PROMO50": 0.50,
        }

        if discount_code in DISCOUNT_CODES:
            self.discount_applied = DISCOUNT_CODES[discount_code]
            return True
        return False

    def checkout(self) -> bool:
        if not self.items:
            return False
        self.items.clear()
        self.discount_applied = 0.0
        return True