# engine_face.py

from deepface import DeepFace
import numpy as np
import cv2



class FaceEngine:
    def __init__(self):
        self.model_name = "ArcFace"
        self.detector = "mediapipe"
        self.threshold = 0.5