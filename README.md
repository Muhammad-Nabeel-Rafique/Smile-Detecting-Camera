# Smile-Detecting-Camera

A real-time webcam application built with Python and OpenCV that detects smiles using facial feature cascades and automatically saves high-resolution snapshots.

---

## 🚀 Features

* **Real-Time Detection:** Tracks faces and analyzes mouth regions simultaneously using OpenCV Haar Cascades.
* **Smart Persistence Check:** Requires a smile to be sustained for multiple consecutive frames to avoid false triggers.
* **Automatic Snapshot Capture:** Saves timestamped `.jpg` photos directly into a local `photos/` folder with high-precision timestamps.
* **On-Screen Status HUD:** Displays live tracking status and exit instructions directly on the video feed.

---

## 🛠️ Prerequisites & Installation

1. **Clone the Repository:**

```bash
git clone [https://github.com/Muhammad-Nabeel-Rafique/Smile-Detecting-Camera.git](https://github.com/Muhammad-Nabeel-Rafique/Smile-Detecting-Camera.git)
cd Smile-Detecting-Camera
```

2. **Create a Virtual Environment:**

```bash
python -m venv .venv
```

3. **Install Dependencies (Windows Command Prompt / PowerShell):**

```bash
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

---

## 💻 Running the Application

Launch the script using your project's virtual environment Python executable:

```bash
.\.venv\Scripts\python.exe smile_camera.py
```

* **Controls:** Press **`Q`** on your keyboard while the preview window is active to quit.

---

## 📂 Project Structure

```text
Smile-Detecting-Camera/
│
├── photos/             # Automatically generated folder containing captured smile snapshots
├── .gitignore          # Git exclusion rules (ignores virtual environment & caches)
├── LICENSE             # MIT License
├── README.md           # Project documentation
├── requirements.txt    # Project dependencies
└── smile_camera.py     # Main application script
```

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
