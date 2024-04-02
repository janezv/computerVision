from pynput.mouse import Listener
from PIL import ImageGrab
import cv2
import os

folder_path = "Output/"


def record(start_x, start_y, end_x, end_y, frame_numbers=900, FramesPerSecodn=25):
    global folder_path
    frame: int = 1
    while frame_numbers:
        # Take a screenshot
        # ImageGrab.grab(bbox=(left, top, right, bottom))
        # print('CREATED IMAGE ({0}, {1},{2}, {3})'.format(
        #     start_x, start_y, end_x, end_y))
        screenshot = ImageGrab.grab(bbox=(start_x, start_y, end_x, end_y))

        # Save the screenshot as an image file

        frame_string = str(frame)
        file_name = folder_path+"scrShot"+frame_string+'.jpg'
        screenshot.save(file_name)
        print("Narejen posnetek: "+ file_name)
        frame = frame+1
        if frame > frame_numbers:
            assembleVideo(FramesPerSecodn)
            break


def assembleVideo(FramesPerSecodn=1):
    global folder_path
    output_video = folder_path+'/output_video.avi'

    # Get all PNG files in the folder
    img_files = [f for f in os.listdir(
        folder_path) if f.endswith('.png') or f.endswith('.jpg')]
    # Sort files based on creation time
    sorted_files = sorted(img_files, key=lambda x: os.path.getctime(os.path.join(folder_path, x)))
    first_image = cv2.imread(os.path.join(folder_path, img_files[0]))
    height, width, _ = first_image.shape

    fps = FramesPerSecodn
    output_video_path = folder_path+'/output_video.avi'
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for the output video
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Write each frame to the output video
    for jpg_file in sorted_files:
        image_path = os.path.join(folder_path, jpg_file)
        print("V video dan: " + image_path)
        frame = cv2.imread(image_path)
        out.write(frame)

    # Release everything if job is finished
    out.release()
    cv2.destroyAllWindows()
