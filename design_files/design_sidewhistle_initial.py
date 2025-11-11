#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

import demakein, nesoni
from demakein import design, design_flute

class Design_shaku(design_flute.Tapered_flute):#(demakein.Design_recorder):
    transpose = 12 # 12 # 4 # 7

    n_holes = 10+1 # including embouchure hole

    min_hole_diameters = [ 2.5,4.5,6.0, 3.0,4.5, 2.5,5.5,5.5, 3.5,5.5, 9.5 ]
    max_hole_diameters = [ 2.8,4.8,8.0, 5.0,7.5, 3.9,7.5,7.5, 5.5,7.5, 10.0 ]
    # horiz_angles = [ -15.0 ] + [ 0.0 ] * 6 + [ 180.0 ]
    hole_horiz_angles = [ -15.0, 0.0, 0.0, 180.0, 0.0,  15.0, 0.0, 0.0, -105.0, 0.0]
    # hole_angles = [ -30, 0, 0, 30, 0 ]

    # balance = [None, None, 0.05, None ]
    
    fingerings = [
        ('C4',  [1,1,1 ,1, 1, 1,1,1 ,1, 1, 0]),
        ('C5',  [1,1,1 ,1, 1, 1,1,1 ,1, 0, 0]),
      
        ('C#4', [0,1,1 ,1, 1, 1,1,1 ,1, 1, 0]),
        ('C#5', [0,1,1 ,1, 1, 1,1,1 ,1, 1, 0]),

        ('D4',  [0,0,1 ,1, 1, 1,1,1 ,1, 1, 0]),
        ('D5',  [0,0,1 ,1, 1, 1,1,1 ,1, 1, 0]),
      
        ('D#4', [0,0,1 ,0, 1, 1,1,1 ,1, 1, 0]),#bottom
        ('D#5', [0,0,1 ,0, 1, 1,1,1 ,1, 1, 0]),
      
        ('E4',  [0,0,0 ,1, 1, 1,1,1 ,1, 1, 0]),
        ('E5',  [0,0,0 ,1, 1, 1,1,1 ,1, 1, 0]),
 
        ('F4',  [0,0,0 ,1, 0, 1,1,1 ,1, 1, 0]),
        ('F5',  [0,0,0 ,1, 0, 1,1,1 ,1, 1, 0]),
        
        ('F#4', [0,0,0 ,1, 0, 0,1,1 ,1, 1, 0]), #pinky
        ('F#5', [0,0,0 ,1, 0, 0,1,1 ,1, 1, 0]),

        ('G4',  [0,0,0 ,1, 0, 0,0,1 ,1, 1, 0]),
        ('G5',  [0,0,0 ,1, 0, 0,0,1 ,1, 1, 0]),

        ('G#4', [0,1,1 ,1, 1, 1,1,0 ,1, 1, 0]), #fork
        ('G#5', [0,0,0 ,1, 0, 1,1,0 ,1, 1, 0]),

        ('A4',  [0,0,0 ,1, 0, 0,0,0 ,1, 1, 0]),
        ('A5',  [0,0,0 ,1, 0, 0,0,0 ,1, 1, 0]),

        ('A#4', [0,0,0 ,1, 0, 0,0,0 ,0, 1, 0]),
        ('A#5', [0,0,0 ,1, 0, 0,0,0 ,0, 1, 0]),

        ('B4',  [0,0,0 ,1, 0, 0,0,0 ,1, 0, 0]),
        ('B5',  [0,0,0 ,1, 0, 0,0,0 ,1, 0, 0]),
        
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
    nesoni.run_toolbox(
        [ Design_shaku, demakein.Make_flute ],
        show_make_flags=False)

    
