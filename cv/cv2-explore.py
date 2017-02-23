#!/usr/bin/env python

import io
import pkg_resources
import sys
from time import sleep
from pprint import pprint
import cv2
import picamera
import numpy

pprint({
    'cv2': cv2.__version__,
    'picamera': pkg_resources.get_distribution("picamera").version
})

FACES = '/opt/opencv/data/haarcascades/haarcascade_frontalface_default.xml'
TEMP_IMAGE_PATH = 'shot.jpg'


def extract_features(image):
    face_cascade = FACES


if __name__ == '__main__':
    print("Make picture,...")

    stream = io.BytesIO()

    with picamera.PiCamera() as camera:
        camera.resolution = (600, 500)
        camera.vflip = True
        camera.hflip = True
        camera.capture(stream, format='jpeg')

    buff = numpy.fromstring(stream.getvalue(), dtype=numpy.uint8)
    image = cv2.imdecode(buff, 1)

    face_cascade = cv2.CascadeClassifier(FACES)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    pprint(faces)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 100, 100), 2)

    cv2.imwrite('result.jpg', image)

    #    print("Found {} faces".format(len(faces)))
