#!/usr/bin/env python3

import argparse
import os
from analyser import analyser
from logfileparser import logfileparser
from trackloader import trackloader
from rfexecutor import rfexecutor
from utils import utils

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
            new_rewards = rfexecutor.run_through_new_reward_function(trace_log, center_waypoints, inside_waypoints, outside_waypoints)
            new_reward = sum(new_rewards)
            discounted_9 = round(sum(utils.discount_rewards(new_rewards, 0.9)),3)
            discounted_99 = round(sum(utils.discount_rewards(new_rewards, 0.99)),3)
            discounted_999 = round(sum(utils.discount_rewards(new_rewards, 0.999)),3)
            print("New Record:", new_reward)
            print("Discounted 0.9:", discounted_9)
            print("Discounted 0.99:", discounted_99)
            print("Discounted 0.999:", discounted_999)

    else:
        print("No valid log file supplied with logs argument")
        exit()


if __name__ == "__main__":
    main()
