#!/usr/bin/env python
#-*- coding:utf-8 -*-

class LinkedNode(object):
	"""
	node implementation of linked list, containing a value field and a reference
	to the next node.	
	"""
	def __init__(self, value):
		self._itemValue = value
		self._itemNext = None

class LinkedList(object):
	"""
	a simple linked list implementation, supporting the following functions:
		
		addItem(self, value): add a new node to the linked list with the given value;
		removeItem(self, value): remove a node with the given value from the linked list;
		containItem(self, value): verify if a node with the given value exists in the linked list;
		traverseList(self, func): visit the nodes in the linked list one by one, by the given func;
		reverseTraverseList(self, func): visit the nodes in the linked list one by one(in reverse order), by the given func.
	"""

	def __init__(self):
		self._linkHead = None
		self._linkTail = None

	def addItem(self, value):
		"""
		add a new node to the linked list with the given value.
		"""
		_linkedNode = LinkedNode(value)
		
		#the node we are adding is now both the head and tail of the list
		if self._linkHead == None:  
			self._linkHead = _linkedNode
			self._linkTail = _linkedNode
			return True

		#otherwise, append our node to the end of the list, updating the tail reference appropriately
		self._linkTail._itemNext = _linkedNode
		self._linkTail = _linkedNode
		return True

	def removeItem(self, value):
		"""
		remove a node with the given value from the linked list.
		"""
		if self._linkHead == None:   #the list is empty, return false
			return False

		if self._linkHead._itemValue == value:
			if self._linkHead == self._linkTail: #the Node to remove is the only node in the list
				self._linkHead = None
				self._linkTail = None
			else:
				self._linkHead = self._linkHead.next  #remove the head node
			return True

		_nodeCursor = self._linkHead

		
		while _nodeCursor._itemNext != None and _nodeCursor._itemNext._itemValue != value:
			_nodeCursor = _nodeCursor._itemNext

		if _nodeCursor._itemNext != None:
			if _nodeCursor._itemNext == self._linkTail:   #remove the tail node
				self._linkTail = _nodeCursor
				self._linkTail._itemNext = None
			else:
				#the node to remove is somewhere in between the head and tail
				_nodeCursor._itemNext = _nodeCursor._itemNext._itemNext

			return True

		return False  #doesn't exist

	def containItem(self, value):
		"""
		verify if a node with the given value exists in the linked list.
		"""
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
		visit the nodes in the linked list one by one(in reverse order), by the given func.
		"""
		if self._linkHead == None:
			return False

		_nodeCursor = self._linkTail

		while _nodeCursor != self._linkHead:
			_nodePre = self._linkHead

			while _nodePre._itemNext != _nodeCursor:
				_nodePre = _nodePre._itemNext

			func(_nodeCursor._itemValue)
			_nodeCursor = _nodePre

		func(_nodeCursor._itemValue)
		return True

if __name__ == "__main__":
	linked_list = LinkedList()
	for item in range(10):
		linked_list.addItem(item)

	linked_list.removeItem(5)
	linked_list.removeItem(3)

	def output(item):
		print item,

	linked_list.traverseList(func=output)
	
	print 

	linked_list.reverseTraverseList(func=output)

	print

	print linked_list.containItem(8)
	print linked_list.containItem(3)
