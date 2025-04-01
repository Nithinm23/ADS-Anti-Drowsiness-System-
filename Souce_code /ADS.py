import cv2
import cvzone
import time
import winsound  # For beep sound on Windows
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
import pyfirmata

port = 'COM3'

board = pyfirmata.Arduino(port)

led_pin = 13


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
blinkcounter = 0
counter = 0
yawn_counter = 0
color = (255, 0, 255)
MAR_THRESHOLD = 1.2  # Threshold for detecting yawning
mouth_opened = False

# Variables for eye closure detection
eye_closed = False
eye_closure_start = None
eye_closure_duration = 0

# Variables for head pose detection
looking_straight = True

# Take age input only once at the beginning
"""age = int(input("Enter your age: "))
if age < 18:
    blink_rate_threshold = 5  # Infancy
elif age <= 30:
    blink_rate_threshold = 16  # Childhood
elif age <= 50:
    blink_rate_threshold = 13  # Adolescence
elif age <= 70:
    blink_rate_threshold = 11  # Adulthood
else:
    blink_rate_threshold = 5"""


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

    if faces:
        face = faces[0]
        leftUP, leftDown = face[159], face[23]
        lefteyeLeft, lefteyeRight = face[130], face[243]
        rightUP, rightDown = face[386], face[253]
        righteyeLeft, righteyeRight = face[398], face[255]
        nose = face[1]
        chin = face[152]
        forehead = face[10]

        # Calculate eye aspect ratio (EAR)
        lengthVertical, _ = detector.findDistance(leftUP, leftDown)
        lengthHorizontal, _ = detector.findDistance(lefteyeLeft, lefteyeRight)
        lengthVertical_1, _ = detector.findDistance(rightUP, rightDown)
        lengthHorizontal_1, _ = detector.findDistance(righteyeLeft, righteyeRight)

        ratio = (lengthVertical / lengthHorizontal) * 100 if lengthHorizontal > 0 else 0
        ratioList.append(ratio)
        if len(ratioList) > 3:
            ratioList.pop(0)
        ratioAvg = sum(ratioList) / len(ratioList)

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

        # Eye blink detection
        if ratioAvg < 28.55:  # Adjust this threshold as needed
            if not eye_closed:
                eye_closed = True
                eye_closure_start = time.time()
                blinkcounter += 1  # Increment blink count only once when eyes close
        else:
            if eye_closed:
                eye_closed = False
                eye_closure_duration = time.time() - eye_closure_start
                print(f"Eye was closed for {eye_closure_duration:.2f} seconds")

        # Check if eyes are closed and duration exceeds 2 seconds
        if eye_closed:
            eye_closure_duration = time.time() - eye_closure_start
            if eye_closure_duration > 2:
                print("ALERT: Eyes closed for more than 2 seconds!")
                winsound.Beep(1000, 500)  # Frequency: 1000Hz, Duration: 500ms

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

        # Display looking direction and head pose
        cv2.putText(frame, f'Looking: {looking_direction}', (20, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(frame, f'Head Pose: {head_pose}', (20, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        # Display blink count and eye closure duration
        cv2.putText(frame, f'Blink Count: {blinkcounter}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(frame, f'Eye Close Duration: {eye_closure_duration:.2f} sec', (50, 150), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 0), 2)

        # Display yawn count
        cv2.putText(frame, f'Yawn Count: {yawn_counter}', (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

        # Check blink rate based on age
        '''if blinkcounter > blink_rate_threshold:  # Beep if blink count crosses the threshold
            print(
                f"ALERT: Blink rate crossed the threshold for your age group ({blink_rate_threshold} blinks per minute)!")
            winsound.Beep(1000, 500)  # Frequency: 1000Hz, Duration: 500ms'''

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
