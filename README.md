## Parking Lot Application
This is a terminal-based application that simulates a parking lot with two levels A and B, each having a capacity to park 20 vehicles. The application provides two main functionalities:

1) Assign a parking space to a new vehicle
2) Retrieve the parking spot number of a particular vehicle

## Setup
To run the application, make sure you have Python 3 installed on your system. Clone the repository to your local machine, navigate to the project directory and run the following command:

```
python main.py
```
This will start the application and you will see a prompt where you can enter your commands.

## Usage
The application provides two commands:

park: This command assigns a parking space to a new vehicle. You need to provide the vehicle number as an argument. The application will assign the first available parking spot, starting from level A and moving to level B if level A is full. If there are no available parking spots, the application will return an error message.

spot: This command retrieves the parking spot number of a particular vehicle. You need to provide the vehicle number as an argument. The application will return the level and parking spot number of the vehicle if it is parked in the parking lot. If the vehicle is not parked in the parking lot, the application will return an error message.

## Limitations
The application has the following limitations:

1) The parking lot has a fixed capacity of 40 vehicles (20 on each level). You cannot change this capacity.
2) The application does not support removing a parked vehicle from the parking lot.
3) The application does not persist data between sessions. If you exit the application, all parking data will be lost.

## Future Work
The following features can be added to the application in the future:

1) Support for removing a parked vehicle from the parking lot.
2) Support for multiple parking lots.
3) Persist data between sessions by using a database or file storage.

## Usage Example
<img width="1680" alt="Screenshot 2023-04-29 at 3 10 39 AM" src="https://user-images.githubusercontent.com/45177819/235260184-2c520f3e-e69b-4788-8222-d4c525f6461d.png">

