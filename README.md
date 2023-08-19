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