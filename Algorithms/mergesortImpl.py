#!/usr/bin/env python
#-*- coding:utf-8 -*-

def merge(left, right):
	result = []
	i = 0
	j = 0

	while i<len(left) and j<len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
			continue
		else:
			result.append(right[j])
			j += 1
			continue

	if i == len(left):
		result.extend(right[j:])
	else:
		result.extend(left[i:])

	return result

def mergesort(alist):
	if len(alist) == 1:
		return alist

	mid = len(alist) / 2

	left, right = alist[:mid], alist[mid:]

	return merge(mergesort(left), mergesort(right))

if __name__ == "__main__":
	alist = [1, 29, 22, 100, 37, 88, 64, 23, 17, 10]
	result = mergesort(alist)

	for val in result:
		print val,
