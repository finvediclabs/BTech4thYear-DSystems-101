def log_message(message):
    # Function to log messages
    print(f"[LOG] {message}")

def format_order(order):
    # Function to format order data
    return f"Order ID: {order['id']}, Quantity: {order['quantity']}, Price: {order['price']}"