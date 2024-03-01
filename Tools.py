from PIL import ImageGrab
import cv2
import os


def prtScr(name):
    # Take a screenshot
    screenshot = ImageGrab.grab()

    # Save the screenshot as an image file
    screenshot.save(name)

    print("Screenshot saved as 'screenshot.png'")


def assembleVideo(folder_path):
    output_video = folder_path+'/output_video.avi'

    # Get all PNG files in the folder
    png_files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    png_files.sort()
    first_image = cv2.imread(os.path.join(folder_path, png_files[0]))
    height, width, _ = first_image.shape

    # Define video codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video_writer = cv2.VideoWriter(output_video, fourcc, 10.0, (width, height))

    # Write each frame to the video
    for png_file in png_files:
        image = cv2.imread(os.path.join(folder_path, png_file))
        video_writer.write(image)

    # Release VideoWriter object
    video_writer.release()
    print(f"Video assembled successfully: {output_video}")
