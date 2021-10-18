#!/usr/bin/python3
import json
import requests
from pprint import pprint
from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image


def main():
 while True:
     camera = PiCamera()
     stream = BytesIO()
     camera.start_preview()
     sleep(2)
     camera.capture(stream, format='jpeg')
     stream.seek(0)

     response = requests.post(
             'https://api.platerecognizer.com/v1/plate-reader/',
             #data=dict(regions=['us-ca'], config=json.dumps(dict(region="strict"))),  # Optional
             files=dict(upload=stream.read()),
             headers={'Authorization': 'Token 4632e5c9355e589155eb276c630d7d798fbc93bd'})
     response = response.json()
     #pprint(response)
     amount = response['results']

     count = 0
     for count, x in enumerate(amount):
             plate = response['results'][count]['plate']
             score = response['results'][count]['score']

             if float(score) < 0.70:
                     print("Couldn't find license plate or accuracy too low.")
             else:
                     print("Accuracy:  " + str(score))
                     print("Plate: " + str(plate))
             count += 1
     camera.close()
     #camera.stop_preview()
     sleep(2)

if __name__ == '__main__':  # run tests if called from command-line
    main()

