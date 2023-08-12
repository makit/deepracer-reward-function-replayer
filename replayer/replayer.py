#!/usr/bin/env python3

import argparse
import os
from analyser import analyser
from logfileparser import logfileparser
from trackloader import trackloader

LOGS_DIR = 'logs'

parser = argparse.ArgumentParser()
parser.add_argument("--log", help="The robomaker log file to parse")


def main():
    args = parser.parse_args()
    logfile = LOGS_DIR + '/' + args.log
    # Check if file exists
    if os.path.isfile(logfile):
        world_name, completed_trace_logs = logfileparser.parse_log_file(logfile)
        if world_name:
            print("Log file parsed successfully, world name: " + world_name + ", number of completed trace logs: " + str(len(completed_trace_logs)))

        center_waypoints, inside_waypoints, outside_waypoints = trackloader.load_track(world_name)

        for trace_log in completed_trace_logs:
            analyser.analyse_episode(trace_log)
    else:
        print("No valid log file supplied with logs argument")
        exit()


if __name__ == "__main__":
    main()
