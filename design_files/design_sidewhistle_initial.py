#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

import demakein
from demakein import design, design_flute
import sys
import os

class Design_shaku(design_flute.Tapered_flute):#(demakein.Design_recorder):
    transpose = 10 # 12 # 4 # 7

    n_holes = 10+1 # including embouchure hole

    min_hole_diameters = [ 2.5,4.5,6.0, 3.0,4.5, 2.5,5.5,5.5, 3.5,5.5, 9.5 ]
    max_hole_diameters = [ 2.8,4.8,8.0, 5.0,7.5, 3.9,7.5,7.5, 5.5,7.5, 10.0 ]
    # horiz_angles = [ -15.0 ] + [ 0.0 ] * 6 + [ 180.0 ]
    hole_horiz_angles = [ -15.0, 0.0, 0.0, 180.0, 0.0,  15.0, 0.0, 0.0, -105.0, 0.0]
    # hole_angles = [ -30, 0, 0, 30, 0 ]

    # balance = [None, None, 0.05, None ]
    
    fingerings = [
        #        e e  a m i  p  a m i  p  Amb
        ('C4',  [1,1, 1,1,1, 1, 1,1,1, 1, 0]),
        ('C5',  [1,1 ,1,1,1, 1, 1,1,1, 0, 0]),
    
        ('C#4', [0,1, 1,1,1, 1, 1,1,1, 1, 0]),
        ('C#5', [0,1, 1,1,1, 1, 1,1,1, 1, 0]),
    
        ('D4',  [0,0, 1,1,1, 1, 1,1,1, 1, 0]),
        ('D5',  [0,0, 1,1,1, 1, 1,1,1, 1, 0]),
    
        ('E4',  [0,0, 0,1,1, 1, 1,1,1, 1, 0]),
        ('E5',  [0,0, 0,1,1, 1, 1,1,1, 1, 0]),

        ('F#4', [0,0, 0,0,1, 1, 1,1,1, 1, 0]),
        ('F#5', [0,0, 0,0,1, 1, 1,1,1, 1, 0]),
    
        ('G4',  [0,0, 0,0,0, 1, 1,1,1, 1, 0]),#bottom
        ('G5',  [0,0, 0,0,0, 1, 1,1,1, 1, 0]),
        #        e e  a m i  p  a m i  p  Amb
        ('G#4', [0,0, 0,0,1, 0, 1,1,1, 1, 0]),
        ('G#5', [0,0, 0,0,1, 0, 1,1,1, 1, 0]),
        #        e e  a m i  p  a m i  p  Amb
        ('A4',  [0,0, 0,0,0, 1, 0,1,1, 1, 0]),
        ('A5',  [0,0, 0,0,0, 1, 0,1,1, 1, 0]),
        #        e e  a m i  p  a m i  p  Amb
        ('B4',  [0,0, 0,0,0, 1, 0,0,1, 1, 0]), #pinky
        ('B5',  [0,0, 0,0,0, 1, 0,0,1, 1, 0]),
        #        e e  a m i  p  a m i  p  Amb
        ('C5',  [0,0, 0,1,0, 1, 1,1,0, 1, 0]),
        ('C6',  [0,0, 0,1,0, 1, 1,1,0, 1, 0]),
        #        e e  a m i  p  a m i  p  Amb
        ('C#5', [0,0, 0,0,0, 1, 0,0,0, 1, 0]), #fork
        ('C#6', [0,0, 0,0,0, 1, 0,0,0, 1, 0]),
        #        e e  a m i  p  a m i  p  Amb
        ('D5',  [0,0, 0,0,0, 1,0,0 ,1, 0, 0]),
        ]
    

    # inner_diameters = [ 
    #     (8.0, 14.0), 
    #     # (17.0, 17.0), 
    #     # (22.0, 22.0),
    #     # (26.0, 26.0),
    #     # (26.0, 27.0),
    #     # (28.0, 31.0),
    #     (9.0, 14.0)
    #     ]
    

    # # in this case ~diameter = thickness * 2~
    # outer_add = True
    # outer_diameters = [ 10.0, 10.0]
    # outer_fractions = []
    # initial_outer_fractions = []

    # initial_inner_fractions = [] # [ 0.135, 0.176, 0.235, 0.276 ]
    # min_inner_fraction_sep = [ 0.05 ]
    
    initial_length = design.wavelength('C4') * 0.5



if __name__ == '__main__':
    # Simple argument parser to replace nesoni.run_toolbox
    if len(sys.argv) < 2:
        print("Usage: python design_sidewhistle_initial.py <output_dir> [--workers N]")
        sys.exit(1)
    
    output_dir = sys.argv[1]
    
    # Parse workers argument if provided
    workers = None
    for i, arg in enumerate(sys.argv):
        if arg == '--workers' and i + 1 < len(sys.argv):
            workers = int(sys.argv[i + 1])
            break
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Create and run the design
    design_instance = Design_shaku()
    design_instance.output_dir = output_dir
    if workers is not None:
        design_instance.n_worker_processes = workers
    design_instance.run()
