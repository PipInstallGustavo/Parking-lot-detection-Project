# Parking Lot Detection using OpenCV

![Captura de tela de 2025-03-26 17-59-49](https://github.com/user-attachments/assets/f93f0a9a-ddaf-4441-8952-811190f41aa7)

## Overview

This project utilizes OpenCV to detect parking lots and determine when a car is occupying a specific lot. The system processes video or image inputs and identifies vacant and occupied parking spaces.

## Features
- Detects parking spaces in a given area
- Determines if a parking lot is occupied or vacant
- Uses OpenCV for image processing and contour detection
- Can process real-time video feeds or static images
- Tracks how many parking lots are available

## Requirements
- Python 3.x
- OpenCV
- NumPy

## Installation
```bash
pip install opencv-python numpy
```

## Usage
1. Clone the repository:
```bash
git clone https://github.com/PipInstallGustavo/Parking-lot-detection-Project.git
```
2. Run the detection script:
```bash
python main.py 
```

## How It Works
1. Preprocesses the image/video using OpenCV (grayscale, thresholding, edge detection).
2. Detects contours and identifies parking spots.
3. Analyzes whether each parking lot is occupied or vacant.
4. Displays the processed output with highlighted parking spots.

