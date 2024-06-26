import librosa
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import pandas as pd

def calculate_mfcc_zcr():
    extract_audio = []

    audio_paths = ['Dans1_audio.mp3', 'Dans2_audio.mp3', 'Dans3_audio.mp3', 'Dans4_audio.mp3', 'Dans5_audio.mp3', 'Dans6_audio.mp3', 'Dans7_audio.mp3', 'Dans8_audio.mp3', 'Dans9_audio.mp3', 'Dans10_audio.mp3']

    frame_size = 2048
    hop_length = 512
    window_type = 'hamming'

    third_mfcc_means = []
    zcr_means = []

    for i, audio_path in enumerate(audio_paths):    
        x, sr = librosa.load(audio_path, sr=None)
        window = np.hamming(frame_size)
        frames = librosa.util.frame(x, frame_length=frame_size, hop_length=hop_length)
        windowed_frames = frames * window[:, np.newaxis]
        
        mfccs = librosa.feature.mfcc(y=x, sr=sr, n_mfcc=13, n_fft=frame_size, hop_length=hop_length, window=window)
        third_mfcc = mfccs[2, :]  
        mean_third_mfcc = np.mean(third_mfcc)  
        third_mfcc_means.append(mean_third_mfcc) 
        
        zcr = librosa.feature.zero_crossing_rate(x)
        mean_zcr = np.mean(zcr)
        zcr_means.append(mean_zcr)
       
        extract_audio.append((mean_zcr, mean_third_mfcc))
    
    return extract_audio

extract_audio_results = calculate_mfcc_zcr()
print("Perechile de valori ZCR si MFCC", extract_audio_results)