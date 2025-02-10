''' Executing this function initiates the application of emotion
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    result = format_emotion_response(response)
    return result

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

def format_emotion_response(emotion_response):
    """
    Formats the emotion detection response into a human-readable string.

    Args:
        emotion_response (dict): A dictionary containing emotion scores and the dominant emotion.
            Expected keys: 'anger', 'disgust', 'fear', 'joy', 'sadness', and 'dominant_emotion'.

    Returns:
        str: A formatted string describing the emotion analysis result.
    """
    emotions = [
        f"'{key}': {value}"
        for key, value in emotion_response.items()
        if key != 'dominant_emotion'
    ]
    emotions_str = ', '.join(emotions)
    dominant_emotion = emotion_response['dominant_emotion']
    result_str = (
    f"For the given statement, the system response is {emotions_str}. "
    f"The dominant emotion is {dominant_emotion}."
    )

    return result_str

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
