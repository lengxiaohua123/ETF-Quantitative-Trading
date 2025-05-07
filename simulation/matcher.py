class Matcher:
    def match(self, order, market_data):
        # 简单的撮合逻辑
        return {
            "order_id": order["id"],
            "status": "filled",
            "filled_price": market_data["price"],
            "filled_volume": order["volume"]
        }