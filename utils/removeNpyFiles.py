import os
import glob

# Define the path to the dataset directory
dataset_dir = '../dataset/Dataset'

# Loop over the game directories
for game_dir in glob.glob(os.path.join(dataset_dir, 'game*')):
    # Loop over the clip directories in each game directory
    for clip_dir in glob.glob(os.path.join(game_dir, 'Clip*')):
        # Loop over the .npy files in each clip directory
        for npy_file in glob.glob(os.path.join(clip_dir, '*.npy')):
            # Delete the .npy file
            os.remove(npy_file)
