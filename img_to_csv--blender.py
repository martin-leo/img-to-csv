#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Léo M. July 2016, Public Domain
import sys, os, bpy, math
from os.path import basename

path = '/Users/username/Desktop/nom_du_fichier.jpg'

def print_status(current, maximum):
    '''Output progress in terminal output'''
    output = "\ravancement : " + str( int( current / maximum * 100 ) ) + "%"
    sys.stdout.write(output)
    sys.stdout.flush()

def pixel_values(image, x, y):
    '''Return the RGB values of a given pixel in a given image,
    using a left to right, top to bottom order
    (blender use a bottom to top order)
    Image, int -> Array'''
    pixels = image.pixels
    w = image.size[0] # image height
    h = image.size[1] # image width
    c = 4; # colour canals : RGBA = 4
    base = ( w * c ) * ( h - x - 1) + ( y * c ) # Pixel information start at this position
    R_pos = base + 0 ; # R
    G_pos = base + 1; # G
    B_pos = base + 2; # B
    # A_pos = base + 3; # A
    return [ int( pixels[R_pos] * 255), int( pixels[G_pos] * 255), int(  pixels[B_pos] * 255) ]

def main():
    '''Main function'''
    bpy.ops.image.open(filepath=path) # open file
    for image in bpy.data.images:
        directory = os.path.dirname(image.filepath)
        filename = os.path.splitext(image.filepath)[0].split("/")[-1]

        # using a cursor to display progress
        progress = bpy.context.window_manager
        progress.progress_begin(0, 100)
        # output in the terminal which image we are processing
        print("traitement de" + filename)
        # opening the csv output file
        file = open(directory+"/"+filename+".csv", "w")
        # emptying the output file
        file.seek(0)
        file.truncate()
        # looping through the pixels
        for y in range(image.size[0]):
            csv_line = ""; # buffer for line data
            for x in range(image.size[1]):
                csv_line += str( pixel_values(image, x, y) )
                if x < image.size[1] - 1:
                    csv_line += "|"
            file.write(csv_line + "\n")
            print_status(y, image.size[0])
            progress.progress_update( y / image.size[0] * 100 )
        file.close()
        print_status(1,1)
        progress.progress_end()
        print("\n")

main()
