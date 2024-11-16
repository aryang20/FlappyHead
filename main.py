import cv2 
import mediapipe as mp
import sys, time, random
import pygame
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
pygame.init()
cap = cv2.VideoCapture(0)
screenWidth = 800
screenHeight = 800
screen = pygame.display.set_mode([screenWidth, screenHeight])
running = True
while  running:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  ret, frame = cap.read(0)
  if not ret:
    break
  
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  fliped_jawn = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
  frame_surface = pygame.surfarray.make_surface(fliped_jawn)
  screen.blit(frame_surface, (0, 0))
  pygame.display.flip()
  
  
  




















