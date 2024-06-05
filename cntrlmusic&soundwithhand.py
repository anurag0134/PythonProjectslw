#working code
import cv2
import mediapipe as mp
import pyautogui

# Initialize Mediapipe Hand model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Function to recognize gestures
def recognize_gesture(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    # Thumb Up Gesture
    if thumb_tip.y < thumb_ip.y < index_finger_tip.y < middle_finger_tip.y < ring_finger_tip.y < pinky_tip.y:
        return "thumbs_up"
    
    # Palm Open Gesture
    if (index_finger_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and
        middle_finger_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and
        ring_finger_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y and
        pinky_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y):
        return "palm_open"
    
    
    if (index_finger_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and    # Fist Gesture
        middle_finger_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and
        ring_finger_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y and
        pinky_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y):
        return "fist"
    
    
    if (index_finger_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and   # Peace Gesture (Two Fingers Up)
        middle_finger_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and
        ring_finger_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y and
        pinky_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y):
        return "peace"
    
   
    if (index_finger_tip.y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and    # One Finger Up Gesture (Previous Track)
        middle_finger_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and
        ring_finger_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y and
        pinky_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y):
        return "one_finger_up"

    return None

# OpenCV for capturing video input
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip the frame horizontally for a later selfie-view display
    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            gesture = recognize_gesture(hand_landmarks)
            
            if gesture == "thumbs_up":
                pyautogui.press('volumeup')  # Increase volume
            elif gesture == "palm_open":
                pyautogui.press('playpause')  # Play/Pause music
            elif gesture == "fist":
                pyautogui.press('volumedown')  # Decrease volume
            elif gesture == "peace":
                pyautogui.press('nexttrack')  # Next track
            elif gesture == "one_finger_up":
                pyautogui.press('prevtrack')  # Previous track

    cv2.imshow('Hand Gesture Recognition', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
