from django.urls import path
from .views import ElevatorSystem

urlpatterns = [
    path("initialize/", ElevatorSystem.as_view({"post":"initialize"})),
    # URL for getting all the requests for a specific elevator
    path("<int:elevator_id>/requests/", ElevatorSystem.as_view({"get":"get_all_requests"})),
    # URL for getting the next floor for a specific elevator
    path("<int:elevator_id>/next-floor/", ElevatorSystem.as_view({"get":"get_next_floor"})),
    # URL for getting the direction of a specific elevator
    path("<int:elevator_id>/direction/", ElevatorSystem.as_view({"get":"get_direction"})),
    # URL for getting the floor number to reach for a specific elevator
    path(
        "<int:elevator_id>/floor/<int:requested_floor>/",
        ElevatorSystem.as_view({"get":"put_floor_number_to_reach"}),
    ),
    # URL for assigning an elevator to a requested floor
    path("assign-elevator/<int:requested_floor>/", ElevatorSystem.as_view({"get":"assign_elevator"})),
    # URL for getting the status of a specific elevator
    path("<int:elevator_id>/status/", ElevatorSystem.as_view({"get":"get_elevator_status"})),
    # URL for updating the door status of a specific elevator
    path(
        "<int:elevator_id>/door-status/",
        ElevatorSystem.as_view({"post":"update_door_status"}),
    ),
]
