import requests
from PIL import Image
from flask import Flask, render_template, request, url_for
import json

from localizer import process_image

app = Flask(__name__)


# Route to display the web form
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/canvas')
def canvas():
    return render_template('canvas.html')


# Route to handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    import cv2
    import numpy as np
    # Get the image file from the form
    img_file = request.files['image']
    img =  img = cv2.imdecode(np.frombuffer(img_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    result = process_image(img)
    # Send the image file to the API
    #api_url = 'https://api.example.com/image-classifier'
    #headers = {'Content-Type': 'image/jpeg'}
    #response = requests.post(api_url, headers=headers, data=image_file.read())

    #result = json.loads(response.text)
    img_url = url_for('static', filename=result)
    return render_template('result.html', img_url=img_url)


if __name__ == '__main__':
    app.run(debug=True)
