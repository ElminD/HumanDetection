# HumanDetection
HumanDetection is a Computer Vision project detecting Human Faces, Eyes, Upper body and, Full Body.
Using OpenCV 
<a href="https://opencv.org/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/opencv/opencv-icon.svg" alt="opencv" width="40" height="40"/> </a>
and Python <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> 
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install opencv for python.

```bash
pip install opencv-python
```

## Usage

```python
#Line 31
cap = cv2.VideoCapture(0)
0,1,2. Change value based on which webcam you wish to use 

#Most Video files are also supported 
cap = cv2.VideoCapture('video.mp4')
```

## Demo

🟦Blue Boxes = Face  <br />
🟩Green Boxes  = Eyes  <br />
🌸Pink Boxes  = Upper Body  <br />
🟨Yellow Boxes = Full Body  <br />

The 🔥🗺️ HeatMap detects change and will increase in "temp" based on movement

<img src="https://github.com/ElminD/HumanDetection/blob/main/opencvgif.gif">
<img src="https://github.com/ElminD/HumanDetection/blob/main/opencvgif2.gif">
<img src="https://github.com/ElminD/HumanDetection/blob/main/opencvgif3.gif">
