from PIL import ImageGrab
import cv2
import os


def prtScr(name):
    # Take a screenshot
    screenshot = ImageGrab.grab()

    # Save the screenshot as an image file
    screenshot.save(name)

    print("Screenshot saved as 'screenshot.png'")


def assembleVideo(folder_path, FramesPerSecodn=1):
    output_video = folder_path+'/output_video.avi'

    # Get all PNG files in the folder
    img_files = [f for f in os.listdir(
        folder_path) if f.endswith('.png') or f.endswith('.jpg')]
    img_files.sort()
    # Get the first image to extract its dimensions
    first_image = cv2.imread(os.path.join(folder_path, img_files[0]))
    height, width, _ = first_image.shape

    fps = FramesPerSecodn
    output_video_path = folder_path+'/output_video.avi'
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for the output video
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Write each frame to the output video
    for jpg_file in img_files:
        image_path = os.path.join(folder_path, jpg_file)
        frame = cv2.imread(image_path)
        out.write(frame)

    # Release everything if job is finished
    out.release()
    cv2.destroyAllWindows()
