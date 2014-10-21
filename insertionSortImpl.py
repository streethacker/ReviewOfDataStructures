#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
simple implementation of insertion sort, like pick up cards and insert into the right place.
"""

def InsertionSort(alist):
	for i in range(1, len(alist)):
		pos, pickup = i, alist[i]
		while pos > 0 and pickup  < alist[pos-1]:
			alist[pos] = alist[pos-1]
			pos -= 1
		alist[pos] = pickup
	return True

if __name__ == "__main__":
	arr = [99, 8, 102, 4, 55, 64, 71, 32, 1024]
	InsertionSort(arr)

	for item in arr:
		print item,
