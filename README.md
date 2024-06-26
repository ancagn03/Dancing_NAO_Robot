# Dancing NAO Robot
Based on scripts that calculate specific audio parameters and a control script for the robot, NAO is capable of learning to dance to new songs. It associates each song with one of the ten available movements.

# Script Description

`extract_script.py` extracts audio parameters from audio files in the project database

`test_script.py` extracts audio parameters from a new audio file

`calculate_distance_min.py`  calculates the point determined by the audio parameters from `extract_script.py`, that is closest to the new point and returns the name of the associated dance

`robot_control.py` contains dances and associates audio files with corresponding dances

`main1_melody.py` integrates the other scripts and makes the robot dance



