# Image Selector and Converter

This project is a GUI application built using Python's [`tkinter`](command:_github.copilot.openSymbolFromReferences?%5B%22tkinter%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fumuttopalak%2Fprojects%2Fbase64-image-saver%2Fmain.py%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fumuttopalak%2Fprojects%2Fbase64-image-saver%2Fmain.py%22%2C%22path%22%3A%22%2FUsers%2Fumuttopalak%2Fprojects%2Fbase64-image-saver%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A7%7D%7D%5D%5D "Go to definition") library. It allows users to select images, convert them to Base64 format, save the Base64 data to a JSON file, and convert Base64 data back to images.

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
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
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

- [`main.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fumuttopalak%2Fprojects%2Fbase64-image-saver%2Fmain.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/umuttopalak/projects/base64-image-saver/main.py"): The main script containing the [`ImageSelectorApp`](command:_github.copilot.openSymbolFromReferences?%5B%22ImageSelectorApp%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fumuttopalak%2Fprojects%2Fbase64-image-saver%2Fmain.py%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fumuttopalak%2Fprojects%2Fbase64-image-saver%2Fmain.py%22%2C%22path%22%3A%22%2FUsers%2Fumuttopalak%2Fprojects%2Fbase64-image-saver%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A10%2C%22character%22%3A6%7D%7D%5D%5D "Go to definition") class and its methods.
- [`README.md`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fumuttopalak%2Fprojects%2Fbase64-image-saver%2FREADME.md%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/umuttopalak/projects/base64-image-saver/README.md"): This file.

## License

This project is licensed under the MIT License. See the [`LICENSE`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fumuttopalak%2Fprojects%2Fbase64-image-saver%2FLICENSE%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/Users/umuttopalak/projects/base64-image-saver/LICENSE") file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgements

- [Pillow](https://python-pillow.org/) for image processing.
- Python's [`tkinter`](command:_github.copilot.openSymbolFromReferences?%5B%22tkinter%22%2C%5B%7B%22uri%22%3A%7B%22%24mid%22%3A1%2C%22fsPath%22%3A%22%2FUsers%2Fumuttopalak%2Fprojects%2Fbase64-image-saver%2Fmain.py%22%2C%22external%22%3A%22file%3A%2F%2F%2FUsers%2Fumuttopalak%2Fprojects%2Fbase64-image-saver%2Fmain.py%22%2C%22path%22%3A%22%2FUsers%2Fumuttopalak%2Fprojects%2Fbase64-image-saver%2Fmain.py%22%2C%22scheme%22%3A%22file%22%7D%2C%22pos%22%3A%7B%22line%22%3A4%2C%22character%22%3A7%7D%7D%5D%5D "Go to definition") library for the GUI.

## Contact

For any questions or suggestions, please contact [your-email@example.com](mailto:your-email@example.com).

---

Feel free to customize this README to better fit your project's specifics and your preferences.
