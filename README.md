# SVG Gradient Converter

## Description
SVG Gradient Converter is a Python-based tool that replaces solid color fills in SVG files with gradient fills. It processes multiple SVG files from a source directory and saves the modified files to a destination directory.

## Features
- Converts solid color fills in SVG files to linear gradients.
- Supports batch processing of SVG files in a directory.
- Simple command-line interface for easy usage.
- Allows users to specify gradient start and end colors.

## Installation
Ensure you have Python installed on your system. Then, clone this repository and install dependencies (if needed).

```sh
# Clone the repository
git clone https://github.com/NSTechBytes/SVG-Gradient-Converter.git
cd SVG-Gradient-Converter
```

## Usage
You can run the script using the command line:

```sh
python SVG-Gradient-Converter.py <source_folder> <destination_folder> <color1> <color2>
```

### Example
```sh
python SVG-Gradient-Converter.py ./input ./output #FF0000 #0000FF
```
This converts all SVG files in the `input` folder and saves the output with a red-to-blue gradient in the `output` folder.

## Alternative Usage
If no arguments are provided, the script will prompt you for inputs:

```sh
python SVG-Gradient-Converter.py
```

You will be asked to enter:
- Source folder path
- Destination folder path
- Start gradient color (e.g., `#FF0000`)
- End gradient color (e.g., `#0000FF`)

## How It Works
1. The script parses each SVG file in the source directory.
2. It creates a linear gradient definition with user-specified colors.
3. It replaces all solid fill colors in the SVG with the generated gradient.
4. The modified SVG files are saved to the destination folder.

## Dependencies
- Python 3.x
- `xml.etree.ElementTree` (built-in Python module)

## License
This project is licensed under the MIT License.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Author
Developed by [Nasir Shahbaz](https://github.com/NSTechBytes).

