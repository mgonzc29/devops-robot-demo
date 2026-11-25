def can_move(distance: float) -> bool:
    #Return True if the robot can move safely.
    if distance < 0:
        raise ValueError("Distance cannot be negative")
    return distance > 0.5