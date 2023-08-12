# Deepracer Reward Function Replayer
TODO

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

## Run the application
```bash
python replayer/replayer.py --log deepracer-0_robomaker.1.qruf1ugxngzium4frmxj61jcu.log
```

TODO