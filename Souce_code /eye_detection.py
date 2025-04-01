import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
import winsound  # For beep sound on Windows
import time 
# Initialize video capture
vid = cv2.VideoCapture(0)

# Initialize face mesh detector
detector = FaceMeshDetector(maxFaces=1)

# Initialize live plot
plotY = LivePlot(640, 360, [20, 40], invert=True)

# Define facial landmarks for eyes and mouth
idlist = [22, 23, 24, 25, 26, 110, 112, 130, 157, 158, 159, 160, 161, 243, 339, 254, 255, 253, 252, 256, 359, 263, 388,
          387, 386, 385, 384, 398]

# Variables for blink and yawn detection
ratioList = []
a = time.time()
b = 0
blinkcounter = 0
counter = 0
color = (255, 0, 255)

# Variables for eye closure detection
eye_closed = False
eye_closure_start = None
eye_closure_duration = 0

while True:
    success, frame = vid.read()
    if not success:
        break

    frame, faces = detector.findFaceMesh(frame, draw=False)

    if b < 60:
        b = time.time() - a
        print(b)

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
              
        # Display blink count and eye closure duration
        cv2.putText(frame, f'Blink Count: {blinkcounter}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.putText(frame, f'Eye Close Duration: {eye_closure_duration:.2f} sec', (50, 150), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 0), 2)
      
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
