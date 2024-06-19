# python--Display-Icons-Program
This Python program allows users to select and display icons fetched from the GitHub Emojis API.

## Project Overview

The application fetches a list of icon names from the GitHub Emojis API and provides the following functionalities:

- **Fetch Icons**: Fetches a list of icon names from the GitHub Emojis API.
- **Display Options**:
  - Option 1: Print all icons.
  - Option 2: Search icons by keyword.

## Steps to Run the Program

### 1. Setup Virtual Environment

First, create a virtual environment to isolate dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies

Install the required libraries using the provided requirements file:

```bash
pip install -r requirements.txt
```

### 3. Run the Program

Execute the main program `display_icons.py`:

```bash
python display_icons.py
```

## Program Features

- **Option 1: Print all icons**
  - Calls `print_all_icons()` function to display all available icon names.
  
- **Option 2: Search icons by keyword**
  - Calls `search_icons_by_keyword()` function to filter icons based on user-entered keyword.
  - Case-insensitive search that matches icons regardless of case.
  - Notifies the user if no icons match the keyword.

- **Choose an Icon**
  - After selecting an option, the user can choose an icon from the displayed list.
  - Calls `display_icon(icon_name)` function to display the selected icon using PIL library.

## Error Handling

- Handles potential errors during API requests using `requests` library.
- Exception handling for opening and displaying images from URLs using PIL.

## Requirements

- Python 3.x
- requests library (for API requests)
- PIL (Pillow) library (for image display)

## Example Usage

Upon running the program, users will be prompted to select an option (1 or 2). After choosing an option, they can further select an icon to display.

## Additional Resources

Learn more about how to open an image from a URL in Python using PIL:
- [How to Open an Image from URL in PIL](https://www.geeksforgeeks.org/how-to-open-an-image-from-the-url-in-pil/)
