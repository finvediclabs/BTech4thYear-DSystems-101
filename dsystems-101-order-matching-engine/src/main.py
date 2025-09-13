# dsystems-101-order-matching-engine/src/main.py

import sys
from engine import OrderMatcher
from pubsub import PubSubManager
from config.settings import KafkaConfig, RedisConfig

def main():
    try:
        # Initialize the order matcher
        order_matcher = OrderMatcher()
        
        # Initialize the pub-sub manager
        pubsub_manager = PubSubManager(KafkaConfig, RedisConfig)
        
        # Start the pub-sub system
        pubsub_manager.start()
        
        print("Distributed Order Matching Engine is running...")
        
        # Example of how to match an order
        # order = {"id": 1, "type": "buy", "amount": 100}
        # order_matcher.match_order(order)
        
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()