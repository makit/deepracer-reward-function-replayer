import math


def reward_function(params):
    if params["is_offtrack"] or params["is_crashed"]:
        return 0.0001

    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    track_direction = math.degrees(track_direction)
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    if direction_diff > 60:
        reward = 0.0001
    else:
        reward = ((2 - (direction_diff / 60)) ** 3) / 8

    return reward