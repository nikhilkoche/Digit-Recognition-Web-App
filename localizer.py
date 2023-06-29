def process_image(image):
    import cv2
    import numpy as np
    from tensorflow import keras

    # Load pre-trained MNIST model(should be in same dir as this file)
    model = keras.models.load_model('2nd.h5')

    # Load image and convert to grayscale(should be in same dir as this file)
    # image = cv2.imread(img)

    # converting the color space from BGR to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to convert image to binary
    # 1----the threshold() function of OpenCV is used to apply thresholding to the grayscale image.
    # 2----The second argument (0) specifies the threshold value (in this case, it is set to zero).
    # 3----The third argument (255) specifies the maximum value to be assigned to pixels above the threshold.

    # 4----The fourth argument (cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) specifies the thresholding type,
    # which is a combination of two types of thresholding: THRESH_BINARY_INV and THRESH_OTSU.

    # 5----THRESH_BINARY_INV is a type of thresholding that assigns a value of 255 to pixels below the threshold,
    # and 0 to pixels above the threshold. This is the inverse of the usual binary thresholding,
    # where pixels above the threshold are assigned 255 and pixels below the threshold are assigned 0.

    # 6----THRESH_OTSU is a type of thresholding that automatically calculates the threshold value based on the image histogram,
    # using Otsu's method. This method calculates the threshold that minimizes the intra-class variance of the two groups of
    # pixels separated by the threshold, assuming a bimodal intensity distribution of the image.

    # 7----The threshold() function returns two values: the threshold value used, and the binary image.
    # In this line of code, the first value is assigned to _ (which is a convention to indicate that the value is not used),
    # and the second value is assigned to the variable binary.

    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours of digits in the image
    # The findContours() function is called with three arguments.
    # The first argument is the binary image, binary.

    # The second argument (cv2.RETR_EXTERNAL) specifies the retrieval mode for the contours.

    # RETR_EXTERNAL retrieves only the external contours, which are the contours that form the outer boundary of the connected regions.

    # The third argument (cv2.CHAIN_APPROX_SIMPLE) specifies the contour approximation method.
    # CHAIN_APPROX_SIMPLE compresses horizontal, vertical, and diagonal segments and leaves only their end points.
    # For example, a straight line segment will be represented by only two points, the start point and the end point.

    # The findContours() function returns two values: the list of contours, contours,
    # and the hierarchy of the contours, hierarchy. The hierarchy describes the parent-child relationships between contours,
    # if any. In this code, only contours is used.

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop through each contour and predict the digit using the MNIST model
    for contour in contours:
        # Get bounding rectangle of contour
        x, y, w, h = cv2.boundingRect(contour)

        # Crop digit from image
        digit = binary[y:y + h, x:x + w]

        # Resize digit to 28x28 (size expected by MNIST model)
        digit = cv2.resize(digit, (28, 28))

        # Reshape digit to 1D array (required by MNIST model)
        digit = digit.reshape(1, 28, 28, 1)

        # Normalize pixel values
        digit = digit / 255.0

        # Predict digit using MNIST model
        prediction = model.predict(digit)
        digit_class = np.argmax(prediction)

        # Draw bounding box and predicted digit on image
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, str(digit_class), (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show image with predicted digits and bounding boxes
    # cv2.imshow('image', image)
    cv2.imwrite('static/image_processed.jpg', image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return 'image_processed.jpg'
    # Adding this comment to make a repository commit as part of the 
    # Consulting AND Prof Communication assignment
