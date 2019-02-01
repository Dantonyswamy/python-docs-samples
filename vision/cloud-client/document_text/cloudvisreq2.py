import argparse
import base64
import json
import io
import os
from google.cloud import vision
from google.cloud.vision import types




def main():

    client = vision.ImageAnnotatorClient()

    # text.png is the image file.
    with io.open('sample.jpg', 'rb') as image_file:
       content = image_file.read()
       image = types.Image(content=content)

    response = client.text_detection(image=image)

    return response

if __name__ == '__main__':

    response=main()

    texts = response.text_annotations
    with open('newfile.txt','w', encoding='utf-8') as outfile:
        for text in texts:
           outfile.write(text.description+'\n')
