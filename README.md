# Image Classification using YOLOv8

This project demonstrates how to use the YOLOv8 model for image classification. The user can input an image, and the model will classify the image into the top 5 categories along with their confidence scores. The results are displayed both visually on the image and printed in the console.

## Project Overview

In this project, I used the YOLOv8 image classification model to classify a given image. The model outputs the top 5 classes along with their corresponding confidence scores, which are then drawn onto the image. This project is useful for classifying images into predefined categories using a pre-trained YOLOv8 model.

## Features

- **Image Classification**: Classifies a given image using the YOLOv8 model.
- **Top 5 Predictions**: Displays the top 5 predicted classes with their confidence scores on the image.
- **Custom Model Path**: You can specify your own model path to use a custom YOLOv8 model.

## How It Works

1. **Image Input**:
   - The script reads the image from a specified file path and resizes it to a fixed dimension (640x480 pixels).
   
2. **Model Loading**:
   - The pre-trained YOLOv8 model is loaded from the specified path, allowing it to perform image classification.

3. **Classification**:
   - The model predicts the top 5 most likely classes for the image along with their confidence scores.

4. **Displaying Results**:
   - The top 5 predictions, along with their confidence scores, are drawn onto the image using OpenCV.
   - The results are also printed to the console.

5. **Exiting**:
   - The processed image is displayed in a window, and the program can be exited by pressing any key.

## How to Run

### Dependencies

To run this project, you need the following libraries installed:
- `opencv-python`
- `numpy`
- `ultralytics`

You can install the necessary dependencies using `pip`:
```bash
pip install opencv-python numpy ultralytics
