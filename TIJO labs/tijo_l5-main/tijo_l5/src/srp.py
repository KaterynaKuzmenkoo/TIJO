# Naruszona zasada SRP

class Order:
    def __init__(self, id, items, customer):
        self.id = id
        self.items = items
        self.customer = customer


class OrderProcessor:
    def __init__(self, order, order_validator, order_item, order_mail):
        self.order_validator = order_validator
        self.order_item = order_item
        self.order_mail = order_mail
        self.order = order

    def process_order(self):
        self.order_validator.validate_order(self.order)
        self.order_item.save_order_to_database(self.order)
        self.order_mail.send_confirmation_email(self.order)

class OrderValidator:
    def validate_order(self,order):
        self.order = order
        print("Walidacja zamowienia.")

class OrderItem:
    def save_order_to_database(self,order):
        self.order = order
        print("Zapisywanie zamowienia do bazy danych.")

class OrderMail:
    def send_confirmation_email(self, order):
        self.order = order
        print("Wysylanie e-maila potwierdzajacego.")


order = Order("123", ["Produkt A", "Produkt B"], "Jan Kowalski")

order_validator = OrderValidator()
order_item = OrderItem()
order_mail = OrderMail()
processor = OrderProcessor(order, order_validator, order_item, order_mail)
processor.process_order()