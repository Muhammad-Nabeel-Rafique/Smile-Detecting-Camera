# 😄 Smile Detecting Camera

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)
![GitHub Stars](https://img.shields.io/github/stars/Muhammad-Nabeel-Rafique/Smile-Detecting-Camera?style=flat&logo=github)

<p align="center">
  <strong>📸 Your Smile. Your Camera. Automatic Photography.</strong>
</p>

<p align="center">
  A real-time smile detection application built using Python and OpenCV.
  Detect smiles, capture moments, and save photos automatically!
</p>

---

## 🌟 About The Project

Ever wished your camera could automatically capture a photo whenever you smile?

**Smile Detecting Camera** makes that possible!

This project uses computer vision and OpenCV's Haar Cascade classifiers to detect human faces and recognize smiles through a webcam.

Unlike traditional camera applications, it doesn't require you to press a button to take a picture. Simply smile at the camera, maintain your smile for a few consecutive frames, and the application automatically captures and saves your photo.

**Just Smile. Let the Camera Do the Rest!** 😁

---

## 🚀 Features

- 🎯 **Real-Time Face Detection** – Detects human faces continuously using your webcam.
- 😁 **Smile Recognition** – Analyzes facial regions to identify smiles.
- 🧠 **Smart Smile Verification** – Requires a smile to be detected across 4 consecutive frames.
- 📸 **Automatic Photo Capture** – Takes a snapshot automatically when a smile is verified.
- 🕒 **Timestamped Filenames** – Gives every captured photo a unique filename.
- 🖥️ **Live Camera Preview** – Displays face detection, smile detection, and application status.
- 💾 **Automatic Photo Storage** – Saves captured images inside a local `photos/` directory.
- ⚡ **Easy Exit** – Press `Q` to close the application.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Computer vision and image processing |
| Haar Cascade | Face and smile detection |
| Webcam | Real-time video input |

---

## 📂 Project Structure

```text
Smile-Detecting-Camera/
│
├── photos/                 # Automatically saved snapshots
│
├── .gitignore              # Git ignore configuration
├── LICENSE                 # MIT License
├── README.md               # Project documentation
├── requirements.txt        # Project dependencies
└── smile_camera.py         # Main application

Note: The "photos/" directory is automatically created when the first photo is captured.
```

---

⚙️ Installation & Setup

Follow these steps to install and run the project.

1. Clone the Repository
```
git clone https://github.com/Muhammad-Nabeel-Rafique/Smile-Detecting-Camera.git
```

2. Navigate to the Project Directory
```
cd Smile-Detecting-Camera
```
3. Create a Virtual Environment
```
python -m venv .venv
```
4. Install Dependencies

Windows (Command Prompt / PowerShell):
```
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```
Linux / macOS:
```
source .venv/bin/activate
pip install -r requirements.txt
```
---

▶️ Running the Application

After installing the dependencies, launch the application.

Windows:
```
.\.venv\Scripts\python.exe smile_camera.py
```
Linux / macOS:
```
python smile_camera.py
```
Make sure your webcam is connected and available.

---

🎮 How to Use

1. Launch the application.
2. Allow webcam access if requested by your operating system.
3. Position your face in front of the camera.
4. Wait for the application to detect your smile.
5. Maintain your smile while the application verifies it.
6. Once verified, your photo will automatically be captured.
7. Press Q while the camera window is active to exit.

---

## 📸 Automatic Photo Storage

All captured photographs are automatically saved inside the `photos/` directory.

Each photograph receives a unique timestamp-based filename, making it easy to organize and identify captured moments.

**Example Folder Structure:**

```text
photos/
│
├── smile_20261114_081000_123456.jpg
├── smile_20261114_081025_654321.jpg
└── smile_20261114_081130_987654.jpg
```
Image Format: JPG

Storage: Local project directory

The application saves the original camera frame without the detection rectangles and text displayed in the live preview.

---

🔍 How It Works

The application follows a simple computer vision workflow:

1. Camera Initialization: Opens the default webcam and requests a resolution of 1280 × 720.
2. Frame Processing: Continuously reads frames from the webcam.
3. Face Detection: Uses the Haar Cascade face classifier to locate faces.
4. Smile Detection: Analyzes the lower facial region to identify smiles.
5. Smile Verification: Checks whether a smile is detected across four consecutive frames.
6. Automatic Capture: Saves a photograph when the verification condition is satisfied.
7. Live Display: Shows the camera feed with detection information and application status.

---

🐛 Troubleshooting

Camera Not Opening?

- Make sure your webcam is connected.
- Close other applications that might be using the camera.
- Check your operating system's camera permissions.

Missing Dependencies?

- Make sure the virtual environment is activated or use its Python executable.
- Install the required packages again using "requirements.txt".

No Smile Detected?

- Make sure your face is clearly visible.
- Try improving the lighting.
- Face the camera directly.

---

🔒 Privacy

- All captured photographs are stored locally on your computer.
- The application does not include cloud-upload functionality.
- Your photographs are not automatically shared with external services.

---

📜 License

This project is distributed under the [MIT License](LICENSE).

You are free to use, modify, and distribute this project according to the license terms.

---

👨‍💻 Author

Muhammad Nabeel Rafique

- 🐙 GitHub: "Muhammad-Nabeel-Rafique" (https://github.com/Muhammad-Nabeel-Rafique)
- 🚀 Repository: "Smile Detecting Camera" (https://github.com/Muhammad-Nabeel-Rafique/Smile-Detecting-Camera)

---

<p align="center">
  ⭐ If you like this project, consider giving it a star!
</p><p align="center">
  Made using Python and OpenCV
</p>
