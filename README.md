# Simple ChatGPT CLI

This Python script provides a simple command-line interface for interacting with the OpenAI API's `text-davinci-003` model.

## Prerequisites

* Python 3.x
* `requests` library (install with `pip install requests`)
* An OpenAI API key (create an account and get your key from [OpenAI](https://openai.com/))

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <your_repo_url>
    cd your-repo-name
    ```
2.  **Create `skChatGPT.txt`:**
    * Create a file named `skChatGPT.txt` in the same directory as `chatgpt_cli.py`.
    * Paste your OpenAI API key into this file.
3.  **Install dependencies:**
    ```bash
    pip install requests
    ```

## Usage

1.  **Run the script:**
    ```bash
    python your_script_name.py
    ```
2.  **Enter prompts:**
    * Type your prompt and press Enter.
    * The script will display the ChatGPT response with a typewriter effect.
3.  **Exit:**
    * Type "done" and press Enter to exit the program.

## Security

* The API key is read from a separate file (`skChatGPT.txt`) and is excluded from Git using `.gitignore`. **Do not commit your API key directly to the repository.**

## Note

* The model used is `text-davinci-003`.
* The `max_tokens` is set to 100, limiting the response length.
* The script adds a small delay to the response output to simulate a typewriter effect.
