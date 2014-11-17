#!/usr/bin/env python
#-*- coding:utf-8 -*-

def concatenate(less, equal, greater):
	result = []
	
	result.extend(less)
	result.extend(equal)
	result.extend(greater)

	return result

def quicksort(alist):
	if len(alist) <= 1:
		return alist

	less, equal, greater = [], [], []

	pivot = alist[0]
	
	for val in alist:
		if val == pivot:
			equal.append(val)
		elif val < pivot:
			less.append(val)
		else:
			greater.append(val)

	return concatenate(quicksort(less), equal, quicksort(greater))

if __name__ == "__main__":
	alist = [3, 8, 19, 22, 17, 100, 77, 64, 32, 30]
	result = quicksort(alist)
	
	for val in result:
		print val,
