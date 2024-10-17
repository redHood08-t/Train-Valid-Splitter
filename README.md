## Installation
To get started, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/redHood08-t/Train-Valid-Splitter.git
    cd Train-Valid-Splitter
    ```

2. **Install required dependencies** using `pip`:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To split your dataset into `train` and `val` directories, use the following command:

```bash
python train_valid_split.py -id <input_directory> -od <output_directory> -vr <validation_ratio>


## Features
- **Train/Validation Split**: Automatically splits your dataset into `train` and `val` sets based on the specified ratio.
- **YOLO Format Support**: Handles datasets in YOLO format, including both `.jpg` images and `.txt` annotations.
- **Customizable Validation Ratio**: You can specify any validation ratio (e.g., 0.2 for 20% validation).
- **Automatic Directory Creation**: Automatically creates `train` and `val` directories in the output folder.
- **Progress Indicator**: Uses `tqdm` to show progress bars for both training and validation splits.

## Contributing
Contributions are welcome! If you'd like to help improve this project:

1. Fork the repository.
2. Create a new branch for your changes:
    ```bash
    git checkout -b feature-branch
    ```
3. Commit your changes and push them to your forked repository:
    ```bash
    git push origin feature-branch
    ```
4. Submit a pull request with a detailed description of your changes.

Please make sure to follow coding standards and include clear commit messages.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more information.
