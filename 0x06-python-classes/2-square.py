#!/usr/bin/python3
"""Definws class. has a size"""
def __init__(self, size=0):
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise valueError("size must be >= 0")
    self.__size = size
