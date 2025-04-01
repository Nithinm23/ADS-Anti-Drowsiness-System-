import cv2
import cvzone
import time
import winsound  # For beep sound on Windows
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
import pyfirmata

# Initialize video capture
vid = cv2.VideoCapture(0)

# Initialize face mesh detector
detector = FaceMeshDetector(maxFaces=1)

# Initialize live plot
plotY = LivePlot(640, 360, [20, 40], invert=True)

# Define facial landmarks for eyes and mouth
idlist = [22, 23, 24, 25, 26, 110, 112, 130, 157, 158, 159, 160, 161, 243, 339, 254, 255, 253, 252, 256, 359, 263, 388,
          387, 386, 385, 384, 398]
mouth_id_list = [61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 185, 40, 39, 37, 0, 267, 269, 270, 409, 78, 95, 88,
                 178, 87, 14, 317, 402, 318, 324, 308, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308]

# Variables for blink and yawn detection
ratioList = []
a = time.time()
b = 0
color = (255, 0, 255)
# Variables for head pose detection
looking_straight = True

while True:
    success, frame = vid.read()
    if not success:
        break

    frame, faces = detector.findFaceMesh(frame, draw=False)

    if b < 60:
        b = time.time() - a
        print(b)

    if faces:
        face = faces[0]
        leftUP, leftDown = face[159], face[23]
        lefteyeLeft, lefteyeRight = face[130], face[243]
        rightUP, rightDown = face[386], face[253]
        righteyeLeft, righteyeRight = face[398], face[255]
        nose = face[1]
        chin = face[152]
        forehead = face[10]
      
        # Detect head pose (up, down, left, right)
        if nose[0] < lefteyeLeft[0]:
            looking_direction = "Right"
            looking_straight = False
        elif nose[0] > righteyeRight[0]:
            looking_direction = "Left"
            looking_straight = False
        else:
            looking_direction = "Straight"
            looking_straight = True

        # Use specified mesh points (10, 152, 352, 123) to detect up and down
        point_10 = face[10]  # Forehead
        point_152 = face[152]  # Chin
        point_352 = face[352]  # Left cheek
        point_123 = face[123]  # Right cheek

        # Calculate vertical distance between point 10 (forehead) and 152 (chin)
        vertical_distance, _ = detector.findDistance(point_10, point_152)

        # Calculate horizontal distance between point 352 (left cheek) and 123 (right cheek)
        horizontal_distance, _ = detector.findDistance(point_352, point_123)

        # Determine if head is up or down based on vertical and horizontal distances
        if vertical_distance > horizontal_distance * 1.2:  # Head is up
            head_pose = ""
            looking_straight = True
        else:
            head_pose = "Danger"
            looking_direction = ""
            looking_straight = False

            board.digital[led_pin].write(1)
            time.sleep(1)
            board.digital[led_pin].write(0)
            time.sleep(1)
            # Play beep sound if head pose is "danger"
            winsound.Beep(1000, 500)  # Frequency: 1000Hz, Duration: 500ms

        # Display looking direction and head pose
        cv2.putText(frame, f'Looking: {looking_direction}', (20, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(frame, f'Head Pose: {head_pose}', (20, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
      
        # Reset counters after 60 seconds
        if b >= 60:
            a = time.time()
            b = 0
            blinkcounter = 0
            yawn_counter = 0

        # Update live plot
        imgPlot = plotY.update(ratioAvg, color)
        frame = cv2.resize(frame, (640, 360))
        imgstack = cvzone.stackImages([frame, imgPlot], 1, 1)
    else:
        frame = cv2.resize(frame, (640, 360))
        imgstack = cvzone.stackImages([frame, frame], 1, 1)

    # Display the frame
    cv2.imshow('frame', imgstack)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release resources
vid.release()
cv2.destroyAllWindows()
