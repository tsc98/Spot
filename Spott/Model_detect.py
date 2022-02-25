# TODO develop a function for the webcom
# TODO develop this into a notebook.

import cv2
import torch
from time import time
import numpy as np

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

    def score_frame(self, frame):
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
        # If using a different model then the results.xyxyn will have to change to reflect the output of the new model.
        labels, cord = results.xyxyn[0][:,-1], results.xyxyn[0][:,:-1]
        return labels, cord

    def class_to_label(self, x):
        return self.classes[int(x)]

    def plot_boxes(self, results, frame):
        # For every label identified in the image, this takes the coords and then applies a bounding box and text
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.4: #change this parameter if there are too many false (+)ve
                x1,y1,x2,y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1,y1), (x2,y2), bgr, 2)
                cv2.putText(frame, self.class_to_label(labels[i]), (x1,y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)

        return frame

    def __call__(self):
        """
        This function is called when class is executed, it runs the loop to read the video frame by frame,
        and write the output into a new file.
        :return: void
        """
        cap = self.get_video_capture()
        assert cap.isOpened()

        while True:

            start_time = time()

            ret, frame = cap.read()
            assert ret

            results = self.score_frame(frame)
            frame = self.plot_boxes(results, frame)

            end_time = time()
            fps = 1 / np.round(end_time - start_time, 2)
            # print(f"Frames Per Second : {fps}")

            cv2.putText(frame, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

            cv2.imshow('UxV Detection', frame)

            if cv2.waitKey(5) & 0xFF == 27:
                break

        cap.release()


# Create a new object and execute.
detector = UxvDetect(capture_index=0, model_name=model_path)
detector()