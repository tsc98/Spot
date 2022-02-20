
Spott - v1 2022-02-20 4:45pm
==============================

This dataset was exported via roboflow.ai on February 20, 2022 at 4:46 PM GMT

It includes 1150 images.
UAS are annotated in YOLO v5 PyTorch format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* Random rotation of between -15 and +15 degrees
* Random shear of between -15° to +15° horizontally and -15° to +15° vertically
* Random exposure adjustment of between -34 and +34 percent

The following transformations were applied to the bounding boxes of each image:
* Salt and pepper noise was applied to 5 percent of pixels


