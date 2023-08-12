import numpy as np
import os


def load_track(world_name):
    print("Loading track: " + world_name)
    track_file_name = "./tracks/" + world_name + ".npy"
    if os.path.isfile(track_file_name):
        loaded_route = np.load("./tracks/" + world_name + ".npy")
        center_waypoints = [[r[0], r[1]] for r in loaded_route]
        inside_waypoints = [[r[2], r[3]] for r in loaded_route]
        outside_waypoints = [[r[4], r[5]] for r in loaded_route]
        print("Loaded track: " + world_name + ", number of waypoints: " + str(len(center_waypoints)))
        return center_waypoints, inside_waypoints, outside_waypoints
    else:
        print("Track file not found: " + track_file_name)

    return None, None, None
