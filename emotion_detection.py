import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=header)
    formatted_response=json.loads(response.text)
    imotion = extract_emotion(formatted_response)
    return imotion

def extract_emotion(imotion_predictions):
    emotion_data = imotion_predictions['emotionPredictions'][0]['emotion']
    dominant_emotion = max(emotion_data, key=emotion_data.get)
    imotion = {
        'anger': emotion_data['anger'],
        'disgust': emotion_data['disgust'],
        'fear': emotion_data['fear'],
        'joy': emotion_data['joy'],
        'sadness': emotion_data['sadness'],
        'dominant_emotion': dominant_emotion
    }
    return imotion


