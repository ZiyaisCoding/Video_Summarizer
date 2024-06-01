import cv2
import numpy as np


def video_conv(video_path, output_path):
    cap = cv2.VideoCapture(video_path)

    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Resize the frame
        resized_frame = cv2.resize(frame, (128, 128))
        # Normalize the frame to be between 0 and 1
        normalized_frame = resized_frame / 255.0
        # Append the frame to the list
        frames.append(normalized_frame)

    cap.release()

    # Convert list of frames to a NumPy array
    video_array = np.array(frames)

    # Save the processed video frames as a NumPy array file
    np.save(output_path, video_array)


if __name__ == '__main__':
    import sys
    video_path = sys.argv[1]
    output_path = sys.argv[2]
    video_conv(video_path, output_path)
