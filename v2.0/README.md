# Keyring Tools

![Version](https://img.shields.io/badge/version-v2.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

**Keyring Tools** is a cross-platform password management tool that uses the system keyring to securely store, retrieve, and delete passwords. It provides both a graphical user interface (GUI) and a command-line interface (CLI) for managing passwords.

---

## Features

- **Password Management**:
  - Set, get, and delete passwords securely using the system keyring.
- **Bulk Operations**:
  - Process multiple password operations via a CSV file.
- **Clipboard Integration**:
  - Copy retrieved passwords to the clipboard with a single click.
- **Cross-Platform**:
  - Works on Windows, macOS, and Linux.
- **User-Friendly GUI**:
  - Intuitive interface for managing passwords.
- **CLI Support**:
  - Perform operations directly from the command line.

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/cdwlabs/Mid-America-EN-Sandbox.git
    cd keyring_tools
    ```

    or

    ```bash
    git clone https://github.com/RacerJay/keyring-tools.git
    cd keyring_tools
    ```

2. Install dependencies:

    Ensure you have Python 3 installed, then run:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:

- For GUI mode:

    ```bash
    python keyring_tools.py
    ```

- For CLI mode:

    ```bash
    python keyring_tools.py [set|get|del] [args]
    ```

---

## Usage

### GUI Mode

- Launch the application.
- Select the desired function: **Set**, **Get**, or **Delete**.
- Enter the **System Name**, **Username**, and (if applicable) **Password**.
- Click **Go** to execute the operation.
- Use the **Process Bulk CSV** button to perform multiple operations from a CSV file.

### CLI Mode

#### Set Password

```bash
python keyring_tools.py set <system> <username> <password>
```

#### Get Password

```bash
python keyring_tools.py get <system> <username>
```

#### Delete Password

```bash
python keyring_tools.py del <system> <username>
```

#### Bulk CSV Processing

```bash
python keyring_tools.py --bulk <path_to_csv_file>
```

---

## CSV Format for Bulk Processing

The CSV file should have the following columns:

- `function`: The operation to perform (`set`, `get`, or `del`).
- `system`: The system/service name.
- `username`: The username for the service.
- `password`: The password to store (required for `set` operations).

Example CSV:

```csv
function,system,username,password
set,example_system,user1,password123
get,example_system,user1,
del,example_system,user1,
```

---

## Changelog

- `v2.0 (04-17-2025)` - v2.0 Initial Release
  - `Added:` Added comprehensive docstrings, added type hints throughout the code for improved organization and enhanced maintainability.
  - `Added:` Dark mode skin.
  - `Changed:` Consolidated bulk processing.
  - `Fixed:` Bug in GUI 'set' operation where passwords were getting saved as blank passwords.
  - `Changed:` Cleaned up constants and variables (PEP 8).
  - `Added:` Reveal toggle for password.
  - `Added:` Copy to clipboard clears after 30s and on Quit.
  - `Added:` Input fields now have character limits.
- `v1.0 (04-22-2023)` - v1.0 Initial Release

---

## Limitations

- Input fields have character limits
  - **System Name**: ≤254 characters
  - **Username**: ≤32 characters
  - **Password**: ≤400 characters
- All input fields will be striped of leading and trailing blank space unless surrounded by quotation marks.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Contributing & Support

Contributions are welcome! For questions or issues, please open an issue or submit a pull request on the GitHub repository [cdwlabs's Mid-America-EN-Sandbox](https://github.com/cdwlabs/Mid-America-EN-Sandbox), or [RacerJay's keyring_tools](https://github.com/RacerJay/keyring-tools), or contact the author at <jason.thomaschefsky@cdw.com>.

---

## Acknowledgments

- [**PySide6**](https://pypi.org/project/PySide6/): For the GUI framework.
- [**Keyring**](https://pypi.org/project/keyring/): For secure credential storage.
- [**Pyperclip**](https://pypi.org/project/pyperclip/): For clipboard functions.
- > Our new A.I. Overlords
  - [**DeepSeek**](https://www.deepseek.com/): For generating 95%+ of this script's code.
  - [**Perplexity's Claude**](https://claude.ai/) & [**ChatGTP**](https://chatgpt.com/): For trying their best.
