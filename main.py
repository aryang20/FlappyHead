import cv2
import mediapipe as mp
import pygame

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)
pygame.init()


cap = cv2.VideoCapture(0)
screenWidth = 800
screenHeight = 800
screen = pygame.display.set_mode([screenWidth, screenHeight])
running = True
pipePath = "images/pipe_sprite_single.png"
spritePath = "/images/flap.png"


class Pipe:
    def __init__(self, speed=5):
        self.speed = speed
        self.x = screenWidth
    def move(self):
        self.x -= self.speed
    def draw(self):
        pass 



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ret, frame = cap.read()
    if not ret:
        break
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(frame_rgb)
    if results.detections:
        for detection in results.detections:
            mp_drawing.draw_detection(frame, detection)
    flipped_frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    flipped_frame_rgb = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2RGB)
    frame_surface = pygame.surfarray.make_surface(flipped_frame_rgb)
    screen.blit(frame_surface, (0, 0))
    pygame.display.flip()

