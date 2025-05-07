from simulation.order_manager import OrderManager

order_manager = OrderManager()

def place_order(order):
    order_manager.place_order(order)
    return order_manager.get_orders()