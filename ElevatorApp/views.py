from django.shortcuts import render, redirect
from .models import Elevator
from django.http import JsonResponse

# in elevator_system/views.py

from django.shortcuts import render, redirect
from .models import Elevator
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def initializeElevatorSystem(request):
    if request.method == "POST":
        num_of_elevators = int(request.POST.get("no_of_elevators"))
        elevators = []
        try:
            for i in range(0,num_of_elevators):
                elevator = Elevator.objects.create()
                elevators.append(elevator)
        except Exception as exc:
            return JsonResponse({"message":"Error occured while creating elevators"})
        return JsonResponse({"message":str(elevators)})
    
def getAllRequests(request, elevator_id):
    if request.method=="GET":
        try:
            # Get the elevator object with the given id from the database
            elevator = Elevator.objects.get(id=elevator_id)
        except Exception as exc:
            return JsonResponse({"message": "Elevator doesn't exist"})
        # Return a message with the list of destinations for the elevator
        return JsonResponse({"message": str(elevator.destinations)})


# Method to get the next floor for a specific elevator
def getNextFloor(request, elevator_id):
    try:
        # Get the elevator object with the given id from the database
        elevator = Elevator.objects.get(id=elevator_id)
    except Exception as exc:
        return JsonResponse({"message": "Elevator doesn't exist"})
    # Return a message with the next destination floor for the elevator
    if not elevator.destinations:
        return JsonResponse({"message":"-1"})
    return JsonResponse({"message": str(elevator.destinations[0])})


# Method to get the direction of a specific elevator
def getDirection(request, elevator_id):
    try:
        # Get the elevator object with the given id from the database
        elevator = Elevator.objects.get(id=elevator_id)
    except Exception as exc:
        return JsonResponse({"message": "Elevator doesn't exist"})
    # Return a message with the direction of the elevator
    return JsonResponse({"message": elevator.direction})


# Method to get the floor number from the user to reach for a specific elevator
def getFloorNumberToReach(request, elevator_id, requested_floor):
    # Get the elevator object with the given id from the database
    elevator = Elevator.objects.get(id=elevator_id)
    # Add the requested floor to the list of destinations for the elevator
    elevator.add_destination(requested_floor)
    # Set the direction of the elevator based on the requested floor
    if elevator.current_floor <= requested_floor:
        elevator.direction = "up"
    else:
        elevator.direction = "down"
    # Save the updated elevator object in the database
    elevator.save()
    # If the elevator is stopped, start moving it to the next destination
    elevator.move()

    return JsonResponse({"message": "Destination added successfully"})


# Method to assign an elevator to a requested floor
def assignElevator(request, requested_floor):
    # Get all available elevators that are not out of order and not busy
    available_elevators = Elevator.objects.exclude(status="not_working")
    # If there are no available elevators, return None
    if not available_elevators:
        return JsonResponse({"message":"Elevators not available"})

    # Find the elevator that is closest to the requested floor and moving in the correct direction
    best_elevator = None
    best_distance = None
    for elevator in available_elevators:
        if elevator.direction == "up" and requested_floor >= elevator.current_floor:
            distance = requested_floor - elevator.current_floor
        elif elevator.direction == "down" and requested_floor <= elevator.current_floor:
            distance = elevator.current_floor - requested_floor
        else:
            distance = abs(requested_floor - elevator.current_floor)

        if best_elevator is None or distance < best_distance:
            best_elevator = elevator
            best_distance = distance

    best_elevator.add_destination(requested_floor)
    best_elevator.move()

    return JsonResponse({"message": "Destination added successfully"})

# Method to get elevator status for the reuqested elevator_id
def elevatorStatus(request, elevator_id):
    try:
        # Get the elevator object with the given id from the database
        elevator = Elevator.objects.get(id=elevator_id)
    except Exception as exc:
        return JsonResponse({"message": "Elevator doesn't exist"})
    # Return a status with the list of destinations for the elevator
    return JsonResponse({"message": elevator.status})

# Method to get elevator status for the reuqested elevator_id
@csrf_exempt
def updateDoorStatus(request,elevator_id):
    if request.method == "POST":
        try:
            door_status = request.POST.get("door_status")
            print(door_status)
            # updates the elevator object door status with the given id from the database
            elevator = Elevator.objects.get(id=elevator_id)
            elevator.door = door_status
            elevator.save()
        except Exception as exc:
            return JsonResponse({"message": "Elevator doesn't exist"})
        # Return a message with the list of destinations for the elevator
        return JsonResponse({"message": door_status})
