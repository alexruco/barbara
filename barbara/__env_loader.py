# liane/env_loader.py

from dotenv import load_dotenv
import os

# Use a global variable to ensure the .env file is loaded only once
ENV_LOADED = False

def load_env():
    global ENV_LOADED
    if not ENV_LOADED:
        dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        ENV_LOADED = True

def get_env_variable(var_name):
    load_env()
    return os.getenv(var_name)
