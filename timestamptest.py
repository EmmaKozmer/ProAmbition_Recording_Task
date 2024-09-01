import cv2
import time

# Default camera (index 0)
cap = cv2.VideoCapture(1)

# Fehlermeldung, falls video capture object nicht erfolgreich initialisiert worden ist
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Höhe und Breite des frames einstellen
frame_width = int(cap.get(3)) 
frame_height = int(cap.get(4)) 


VideoWriter object für AVI format 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame_width, frame_height))

# Textformattierung
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255, 255, 255)  # Weiss
thickness = 2
position = (10, 50)  # Position des timestamps on the frame

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Momentane Zeit holen
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Aufs video tun
    cv2.putText(frame, timestamp, position, font, font_scale, color, thickness, cv2.LINE_AA)

    # Schreiben 
    out.write(frame)

    # Frame anzeigen
    cv2.imshow('Timestamped Video', frame)

    # Schauen, dass es aufhört, wenn man auf q drückt. 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# alles stoppen 
cap.release()
out.release()
cv2.destroyAllWindows()