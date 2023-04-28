from parking_lot import ParkingLot


class ParkingTerminal:
    def __init__(self):
        self.parking_lot = ParkingLot()

    """
    This function displays the available options to the user
    """
    def print_menu(self):
        print("Welcome to Parking Terminal!")
        print("1. Park a vehicle")
        print("2. Retrieve parking spot of a vehicle")
        print("3. Exit")

    """
    This function performs the action which user opts for
    
    Parameters:
    Choice (string) -- User Opted Choice
    """
    def handle_choice(self, choice):
        if choice == "1":
            vehicle_no = input("Enter vehicle number: ")
            result = self.parking_lot.assign_parking_space(vehicle_no)
            print(result+"\n")
        elif choice == "2":
            vehicle_no = input("Enter vehicle number: ")
            result = self.parking_lot.get_parking_spot(vehicle_no)
            if result:
                print(f"Vehicle {vehicle_no} is parked in Level {result.get('level')} and Spot {result.get('spot')}\n")
            else:
                print(f"Vehicle {vehicle_no} is not parked in the parking lot\n")
        elif choice == "3":
            exit()
        else:
            print("Invalid choice\n")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice: ")
            print()
            self.handle_choice(choice)


if __name__ == '__main__':
    terminal = ParkingTerminal()
    terminal.run()
