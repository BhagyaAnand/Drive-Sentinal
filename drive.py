import cv2
import mediapipe as mp
import pygame
import numpy as np
from collections import deque

pygame.mixer.init()

mp_face = mp.solutions.face_mesh
face = mp_face.FaceMesh(max_num_faces=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

LEFT_EYE  = [33,160,158,133,153,144]
RIGHT_EYE = [263,387,385,362,380,373]

def ear(lm, pts):
    h = abs(lm[pts[1]].y - lm[pts[5]].y)
    w = abs(lm[pts[0]].x - lm[pts[3]].x)
    return h / (w + 1e-6)

THRESHOLD = 0.170   

history = deque(maxlen=20)  
closed_frames = 0
FRAMES_THRESHOLD = 15        

alarm_on = False

while True:
    ok, frame = cap.read()
    if not ok:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = face.process(rgb)

    if res.multi_face_landmarks:
        lm = res.multi_face_landmarks[0].landmark

        avg = (ear(lm, LEFT_EYE) + ear(lm, RIGHT_EYE)) / 2

        eyes_open = avg >= THRESHOLD

        history.append(1 if eyes_open else 0)

        open_ratio = sum(history) / len(history)

        if open_ratio < 0.5:
            closed_frames += 1
        else:
            closed_frames = 0
            if alarm_on:
                pygame.mixer.stop()
                alarm_on = False

        if closed_frames >= FRAMES_THRESHOLD:
            cv2.putText(frame, "EYES CLOSED!", (50, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,0,255), 3)

            if not alarm_on:
                sample_rate = 44100
                t = np.linspace(0, 1, int(sample_rate))
                wave = (32767 * np.sin(2 * np.pi * 1000 * t)).astype(np.int16)
                wave_stereo = np.column_stack([wave, wave])
                sound = pygame.sndarray.make_sound(wave_stereo)
                sound.play(-1)
                alarm_on = True

        else:
            cv2.putText(frame, "EYES OPEN", (50, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 3)

        cv2.putText(frame, f"EAR: {avg:.3f}", (50, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

    else:
        cv2.putText(frame, "FACE NOT DETECTED", (50, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,0,255), 2)

    cv2.imshow("Eye Detector", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.quit()