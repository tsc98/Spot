# Spot

This is a transfer learning version of YOLOv5 to detect UAS, UGVs, People (military), cars and aeroplanes. 

The trained models will be kept in /Spott/Trained_models, these will be regularly updated, with the training data and size of model annotated. 
The spot_yolo_train2.ipynb should be used in colab to support new training iterations (colab works pretty well with it + GPU Spt)

The Model_detect script will call the predictor for the devices primary camera. 

To initiate in terminal/Command Line call the detect.py from yolov5 directly using:

!python detect.py --weights (model path) --img 416 --conf 0.5 --source 0 

