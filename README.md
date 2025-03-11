# PDF Import Starter

Welcome to the pdf-import-starter project! This repository provides starter code for importing and processing PDF files. This README will guide you through setting up the project on your machine using Poetry for dependency management.

## Prerequisites

Before you begin, ensure you have the following installed:

-    Git: To clone this repository.
-    Python 3.13.2: Managed via pyenv (we’ll install this below).
-    Poetry: For dependency management and virtual environments.

### Setup Instructions

Follow these steps to get the project up and running.

1. Clone the Repository
   Clone this repository to your local machine:

git clone https://github.com/upskill-pro-admin/pdf-import-starter.git
cd pdf-import-starter

2. Install pyenv
   pyenv lets you manage multiple Python versions. Install it based on your operating system:

-    macOS (using Homebrew)

`brew install pyenv`

-    Linux

`curl https://pyenv.run | bash`

-    Windows (using pyenv-win)
     Follow the pyenv-win installation guide.

After installation, add pyenv to your shell:

macOS/Linux: Edit ~/.zshrc or ~/.bashrc:

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"

Reload your shell:

source ~/.zshrc # or ~/.bashrc

Windows: Use PowerShell to set up PATH (see pyenv-win docs).
Verify installation:

pyenv --version 3. Install Python 3.13.2
Install the required Python version:

pyenv install 3.13.2
Set it as the local version for this project:

pyenv local 3.13.2
Verify:

python --version # Should show Python 3.13.2

4. Install Poetry
   Install Poetry globally:

curl -sSL https://install.python-poetry.org | python3 -
Add Poetry to your PATH (if not automatic):

macOS/Linux: Edit ~/.zshrc or ~/.bashrc:

export PATH="$HOME/.local/bin:$PATH"
Reload shell:

source ~/.zshrc # or ~/.bashrc

Windows: Ensure %USERPROFILE%\.local\bin is in your PATH.
Verify:

poetry --version

5. Set Up the Poetry Environment
   Initialize the Poetry virtual environment with Python 3.13.2:

poetry env use $(pyenv which python)
Install dependencies:

poetry install
This installs runtime dependencies and development tools like behave and black.

6. Activate the Virtual Environment
   Start a shell within the Poetry environment:

poetry shell
Verify Python version inside the shell:

python --version # Should show Python 3.13.2
To exit the shell:

exit

7. Configure Your IDE (Optional)
   If you’re using an IDE like VS Code, set the Python interpreter to the Poetry virtual environment.

VS Code
Open the project in VS Code:

code .
Open the Command Palette (Cmd + Shift + P or Ctrl + Shift + P).
Type and select: Python: Select Interpreter.
Choose the Poetry environment:
Run poetry env info in your terminal to find the path (e.g., ~/.cache/pypoetry/virtualenvs/pdf-import-starter-XXXXXX/bin/python).
Select that path in VS Code.
Verify:
Open a terminal in VS Code (Terminal > New Terminal).
Run python --version; it should show 3.13.2. 8. Run the Project
With the environment set up, you can now use the project. For example:

Run tests with behave (if applicable):

behave
Format code with black:

black .
Lint with ruff:

ruff check .
Troubleshooting
Poetry complains about Python version:
Ensure python --version shows 3.13.2 before running Poetry commands.
Recreate the environment:

poetry env remove python
poetry env use $(pyenv which python)
poetry install
Commands not found:
Verify pyenv and poetry are in your PATH (see steps 2 and 4).

## Contributing

Feel free to submit issues or pull requests to improve this starter project!
