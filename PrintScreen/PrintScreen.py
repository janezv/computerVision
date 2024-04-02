import cv2

# Function to capture screenshot
count_images: int = 0

# Open webcam
cap = cv2.VideoCapture(0)

while True:

    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Webcam', frame)

    # Check for key press
    key = cv2.waitKey(1)
    if key == ord('q'):  # Quit when 'q' is pressed
        break
    elif key == ord('a'):  # Capture screenshot when 'a' is pressed
        count_images = count_images+1
        count_str = str(count_images)
        cv2.imwrite('screenshot'+count_str+'.png', frame)
        print("Screenshot saved")

# Release the capture
cap.release()
cv2.destroyAllWindows()
