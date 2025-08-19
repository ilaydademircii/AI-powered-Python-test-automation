# AI-powered Python Test Automation

This project provides an AI-powered system for automating Python software tests. It generates test code for selected Python files, runs the tests, and displays the results through a GUI. The project uses **PySimpleGUI** for the interface, **OpenAI API** for test generation, and **subprocess** for running the tests.

## Features

* **File Handling:** Reads the selected file, writes and saves the generated test code.
* **AI-powered Test Generation:** Generates test code using OpenAI API based on the file content.
* **GUI Interface:** User-friendly interface built with PySimpleGUI.
* **Test Execution:** Runs the generated test code and displays the output.
* **Reporting:** Shows test output and any error messages to the user.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ilaydademircii/AI-powered-Python-test-automation.git
cd AI-powered-Python-test-automation
```

2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key:

```bash
export OPENAI_API_KEY='your-api-key'
```

4. Run the application:

```bash
python main.py
```

## Usage

* Click **“Generate Test”** to create test code for the selected file.
* Click **“Run Test”** to execute the generated test code and see the results in the GUI.
* Test outputs and error messages appear in the Multiline output field.

## License

This project is licensed under the MIT License.

