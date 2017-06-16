#!/usr/bin/env python
"""Run Atari Environment with DQN."""
import argparse
import os
import random

import numpy as np
import tensorflow as tf
from keras.layers import (Activation, Convolution2D, Dense, Flatten, Input,
                          Permute)
from keras.models import Model
from keras.optimizers import Adam

import deeprl_hw2 as tfrl

from deeprl_hw2.objectives import *
import gym
import gym_gazebo

def main():  # noqa: D103
    parser = argparse.ArgumentParser(description='Run DQN on UAV monocular images in Gazebo \m/')
    parser.add_argument('--env', default='QuadNavGym-v0', help='Atari env name')
    parser.add_argument('--mode', default='vanilla', type=str, help='vanilla or double dqn')
    parser.add_argument('--question', default='deep', type=str, help='q2, q3, q4, deep, q7, eval_table')
    parser.add_argument('--resume_dir', default=None, type=str, help='resume dir')

    args = parser.parse_args()
    print " MODE IS", args.mode

    print "resum" ,args.resume_dir
    print(args.resume_dir is None)

    if args.question=="q2":
        from deeprl_hw2.dqn_q2 import DQNAgent
    elif args.question=="q3":
        from deeprl_hw2.dqn_q3 import DQNAgent
    elif args.question=="q4":
        from deeprl_hw2.dqn_q4 import DQNAgent
    elif args.question=="q7":
        from deeprl_hw2.dqn_q7 import DQNAgent
    elif args.question=="eval_table":
        from deeprl_hw2.evaluation_table import DQNAgent
    elif args.resume_dir is not None:
        from deeprl_hw2.dqn_eval import DQNAgent
    else:
        from deeprl_hw2.dqn import DQNAgent

    video_every_nth = 50000
    eval_every_nth = 25000

    if args.env == "breakout":
        args.env = 'Breakout-v0'
        video_every_nth = 50000
    if args.env == "space_invaders":
        args.env = 'SpaceInvaders-v0'
    if args.env == 'enduro':
        args.env = 'Enduro-v0'
        video_every_nth = 50000
        eval_every_nth = 50000        

    if args.resume_dir is not None:
        agent = DQNAgent(env=args.env, gamma=0.99, target_update_freq=10000, num_burn_in=25000, train_freq=4, batch_size=32, mode=args.mode, resume_dir=args.resume_dir)
    else:
        raise ValueError()

    agent.evaluate(num_episodes=100, max_episode_length=1000, gen_video=False)

if __name__ == '__main__':
    main()
