#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
a simple implementation of the selection sort, the basic concepts:
find the minimum elememt, if not the alist[i], then swap them.
"""

def SelectionSort(alist):
	for i in range(len(alist)):
		minIndex = i
		for j in range(i+1, len(alist)):
			if alist[j] < alist[minIndex]:
				minIndex = j
		if minIndex != i:
			alist[i], alist[minIndex] = alist[minIndex], alist[i]

	return True

if __name__ == "__main__":
	arr = [7, 1024, 3, 92, 88, 14, 9, 12, 102, 200]
	SelectionSort(arr)

	for item in arr:
		print item,
