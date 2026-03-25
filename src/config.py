import os

from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Universal Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_DIR = os.path.join(BASE_DIR, "input")

# Create input folder if it doesn't exist
if not os.path.exists(INPUT_DIR):
    os.makedirs(INPUT_DIR)
