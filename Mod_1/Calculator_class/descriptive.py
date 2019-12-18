#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""
import math


class Calculator:
    def __init__(self, data):
        self.data = sorted(data)
        self.update_data()

    def update_data(self):
        self.length = self._calc_length()
        self.mean = self._calc_mean()
        self.median = self._calc_median()
        self.variance = self._calc_variance()
        self.stand_dev = self._calc_stand_dev()

    def add_data(self, new_data):
        self.data.extend(new_data)
        self.data = sorted(self.data)
        self.update_data()

    def remove_data(self, old_data):
        self.data = [d for d in self.data if d not in old_data]
        self.update_data()

    def _calc_mean(self):
        return (sum(self.data) / len(self.data))

    def _calc_length(self):
        return len(self.data)

    def _calc_median(self):
        if len(self.data) % 2 == 0:
            mid_left = self.data[len(self.data) // 2 - 1]
            mid_right = self.data[len(self.data) // 2]
            avg = (mid_left + mid_right) / 2
        else:
            avg = self.data[len(self.data) // 2]
        return avg

    def _calc_variance(self):
        avg_x = (sum(self.data) / len(self.data))
        added_up = []
        for item in self.data:
            added_up.append((item - avg_x)**2)
        return (sum(added_up) / (len(self.data) - 1))

    def _calc_stand_dev(self):
        return math.sqrt(self.variance)