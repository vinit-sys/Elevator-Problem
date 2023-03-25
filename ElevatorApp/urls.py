from django.urls import path
from . import views

urlpatterns = [
    path("initialize/", views.initializeElevatorSystem),
    # URL for getting all the requests for a specific elevator
    path("<int:elevator_id>/requests/", views.getAllRequests),
    # URL for getting the next floor for a specific elevator
    path("<int:elevator_id>/next-floor/", views.getNextFloor),
    # URL for getting the direction of a specific elevator
    path("<int:elevator_id>/direction/", views.getDirection),
    # URL for getting the floor number to reach for a specific elevator
    path(
        "<int:elevator_id>/floor/<int:requested_floor>/",
        views.getFloorNumberToReach,
    ),
    # URL for assigning an elevator to a requested floor
    path("assign-elevator/<int:requested_floor>/", views.assignElevator),
    # URL for getting the status of a specific elevator
    path("<int:elevator_id>/status/", views.elevatorStatus),
    # URL for updating the door status of a specific elevator
    path(
        "<int:elevator_id>/door-status/",
        views.updateDoorStatus,
    ),
]
