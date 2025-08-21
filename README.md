# file-handling-python


A simple Python script that reads a file, converts its contents to **uppercase**, and saves the modified text into a new file.

---

## Features

* Prompts the user to input a file name.
* Reads and processes the file contents.
* Converts all text to **uppercase**.
* Saves the modified content into a new file prefixed with `modified_`.
* Handles common file errors gracefully (e.g., missing file, permission issues).

---

## How It Works

1. The program asks you to enter the name of an existing file (e.g., `data.txt`).
2. It opens and reads the file content.
3. Converts all text to uppercase.
4. Saves the modified text into a new file named `modified_data.txt`.
5. Displays a success message once completed.

---

## Requirements

* Python 3.x installed on your system.
* A text file to test with.

---

## Usage

1. Clone or download this script.
2. Open a terminal/command prompt in the script’s directory.
3. Run the script:

```bash
python file_handler.py
```

4. Enter the name of the file you want to process when prompted:

```text
Enter the name of the file: data.txt
```

5. The modified file will be saved as:

```text
modified_data.txt
```

---

## Error Handling

The script includes exception handling for common issues:

* **FileNotFoundError** → The file doesn’t exist.
* **PermissionError** → You don’t have permission to read/write the file.
* **General Exception** → Any other unexpected errors.

---

## Example

Suppose you have a file named `notes.txt` containing:

```text
Hello world!
This is a test file.
```

After running the script, you’ll get a new file: `modified_notes.txt` containing:

```text
HELLO WORLD!
THIS IS A TEST FILE.
```

Author: Maureen Chelangat.