import rclpy
from rclpy.node import Node
import random

class Simulator(Node):
    def __init__(self):
        super().__init__('simulation')
        self.timer = self.create_timer(0.5, self.publish_data)

    def publish_data(self):
        data_list = [
            random.uniform(0, 40),  #temperature
            random.uniform(100, 1050), #pressure
            random.uniform(0, 100),  # humidity
        ]
        print(f"Sensor data: Temperature: {data_list[0]} C, Pressure: {data_list[1]} mb, Humidity: {data_list[2]} %")

def main(args=None):
    rclpy.init(args=args)
    simulator = Simulator()
    rclpy.spin(simulator)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
