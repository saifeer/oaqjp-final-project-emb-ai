''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions and
        the dominant emotion for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Check if the dominant_emotion is None, indicating an error or invalid input
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # Return a formatted string
    return f"For the given statement, the system response is 'anger': \
        {response['anger']}, 'disgust': {response['disgust']}, 'fear': \
        {response['fear']}, 'joy': {response['joy']} and 'sadness': \
        {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    ''' This code renders the index page for the application
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
