# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 23:55:16 2023

@author: ASUS
"""

class TreeComparator:
    
    def compare(self, node1, node2):
        
        #check the base case (so these node1 and node2 may be the nodes of a leaf node)
        # node1 may be a None or node2 may be a None
        if (node1 is None and node2 is None) or (node1 is None and node2 is not None) or (node1 is not None and node2 is None ):
            
            return node1 == node2
            
        # we have to check the values in nodes
        if node1.data is not node2.data:
            return False
        
        #check all the left and right subtrees (children) recursively 
        return self.compare(node1.left_node, node2.left_node) and self.compare(node1.right_node, node2.right_node)
    
class Node:
    
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent
        self.right_node = None
        self.left_node = None
        
class BinarySearchTree:
    
    def __init__(self):
        self.root = None
        
    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)
            
    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)
        
    def insert_node(self, data, node):
        #we have to go to the left subtree
        if data < node.data:
            if node.left_node:
                self.insert_node(data, node.left_node)
            else:
                node.left_node = Node(data, node)
                
        #we have to visit the right subtree
        else:
            if node.right_node:
                 self.insert_node(data, node.right_node)
            else:
                 node.right_node = Node(data, node)
                 
    def remove_node(self, data, node):
        
        if node is None:
            return
        
        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:
            
            if node.left_node is None and node.right_node is None:
                print("Removing a leaf node...%d" %node.data)
                
                parent = node.parent
                
                if parent is not None and parent.left_node == Node:
                    parent.left_node = None
                if parent is not None and parent.right_node == Node:
                    parent.right_node = None
                
                if parent is None:
                    self.root = None
                    
                del Node
            
            elif node.left_node is None and node.right_node is not None:
                print("Removing a node with single right child...")
                
                parent = node.parent
                
                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node == node.left_node
                    if parent.rightChild == node:
                        parent.right_node = node.right_node
                        
                else:
                    self.root = node.right_node
                    
                node.right_node.parent = parent
                del node
                
            elif
                            
            
            
            
            
            