# Создать класс MyTime. Атрибуты: hours, minutes, seconds.
# Методы: переопределить магические методы сравнения (==, !=, >=, <=, <, >).

from __future__ import division

class MyTime:

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

        self.overall = hours * 60 * 60 +minutes * 60 + seconds

    def __add__(self, other):
        ...

    def __sub__(self, other):
        ...
    def __divmod__(self, other):
        ...


    def __eq__(self, other):
        return self.overall == other.overall

    def __ne__(self, other):
        return self.overall != other.overall

    def __ge__(self, other):
        return len(self.word) >= len(other)

    def __le__(self, other):
        return len(self.word) <= len(other)
