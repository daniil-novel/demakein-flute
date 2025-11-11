#!/usr/bin/env python
# -*- coding: utf-8 -*-

import demakein
from demakein import design, design_flute

class Design_diagonal_flute(design_flute.Tapered_flute):
    """
    Простая стандартная флейта 30 см с амбушюрным отверстием в размер канала
    """
    transpose = 12  # Транспозиция для получения нужной длины
    
    embextra = 1.0  # Амбушюрное отверстие в размер канала
    
    n_holes = 6  # 6 основных отверстий
    
    # Простые диаметры отверстий
    min_hole_diameters = [4.0, 4.0, 4.0, 4.0, 4.0, 4.0]
    max_hole_diameters = [6.0, 6.0, 6.0, 6.0, 6.0, 6.0]
    
    # Все отверстия прямые (без диагональных углов)
    hole_horiz_angles = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    
    # Простые аппликатуры
    fingerings = [
        ('C4',  [1, 1, 1, 1, 1, 1]),
        ('D4',  [0, 1, 1, 1, 1, 1]),
        ('E4',  [0, 0, 1, 1, 1, 1]),
        ('F4',  [0, 0, 0, 1, 1, 1]),
        ('G4',  [0, 0, 0, 0, 1, 1]),
        ('A4',  [0, 0, 0, 0, 0, 1]),
        ('B4',  [0, 0, 0, 0, 0, 0]),
        
        ('C5',  [1, 1, 1, 1, 1, 0]),
        ('D5',  [0, 1, 1, 1, 1, 0]),
        ('E5',  [0, 0, 1, 1, 1, 0]),
    ]
    
    # Длина основана на длине волны с транспозицией
    initial_length = design.wavelength('C4') * 0.5


class Design_diagonal_flute_advanced(Design_diagonal_flute):
    """
    Продвинутая диагональная флейта с более сложной геометрией
    """
    
    # Больше отверстий для расширенного диапазона
    n_holes = 10
    
    min_hole_diameters = [3.0, 4.0, 4.5, 5.0, 5.5, 6.0, 4.0, 3.5, 4.0, 3.0]
    max_hole_diameters = [5.0, 6.0, 6.5, 7.0, 7.5, 8.0, 6.0, 5.5, 6.0, 5.0]
    
    # Более сложная диагональная схема
    hole_horiz_angles = [
        0.0,    # 1-е отверстие
        20.0,   # 2-е отверстие - вправо
        -20.0,  # 3-е отверстие - влево
        40.0,   # 4-е отверстие - сильно вправо
        -40.0,  # 5-е отверстие - сильно влево
        60.0,   # 6-е отверстие - очень сильно вправо
        -60.0,  # 7-е отверстие - очень сильно влево
        30.0,   # 8-е отверстие - умеренно вправо
        -30.0,  # 9-е отверстие - умеренно влево
        0.0     # 10-е отверстие - прямо
    ]
    
    hole_angles = [
        0.0,    # 1-е отверстие
        -3.0,   # 2-е отверстие
        -3.0,   # 3-е отверстие
        -6.0,   # 4-е отверстие
        -6.0,   # 5-е отверстие
        -12.0,  # 6-е отверстие
        -12.0,  # 7-е отверстие
        -18.0,  # 8-е отверстие
        -18.0,  # 9-е отверстие
        -25.0   # 10-е отверстие
    ]
    
    # Расширенные аппликатуры
    fingerings = [
        # Основная октава
        ('C4',  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
        ('D4',  [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
        ('E4',  [0, 0, 1, 1, 1, 1, 1, 1, 1, 1]),
        ('F4',  [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]),
        ('G4',  [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]),
        ('A4',  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]),
        ('B4',  [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]),
        ('C5',  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]),
        
        # Дополнительные ноты
        ('C#4', [1, 0, 1, 1, 1, 1, 1, 1, 1, 1]),
        ('D#4', [0, 1, 0, 1, 1, 1, 1, 1, 1, 1]),
        ('F#4', [0, 0, 0, 1, 0, 1, 1, 1, 1, 1]),
        ('G#4', [0, 0, 0, 0, 1, 0, 1, 1, 1, 1]),
        ('A#4', [0, 0, 0, 0, 0, 1, 0, 1, 1, 1]),
        
        # Верхний регистр
        ('D5',  [0, 1, 1, 1, 1, 1, 1, 1, 0, 0]),
        ('E5',  [0, 0, 1, 1, 1, 1, 1, 1, 0, 0]),
        ('F5',  [0, 0, 0, 1, 1, 1, 1, 1, 0, 0]),
        ('G5',  [0, 0, 0, 0, 1, 1, 1, 1, 0, 0]),
        ('A5',  [0, 0, 0, 0, 0, 1, 1, 1, 0, 0]),
        ('B5',  [0, 0, 0, 0, 0, 0, 1, 1, 0, 0]),
        ('C6',  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]),
    ]


if __name__ == '__main__':
    import sys
    import os
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'design-diagonal' or sys.argv[1] == 'Design_diagonal_flute':
            if len(sys.argv) < 3:
                print("Usage: python design_diagonal_flute.py design-diagonal <output_dir>")
                sys.exit(1)
            
            output_dir = sys.argv[2]
            os.makedirs(output_dir, exist_ok=True)
            
            design = Design_diagonal_flute()
            design.output_dir = output_dir
            design.run()
            
        elif sys.argv[1] == 'design-diagonal-advanced' or sys.argv[1] == 'Design_diagonal_flute_advanced':
            if len(sys.argv) < 3:
                print("Usage: python design_diagonal_flute.py design-diagonal-advanced <output_dir>")
                sys.exit(1)
            
            output_dir = sys.argv[2]
            os.makedirs(output_dir, exist_ok=True)
            
            design = Design_diagonal_flute_advanced()
            design.output_dir = output_dir
            design.run()
            
        elif sys.argv[1] == 'make-flute':
            if len(sys.argv) < 4:
                print("Usage: python design_diagonal_flute.py make-flute <input_file> <output_dir>")
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
            print("  design-diagonal <output_dir>          - Design basic diagonal flute")
            print("  design-diagonal-advanced <output_dir> - Design advanced diagonal flute")
            print("  make-flute <input_file> <output_dir>  - Make 3D models from design")
    else:
        print("Available commands:")
        print("  design-diagonal <output_dir>          - Design basic diagonal flute")
        print("  design-diagonal-advanced <output_dir> - Design advanced diagonal flute")
        print("  make-flute <input_file> <output_dir>  - Make 3D models from design")
