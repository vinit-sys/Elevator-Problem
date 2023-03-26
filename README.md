## Elevator-Problem API's

This repository contains API documentation for an elevator system.

### initializeElevatorSystem()

Initializes the elevator system with a specified number of elevators.

**Endpoint:**
> https://vinitprojects.pythonanywhere.com/elevator-system/initialize/

```
Method: POST
Request format: application/json
Response format: application/json
Request fields:
no_of_elevators: integer (number of elevators to initialize)
Response fields:
message: string (status message for the initialization request)
HTTP Status Codes:
201 (CREATED): The request was successful and the elevators were created.
500 (INTERNAL_SERVER_ERROR): Error occurred while creating elevators.
```

### getAllRequests()

Retrieves all destinations for an elevator.

Endpoint:
> https://vinitprojects.pythonanywhere.com/elevator-system/<int:elevator_id>/requests/
```
Method: GET
Request format: None
Response format: application/json
Response fields:
message: string (comma-separated list of destinations for the elevator)
HTTP Status Codes:
200 (OK): The request was successful and the list of destinations is returned.
404 (NOT_FOUND): Elevator with the given ID doesn't exist.
```

### getNextFloor()

Retrieves the next destination floor number for an elevator.

Endpoint:
> https://vinitprojects.pythonanywhere.com/elevator-system/<int:elevator_id>/next-floor/
```
Method: GET
Request format: None
Response format: application/json
Response fields:
message: integer (floor number of the next destination for the elevator)
HTTP Status Codes:
200 (OK): The request was successful and the next destination floor number is returned.
204 (NO_CONTENT): The elevator doesn't have any next destination.
```
### getDirection()

Retrieves the current direction of an elevator.

Endpoint:
> https://vinitprojects.pythonanywhere.com/elevator-system/<int:elevator_id>/direction/
```
Method: GET
Request format: None
Response format: application/json
Response fields:
message: string (direction of the elevator: "up" or "down")
HTTP Status Codes:
200 (OK): The request was successful and the direction of the elevator is returned.
404 (NOT_FOUND): Elevator with the given ID doesn't exist.
```
### putFloorNumberToReach()

Adds a new destination floor number for an elevator.

Endpoint:
> https://vinitprojects.pythonanywhere.com/elevator-system/<int:elevator_id>/floor/<int:floor_number>/
```
Method: GET
Request format: application/json
Response format: application/json
Request fields:
requested_floor: integer (floor number requested by the user)
Response fields:
message: string (status message for adding the destination)
HTTP Status Codes:
200 (OK): The request was successful and the destination was added to the elevator.
404 (NOT_FOUND): Elevator with the given ID doesn't exist.
```
### assignElevator()

Assigns an available elevator to a requested floor.

Endpoint: 
> https://vinitprojects.pythonanywhere.com/elevator-system/assign-elevator/<int:floor_number>/
```
Method: POST
Request format: None
Response format: application/json
Response fields:
message: string (status message for the request)
HTTP Status Codes:
200 (OK): The request was successful and an elevator was assigned to the requested floor.
404 (NOT_FOUND): No elevators are available.
```
### elevatorStatus()

Retrieves the current status of an elevator.

Endpoint: 
> https://vinitprojects.pythonanywhere.com/elevator-system/<int:elevator_id>/status/
```
Method: GET
Request format: None
Response format: application/json
Response fields:
message: string (status of elevator)
HTTP Status Codes:
200 (OK): The request was successful.
404 (INTERNAL_SERVER_ERROR): Elevator doesn't exist.
```

### updateDoorStatus()

Update the door status of an elevator.

Endpoint: 
> https://vinitprojects.pythonanywhere.com/elevator-system/<int:elevator_id>/door-status/
```
Method: POST
Request format: application/json
Response format: application/json
Request fields:
door_status: String (door status either open or close)
Response fields:
message: string (status message for the initialization request)
HTTP Status Codes:
200 (OK): The request was successful and return updated status of door.
404 (INTERNAL_SERVER_ERROR): Elevator doesn't exist.
```

