import cv2
import mediapipe as mp

# Initialize MediaPipe Hand module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Open the webcam
cap = cv2.VideoCapture(1)

# Function to count extended fingers
def count_fingers(hand_landmarks, handedness):
    finger_tips = [4, 8, 12, 16, 20]  # Thumb, Index, Middle, Ring, Little finger tips
    finger_mcp = [2, 6, 10, 14, 18]  # Corresponding MCP joints
    
    fingers = []
    
    # Thumb condition based on hand orientation
    thumb_tip = hand_landmarks.landmark[finger_tips[0]]
    thumb_mcp = hand_landmarks.landmark[finger_mcp[0]]
    if handedness == "Right":
        fingers.append(thumb_tip.x > thumb_mcp.x)  # Right hand: Tip should be to the right of MCP
    else:
        fingers.append(thumb_tip.x < thumb_mcp.x)  # Left hand: Tip should be to the left of MCP
    
    # Check other fingers normally using y-coordinates
    for tip, mcp in zip(finger_tips[1:], finger_mcp[1:]):
        fingers.append(hand_landmarks.landmark[tip].y < hand_landmarks.landmark[mcp].y)
    
    return sum(fingers)  # Count number of extended fingers

# Set up MediaPipe Hands
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=2) as hands:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the image color from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process the frame and detect hands
        results = hands.process(frame_rgb)
        
        total_fingers = 0
        
        # Draw hand landmarks and count fingers
        if results.multi_hand_landmarks and results.multi_handedness:
            for hand_landmarks, handedness_info in zip(results.multi_hand_landmarks, results.multi_handedness):
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Get handedness (Left or Right)
                handedness = handedness_info.classification[0].label
                
                # Count fingers
                fingers_count = count_fingers(hand_landmarks, handedness)
                total_fingers += fingers_count
                
                # Display count on screen
                cv2.putText(frame, f"{handedness} Hand: {fingers_count} fingers", (10, 30 if handedness == "Right" else 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        
        # Display total fingers detected
        cv2.putText(frame, f"Total Fingers: {total_fingers}", (10, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        # Display the result
        cv2.imshow('Hand Detection', frame)
        
        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


# Release resources
cap.release()
cv2.destroyAllWindows()