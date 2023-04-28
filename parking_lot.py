class ParkingLot:
    def __init__(self):
        self.level_a = [0] * 20  # parking lot A having 20 slots
        self.level_b = [0] * 20  # parking lot B having 20 slots
        self.next_space_a = 1   # Next Available Space Number in Parking Lot A
        self.next_space_b = 21  # Next Available Space Number in Parking Lot B
        self.vehicles = {}

    """
    This function Assigns the Parking space for the given Vehicle Number
    
    Parameters:
    vehicle_no (string) -- Vehicle No for which Parking Space needs to be alloted
    """
    def assign_parking_space(self, vehicle_no):
        if self.vehicles.get(vehicle_no):
            return f"Parking Slot Already Allocated, Vehicle {vehicle_no} is parked in Level {self.vehicles.get(vehicle_no).get('level')} and Spot {self.vehicles.get(vehicle_no).get('spot')}"
        if self.next_space_a <= 20:
            self.level_a[self.next_space_a - 1] = vehicle_no
            self.vehicles[vehicle_no] = {"level": "A", "spot": self.next_space_a}
            self.next_space_a += 1
            return f"Congratulations, your vehicle has been successfully parked. Your vehicle {vehicle_no} is parked " \
                   f"in level {self.vehicles.get(vehicle_no).get('level')} and spot {self.vehicles.get(vehicle_no).get('spot')}. " \
                   f"Thank you for choosing our parking facility. Have a great day!"
        elif self.next_space_b <= 40:
            self.level_b[self.next_space_b - 21] = vehicle_no
            self.vehicles[vehicle_no] = {"level": "B", "spot": self.next_space_b}
            self.next_space_b += 1
            return f"Congratulations, your vehicle has been successfully parked. Your vehicle {vehicle_no} is parked " \
                   f"in level {self.vehicles.get(vehicle_no).get('level')} and spot {self.vehicles.get(vehicle_no).get('spot')}. " \
                   f"Thank you for choosing our parking facility. Have a great day!"
        else:
            return "Sorry, parking lot is full."

    """
    This function fetches the parking spot for the given Vehicle Number

    Parameters:
    vehicle_no (string) -- Vehicle No for which parking spot to be fetched
    """
    def get_parking_spot(self, vehicle_no):
        if self.vehicles.get(vehicle_no):
            return self.vehicles.get(vehicle_no)
        else:
            return False
