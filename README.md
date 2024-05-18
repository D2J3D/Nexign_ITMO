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
### 1. YOLOv8 for POSM detection

**About:**

Validation predicts and labels comparison

![image](https://github.com/D2J3D/Nexign_ITMO/assets/120342275/ed2e1497-ba52-4fd8-80b4-153c0df6173c)

**Metrics and losses:**

![image](https://github.com/D2J3D/Nexign_ITMO/assets/120342275/ef1bb39b-43a5-44a1-9eeb-9c783d7df76a)


![image](https://github.com/D2J3D/Nexign_ITMO/assets/120342275/07053b21-384b-4543-91e6-a70387c509c4)

![image](https://github.com/D2J3D/Nexign_ITMO/assets/120342275/aee33677-5cd4-42bd-9c99-00653d485d45)


### 2. detection + Instance Segmentation

**About:**

Validation predicts:

![val_batch1_labels_51_ce96014e2ca197ca672e](https://github.com/D2J3D/Nexign_ITMO/assets/120342275/24183718-6900-4a14-9e34-ce3eb01bca0e)

![image](https://github.com/D2J3D/Nexign_ITMO/assets/120342275/34177fbb-750a-4c36-b713-4545aed920da)

![image](https://github.com/D2J3D/Nexign_ITMO/assets/120342275/6e6db631-5fdc-43e7-bc41-254e501f692d)

![image](https://github.com/D2J3D/Nexign_ITMO/assets/120342275/96718bc2-d2b9-4233-8e05-79063e6cec3e)

![image](https://github.com/D2J3D/Nexign_ITMO/assets/120342275/f69c41f0-cfd4-46b8-9d15-6bf9de63d739)






