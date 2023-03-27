# Elevator-Problem
## Overview
This project describes an elevator system with various capabilities, including moving up and down, opening and closing doors, and assigning elevators to different floors. It also lists some assumptions that will guide the development of a Django project to maintain the system. The project will have several API endpoints, allowing for the initialization of the system, fetching requests for a given elevator, saving user requests, and opening/closing doors.

## Installation
After cloning the project.

First, create virtual environment for the project.In this project I used virtualenv
```sh
pip install virtualenv
```
Now install the requirements from the file requirements.txt.
```sh
pip install -r path/to/requirements.txt
```
Now setup .env file inside ElevatorProject folder.(where settings file is located)

inside /.env
```
SECRET_KEY='scret_key'
DATABASE_ENGINE='django.db.backends.postgresql'
DATABASE_NAME='database_name'
DATABASE_USER='database_user'
DATABASE_PASSWORD='database_password'
DATABASE_HOST='database_host'
DATABASE_PORT='port_number'
```
Migrate the database
```sh
python manage.py migrate
```
Now run the server
```sh
python manage.py runserver
```



## Architecture:

- The system will follow the client-server architecture.

- The Elevator controller acts as a server and provides endpoints to communicate with the client.

- The client can be any user interface that sends requests to the elevator controller.

### Elevator Model

The Elevator model will consist of the following fields:
```
id: Primary key of the elevator.
current_floor: Current floor of the elevator.
destinations: List of destinations the elevator needs to visit.
direction: The direction the elevator is moving.
status: The status of the elevator.
door_status : The status of the door.
```
### The Elevator Controller:

1 The Elevator controller will handle requests from the client and interact with the Elevator model.

2 The Elevator controller will perform the following tasks:

- Create the required number of elevators.

- Assign the nearest available elevator to the requested floor.

- Get the list of destinations for the requested elevator.

- Get the next floor for the requested elevator.

- Get the direction of the requested elevator.

- Add the requested floor to the destination list of the requested elevator.

- Update the door status of the requested elevator.

- Get the status of the requested elevator.

3 The Elevator controller will communicate with the Elevator model using the ORM provided by Django.

4 The Elevator controller will respond to the client with JSON formatted data.

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

