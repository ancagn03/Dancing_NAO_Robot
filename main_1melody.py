# -*- coding: utf-8 -*-
import numpy as np
from test_script import calculate_mfcc_zcr_test, calculate_mfcc_zcr_for_single_file
from extract_script import calculate_mfcc_zcr
from calculate_distantace_min import calculate_distance_and_find_closest
from paramiko import SSHClient
from scp import SCPClient
import os

def main():

    initial_melodies = calculate_mfcc_zcr()
    
    test_melody_path = 'test2_audio.mp3'
    test_melodies = [calculate_mfcc_zcr_for_single_file(test_melody_path)]
    closest_results = calculate_distance_and_find_closest(initial_melodies, test_melodies)
    dance = closest_results[0]
    
    print("Cea mai apropiată melodie: ", dance)

    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect("192.168.0.117", username='nao', password='nao')

    scp = SCPClient(ssh.get_transport())
    scp.put(test_melody_path, remote_path='/home/nao')
    scp.close()

    os.system('C:/Python27/python.exe robot_control.py ' + test_melody_path  +' '+ dance) 
   
if __name__ == "__main__":
    main()
