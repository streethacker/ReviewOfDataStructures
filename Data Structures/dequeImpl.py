#!/usr/bin/env python
#-*- coding:utf-8 -*-

from doublyLinkedListImpl import DoublyLinkedNode, DoublyLinkedList

class Deque(DoublyLinkedList):
	"""
	a simple double ended queue implementation based on doubly linked list.
	inheritted from the DoublyLinkedList, so that we can reuse some of the
	operations defined in the doubly linked list data structure.
	"""
	def dequeueFront(self):
		"""
		dequeue from the left end of the queue, that is, remove the first node of the doubly linked list.
		it's much simpler than removeItem() operation of the standard doubly linked list, because all the
		deletion occurs at the beginning end, and we can make extensive use of the head pointer.
		"""
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
		"""
		dequeue from the right end of the queue, opposite to the dequeueFront() method. make full use of the
		tail pointer.
		"""
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
		"""
		enqueue from the left end, much simpler than a standard insertion of the doubly linked list, due to
		the head pointer.
		"""
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
		"""
		enqueue at the right end, opposite to the enqueueFront() method, the same as the standard addItem() operation,
		and benefit from the inheritance, just call the addItem() method directly.
		"""
		super(Deque, self).addItem(value)

	def peekFront(self):
		"""
		unlike the dequeueFront, peekFront() method just return the left-most node(pointed by head pointer)
		without removing it.
		"""
		if self._linkHead == None:
			return False

		return self._linkHead._itemValue

	def peekBack(self):
		"""
		opposite to the peekFront() method.
		"""
		if self._linkHead == None:
			return False

		return self._linkTail._itemValue

	def traverseDeque(self, func):
		"""
		the same as the standard traverseList() operation.
		"""
		super(Deque, self).traverseList(func)

	def reverseTraverseDeque(self, func):
		"""
		the same as the standard reverseTraverseList() operation.
		"""
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
