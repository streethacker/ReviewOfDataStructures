#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
bubble sort implementation, basic concepts:
promote the minimum item one by one, from end to beginning.
"""

def BubbleSort(alist):
	for i in range(0, len(alist)):
		for j in range(len(alist)-1, i, -1):
			if alist[j] < alist[j-1]:
				alist[j], alist[j-1] = alist[j-1], alist[j]

	return True

if __name__ == "__main__":
	arr = [99, 82, 107, 16, 2, 8, 104, 33, 24, 32, 64]
	BubbleSort(arr)

	for item in arr:
		print item,
