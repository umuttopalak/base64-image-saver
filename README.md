# Image Selector and Converter

This project is a GUI application built using Python's `tkinter` library. It allows users to select images, convert them to Base64 format, save the Base64 data to a JSON file, and convert Base64 data back to images.

## Features

- **Select Images**: Choose multiple images from your file system.
- **Display Images**: Display selected images in a scrollable view.
- **Convert to Base64**: Convert selected images to Base64 format.
- **Save Base64 Data**: Save the Base64 data of images to a JSON file.
- **Convert to Image**: Convert Base64 data from a JSON file back to images and save them.

## Requirements

- Python 3.x
- `Pillow` library for image processing

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/umuttopalak/base64-image-saver.git
    cd base64-image-saver
    ```

2. **Install the required libraries**:
    ```sh
    pip install pillow
    ```

## Usage

1. **Run the application**:
    ```sh
    python main.py
    ```

2. **Select Images**:
    - Click the "Select Images" button to open a file dialog and choose images.

3. **Convert to Base64**:
    - After selecting images, click the "Convert To Base64" button to convert the images to Base64 format.

4. **Save Base64 Data**:
    - Click the "Save File" button to save the Base64 data to a JSON file.

5. **Convert to Image**:
    - Click the "Convert To Image" button to select a JSON file containing Base64 data and convert it back to images.

## Project Structure

- `main.py` class and its methods.
- `README.md` This file.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [Pillow](https://python-pillow.org/) for image processing.
- Python's `tkinter` library for the GUI.

## Contact

For any questions or suggestions, please contact [umuttopalak@hotmail.com](mailto:umuttopalak@hotmail.com).

---

Feel free to customize this README to better fit your project's specifics and your preferences.
