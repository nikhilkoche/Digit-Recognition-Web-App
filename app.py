import requests
from flask import Flask, render_template, request
import json
app = Flask(__name__)


# Route to display the web form
@app.route('/')
def index():
    return render_template('index.html')


# Route to handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Get the image file from the form
    image_file = request.files['image']

    # Send the image file to the API
    api_url = 'https://api.example.com/image-classifier'
    headers = {'Content-Type': 'image/jpeg'}
    response = requests.post(api_url, headers=headers, data=image_file.read())

    result = json.loads(response.text)
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
