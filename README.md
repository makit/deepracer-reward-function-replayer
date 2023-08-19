# AWS DeepRacer Reward Function Replayer
This utility will take a AWS DeepRacer RoboMaker log file and a Reward Function, and replay the completed episodes through the new reward function for comparison.

This can be useful when making changes to the Reward Function as part of balancing the rewards, as it allows seeing what the reward impact would be when compared to the existing rewards.

As it is just running the function for the reward numbers, then this is in no way a replacement for actually training and evaluating a model. With a new reward function then the model would learn in a different way, so it would drive differently. I found this utility useful for situations such as seeing that I was accidently rewarding an agent for going slower because it would gain high reward for steering that would offset speed/time. Using this utility I could tweak the function and check that this isn't the case by comparing a fast and slow episode from the log with the new and old reward function.

# Setup
## Install Python Dependencies
```bash
pip install -r requirements.txt
```
 Or use a venv:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Download the tracks
```bash
./download_tracks.sh
```

## Save your log files into the logs folder
Take the log file you wish to use and save it into the logs folder. 
This is the robolog file that has a name like:
```
deepracer-0_robomaker.1.qruf1ugxngzium4frmxj61jcu.log
```
And contains lines like:
```
SIM_TRACE_LOG:685,466,-1.3376,3.0873,-94.6072,30.00,1.30,9,0.5535,False,True,82.3476,161,76.75,7271.612,in_progress,0.00
```

## Add your reward function
Add your reward function to the `new_reward_function.py` file.

## Run the application
```bash
python replayer/replayer.py --log log_file_name.log
```

# Example Output
* The output will be in the `output` directory and a sub directory named after the input log file.
* It will contain a file for each completed episode found in the input file.
* Each file will contain the print output of the reward function and SIM_TRACE_LOG lines to mirror what robomaker does
* At the bottom of the file will be details around the old reward and new reward

```
...
Next Point:  [-2.357342481613159, -0.08637823164463043]
Track Direction:  177.2035940150002
Heading:  -178.9834
Direction Diff:  356.1869940150002
Reward:  0.9076717299590026
SIM_TRACE_LOG:63,490,-2.1543,-0.1288,-178.9834,13.0,2.5,17,0.9076717299590026,False,True,99.8275,11,76.75,1943.072,0.00

Next Point:  [-2.6585274934768677, -0.0807376503944397]
Track Direction:  178.92709228213857
Heading:  -174.9086
Direction Diff:  353.83569228213855
Reward:  0.8536731477101511
SIM_TRACE_LOG:63,491,-2.3595,-0.1548,-174.9086,13.0,2.5,17,0.8536731477101511,True,True,100.0,12,76.75,1943.124,0.00

OVERALL STATS
Time: 32.899
Total reward: 307.588
Number of steps: 491
Expected number of steps: 493
Total discounted reward 0.9: 3038.02
Total discounted reward 0.99: 24743.16
Total discounted reward 0.999: 64099.762
Reward Based on New Reward Function: 374.780
Discounted Reward Based on New Reward Function 0.9: 3674.536
Discounted Reward Based on New Reward Function 0.99: 30092.341
Discounted Reward Based on New Reward Function 0.999: 79272.305
Reward Difference: 67.192
Discounted Reward Difference 0.9: 636.516
Discounted Reward Difference 0.99: 5349.181
Discounted Reward Difference 0.999: 15172.543
```

From the above example you can see:
* The number of steps for the episode was 491, but based on the expected 15 per second it should have been 493. 
* The total reward for the episode was 307.588
* Discounted rewards on this are shown at different gamma values for demonstration purposes: 3038.02/24743.16/64099.762
* Through the new reward function then the reward would have been 374.780
* This is a difference of 67.192 higher. Discounted values shown too.
* The trace can show the differnce at each step for comparison, including any print statements within the function