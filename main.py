import cv2
import mediapipe as mp
import sys, time, random
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


pipePath = "/images/pipe_sprite_single.png"
flapPath = "/images/flap.png"

class Pipe:
    def __init__(self):
        self.gap = 200  
        self.width = 80
        self.x = screenWidth
        self.height = random.randint(150, screenHeight - 150 - self.gap)
        self.color = (0, 255, 0)  
        self.speed = 5
        
    def move(self):
        self.x -= self.speed
        
    def draw(self, screen):
        # Draw top pipe
        pygame.draw.rect(screen, self.color, (self.x, 0, self.width, self.height))
        # Draw bottom pipe
        bottom_height = screenHeight - (self.height + self.gap)
        pygame.draw.rect(screen, self.color, 
                        (self.x, self.height + self.gap, self.width, bottom_height))
        
    def off_screen(self):
        return self.x + self.width < 0

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















