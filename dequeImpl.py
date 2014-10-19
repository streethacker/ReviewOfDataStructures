#!/usr/bin/env python
#-*- coding:utf-8 -*-

from doublyLinkedListImpl import DoublyLinkedNode, DoublyLinkedList

class Deque(DoublyLinkedList):
	def dequeueFront(self):
		if self._linkHead == None:
			return False

		if self._linkHead == self._linkTail:
			_nodeReturn = self._linkHead

			self._linkHead = None
			self._linkTail = None

			return _nodeReturn

		_nodeReturn = self._linkHead
		self._linkHead = self._linkHead._itemNext
		self._linkHead._itemPre = None

		return _nodeReturn._itemValue

	def dequeueBack(self):
		if self._linkHead == None:
			return False

		if self._linkHead == self._linkTail:
			_nodeReturn = self._linkHead

			self._linkHead = None
			self._linkTail = None

			return _nodeReturn

		_nodeReturn = self._linkTail
		self._linkTail = self._linkTail._itemPre
		self._linkTail._itemNext = None

		return _nodeReturn._itemValue

	def enqueueFront(self, value):
		_linkedNode = DoublyLinkedNode(value)

		if self._linkHead == None:
			self._linkHead = _linkedNode
			self._linkTail = _linkedNode

			return True

		_linkedNode._itemNext = self._linkHead
		self._linkHead._itemPre = _linkedNode
		self._linkHead = _linkedNode

		return True

	def enqueueBack(self, value):
		super(Deque, self).addItem(value)

	def peekFront(self):
		if self._linkHead == None:
			return False

		return self._linkHead._itemValue

	def peekBack(self):
		if self._linkHead == None:
			return False

		return self._linkTail._itemValue

	def traverseDeque(self, func):
		super(Deque, self).traverseList(func)

	def reverseTraverseDeque(self, func):
		super(Deque, self).reverseTraverseList(func)

if __name__ == "__main__":
	deque = Deque()

	for item in range(10):
		deque.enqueueBack(item)

	def output(value):
		print value,

	deque.traverseDeque(func=output)
	print
	deque.reverseTraverseDeque(func=output)
	print

	deque.enqueueFront(100)
	deque.enqueueFront(315)
	deque.enqueueFront(45)

	deque.traverseDeque(func=output)
	print

	deque.dequeueBack()
	deque.dequeueFront()

	deque.traverseDeque(func=output)
	print

	print deque.peekBack()
	print deque.peekFront()
