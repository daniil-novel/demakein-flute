#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
#
# Флейта для Александра Евгеньевича - транспонирована на 1 тон ниже (Bb вместо C)
# Flute for Aleksandr Evgenievich - transposed 1 whole tone lower (Bb instead of C)

import demakein, nesoni
from demakein import design, design_flute

class Design_shaku(design_flute.Tapered_flute):#(demakein.Design_recorder):
    transpose = 10  # Изменено с 12 на 10 (1 тон ниже = -2 полутона)

    n_holes = 10+1 # including embouchure hole

    min_hole_diameters = [ 2.5,4.5,6.0, 3.0,4.5, 2.5,5.5,5.5, 3.5,5.5, 9.5 ]
    max_hole_diameters = [ 2.8,4.8,8.0, 5.0,7.5, 3.9,7.5,7.5, 5.5,7.5, 10.0 ]
    # horiz_angles = [ -15.0 ] + [ 0.0 ] * 6 + [ 180.0 ]
    hole_horiz_angles = [ -15.0, 0.0, 0.0, 180.0, 0.0,  15.0, 0.0, 0.0, -105.0, 0.0]
    # hole_angles = [ -30, 0, 0, 30, 0 ]

    # balance = [None, None, 0.05, None ]
    
    # Аппликатуры транспонированы на 1 тон ниже
    # Fingerings transposed down by 1 whole tone
    fingerings = [
        ('Bb3', [1,1,1 ,1, 1, 1,1,1 ,1, 1, 0]),  # было C4
        ('Bb4', [1,1,1 ,1, 1, 1,1,1 ,1, 0, 0]),  # было C5
      
        ('B3',  [0,1,1 ,1, 1, 1,1,1 ,1, 1, 0]),  # было C#4
        ('B4',  [0,1,1 ,1, 1, 1,1,1 ,1, 1, 0]),  # было C#5

        ('C4',  [0,0,1 ,1, 1, 1,1,1 ,1, 1, 0]),  # было D4
        ('C5',  [0,0,1 ,1, 1, 1,1,1 ,1, 1, 0]),  # было D5
      
        ('D4',  [0,0,0 ,1, 1, 1,1,1 ,1, 1, 0]),  # было D#4 #bottom
        ('D5',  [0,0,0 ,1, 1, 1,1,1 ,1, 1, 0]),  # было D#5
      
        ('E4',  [0,0,0 ,0, 1, 1,1,1 ,1, 1, 0]),  # было E4
        ('E5',  [0,0,0 ,0, 1, 1,1,1 ,1, 1, 0]),  # было E5
 
        ('F4',  [0,0,0 ,0, 0, 1,1,1 ,1, 1, 0]),  # было F4
        ('F5',  [0,0,0 ,0, 0, 1,1,1 ,1, 1, 0]),  # было F5
        
        ('F#4', [0,0,0 ,0, 1, 0,1,1 ,1, 1, 0]),  # было F#4 #pinky
        ('F#5', [0,0,0 ,0, 1, 0,1,1 ,1, 1, 0]),  # было F#5

        ('G4',  [0,0,0 ,0, 0, 1,0,1 ,1, 1, 0]),  # было G4
        ('G5',  [0,0,0 ,0, 0, 1,0,1 ,1, 1, 0]),  # было G5

        ('A4',  [0,0,0 ,0, 0, 1,0,0 ,1, 1, 0]),  # было G4
        ('A5',  [0,0,0 ,0, 0, 1,0,0 ,1, 1, 0]),  # было G5

        ('A#4', [0,0,0 ,1, 0, 1,1,1 ,0, 1, 0]),  # было A#4
        ('A#5', [0,0,0 ,1, 0, 1,1,1 ,0, 1, 0]),  # было A#5

        ('B4',  [0,0,0 ,0, 0, 1,0,0 ,0, 1, 0]),  # было A4
        ('B5',  [0,0,0 ,0, 0, 1,0,0 ,0, 1, 0]),  # было A5

        ('C5',  [0,0,0 ,0, 0, 0,0,0 ,0, 0, 0]),  # было B4
        
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
    
    # Начальная длина изменена для Bb3 вместо C4
    # Initial length changed for Bb3 instead of C4
    initial_length = design.wavelength('Bb3') * 0.5



if __name__ == '__main__':
    nesoni.run_toolbox(
        [ Design_shaku, demakein.Make_flute ],
        show_make_flags=False)
