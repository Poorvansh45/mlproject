## This module provides logging functionality for the project
## It sets up a logger that can be used across different modules
## The logger writes logs to a file and also outputs them to the console
## It includes different log levels such as INFO, DEBUG, WARNING, and ERROR
## The log format includes timestamps, log levels, and messages
## This helps in tracking the flow of execution and debugging issues
## for example, logging data loading steps, model training progress, and evaluation results

import logging
import os
from datetime import datetime

# Generate log filename
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Folder where logs will be stored
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)  # ✅ create only the folder

# Complete log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")
