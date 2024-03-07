import cv2

# Define desired cropping parameters (adjust as needed)
x_start = 0  # Starting X coordinate (can be 0 for full width)
y_start = 0  # Starting Y coordinate (can be 0 for full height)
width = 1280  # Width of cropped area
height = 720  # Height of cropped area

# Initialize video capture
cam = cv2.VideoCapture(0)

# Create named window
cv2.namedWindow("Python Webcam App")

img_counter = 0

while True:
  # Capture frame
  ret, frame = cam.read()

  if not ret:
    print("Failed to grab frame")
    break

  # Crop the frame using slicing
  cropped_frame = frame[y_start:y_start+height, x_start:x_start+width]

  # Display original and/or cropped frames
  # cv2.imshow("Original Frame", frame)
  cv2.imshow("Cropped Frame", cropped_frame)

  # Handle key presses
  k = cv2.waitKey(1)

  if k % 256 == 27:
    print("Escape hit, closing app")
    break
  elif k % 256 == 32:
    img_name = "opencv_frame_{}.png".format(img_counter)
    # Save the cropped frame instead of the original
    cv2.imwrite(img_name, cropped_frame)
    print("Screenshot Taken:", img_name)
    img_counter += 1

# Release resources
cam.release()

cv2.destroyAllWindows()
