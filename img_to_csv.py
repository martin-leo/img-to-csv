#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Léo M. July 2016, Public Domain
import sys, os, subprocess
from PIL import Image
from os.path import basename

def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

path = sys.argv[1]
directory = os.path.dirname(path)
filename = os.path.splitext(path)[0].split("/")[-1]
image = Image.open(path)
pixelAccess_object = image.load()

pixels = "";
for x in range(image.size[0]):
    for y in range(image.size[1]):
        pixels += str(list(pixelAccess_object[x,y]))
        if y < image.size[1]-1:
            pixels += "|"
    if x < image.size[0]-1:
        pixels += "\n"

file = open(directory+"/"+filename+".csv", "w")
file.write(pixels)
file.close()
