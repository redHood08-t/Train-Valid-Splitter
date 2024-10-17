import argparse
import glob
from pathlib import Path
import random
import shutil
from tqdm import tqdm

def train_test_valid(in_dir, valid_ratio, out_dir):
    """
    Splits a dataset into training and validation sets.

    Args:
        in_dir (str): The input directory containing images and corresponding YOLO annotation files.
        valid_ratio (float): The ratio of the dataset to use for validation.
        out_dir (str): The output directory where train/val folders will be created.
    """
    # Find all image files in the input directory
    images_path = glob.glob(f'{in_dir}/*.jpg')
    
    # Determine the number of validation samples
    valid_count = int(round(valid_ratio * len(images_path), 0))
    
    # Shuffle the images to randomize the train/validation split
    random.shuffle(images_path)

    # Create the output directories
    if valid_count > 0:
        Path(f'{out_dir}/val').mkdir(exist_ok=True, parents=True)
    Path(f'{out_dir}/train').mkdir(exist_ok=True, parents=True)

    # Copy files to the validation folder
    for _ in tqdm(range(valid_count), desc="Processing validation data"):
        image_path = images_path.pop()
        text_path = f'{in_dir}/{Path(image_path).stem}.txt'
        shutil.copy(image_path, f'{out_dir}/val')
        shutil.copy(text_path, f'{out_dir}/val')

    # Copy remaining files to the training folder
    for _ in tqdm(range(len(images_path)), desc="Processing training data"):
        image_path = images_path.pop()
        text_path = f'{in_dir}/{Path(image_path).stem}.txt'
        shutil.copy(image_path, f'{out_dir}/train')
        shutil.copy(text_path, f'{out_dir}/train')


if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Split dataset into training and validation sets')
    
    parser.add_argument('-id', '--in_dir', required=True, help='Input directory containing images and YOLO annotation files')
    parser.add_argument('-od', '--out_dir', required=True, help='Output directory to save train/val split')
    parser.add_argument('-vr', '--valid_ratio', type=float, required=True, help='Ratio of data to use for validation')

    # Parse the arguments
    args = parser.parse_args()

    # Perform the train/validation split
    train_test_valid(args.in_dir, args.valid_ratio, args.out_dir)
