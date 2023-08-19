#!/usr/bin/env python3

import numpy as np


def discount_rewards(rewards, gamma):
    """
    Compute the discounted rewards for a list of rewards
    :param rewards: The list of rewards
    :param gamma: The discount factor
    :return: The discounted rewards
    """
    discounted_rewards = np.zeros_like(rewards, dtype=float)
    r = 0
    for t in reversed(range(0, len(rewards))):
        r = rewards[t] + gamma * r
        discounted_rewards[t] = r
    return discounted_rewards
