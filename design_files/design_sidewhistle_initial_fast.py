#!/usr/bin/env pypy
# -*- coding: utf-8 -*-
# 
# БЫСТРАЯ ВЕРСИЯ - пониженная точность для ускорения расчетов
# Подходит для предварительных прогонов и тестирования

import demakein
from demakein import design, design_flute
import sys
import os

class Design_shaku_fast(design_flute.Tapered_flute):
    transpose = 10
    
    n_holes = 10+1  # including embouchure hole
    
    min_hole_diameters = [ 2.5,4.5,6.0, 4.5,4.5, 3.5,5.5,5.5, 3.5,5.5, 9.5 ]
    max_hole_diameters = [ 4.5,6.0,8.0, 6.0,5.5, 6.0,7.5,7.5, 6.5,7.5, 10.0 ]
    hole_horiz_angles = [ -15.0, -15.0, 0.0, 0.0, 0.0,  0.0, 180.0, 0.0, 0.0, -105.0, 0.0]
    
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
    
        ('G4',  [0,0, 0,0,0, 1, 1,1,1, 1, 0]),
        ('G5',  [0,0, 0,0,0, 1, 1,1,1, 1, 0]),
        
        ('G#4', [0,0, 0,0,1, 0, 1,1,1, 1, 0]),
        ('G#5', [0,0, 0,0,1, 0, 1,1,1, 1, 0]),
        
        ('A4',  [0,0, 0,0,0, 1, 0,1,1, 1, 0]),
        ('A5',  [0,0, 0,0,0, 1, 0,1,1, 1, 0]),
        
        ('B4',  [0,0, 0,0,0, 1, 0,0,1, 1, 0]),
        ('B5',  [0,0, 0,0,0, 1, 0,0,1, 1, 0]),
        
        ('C5',  [0,0, 0,1,0, 0, 1,1,0, 1, 0]),
        ('C6',  [0,0, 0,1,1, 1, 1,1,0, 1, 0]),
        
        ('C#5', [0,0, 0,0,0, 1, 0,0,0, 1, 0]),
        ('C#6', [0,0, 0,0,0, 1, 0,0,0, 1, 0]),
        
        ('D5',  [0,0, 0,0,0, 1,0,1 ,0, 0, 0]),
    ]
    
    initial_length = design.wavelength('C4') * 0.5
    
    # ═══════════════════════════════════════════════════════
    # ПАРАМЕТРЫ УСКОРЕНИЯ (снижение точности для скорости)
    # ═══════════════════════════════════════════════════════
    
    # Уменьшаем размер пула решений (по умолчанию ~200)
    # Меньше = быстрее, но менее точный результат
    max_n_samples = 100  # Вместо ~200 (50% скорости)
    
    # Ускоряем сходимость оптимизации
    # Останавливаемся раньше при достижении приемлемого результата
    max_n_no_improvement = 20  # Вместо 40-50 (быстрее остановка)
    
    # Снижаем точность расчета резонансов
    # Меньше итераций = быстрее расчет
    wavelength_sensitivity = 0.02  # Вместо 0.01 (менее точно, но в 2 раза быстрее)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: pypy3.10 design_sidewhistle_initial_fast.py <output_dir> [--workers N]")
        print("")
        print("БЫСТРАЯ ВЕРСИЯ - пониженная точность для ускорения")
        print("Примерно в 2-3 раза быстрее стандартной версии")
        print("")
        sys.exit(1)
    
    output_dir = sys.argv[1]
    
    workers = None
    for i, arg in enumerate(sys.argv):
        if arg == '--workers' and i + 1 < len(sys.argv):
            workers = int(sys.argv[i + 1])
            break
    
    os.makedirs(output_dir, exist_ok=True)
    
    print("=" * 60)
    print("БЫСТРЫЙ РЕЖИМ - некоторые параметры снижены для скорости")
    print("max_n_samples: 100 (норма: ~200)")
    print("max_n_no_improvement: 20 (норма: ~40)")
    print("wavelength_sensitivity: 0.02 (норма: 0.01)")
    print("=" * 60)
    print("")
    
    design_instance = Design_shaku_fast()
    design_instance.output_dir = output_dir
    if workers is not None:
        design_instance.n_worker_processes = workers
    design_instance.run()