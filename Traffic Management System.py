import time
import random

# Class to represent a traffic light
class TrafficLight:
    def __init__(self, direction):
        self.direction = direction
        self.state = 'Red'  # Initial state of the traffic light
        self.cycle_duration = 0  # Duration of the light cycle in seconds

    # Method to change the state of the traffic light
    def change_state(self):
        if self.state == 'Red':
            self.state = 'Green'
            self.cycle_duration = random.randint(5, 10)  # Green light for 5 to 10 seconds
        elif self.state == 'Green':
            self.state = 'Yellow'
            self.cycle_duration = 3  # Yellow light for 3 seconds
        else:
            self.state = 'Red'
            self.cycle_duration = random.randint(5, 10)  # Red light for 5 to 10 seconds

    # Method to simulate the traffic light cycle
    def run_cycle(self):
        print(f"{self.direction} light is now {self.state} for {self.cycle_duration} seconds.")
        time.sleep(self.cycle_duration)

# Traffic Management System class
class TrafficManagementSystem:
    def __init__(self):
        # Initialize traffic lights for each direction
        self.lights = {
            'North': TrafficLight('North'),
            'South': TrafficLight('South'),
            'East': TrafficLight('East'),
            'West': TrafficLight('West')
        }

    # Method to run the traffic management system
    def run(self):
        while True:
            for direction, light in self.lights.items():
                light.run_cycle()  # Run the cycle for each traffic light
                light.change_state()  # Change the state of the traffic light

            print("\n--- Status Update ---")
            for direction, light in self.lights.items():
                print(f"{direction} light: {light.state}")
            print("---------------------")

# Main function to run the traffic management system
if __name__ == "__main__":
    tms = TrafficManagementSystem()
    try:
        tms.run()
    except KeyboardInterrupt:
        print("\nTraffic Management System stopped.")
