import base64

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

# Route to display the web form
@app.route('/image2digits')
def image2difits():
    return render_template('image2digits.html')


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
    img =  cv2.imdecode(np.frombuffer(img_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    result = process_image(img)
    # Send the image file to the API
    #api_url = 'https://api.example.com/image-classifier'
    #headers = {'Content-Type': 'image/jpeg'}
    #response = requests.post(api_url, headers=headers, data=image_file.read())

    #result = json.loads(response.text)
    img_url = url_for('static', filename=result)
    return render_template('result.html', img_url=img_url)

@app.route('/submit_canvas', methods=['POST'])
def submit_canvas():
    import cv2
    import numpy as np
    import base64

    # Get the image file from the form
    image_data = request.json['image_data']
    img_bytes = base64.b64decode(image_data.split(',')[1])
    img_arr = np.frombuffer(img_bytes, dtype=np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    # Convert the image to grayscale using cv2.cvt
    #img =  img = cv2.imdecode(np.frombuffer(img_file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    result = process_image(img)
    # Send the image file to the API
    #api_url = 'https://api.example.com/image-classifier'
    #headers = {'Content-Type': 'image/jpeg'}
    #response = requests.post(api_url, headers=headers, data=image_file.read())

    #result = json.loads(response.text)
    img_url = url_for('static', filename=result)
    return render_template('result.html', img_url=img_url)

@app.route('/save_image', methods=['POST'])
def save_image():
    # Get the base64-encoded image data from the request
    image_data = request.form['image_data']
    # Decode the image data and save it to a file
    with open('image.png', 'wb') as f:
        f.write(base64.b64decode(image_data.split(',')[1]))
    # Return a response to the client
    return 'Image saved successfully'

if __name__ == '__main__':
    app.run(debug=True)
