#!/usr/bin/env python
#-*- coding:utf-8 -*-

class MinHeap(object):
	"""
	a simple implementation of Minimum Heap, based on python's list.
	supporting for the following functions:
		a.fetchMinItem(self): pop the minimum item of in the heap, O(1) complexity;
		b.peekMinItem(self): get(but not pop) the minimum item of the heap, O(1) too;
		c.addItem(self, value): insert an item into the heap, then validate the order automatically;
		d.removeItem(self, value): remove an item from the heap, then validate the order automatically;
		e.containItem(self, value): verify if an item exists in the heap;
		f.traverseItem(self, func): visit the items one by one, with the given function func;
	"""
	def __init__(self):
		self._itemList = []
		self._counter = 0

	def fetchMinItem(self):
		self._counter -= 1
		return self._itemList.pop(0)

	def peekMinItem(self):
		return self._itemList[0]

	def addItem(self, value):
		if self._counter == 0:
			self._itemList.append(value)
			self._counter += 1
			return True

		self._itemList.append(value)
		self._counter += 1
		
		_index = self._counter - 1
		while _index > 0 and self._itemList[_index] < self._itemList[(_index-1)/2]:
			self._itemList[_index], self._itemList[(_index-1)/2] = self._itemList[(_index-1)/2], self._itemList[_index]
			_index = (_index - 1) / 2

		return True

	def removeItem(self, value):
		"""
		removeItem(self, value) is the most complex method of the MinHeap data structure:
			1. we find the index of the value gonna remove, using a help method _findItemIndex(), if not found, return None;
			2. then swap the value with the last item in the heap;
			3. finally shifdown the new node and validate the order;
		"""
		_indexToRemove = self._findItemIndex(value)

		if _indexToRemove == None:
			return False

		self._itemList[_indexToRemove] = self._itemList[self._counter-1]

		_leftChildIndex = _indexToRemove * 2 + 1
		_rightChildIndex = _indexToRemove * 2 + 2

		#find the minimum one of the left child and right child, 
		#replace the current node by the minimum, and,
		#then shift down in the same fashion.
		while _leftChildIndex < self._counter-1 and (self._itemList[_leftChildIndex] < self._itemList[_indexToRemove] or \
			self._itemList[_rightChildIndex] < self._itemList[_indexToRemove]):
			if self._itemList[_leftChildIndex] < self._itemList[_rightChildIndex]:
				self._itemList[_leftChildIndex], self._itemList[_indexToRemove] = self._itemList[_indexToRemove], self._itemList[_leftChildIndex]
				_indexToRemove = _leftChildIndex
			else:
				self._itemList[_rightChildIndex], self._itemList[_indexToRemove] = self._itemList[_indexToRemove], self._indexToRemove[_rightChildIndex]
				_indexToRemove = _rightChildIndex

			_leftChildIndex = _indexToRemove * 2 + 1
			_rightChildIndex = _indexToRemove * 2 + 2

		self._counter -= 1
		self._itemList.pop()
		return True

	def containItem(self, value):
		if _findItemIndex(value) == None:
			return False

		return True

	def traverseItem(self, func):
		for item in self._itemList:
			func(item)

	def _findItemIndex(self, value):
		for (index, item) in enumerate(self._itemList):
			if item == value:
				return index

		return None

if __name__ == "__main__":
	minHeap = MinHeap()
	for value in [99, 20, 10, 77, 8, 33, 6, 12, 24, 64, 32]:
		minHeap.addItem(value)

	def output(value):
		print value,

	minHeap.traverseItem(func=output)
	print

	print minHeap.peekMinItem()

	minHeap.traverseItem(func=output)
	print

	minHeap.removeItem(64)
	minHeap.removeItem(20)
	minHeap.removeItem(10)
	minHeap.traverseItem(func=output)
