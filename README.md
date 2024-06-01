## Video Summarization Project

This project is a part of my B.Tech program in Artificial Intelligence Engineering. The goal of this project is to implement a model that summarizes a video to 30-40% of its original length.

## Setup Instructions

1.Create a Virtual Environment:

```bash
python -m venv env
source env/bin/activate   # On Windows, use `env\Scripts\activate`
```

## 2.Install Dependencies:

```bash
pip install -r requirements.txt
```
If the above command does not work, you can manually install the required libraries with the specified versions:
```bash
pip install tensorflow==2.10.0
pip install numpy==1.26.4
pip install scikit-learn==1.4.2
pip install opencv-python==4.6.0
pip install flask==3.0.3
```

## Running the Application

1.Run the Application:
```bash
python app.py
```
2.Access the Application:

Open your browser and go to the provided local URL. A basic HTML interface will be displayed where you can interact with the application.
## Enjoy the Magic

The application will handle the rest, providing you with a summarized version of your video.

## License

[MIT](https://choosealicense.com/licenses/mit/)
