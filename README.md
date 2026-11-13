# Smile Camera

A small webcam app that saves a photo after it detects a smile for a few frames.
The camera feed is processed locally, and photos are saved in the `photos` folder.
Smile detection is approximate and can produce false positives or miss a smile.

## Run on Windows

1. Create a virtual environment:

   ```powershell
   python -m venv .venv
   ```

2. Install the dependency and start the app using the project environment:

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   .\.venv\Scripts\python.exe smile_camera.py
   ```

Allow webcam access if Windows asks. Press **Q** in the preview window to quit.
