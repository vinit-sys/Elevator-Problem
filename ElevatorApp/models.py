from django.db import models
import time

# Choices for the status of the elevator
ELEVATOR_STATUS_CHOICES = (
    ("start", "START"),  # Elevator is moving
    ("stop", "STOP"),  # Elevator is stopped
    ("not_working", "NOT WORKING"),  # Elevator is out of service
)

# Choices for the status of the elevator door
DOOR_STATUS_CHOICES = (
    ("open", "OPEN"),  # Door is open
    ("close", "CLOSE"),  # Door is closed
)

# Choices for the direction the elevator is moving
DIRECTION_CHOICES = (
    ("up", "UP"),  # Elevator is moving up
    ("down", "DOWN"),  # Elevator is moving down
    ("idle", "IDLE"),  # Elevator is not moving
)


class Elevator(models.Model):
    current_floor = models.IntegerField(default=1)  # The current floor of the elevator
    destinations = models.JSONField(
        default=list,null=True,blank=True
    )  # The list of floors the elevator needs to go to
    status = models.CharField(
        max_length=20, choices=ELEVATOR_STATUS_CHOICES, default="stop"
    )  # The status of the elevator (moving, stopped, or out of service)
    direction = models.CharField(
        max_length=4, choices=DIRECTION_CHOICES, default="idle"
    )  # The direction the elevator is moving
    door = models.CharField(
        max_length=5, choices=DOOR_STATUS_CHOICES, default="close"
    )  # The status of the elevator door

    # Define the string representation of the Elevator model
    def __str__(self):
        return f"elevator_id : {self.id}"

    # Define a method to move the elevator to the next destination floor
    def move(self):
        self.status = "start"  # Set the status of the elevator to "moving"
        self.save()
        if not self.destinations:  # If there are no destinations, return
            return
        
        if (
            self.current_floor < self.destinations[0]
        ):  # If the current floor is less than the next destination floor
            self.current_floor = self.destinations[
                0
            ]  # Move the elevator up to the next destination floor

        else: # If the current floor is greater than the next destination floor
            self.current_floor = self.destinations[
                0
            ]  # Move the elevator down to the next destination floor
        self.destinations.pop(
            0
        )  # Remove the destination from the list of destinations
        self.status = "stop"  # Set the status of the elevator to "stopped"
        self.save()

    # Define a method to add a floor to the list of destinations
    def add_destination(self, floor):
        if (
            floor not in self.destinations
        ):  # If the floor is not already in the list of destinations
            self.destinations.append(floor)  # Add the floor to the list of destinations
            self.destinations.sort()  # Sort the list of destinations in ascending order

    # Define a method to check if the elevator has any destinations
    def is_busy(self):
        return bool(
            self.destinations
        )  # Return True if there are destinations, False otherwise
