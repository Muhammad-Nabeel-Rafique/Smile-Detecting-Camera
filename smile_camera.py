from __future__ import annotations

from datetime import datetime
from pathlib import Path

import cv2


def load_detector(filename: str) -> cv2.CascadeClassifier:
    cascade_path = Path(cv2.data.haarcascades) / filename
    detector = cv2.CascadeClassifier(str(cascade_path))
    if detector.empty():
        raise FileNotFoundError(f"Could not load OpenCV detector: {cascade_path}")
    return detector


def main() -> None:
    if not hasattr(cv2, "CascadeClassifier"):
        raise RuntimeError(
            "This app needs OpenCV 4. Run it with the project's environment: "
            r".\.venv\Scripts\python.exe smile_camera.py"
        )

    face_detector = load_detector("haarcascade_frontalface_default.xml")
    smile_detector = load_detector("haarcascade_smile.xml")

    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        camera.release()
        raise RuntimeError("Could not open webcam. Check that it is connected and available.")

    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    photos_dir = Path(__file__).resolve().parent / "photos"
    smile_frames = 0
    smile_latched = False

    try:
        while True:
            ok, frame = camera.read()
            if not ok:
                raise RuntimeError("Could not read a frame from the webcam.")

            photo = frame.copy()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(80, 80),
            )

            smiling = False
            for x, y, width, height in faces:
                cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 200, 0), 2)

                face_gray = gray[y : y + height, x : x + width]
                mouth_top = int(height * 0.38)
                mouth_region = face_gray[mouth_top:, :]
                smiles = smile_detector.detectMultiScale(
                    mouth_region,
                    scaleFactor=1.7,
                    minNeighbors=20,
                    minSize=(25, 25),
                )

                if len(smiles) > 0:
                    smiling = True
                    for sx, sy, sw, sh in smiles:
                        top_left = (x + sx, y + mouth_top + sy)
                        bottom_right = (top_left[0] + sw, top_left[1] + sh)
                        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 255), 2)

            if smiling:
                smile_frames += 1
                status = "Smile detected!"
            else:
                smile_frames = 0
                smile_latched = False
                status = "Waiting for a smile..."

            if smile_frames >= 4 and not smile_latched:
                photos_dir.mkdir(parents=True, exist_ok=True)
                filename = datetime.now().strftime("smile_%Y%m%d_%H%M%S_%f.jpg")
                photo_path = photos_dir / filename
                if not cv2.imwrite(str(photo_path), photo):
                    raise OSError(f"Could not save photo: {photo_path}")
                smile_latched = True
                status = f"Photo saved: {filename}"

            cv2.putText(
                frame,
                status,
                (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2,
            )
            cv2.putText(
                frame,
                "Press Q to quit",
                (20, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.65,
                (255, 255, 255),
                2,
            )
            cv2.imshow("Smile Camera", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
