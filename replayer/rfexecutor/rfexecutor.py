#!/usr/bin/env python3

import math
import new_reward_function as rf


def run_through_new_reward_function(episode, center_waypoints, inside_waypoints, outside_waypoints):
    waypoints = center_waypoints
    track_width = get_distance(inside_waypoints[0], outside_waypoints[0])
    rewards = []
    for trace in episode:
        closest_waypoints = [trace['closest_waypoint'],trace['closest_waypoint']]
        if trace['closest_waypoint'] == len(waypoints)-1:
            closest_waypoints[1] = 1
        else:
            closest_waypoints[1] = trace['closest_waypoint']+1

        params = {
            "all_wheels_on_track": trace['all_wheels_on_track'],
            "x": trace['x'],
            "y": trace['y'],
            "closest_objects": [],
            "closest_waypoints": closest_waypoints,
            "distance_from_center": 10, #TODO: calculate distance from center
            "is_crashed": False,
            "is_left_of_center": False, # TODO: calulate if left of center
            "is_offtrack": False,
            "is_reversed": trace['is_reversed'],
            "heading": trace['heading'],
            "objects_distance": [],
            "objects_heading": [],
            "objects_left_of_center": [],
            "objects_location": [],
            "objects_speed": [],
            "progress": trace['progress'],
            "speed": trace['speed'],
            "steering_angle": trace['steering_angle'],
            "steps": trace['step'],
            "track_length": trace['track_length'],
            "track_width": track_width,
            "waypoints": waypoints,
        }
        reward = rf.reward_function(params)
        rewards.append(reward)
        print(f"SIM_TRACE_LOG:{trace['episode']},{trace['step']},{trace['x']},{trace['y']},{trace['heading']},{trace['steering_angle']},{trace['speed']},{trace['decision']},{reward},{trace['is_reversed']},{trace['all_wheels_on_track']},{trace['progress']},{trace['closest_waypoint']},{trace['track_length']},{trace['timestamp']},{trace['state']}")
        print("")

    return rewards

def get_distance(coordinate1, coordinate2):
    '''Get distance between two points'''
    return math.sqrt(
        (coordinate1[0] - coordinate2[0]) *
        (coordinate1[0] - coordinate2[0]) +
        (coordinate1[1] - coordinate2[1]) *
        (coordinate1[1] - coordinate2[1]))