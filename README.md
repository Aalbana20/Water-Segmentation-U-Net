# Water Segmentation Using U-Net

## Overview

This project focuses on using a U-Net architecture for segmenting water bodies in satellite images. The model is trained to distinguish between water and land pixels in the input images.

## Project Structure

- `data/`: Contains raw and processed data used for training and testing.
- `images/`: Stores images that will be fed into the model during training and testing.
- `output/`: The segmented images and model predictions will be stored here.
- `logs/`: Logs from training and evaluation, such as TensorBoard logs.

## Installation

1. Clone the repository:
   git clone https://github.com/aalbana20/Water-Segmentation-U-Net.git

## Requirements

To set up the project, install the necessary dependencies using the following command:
    pip install -r requirements.txt

Run the training script with the following command:
    python train.py
