#/usr/bin/env python
#-*- coding:utf-8 -*-

class BinaryTreeNode(object):
	"""
	binary tree node implementation, containing three fields: the left pointer, the right
	pointer, and the value field.
	"""
	def __init__(self, value):
		self._itemLeft = None
		self._itemRight = None
		self._itemValue = value

class BinarySearchTree(object):
	def __init__(self):
		self._linkRoot = None
 
	def addItem(self, value):
		"""
		add a new node to the binary search tree, called the _add_item_recursively() method.
		"""
		if self._linkRoot == None:
			self._linkRoot = BinaryTreeNode(value)
		else:
			return self._add_item_recursively(self._linkRoot, value)

	def _add_item_recursively(self, current, value):
		"""
		recursive implementation of addItem:
			if value < current.Value, inspect the left subtree;
			otherwise, inspect the right subtree;
		"""
		_binaryTreeNode = BinaryTreeNode(value)

		if value < current._itemValue:
			if current._itemLeft == None:
				current._itemLeft = _binaryTreeNode
			else:
				self._add_item_recursively(current._itemLeft, value)
		else:
			if current._itemRight == None:
				current._itemRight = _binaryTreeNode
			else:
				self._add_item_recursively(current._itemRight, value)

	def containItem(self, value):
		"""
		verify if value exists in the binary search tree, call the _contain_item_recursively() method.
		"""
		return self._contain_item_recursively(self._linkRoot, value)

	def _contain_item_recursively(self, current, value):
		"""
		recursive implementation of containItem:
			a. the current node is None, value is not in the BST;
			b. current.Value = value, then value is in the BST;
			c. value < current.Value, inspect the left subtree of the current node;
			d. value > current.Value, inspect the right subtree of the current node;
		"""
		if current == None:
			return False

		if current._itemValue == value:
			return True
		elif value < current._itemValue:
			return self._contain_item_recursively(current._itemLeft, value)
		else:
			return self._contain_item_recursively(current._itemRight, value)

	def removeItem(self, value):
		"""
		remove a node from the binary search tree:
			a. the value to remove i sa leaf node;
			b. the value to remove has a right subtree, but no left subtree;
			c. the value to remove has a left subtree, but no right subtree;
			d. the value to remove has both a left and right subtree, in which case we promote the largest value
			in the left subtree.
		"""
		_nodeToRemove = self._findItem(value)

		#if the value to remove does not exist in the BST
		if _nodeToRemove == None:
			return False

		#if the value to remove is the only node in the BST
		if self._linkRoot._itemLeft == None and self._linkRoot._itemRight == None:
			self._linkRoot == None

		_parentNode = self._findParentItem(value)

		if _nodeToRemove._itemLeft == None and _nodeToRemove._itemRight == None:
			if _nodeToRemove._itemValue < _parentNode._itemValue:
				_parentNode._itemLeft = None
			else:
				_parentNode._itemRight = None

		elif _nodeToRemove._itemLeft == None and _nodeToRemove._itemRight != None:
			if _nodeToRemove._itemValue < _parentNode._itemValue:
				_parentNode._itemLeft = _nodeToRemove._itemRight
			else:
				_parentNode._itemRight = _nodeToRemove._itemRight

		elif _nodeToRemove._itemLeft != None and _nodeToRemove._itemRight == None:
			if _nodeToRemove._itemValue < _parentNode._itemValue:
				_parentNode._itemLeft = _nodeToRemove._itemLeft
			else:
				_parentNode._itemRight = _nodeToRemove._itemLeft

		else:
			_largestNodeOfLeft = _nodeToRemove._itemLeft
			while _largestNodeOfLeft._itemRight != None:
				_largestNodeOfLeft = _largestNodeOfLeft._itemRight

			self._findParentItem(_largestNodeOfLeft)._itemRight = None

			_nodeToRemove._itemValue = _largestNodeOfLeft._itemValue
		
		return True

	def _findItem(self, value):
		return self._find_item_recursively(self._linkRoot, value)

	def _find_item_recursively(self, current, value):
		if current == None:
			return None

		if current._itemValue == value:
			return current
		elif value < current._itemValue:
			return self._find_item_recursively(current._itemLeft, value)
		else:
			return self._find_item_recursively(current._itemRight, value)

	def _findParentItem(self, value):
		"""
		return a reference to the parent node of the one with the given value, call _find_parent_item_recursively() method.
		"""
		#if the BST is empty
		if self._linkRoot == None:
			return None

		#if the node with the given value is exactly the root node
		if self._linkRoot._itemValue == value:
			return None

		return self._find_parent_item_recursively(self._linkRoot, value)

	def _find_parent_item_recursively(self, current, value):
		"""
		recursive implementation of _findParentItem:
			a. if value < current.Value, inspect the left subtree;
			b. otherwise, inspect the right subtree;
		"""
		if value < current._itemValue:
			if current._itemLeft == None:
				return None
			elif current._itemLeft._itemValue == value:
				return current
			else:
				return self._find_parent_item_recursively(current._itemLeft, value)
		else:
			if current._itemRight == None:
				return None
			elif current._itemRight._itemValue == value:
				return current
			else:
				return self._find_parent_item_recursively(current._itemRight, value)

	def PreOrder(self, func):
		"""
		pre order traversal of the BST.
		"""
		return self._preOrder(self._linkRoot, func)

	def InOrder(self, func):
		"""
		in order traversal of the BST.
		"""
		return self._inOrder(self._linkRoot, func)

	def PostOrder(self, func):
		"""
		post order traversal of the BST.
		"""
		return self._postOrder(self._linkRoot, func)

	def _preOrder(self, current, func):
		"""
		recursive implementation of PreOrder.
		"""
		if current != None:
			func(current._itemValue)
			self._preOrder(current._itemLeft, func)
			self._preOrder(current._itemRight, func)

	def _inOrder(self, current, func):
		"""
		recursive implementation of InOrder.	
		"""
		if current != None:
			self._inOrder(current._itemLeft, func)
			func(current._itemValue)
			self._inOrder(current._itemRight, func)

	def _postOrder(self, current, func):
		"""
		recursive implementation of PostOrder.	
		"""
		if current != None:
			self._postOrder(current._itemLeft, func)
			self._postOrder(current._itemRight, func)
			func(current._itemValue)

	def BreadthFirst(self, func):
		"""
		breadth first traversal using a python list as queue.
		"""
		_queue = list()
		current = self._linkRoot

		while current != None:
			func(current._itemValue)

			if current._itemLeft != None:
				_queue.append(current._itemLeft)
			if current._itemRight != None:
				_queue.append(current._itemRight)

			if len(_queue) != 0:
				current = _queue.pop(0)
			else:
				current = None

if __name__ == "__main__":
	binarySearchTree = BinarySearchTree()

	def output(value):
		print value,

	for item in [100, 3, 19, 11, 177, 4, 260, 29, 51, 64]:
		binarySearchTree.addItem(item)

	print "InOrder:",
	binarySearchTree.InOrder(func=output)
	print

	print "PreOrder:",
	binarySearchTree.PreOrder(func=output)
	print

	print "PostOrder:",
	binarySearchTree.PostOrder(func=output)
	print 

	print binarySearchTree.containItem(51)
	print binarySearchTree.removeItem(51)
	print binarySearchTree.containItem(51)

	binarySearchTree.InOrder(func=output)
	print

	binarySearchTree.BreadthFirst(func=output)
