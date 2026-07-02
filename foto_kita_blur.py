import cv2
import mediapipe as mp

CAMERA_INDEX = 0
BLUR_SIZE = (99, 99)
PROCESS_WIDTH = 320
PROCESS_HEIGHT = 240

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    model_complexity=0,
    max_num_hands=2,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.5,
)

cap = cv2.VideoCapture(CAMERA_INDEX)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, PROCESS_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, PROCESS_HEIGHT)
cap.set(cv2.CAP_PROP_FPS, 30)


def count_raised_fingers(hand_landmarks):
    landmarks = hand_landmarks.landmark

    finger_states = []
    for tip_idx, pip_idx in [(8, 6), (12, 10), (16, 14), (20, 18)]:
        finger_states.append(landmarks[tip_idx].y < landmarks[pip_idx].y)

    thumb_tip_x = landmarks[4].x
    thumb_ip_x = landmarks[3].x
    thumb_up = thumb_tip_x < thumb_ip_x - 0.03
    finger_states.append(thumb_up)

    return finger_states, sum(finger_states)


def draw_hand_skeleton(frame, hand_landmarks, src_width, src_height, dst_width, dst_height):
    points = []
    for landmark in hand_landmarks.landmark:
        x = int(landmark.x * src_width)
        y = int(landmark.y * src_height)
        x = int(x * dst_width / src_width)
        y = int(y * dst_height / src_height)
        points.append((x, y))

    for start, end in mp_hands.HAND_CONNECTIONS:
        x1, y1 = points[start]
        x2, y2 = points[end]
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    for x, y in points:
        cv2.circle(frame, (x, y), 3, (255, 0, 0), -1)


while True:
    ret, frame = cap.read()
    if not ret:
        print("Gagal membaca frame dari kamera. Pastikan indeks kamera benar.")
        break

    frame = cv2.flip(frame, 1)
    process_frame = cv2.resize(frame, (PROCESS_WIDTH, PROCESS_HEIGHT))
    img_rgb = cv2.cvtColor(process_frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    blur = False
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            _, raised_count = count_raised_fingers(hand_landmarks)
            if raised_count > 0:
                blur = True

    display_frame = frame.copy()
    if blur:
        display_frame = cv2.GaussianBlur(display_frame, BLUR_SIZE, 0)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            draw_hand_skeleton(
                display_frame,
                hand_landmarks,
                PROCESS_WIDTH,
                PROCESS_HEIGHT,
                frame.shape[1],
                frame.shape[0],
            )

    cv2.namedWindow("TikTok Trend: Foto Kita Blur", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("TikTok Trend: Foto Kita Blur", 640, 480)
    cv2.imshow("TikTok Trend: Foto Kita Blur", display_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()