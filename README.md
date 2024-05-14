# Learning Lab from Nexign and ITMO 

## Smart validation. Outlet check
Goal is to filter out inappropriate pictures (like a SIM image).

An image is considered to be inappropriate if a human cannot evaluate the parity by looking at it
### Dataset details
Used parts of Chicago dataset (306 images)

**Classes:**
1. Good
2. Trash

### Model

For this task we used pre-trained (on imageNet) ResNet50, and made fine-tuning on the custom dataset.

## POSM detection and segmentation 

### Dataset details
Combined 2 datasets: 296297_project.tar (870 images) and 296300_project.tar (535 images)


**Classes:**

1. Megafon
2. Yota
3. Opponents

**Augmentation applied:**

-  Flip: Horizontal, Vertical
- 90° Rotate: Clockwise, Counter-Clockwise
- Crop: 0% Minimum Zoom, 20% Maximum Zoom
- Blur: Up to 2.5px
- Noise: Up to 1.2% of pixels

### Model
YOLOV8 from ultralytics 

