#!/usr/bin/env python
# -*- coding: utf-8 -*-

import demakein
from demakein import design, design_flute

class Design_flute_embouchure(design_flute.Tapered_flute):
    transpose = 12 # 12 # 4 # 7

    # Изменяем значение embextra
    embextra = 0.53  # Было 0.53 по умолчанию

    n_holes = 11 # добавляем амбушюрное отверстие + 10 игровых отверстий

    # Первое отверстие - амбушюрное (размер канала), остальные - игровые
    min_hole_diameters = [ 8.0, 2.5,4.5,6.0, 3.0,4.5, 2.5,5.5,5.5, 3.5,5.5]
    max_hole_diameters = [ 14.0, 2.8,4.8,8.0, 5.0,7.5, 3.9,7.5,7.5, 5.5,7.5]
    
    # Амбушюрное отверстие под углом 90 градусов (боковое), остальные как в оригинале
    hole_horiz_angles = [ 90.0, 0.0, 0.0, 180.0, 0.0,  15.0, 0.0, 0.0, -105.0, 0.0, 0.0]

    # Аппликатуры с учетом амбушюрного отверстия (первая позиция всегда 0 - открыто)
    fingerings = [
        ('C4',  [0,1,1,1 ,1, 1, 1,1,1 ,1, 1]),
        ('C5',  [0,1,1,1 ,1, 1, 1,1,1 ,1, 0]),
      
        ('C#4', [0,0,1,1 ,1, 1, 1,1,1 ,1, 1]),
        ('C#5', [0,0,1,1 ,1, 1, 1,1,1 ,1, 1]),

        ('D4',  [0,0,0,1 ,1, 1, 1,1,1 ,1, 1]),
        ('D5',  [0,0,0,1 ,1, 1, 1,1,1 ,1, 1]),
      
        ('D#4', [0,0,0,1 ,0, 1, 1,1,1 ,1, 1]),#bottom
        ('D#5', [0,0,0,1 ,0, 1, 1,1,1 ,1, 1]),
      
        ('E4',  [0,0,0,0 ,1, 1, 1,1,1 ,1, 1]),
        ('E5',  [0,0,0,0 ,1, 1, 1,1,1 ,1, 1]),
 
        ('F4',  [0,0,0,0 ,1, 0, 1,1,1 ,1, 1]),
        ('F5',  [0,0,0,0 ,1, 0, 1,1,1 ,1, 1]),
        
        ('F#4', [0,0,0,0 ,1, 0, 0,1,1 ,1, 1]), #pinky
        ('F#5', [0,0,0,0 ,1, 0, 0,1,1 ,1, 1]),

        ('G4',  [0,0,0,0 ,1, 0, 0,0,1 ,1, 1]),
        ('G5',  [0,0,0,0 ,1, 0, 0,0,1 ,1, 1]),

        ('G#4', [0,0,1,1 ,1, 1, 1,1,0 ,1, 1]), #fork
        ('G#5', [0,0,0,0 ,1, 0, 1,1,0 ,1, 1]),

        ('A4',  [0,0,0,0 ,1, 0, 0,0,0 ,1, 1]),
        ('A5',  [0,0,0,0 ,1, 0, 0,0,0 ,1, 1]),

        ('A#4', [0,0,0,0 ,1, 0, 0,0,0 ,0, 1]),
        ('A#5', [0,0,0,0 ,1, 0, 0,0,0 ,0, 1]),

        ('B4',  [0,0,0,0 ,1, 0, 0,0,0 ,1, 0]),
        ('B5',  [0,0,0,0 ,1, 0, 0,0,0 ,1, 0]),
        
    ]
    
    initial_length = design.wavelength('C4') * 0.5

    # Настройки для амбушюрного отверстия
    # Амбушюрное отверстие должно быть расположено ближе к верхней части флейты
    hole_fractions = [0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.90, 0.95]


if __name__ == '__main__':
    import sys
    import os
    
    # Простая замена nesoni.run_toolbox
    if len(sys.argv) > 1:
        if sys.argv[1] == 'design-flute-embouchure' or sys.argv[1] == 'Design_flute_embouchure':
            if len(sys.argv) < 3:
                print("Usage: python design_flute_embouchure.py design-flute-embouchure <output_dir>")
                sys.exit(1)
            
            output_dir = sys.argv[2]
            # Создаем директорию если не существует
            os.makedirs(output_dir, exist_ok=True)
            
            # Создаем экземпляр и устанавливаем выходную директорию
            design = Design_flute_embouchure()
            design.output_dir = output_dir
            design.run()
            
        elif sys.argv[1] == 'make-flute':
            if len(sys.argv) < 4:
                print("Usage: python design_flute_embouchure.py make-flute <input_file> <output_dir>")
                sys.exit(1)
                
            input_file = sys.argv[2]
            output_dir = sys.argv[3]
            os.makedirs(output_dir, exist_ok=True)
            
            make_flute = demakein.Make_flute()
            make_flute.input_file = input_file
            make_flute.output_dir = output_dir
            make_flute.run()
        else:
            print("Available commands:")
            print("  design-flute-embouchure <output_dir>    - Design the embouchure flute")
            print("  make-flute <input_file> <output_dir>      - Make 3D models from design")
    else:
        print("Available commands:")
        print("  design-flute-embouchure <output_dir>    - Design the embouchure flute")
        print("  make-flute <input_file> <output_dir>      - Make 3D models from design")
