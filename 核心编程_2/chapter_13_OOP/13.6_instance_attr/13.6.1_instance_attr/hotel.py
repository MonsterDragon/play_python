#! /usr/bin/env python3
# -*- coding : UTF-8 -*-

class HotelRoom(object):
    "Hotel room rate calculate"
    def __init__(self, rt, sales=0.085, rm=0.1)
        """HotelRoomCalc default arguements"""
        self.saleTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self, days=1):
        """Calculate total"""
        daily = round((self.roomRate)*(1 + self.roomTax + self.saleTax), 2)
        return float(days * daily)

