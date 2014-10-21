#!/usr/bin/env python
#-*- coding:utf-8 -*-

def BinarySearch(alist, value):
	left, right = 0, len(alist)-1

	while left <= right:
		mid = (left + right) / 2
		if alist[mid] == value:
			return mid
		elif value < alist[mid]:
			right = mid - 1
		else:
			left = mid + 1

	return None

if __name__ == "__main__":
	arr = sorted([44, 3, 190, 23, 64, 10, 112, 99])
	print arr

	print "190:", BinarySearch(arr, 190)
	print "10:", BinarySearch(arr, 10)
	print "64:", BinarySearch(arr, 64)
