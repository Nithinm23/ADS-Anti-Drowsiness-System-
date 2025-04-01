import cv2
import cvzone
import time
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
import winsound  # For beep sound on Windows

# Initialize video capture
vid = cv2.VideoCapture(0)

# Initialize face mesh detector
detector = FaceMeshDetector(maxFaces=1)

# Initialize live plot
plotY = LivePlot(640, 360, [20, 40], invert=True)

mouth_id_list = [61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 185, 40, 39, 37, 0, 267, 269, 270, 409, 78, 95, 88,
                 178, 87, 14, 317, 402, 318, 324, 308, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308]

# Variables for blink and yawn detection
ratioList = []
a = time.time()
b = 0
yawn_counter = 0
color = (255, 0, 255)
MAR_THRESHOLD = 1.2  # Threshold for detecting yawning
mouth_opened = False

# Function to calculate Mouth Aspect Ratio (MAR)
def calculate_MAR(landmarks):
    top_lip = landmarks[62]
    bottom_lip = landmarks[0]
    left_corner = landmarks[12]
    right_corner = landmarks[14]
    mouth_width, _ = detector.findDistance(left_corner, right_corner)
    mouth_height, _ = detector.findDistance(top_lip, bottom_lip)
    return mouth_width / mouth_height


while True:
    success, frame = vid.read()
    if not success:
        break

    frame, faces = detector.findFaceMesh(frame, draw=False)

    if b < 60:
        b = time.time() - a
        print(b)
      
        # Yawn detection
        mar = calculate_MAR(face)
        if mar > MAR_THRESHOLD:  # Mouth is open (yawning)
            if not mouth_opened:
                mouth_opened = True
                yawn_counter += 1  # Increment yawn counter
                print(f"Yawn detected! Yawn count: {yawn_counter}")
                if yawn_counter >= 2:  # Trigger beep if yawn count reaches 2
                    print("ALERT: Yawn count reached 2!")
                    board.digital[led_pin].write(0)
                    time.sleep(1)
                    'winsound.Beep(1000, 500)'  # Frequency: 1000Hz, Duration: 500ms
        else:
            mouth_opened = False
          
        # Display yawn count
        cv2.putText(frame, f'Yawn Count: {yawn_counter}', (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

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
