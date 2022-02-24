# TODO develop a function for the webcom
# TODO develop this into a notebook.

import cv2
import torch
from time import time
import numpy

model_path = '/Users/Tom/PycharmProjects/Spot/Spott/Trained Models/best_m_220222_ED.pt'

class UxvDetect:
    #Implements the yolo v5 custom model stated above.
    def __init__(self, capture_index, model_name):
        self.capture_index = capture_index
        self.model = self.load_model(model_name)
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("Using Device: ", self.device)

    def get_video_capture(self):
        #streams the video object and extracts frames
        return cv2.VideoCapture(self.capture_index)

    def load_model(self, model_name):
        # loads the model from the model_name input, to change model, change the model path var. This will need to be done when model is adapted to a new environment.
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_name, force_reload=True)
        return model