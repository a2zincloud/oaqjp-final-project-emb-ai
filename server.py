from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = imotion_detector(text_to_analyze)
    result = format_emotion_response(response)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

def format_emotion_response(emotion_response):
    emotions = [f"'{key}': {value}" for key, value in emotion_response.items() if key != 'dominant_emotion']
    emotions_str = ', '.join(emotions)
    dominant_emotion = emotion_response['dominant_emotion']
    result_str = f"For the given statement, the system response is {emotions_str}. The dominant emotion is {dominant_emotion}."
    return result_str
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)