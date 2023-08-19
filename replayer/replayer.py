#!/usr/bin/env python3

import argparse
import contextlib
import os
from analyser import analyser
from logfileparser import logfileparser
from trackloader import trackloader
from rfexecutor import rfexecutor
from utils import utils

LOGS_DIR = 'logs'
OUTPUT_DIR = 'output'

parser = argparse.ArgumentParser()
parser.add_argument("--log", help="The robomaker log file to parse")


def main():
    args = parser.parse_args()
    logfile = LOGS_DIR + '/' + args.log

    # Check if file exists
    if not os.path.isfile(logfile):
        print("No valid log file supplied with logs argument")
        exit()
    
    world_name, completed_trace_logs = logfileparser.parse_log_file(logfile)
    if world_name:
        print("Log file parsed successfully, world name: " + world_name + ", number of completed trace logs: " + str(len(completed_trace_logs)))

    center_waypoints, inside_waypoints, outside_waypoints = trackloader.load_track(world_name)

    # Create the output directory, delete if it exists
    output_dir = OUTPUT_DIR + '/' + utils.make_safe_dirname(logfile)
    if os.path.exists(output_dir):
        # delete directory and all files
        for file in os.listdir(output_dir):
            os.remove(output_dir + '/' + file)
        os.rmdir(output_dir)
    os.makedirs(output_dir)

    for trace_log in completed_trace_logs:
        analysed_episode = analyser.analyse_episode(trace_log)

        # We will redirect output here and put the overall stats
        log_for_episode = output_dir + '/episode_' + str(trace_log[0]['episode']) + '.log'

        with open(log_for_episode, 'w') as f:
            with contextlib.redirect_stdout(f):
                new_rewards = rfexecutor.run_through_new_reward_function(trace_log, center_waypoints, inside_waypoints, outside_waypoints)
                print("OVERALL STATS")
                print("Time: " + str(analysed_episode['time']))
                print("Total reward: " + str(analysed_episode['total_reward']))
                print("Number of steps: " + str(analysed_episode['number_steps']))
                print("Expected number of steps: " + str(analysed_episode['expected_steps']))
                print("Total discounted reward 0.9: " + str(analysed_episode['total_discounted_reward_9']))
                print("Total discounted reward 0.99: " + str(analysed_episode['total_discounted_reward_99']))
                print("Total discounted reward 0.999: " + str(analysed_episode['total_discounted_reward_999']))

                new_reward = sum(new_rewards)
                discounted_9 = round(sum(utils.discount_rewards(new_rewards, 0.9)), 3)
                discounted_99 = round(sum(utils.discount_rewards(new_rewards, 0.99)), 3)
                discounted_999 = round(sum(utils.discount_rewards(new_rewards, 0.999)), 3)
                print("Reward Based on New Reward Function:", new_reward)
                print("Discounted Reward Based on New Reward Function 0.9:", discounted_9)
                print("Discounted Reward Based on New Reward Function 0.99:", discounted_99)
                print("Discounted Reward Based on New Reward Function 0.999:", discounted_999)

                print("Reward Difference:", new_reward - analysed_episode['total_reward'])
                print("Discounted Reward Difference 0.9:", discounted_9 - analysed_episode['total_discounted_reward_9'])
                print("Discounted Reward Difference 0.99:", discounted_99 - analysed_episode['total_discounted_reward_99'])
                print("Discounted Reward Difference 0.999:", discounted_999 - analysed_episode['total_discounted_reward_999'])

    print("")
    print("All results written to " + output_dir + "/")   

if __name__ == "__main__":
    main()
