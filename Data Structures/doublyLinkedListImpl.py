#!/usr/bin/env python
#-*- coding:utf-8 -*-

class DoublyLinkedNode(object):
	"""
	node implementation of doubly linked list, containing a value field, a reference to
	the next node and a reference to the previous node.
	"""
	def __init__(self, value):
		self._itemValue = value
		self._itemPre = None
		self._itemNext = None

class DoublyLinkedList(object):
	"""
	a simple doubly linked list implementation supporting the following functions:

	addItem(self, value): add new node to the doubly linked list;
	removeItem(self, value): remove the given node in the doubly linked list;
	containItem(self, value): verify if the given node contains in the doubly linked list;
	traverseList(self, func): visit every node in the doubly linked list one by one, with the given func;
	reverseTraverseList(self, func): visit every node in the doubly linked list one by one(in reverse order), with the given func;

	all these functions are quite resembling the corresponding functions in the standard linked list, except for dealing with
	the additional previous reference.
	"""
	def __init__(self):
		self._linkHead = None
		self._linkTail = None

	def addItem(self, value):
		"""
		add a new node to the doubly linked list with the given value. almost the
		same as the standard linked list, except for dealing with the previous
		reference.
		"""
		_linkedNode = DoublyLinkedNode(value)

		if self._linkHead == None:
			self._linkHead = _linkedNode
			self._linkTail = _linkedNode
			
			return True

		self._linkTail._itemNext = _linkedNode
		_linkedNode._itemPre = self._linkTail
		self._linkTail = _linkedNode
		
		return True

	def removeItem(self, value):
		"""
		remove a node with the given value from the doubly linked list.
		"""
		if self._linkHead == None:
			return False

		if self._linkHead._itemValue == value:
			if self._linkHead == self._linkTail:
				self._linkHead = None
				self._linkTail = None
			else:
				self._linkHead = self._linkHead._itemNext
				self._linkHead._itemPre = None

			return True

		_nodeCursor = self._linkHead

		while _nodeCursor != None and _nodeCursor._itemValue != value:
			_nodeCursor = _nodeCursor._itemNext

		if _nodeCursor != None:
			if _nodeCursor == self._linkTail:
				self._linkTail = _nodeCursor._itemPre
				self._linkTail._itemNext = None
			else:
				_nodeCursor._itemPre._itemNext = _nodeCursor._itemNext
				_nodeCursor._itemNext._itemPre = _nodeCursor._itemPre

			return True

		return False

	def containItem(self, value):
		"""
		verify if a node with the given value exists in the doubly linked list.
		"""
		if self._linkHead == None:
			return False

		_nodeCursor = self._linkHead

		while _nodeCursor != None and _nodeCursor._itemValue != value:
			_nodeCursor = _nodeCursor._itemNext

		if _nodeCursor == None:
			return False

		return True

	def traverseList(self, func):
		"""
		visit the nodes in the linked list one by one, by the given func.
		"""
		if self._linkHead == None:
			return False

		_nodeCursor = self._linkHead

		while _nodeCursor != None:
			func(_nodeCursor._itemValue)
			_nodeCursor = _nodeCursor._itemNext

		return True

	def reverseTraverseList(self, func):
		"""
		visit the nodes in the doubly linked list one by one(in reverse order), by the given func.
		it's much simpler than the standard linked list, because of the reference to the previous
		node.
		"""
		if self._linkHead == None:
			return False

		_nodeCursor = self._linkTail

		while _nodeCursor != None:
			func(_nodeCursor._itemValue)
			_nodeCursor = _nodeCursor._itemPre

		return True


if __name__ == "__main__":
	doubly_linkedlist = DoublyLinkedList()

	for item in range(10):
		doubly_linkedlist.addItem(item)

	doubly_linkedlist.removeItem(9)
	doubly_linkedlist.removeItem(4)


	def output(value):
		print value,

	doubly_linkedlist.traverseList(func=output)
	print
	doubly_linkedlist.reverseTraverseList(func=output)
	print

	print doubly_linkedlist.containItem(5)
	print doubly_linkedlist.containItem(9)
