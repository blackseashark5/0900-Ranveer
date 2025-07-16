#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from random import randint, uniform

class ShelfDataPublisher(Node):
    def __init__(self):
        super().__init__('shelf_data_publisher')
        self.publisher_ = self.create_publisher(String, '/shelf_data', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)

    def timer_callback(self):
        shelf_id = randint(1, 5)
        item = f"Item_{chr(randint(65, 90))}"
        x = round(uniform(-5.0, 5.0), 2)
        y = round(uniform(-5.0, 5.0), 2)
        msg = String()
        msg.data = f"Shelf_{shelf_id}: {item} at (X: {x}, Y: {y})"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Published shelf data: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = ShelfDataPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
