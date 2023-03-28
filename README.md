#Digit Recognition Web App 
This is a web app that uses a pre-trained MNIST model to recognize handwritten digits in an uploaded image and draw bounding boxes around them.

##Getting Started

###Prerequisites
Before you can run this web app, you need to have the following software installed on your system:

+Python 3.x
+Flask
+OpenCV
+TensorFlow
+Numpy

You can install these dependencies using pip by running the following command in your terminal:
```python

pip install -r requirements.txt
```
###Running the Web App
1.Navigate to the project directory and run 'python app.py' to start the Flask server.
2.Open your web browser and go to 'http://localhost:5000' to access the home page.
3.Upload an image containing one or more digits using the file input form.
4.Press the "Submit" button to submit the form and wait for the results to load.
5.The results page will display the uploaded image with bounding boxes around any recognized digits.
###Built With 
-Python
-Flask
-TensorFlow
-OpenCV

###Acknowledgments
-This project was inspired by the [MNIST digit recognition](https://www.tensorflow.org/tutorials/keras/classification) tutorial on the TensorFlow website.

-[OpenCV documentation](https://docs.opencv.org/4.x/)

-[Flask documentation](https://flask.palletsprojects.com/en/2.1.x/)

-[Bootstrap documentation](https://getbootstrap.com/docs/5.1/getting-started/introduction/)


