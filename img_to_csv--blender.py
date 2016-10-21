#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Léo M. July 2016, Public Domain
import sys, os, bpy, math
from os.path import basename

path = '/Users/leo/Travail/ongoing/A.009. Script illustrator François/test-img.jpg'

def pixel_values(image, x, y):
    '''Return the RGB values of a given pixel in a given image,
    using a left to right, top to bottom order
    (blender use a bottom to top order)
    Image, int -> Array'''
    pixels = image.pixels
    w = image.size[0] # image height
    h = image.size[1] # image width
    c = 4; # colour canals : RGBA = 4
    base = ( w * c ) * ( h - y - 1) + ( x * c ) # Pixel information start at this position
    R_pos = base + 0 ; # R
    G_pos = base + 1; # G
    B_pos = base + 2; # B
    # A_pos = base + 3; # A
    return [ int( pixels[R_pos] * 255), int( pixels[G_pos] * 255), int(  pixels[B_pos] * 255) ]

def main():

    bpy.ops.image.open(filepath=path)
    for image in bpy.data.images:
        directory = os.path.dirname(image.filepath)
        filename = os.path.splitext(image.filepath)[0].split("/")[-1]
        pixels = "";
        for y in range(image.size[1]):
            for x in range(image.size[0]):
                pixels += str( pixel_values(image, x, y) )
                if x < image.size[1]:
                    pixels += "|"
            if y < image.size[0]-1:
                pixels += "\n"
        file = open(directory+"/"+filename+".csv", "w")
        file.write(pixels)
        file.close()

main()
