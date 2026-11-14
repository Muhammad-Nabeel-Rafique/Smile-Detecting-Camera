😄 Smile Detecting Camera

<p align="center">
  <strong>📸 Capture your smiles automatically!</strong>
</p><p align="center">
  A real-time smile detection application built with Python and OpenCV that detects human faces, recognizes smiles, and automatically captures photos when a smile is detected.
</p>---

✨ Overview

Smile Detecting Camera is a computer vision project designed to make photography more interactive and intelligent.

Using your webcam and OpenCV's Haar Cascade classifiers, the application continuously monitors your face and detects smiles in real time.

But there's a little more to it!

Instead of capturing a photo immediately after detecting a smile, the application waits until the smile is detected across multiple consecutive frames. Once the condition is satisfied, it automatically captures and saves a snapshot.

No buttons. No manual capturing. Just smile! 😁

---

🚀 Features

Feature| Description
🎯 Real-Time Face Detection| Detects human faces continuously through your webcam.
😁 Smile Recognition| Analyzes facial regions to identify smiles.
🧠 Smart Smile Verification| Requires smile detection across 4 consecutive frames before capturing.
📸 Automatic Photography| Captures and saves a snapshot automatically.
🕒 Timestamped Photos| Generates a unique filename for every captured photo.
🖥️ Live Status Display| Shows detection status directly on the camera preview.
⚡ Easy Exit| Press "Q" to close the application.

---

🛠️ Technologies Used

- Python – Main programming language.
- OpenCV – Computer vision and image processing.
- Haar Cascade Classifiers – Face and smile detection.
- Webcam – Real-time video input.

---

📂 Project Structure

Smile-Detecting-Camera/
│
├── photos/                 # Automatically saved snapshots
│
├── .gitignore              # Git ignored files
│
├── LICENSE                 # MIT License
│
├── README.md               # Project documentation
│
├── requirements.txt        # Required dependencies
│
└── smile_camera.py         # Main application

Note: The "photos/" directory is automatically created when the first snapshot is captured.

---

⚙️ Installation & Setup

Follow these steps to get the project running on your computer.

1. Clone the Repository

git clone https://github.com/Muhammad-Nabeel-Rafique/Smile-Detecting-Camera.git

2. Navigate to the Project Directory

cd Smile-Detecting-Camera

3. Create a Virtual Environment

python -m venv .venv

4. Install Dependencies

Windows (Command Prompt / PowerShell):

.\.venv\Scripts\python.exe -m pip install -r requirements.txt

Linux / macOS:

source .venv/bin/activate
pip install -r requirements.txt

---

▶️ Running the Application

Once the installation is complete, launch the application.

Windows:

.\.venv\Scripts\python.exe smile_camera.py

Linux / macOS:

python smile_camera.py

Make sure your webcam is connected and available.

---

🎮 How to Use

1. Run the Python application.
2. Allow the application to access your webcam if prompted.
3. Position your face in front of the camera.
4. Wait for the application to detect your smile.
5. Maintain your smile while the application verifies it.
6. Once verified, your snapshot will automatically be saved.
7. Press Q while the preview window is active to exit.

---

📸 Automatic Photo Storage

All captured photos are automatically stored inside the "photos/" directory.

Each image receives a unique timestamp-based filename.

Example:

photos/
│
├── smile_20261114_081000_123456.jpg
├── smile_20261114_081025_654321.jpg
└── smile_20261114_081130_987654.jpg

The application saves the original camera frame rather than the preview with detection overlays.

---

🔍 How It Works

The application follows a simple computer vision workflow:

1. Camera Initialization: Opens the default webcam and requests a 1280 × 720 resolution.
2. Frame Processing: Reads video frames continuously.
3. Face Detection: Uses the Haar Cascade face classifier to locate faces.
4. Smile Detection: Analyzes the lower facial region to identify smiles.
5. Smile Verification: Checks whether a smile remains detected across four consecutive frames.
6. Automatic Capture: Saves the image when the verification condition is satisfied.
7. Live Preview: Displays the camera feed with detection information.

---

🐛 Troubleshooting

Camera Not Opening?

- Check whether your webcam is connected.
- Close other applications currently using the camera.
- Make sure your system allows Python to access the webcam.

Missing Dependencies?

- Reinstall the required packages using "requirements.txt".
- Make sure you are running the application with the correct Python environment.

No Smile Detected?

- Ensure your face is clearly visible.
- Try improving the lighting.
- Position your face directly toward the camera.

---

🔒 Privacy

- Captured images are stored locally in the project's "photos/" directory.
- The application does not contain any cloud-upload functionality.
- Photos remain on your computer unless you manually share them.

---

📜 License

This project is open-source and distributed under the MIT License.

You are free to use, modify, and distribute this project according to the license terms.

---

👨‍💻 Author

Muhammad Nabeel Rafique

Python Developer | Computer Vision Enthusiast

- 🐙 GitHub: "Muhammad-Nabeel-Rafique" (https://github.com/Muhammad-Nabeel-Rafique)
- 📌 Project: "Smile-Detecting-Camera" (https://github.com/Muhammad-Nabeel-Rafique/Smile-Detecting-Camera)

---

<p align="center">
  <strong>Made with ❤️ using Python and OpenCV</strong>
</p><p align="center">
  ⭐ If you like this project, consider giving it a star on GitHub!
</p>
