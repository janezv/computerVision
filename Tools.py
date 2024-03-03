from PIL import ImageGrab
import cv2
import os


def prtScr(name):
    # Take a screenshot
    screenshot = ImageGrab.grab()

    # Save the screenshot as an image file
    screenshot.save(name)

    print("Screenshot saved as 'screenshot.png'")


def PictureAverageWidthHeight(folder_path):
    total_width = 0
    total_height = 0
    total_images = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            try:
                img = cv2.imread(file_path)
                height, width, _ = img.shape
                total_width += width
                total_height += height
                total_images += 1
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    if total_images == 0:
        print("No images found in the folder.")
        return None, None

    average_width = total_width / total_images
    average_height = total_height / total_images

    return average_width, average_height


def resize_images(folder_path, target_width, target_height):
    width = int(target_width)
    height = int(target_height)
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            try:
                img = cv2.imread(file_path)
                # image = cv2.imread("Images\\Image1.png")

                resized_img = cv2.resize(img, (width, height))

                cv2.imwrite(file_path, resized_img)
                print(f"Resized {filename} successfully.")
            except Exception as e:
                print(f"Error processing {filename}: {e}")


def assembleVideo(folder_path, intervarl=1):
    output_video = folder_path+'/output_video.avi'

    # Get all PNG files in the folder
    png_files = [f for f in os.listdir(
        folder_path) if f.endswith('.png') or f.endswith('.jpg')]
    png_files.sort()
    duplicateLastImage = png_files[-1]
    png_files.append(duplicateLastImage)
    if len(png_files) == 0:
        print("Ni slik v mapi !!! MAPA JE PRAZNA")
        return
    try:
        averageHeight, averageWidth = PictureAverageWidthHeight(folder_path)
        averageIntHeight = int(averageHeight)
        averageIntWidth = int(averageWidth)
        resize_images(folder_path, averageIntHeight, averageIntWidth)
        fps = intervarl  # Set the frame rate (frames per second)
        # Define video codec and create VideoWriter object
        if os.path.exists(output_video):
            os.remove(output_video)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        video_writer = cv2.VideoWriter(
            output_video, fourcc, fps, (averageIntHeight, averageIntWidth))

        # Write each frame to the video
        for png_file in png_files:
            image = cv2.imread(os.path.join(folder_path, png_file))
            video_writer.write(image)

        # Release VideoWriter object
        video_writer.release()
        print(f"Video assembled successfully: {output_video}")

    except Exception as e:
        print(f"Error processing {e}: {e}")
