import os

from dotenv import load_dotenv

load_dotenv()

SERVER = os.getenv("SERVER", "http://localhost:6479/")
"""
The URL of the Magritte server to connect to.
"""
