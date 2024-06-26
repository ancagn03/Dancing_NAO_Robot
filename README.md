# Dancing NAO Robot
Based on scripts that calculate specific audio parameters and a control script for the robot, NAO is capable of learning to dance to new songs. It associates each song with one of the ten available movements.

# Script Description

`extract_script.py` extracts audio parameters from audio files from project database

`test_script.py` extracts audio parameters from a new audio file

`calculate_distance_min.py` calculates from what point determinated by the audio parameters from `extract_script.py` the new point from is the closest and returns the name of the dance 

`robot_control.py` contains dances and associates audio files with dances

`main1_melody.py` integrates the other scripts and makes the robot to dance



