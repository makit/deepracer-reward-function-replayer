#!/usr/bin/env python3

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from utils import utils


def analyse_episode(episode):
    """
    Analyse an episode and return the results
    :param episode: The episode to analyse
    :return: A dictionary containing the results of the analysis
    """
    time = round(episode[-1]['timestamp'] - episode[0]['timestamp'], 3)
    total_reward = round(sum([result['reward'] for result in episode]), 3)
    number_steps = len(episode)
    expected_steps = int(time * 15)
    rewards = rewards = [result['reward'] for result in episode]
    discounted_reward_9 = utils.discount_rewards(rewards, 0.9)
    discounted_reward_99 = utils.discount_rewards(rewards, 0.99)
    discounted_reward_999 = utils.discount_rewards(rewards, 0.999)
    total_discounted_reward_9 = round(sum(discounted_reward_9), 3)
    total_discounted_reward_99 = round(sum(discounted_reward_99), 3)
    total_discounted_reward_999 = round(sum(discounted_reward_999), 3)

    print("")
    print("EPISODE", episode[0]['episode'])
    print("Time:", time)
    print("Number of Steps:", number_steps)
    print("Expected Steps:", expected_steps)
    print("Reward:", total_reward)
    print("Discounted 0.9:", total_discounted_reward_9)
    print("Discounted 0.99:", total_discounted_reward_99)
    print("Discounted 0.999:", total_discounted_reward_999)

    return {
        'time': time,
        'total_reward': total_reward,
        'number_steps': number_steps,
        'expected_steps': expected_steps,
        'discounted_reward_9': discounted_reward_9,
        'discounted_reward_99': discounted_reward_99,
        'discounted_reward_999': discounted_reward_999,
        'total_discounted_reward_9': discounted_reward_9,
        'total_discounted_reward_99': discounted_reward_99,
        'total_discounted_reward_999': discounted_reward_999
    }