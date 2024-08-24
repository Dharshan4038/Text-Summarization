import os
from pathlib import Path
import logging

# Set up logging for the project
logging.basicConfig(level=logging.INFO, format='[%(levelname)s]:%(message)s:')

project_name = "textSummarizer"


# List of files and directories for the project
list_of_files = [
    ".github.com/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

# Create directories and files for the project
for filepath in list_of_files:
    file_path = Path(filepath)
    filedir, filename = os.path.split(file_path)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Created empty file: {filepath}")

    else:
        logging.info(f"File {filepath} already exists.")
