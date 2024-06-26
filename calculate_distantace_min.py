import numpy as np

def calculate_distance_and_find_closest(initial_melodies, test_melodies):

    initial_melody_names = ['Dans1_audio.mp3', 'Dans2_audio.mp3', 'Dans3_audio.mp3', 'Dans4_audio.mp3', 'Dans5_audio.mp3', 'Dans6_audio.mp3', 'Dans7_audio.mp3', 'Dans8_audio.mp3', 'Dans9_audio.mp3', 'Dans10_audio.mp3']
    test_melody_names = ['test2_audio.mp3', 'test2_audio.mp3', 'test3_audio.mp3', 'test4_audio.mp3', 'test5_audio.mp3', 'test6_audio.mp3', 'test7_audio.mp3', 'test8_audio.mp3', 'test9_audio.mp3', 'test10_audio.mp3']

    def euclidean_distance(points, new_points):
        return np.sqrt((points[0] - new_points[0]) ** 2 + (points[1] - new_points[1]) ** 2)
    
    closest_melodies = []

    for test_melody in test_melodies:
        distances = [euclidean_distance(test_melody, initial_melody) for initial_melody in initial_melodies]
        closest_index = np.argmin(distances)
        closest_melodies.append(initial_melody_names[closest_index])
    
    return closest_melodies


