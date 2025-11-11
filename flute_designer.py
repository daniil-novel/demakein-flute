#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from demakein.design import Instrument_designer, wavelength

class Flute(Instrument_designer):
    closed_top = False
    transpose = 12 # 12 # 4 # 7

    # Изменяем значение embextra
    embextra = 0.53  # Было 0.53 по умолчанию

    n_holes = 10 # including embouchure hole

    inner_diameters = [8.0, 14.0]
    outer_diameters = [14.0, 20.0]

    min_hole_diameters = [ 2.5,4.5,6.0, 3.0,4.5, 2.5,5.5,5.5, 3.5,5.5]
    max_hole_diameters = [ 2.8,4.8,8.0, 5.0,7.5, 3.9,7.5,7.5, 5.5,7.5]
    # horiz_angles = [ -15.0 ] + [ 0.0 ] * 6 + [ 180.0 ]
    hole_horiz_angles = [ -15.0, 0.0, 0.0, 180.0, 0.0,  15.0, 0.0, 0.0, -105.0, 0.0]
    # hole_angles = [ -30, 0, 0, 30, 0 ]

    # balance = [None, None, 0.05, None ]

    fingerings = [
        ('C4',  [1,1,1 ,1, 1, 1,1,1 ,1, 1]),
        ('C5',  [1,1,1 ,1, 1, 1,1,1 ,1, 0]),

        ('C#4', [0,1,1 ,1, 1, 1,1,1 ,1, 1]),
        ('C#5', [0,1,1 ,1, 1, 1,1,1 ,1, 1]),

        ('D4',  [0,0,1 ,1, 1, 1,1,1 ,1, 1]),
        ('D5',  [0,0,1 ,1, 1, 1,1,1 ,1, 1]),

        ('D#4', [0,0,1 ,0, 1, 1,1,1 ,1, 1]),#bottom
        ('D#5', [0,0,1 ,0, 1, 1,1,1 ,1, 1]),

        ('E4',  [0,0,0 ,1, 1, 1,1,1 ,1, 1]),
        ('E5',  [0,0,0 ,1, 1, 1,1,1 ,1, 1]),

        ('F4',  [0,0,0 ,1, 0, 1,1,1 ,1, 1]),
        ('F5',  [0,0,0 ,1, 0, 1,1,1 ,1, 1]),

        ('F#4', [0,0,0 ,1, 0, 0,1,1 ,1, 1]), #pinky
        ('F#5', [0,0,0 ,1, 0, 0,1,1 ,1, 1]),

        ('G4',  [0,0,0 ,1, 0, 0,0,1 ,1, 1]),
        ('G5',  [0,0,0 ,1, 0, 0,0,1 ,1, 1]),

        ('G#4', [0,1,1 ,1, 1, 1,1,0 ,1, 1]), #fork
        ('G#5', [0,0,0 ,1, 0, 1,1,0 ,1, 1]),

        ('A4',  [0,0,0 ,1, 0, 0,0,0 ,1, 1]),
        ('A5',  [0,0,0 ,1, 0, 0,0,0 ,1, 1]),

        ('A#4', [0,0,0 ,1, 0, 0,0,0 ,0, 1]),
        ('A#5', [0,0,0 ,1, 0, 0,0,0 ,0, 1]),

        ('B4',  [0,0,0 ,1, 0, 0,0,0 ,1, 0]),
        ('B5',  [0,0,0 ,1, 0, 0,0,0 ,1, 0]),

    ]

    initial_length = wavelength('C4') * 0.5

    # Параметры для максимальной точности
    ftol = 1e-6  # Уменьшенная tolerance для function value
    xtol = 1e-8  # Уменьшенная tolerance для x values
    initial_accuracy = 0.0001  # Увеличенная начальная точность
    pool_factor = 10  # Увеличенный размер пула

    # Параметры для сверхточного поиска резонанса
    step_cents = 0.1  # Уменьшенный шаг в центах (было 1.0)
    max_steps = 500  # Увеличенное максимальное количество шагов (было 100)

    def true_wavelength_near(self, w, fingers, step_cents=None, max_steps=None):
        """ Переопределенный метод с повышенной точностью """
        if step_cents is None:
            step_cents = self.step_cents
        if max_steps is None:
            max_steps = self.max_steps

        # Вызываем родительский метод с новыми параметрами
        return super().true_wavelength_near(w, fingers, step_cents, max_steps)

    def run(self):
        """ Переопределенный метод run с параметрами максимальной точности """
        import demakein.optimize as optimize

        assert self.initial_length is not None, 'Initial length required'
        assert len(self.min_hole_diameters) == self.n_holes
        assert len(self.max_hole_diameters) == self.n_holes
        assert len(self.hole_angles) == self.n_holes
        assert len(self.inner_diameters) >= 2
        assert len(self.outer_diameters) >= 2

        if not os.path.exists(self.output_dir):
            os.mkdir(self.output_dir)

        state_vec = self.initial_state_vec
        # Используем параметры максимальной точности
        state_vec = optimize.improve(
            self.shell_name(), self._constrainer, self._scorer, state_vec,
            ftol=self.ftol, xtol=self.xtol, initial_accuracy=self.initial_accuracy,
            pool_factor=self.pool_factor, workers=self.workers, monitor=self._save)

        self._save(state_vec)
