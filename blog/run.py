# mypackage/run.py
from uvicorn import run

from app import app

if __name__ == "__main__":
    run(app, host="localhost", port=8000)
