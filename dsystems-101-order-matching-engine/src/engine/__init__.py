class OrderMatcher:
    def __init__(self):
        self.orders = {}

    def match_order(self, order_id, order_details):
        # Logic to match the order
        self.orders[order_id] = order_details
        return f"Order {order_id} matched."

    def get_order_status(self, order_id):
        # Logic to get the status of an order
        return self.orders.get(order_id, "Order not found.")