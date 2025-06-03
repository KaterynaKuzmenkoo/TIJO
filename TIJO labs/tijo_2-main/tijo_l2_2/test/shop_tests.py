from src.shop import ShoppingCart
import unittest

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        print("* setUp()")
        self.shop = ShoppingCart()

    def test_add(self):
        #Arrange
        product = ("Pomidor", 2, 1)

        print("* test_add()")

        #Act
        result = self.shop.add_product(* product)

        #Assert
        self.assertTrue(result)

    def test_remove(self):
        self.shop.add_product("Pomidor", 2, 1)
        product = "Pomidor"

        print("* test_remove()")

        #Act
        result = self.shop.remove_product(product)

        # Assert
        self.assertTrue(result)
        self.assertNotIn(("Pomidor", 2, 1), self.shop.items)

    def test_update_quantity(self):
        #Arrange
        self.shop.add_product("Pomidor", 2, 1)
        product = "Pomidor"
        new_quantity = 10

        print("* test_update_quantity()")

        #Act
        result = self.shop.update_quantity(product, new_quantity)

        #Assert
        self.assertTrue(result)
        self.assertEqual(self.shop.items[0][2], new_quantity)

    def test_get_products(self):
        # Arrange
        self.shop.add_product("Pomidor", 2, 1)
        self.shop.add_product("Chleb", 3, 1)

        print("* test_get_products()")

        # Act
        result = self.shop.get_products()

        # Assert
        self.assertEqual(result, ["Pomidor", "Chleb"])

    def test_count(self):
        #Arrange
        self.shop.add_product("Pomidor", 2, 1)
        self.shop.add_product("Chleb", 3, 3)

        print("* test_count()")

        #Act
        result = self.shop.count_products()

        #Assert
        self.assertEqual(result, 4)

    def test_total_price(self):
        # Arrange
        self.shop.add_product("Pomidor", 2, 1)
        self.shop.add_product("Chleb", 3, 3)

        print("* test_count()")

        # Act
        result = self.shop.get_total_price()

        # Assert
        self.assertEqual(result, 11)

    def test_discount(self):
        #Arrange
        self.shop.add_product("Pomidor", 10, 1)
        self.shop.add_product("Chleb", 3, 1)
        self.assertEqual(self.shop.get_total_price(), 13)
        print("* test_discount()")

        #Act
        result = self.shop.apply_discount_code("PROMO10")
        new_total = self.shop.get_total_price()

        #Assert
        self.assertTrue(result)
        self.assertAlmostEqual(new_total, 11.7)

    def test_checkout(self):
        #Arrange
        self.shop.add_product("Pomidor", 2, 1)
        self.shop.add_product("Chleb", 3, 3)
        print("* test_checkout()")

        #Act
        result = self.shop.checkout()

        #Assert
        self.assertTrue(result)
        self.assertEqual(len(self.shop.items), 0)
        self.assertEqual(self.shop.discount_applied, 0.0)
    def tearDown(self):
        print("* tearDown()")
        self.shop = None

if __name__ == '__main__':
    unittest.main()
