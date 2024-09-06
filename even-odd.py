import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class EvenOddCheckerNode(Node):
    def __init__(self):
        super().__init__('checking')
        self.timer = self.create_timer(1.0, self.check_number)

    def check_number(self):
        number = int(input("Enter a number: "))
        if number % 2 == 0:
            res = "Even"
        else:
            res = "Odd"

        output = f"Number {number} is {res}"
        self.get_logger().info(output)

def main(args=None):
    rclpy.init(args=args)
    node = EvenOddCheckerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
