from flask import Flask, request, render_template, send_file
import os
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'
SUMMARIZED_FOLDER = 'summarized'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)
os.makedirs(SUMMARIZED_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        print(f"Saving uploaded file to {filepath}")
        file.save(filepath)

        # Convert video to numpy array
        numpy_path = os.path.join(PROCESSED_FOLDER, 'video.npy')
        print(f"Converting video to numpy array at {numpy_path}")
        subprocess.run(['python', 'video_conv.py', filepath, numpy_path])

        # Summarize video
        summary_numpy_path = os.path.join(SUMMARIZED_FOLDER, 'summary.npy')
        output_video_path = os.path.join(SUMMARIZED_FOLDER, 'summary.mp4')
        print(
            f"Summarizing video and saving to {summary_numpy_path} and {output_video_path}")
        subprocess.run(['python', 'summarize.py', numpy_path,
                       summary_numpy_path, output_video_path])

        # Verify the summary video file exists
        if not os.path.exists(output_video_path):
            print(f"File not found: {output_video_path}")
            return f"File not found: {output_video_path}", 500

        return send_file(output_video_path, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
