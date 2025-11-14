import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)

finger_tips = [4, 8, 12, 16, 20]

def detectar_gesto(fingers_up, hand_label, landmarks, w, h):
    thumb_tip = landmarks.landmark[4]
    wrist = landmarks.landmark[0]
    index_tip = landmarks.landmark[8]

    if fingers_up == [1, 0, 0, 0, 0] and thumb_tip.y > wrist.y:
        return "DISLIKE"

    if fingers_up == [1, 0, 0, 0, 0] and thumb_tip.y < wrist.y:
        return "LIKE"

    dist = ((thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2) ** 0.5
    if dist < 0.05:
        return "O.K."

    if fingers_up == [0, 1, 1, 0, 0]:
        return "PAZ"

    return None

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = hands.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks, hand_info in zip(results.multi_hand_landmarks, results.multi_handedness):
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            hand_label = hand_info.classification[0].label
            h, w, _ = image.shape

            fingers_up = []
            if hand_label == "Right":
                fingers_up.append(1 if hand_landmarks.landmark[finger_tips[0]].x < hand_landmarks.landmark[finger_tips[0] - 1].x else 0)
            else:
                fingers_up.append(1 if hand_landmarks.landmark[finger_tips[0]].x > hand_landmarks.landmark[finger_tips[0] - 1].x else 0)

            for tip_id in finger_tips[1:]:
                fingers_up.append(1 if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y else 0)

            count = sum(fingers_up)

            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
            wrist_coords = (int(wrist.x * w), int(wrist.y * h) - 30)
            cv2.putText(image, f"{hand_label}: {count} dedos", wrist_coords,
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            gesto = detectar_gesto(fingers_up, hand_label, hand_landmarks, w, h)
            if gesto:
                cv2.putText(image, f"Gesto: {gesto}", (wrist_coords[0], wrist_coords[1] - 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

            for idx, lm in enumerate(hand_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.putText(image, str(idx), (cx, cy),
                            cv2.FONT_HERSHEY_PLAIN, 0.8, (255, 0, 0), 1)

    cv2.imshow('Reconocimiento de Manos', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
