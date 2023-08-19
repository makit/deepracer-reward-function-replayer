#!/usr/bin/env python3

import numpy as np
import string


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


def make_safe_dirname(s):
    """
    Make a string safe to use as a directory name
    :param s: The string to make safe
    :return: The safe string
    """
    safe_chars = set(string.ascii_letters + string.digits + '_- ')
    safe_name = ''.join(c if c in safe_chars else '_' for c in s)
    return safe_name.strip().replace(' ', '_')