# Ikea_image_classifier

## Problem Definition: 
Scrape images from IKEA site(https://www.ikea.com/).

The dataset should be of at least 4 classes and should contain high level categories
and not subcategories, ie., it should be chairs vs tables instead of sitting chair vs bar
chair.

Perform the classification using machine learning technique(for eg. CNNs, RF). The model should be able to predict
the class label of an image. 

# Solution Approach:
1. Used Beautiful Soup to extract images from ikea site. I have used image_scrapper.py for to extract 96 images of 4 different categories having 24 images each.
2. Load the image
3. Image processing -> load the image with RGB format -> resize the image(150,150) -> Normalize the image
4. Model: Used CNN model with Conv2D -> Conv2D -> MaxPool2D -> Conv2D -> Conv2D -> MaxPool2D -> Flatten -> Dense Layer(with 4 output). I have used relu activation, RMSprop optimizer, categorical_crossentropy loss.

Model2: Used CNN model with Conv2D -> Conv2D -> MaxPool2D -> Dropout -> Conv2D -> Conv2D -> MaxPool2D -> Dropout -> Flatten -> Dense -> Dropout -> Dense Layer(with 4 output). I have used relu activation, RMSprop optimizer, categorical_crossentropy loss.

Model3: Trained the model2 on agumented image data. 

Future Work: Will add more image data and then use pre trained model like ResNet50, VGG16, VGG19, MobileNet etc.
