import numpy as np
from tensorflow.keras.models import load_model
import cv2

# Load the saved autoencoder model
m1 = load_model("model")


def summarize_video(numpy_path, summary_numpy_path, output_video_path):
    print(f"Loading video frames from {numpy_path}")
    # Load the video frames from the numpy array
    video_array = np.load(numpy_path)
    print("Video frames loaded successfully")

    # Perform reconstruction using the autoencoder
    reconstructed_video = m1.predict(video_array)
    print("Video reconstructed successfully")

    # Calculate reconstruction errors
    reconstruction_errors = np.mean(
        np.square(video_array - reconstructed_video), axis=(1, 2, 3))
    print("Reconstruction errors calculated")

    # Select top frames with high reconstruction errors for summarization
    # Top 30% in reconstruction error
    threshold = np.percentile(reconstruction_errors, 70)
    distinct_frame_indices = np.where(reconstruction_errors >= threshold)[0]
    print(
        f"Selected frame indices for summarization: {distinct_frame_indices}")

    summarized_frames = video_array[distinct_frame_indices]
    print(f"Summarized frames selected: {summarized_frames.shape}")

    # Save the summarized video frames as a NumPy array file
    np.save(summary_numpy_path, summarized_frames)
    print(f"Summarized video saved to {summary_numpy_path}")

    # Save summarized video in MP4 format
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # MP4 codec
    out = cv2.VideoWriter(output_video_path, fourcc,
                          30.0, (128, 128), isColor=True)

    for frame in summarized_frames:
        # Convert from float32 to uint8 for OpenCV
        frame_uint8 = (frame * 255).astype(np.uint8)
        out.write(frame_uint8)

    out.release()  # Finalize the video
    print(f"Summarized video saved as MP4 to {output_video_path}")


if __name__ == '__main__':
    import sys
    numpy_path = sys.argv[1]
    summary_numpy_path = sys.argv[2]
    output_video_path = sys.argv[3]
    summarize_video(numpy_path, summary_numpy_path, output_video_path)
