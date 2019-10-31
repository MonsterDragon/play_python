#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

def avg(grade_list):
    sum = 0
    for i in grade_list:
        sum += i
    return sum/len(grade_list)

def drop_first_last(grades):
    first, *middle, last = grades
    print(middle, *middle)
    return avg(middle)

if __name__ == "__main__":
    print(drop_first_last((98, 96, 100, 89, 99, 97)))
