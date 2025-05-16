# Human 3Diffusion Blender Addon

This addon integrates the Human 3Diffusion model into Blender for generating 3D avatars from 2D images.

![Demo](https://elhoussainechahboun.com/ScreenRecording2025-02-07at11.42.32PM-ezgif.com-video-to-gif-converter.gif)

## Directory Structure

- __init__.py: Addon entry point
- operators.py: Operators for inference and mesh generation
- ui.py: User interface elements
- inference.py: Script to call Human 3Diffusion inference
- test_imgs/: Directory for user-uploaded input images
- output/: Directory for storing generated outputs
- checkpoints/: Directory for pretrained model weights
- human3diffusion/: Placeholder for the Human 3Diffusion scripts and submodules

## Setup

1. Populate the `checkpoints` folder with the required pretrained weights.
2. Clone the `human3diffusion/` repository into the corresponding directory.
3. Install required Python packages from `requirements.txt`.

## Usage

1. Enable the addon in Blender.
2. Use the UI to upload an image and generate a 3D avatar.

## License


