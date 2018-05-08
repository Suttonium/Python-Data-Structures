class Node:
    def __init__(self, left, right, parent, value):
        """
        Simply Node class to hold a left and right child, potentially a parent, and a value
        :param left: pointer to left child
        :param right: pointer to right child
        :param parent: HAS NOT BE IMPLEMENTED
        :param value: value held within the Node
        """
        self.left = left
        self.right = right
        self.parent = parent
        self.value = value


class BST:
    def __init__(self):
        """
        BST constructor assigning the root Node and number of Nodes within the tree
        """
        self.root = None
        self.number_of_values = 0

    def find(self, value):
        """
        calls helper method to determine if the given value exists within the tree
        :param value: value to be potentially found
        :return: True/False depending on if the value was found
        """
        return self.find_node(self.root, value)

    def find_node(self, root, value):
        """
        helper method to recursively attempt discovery of given value
        :param root: current node
        :param value: value being found
        :return: True/False depending on if the value was found
        """
        if root is None:
            return False
        elif root.value == value:
            return True
        elif root.value > value:
            return self.find_node(root.left, value)
        else:
            return self.find_node(root.right, value)

    def insert(self, value):
        """
        calls helper method to add new node into tree
        :param value: value to be inserted into a new node added into the tree
        :return: the new tree
        """
        self.root = self.insert_node(self.root, value)

    def insert_node(self, root, value):
        """
        helper method to handle insertion of a new value into the tree
        :param root: current value being compared to value being inserted
        :param value: value to be inserted
        :return:
        """
        if root is None:
            return Node(None, None, None, value)
        elif root.value < value:
            root.right = self.insert_node(root.right, value)
        else:  # root.value > value
            root.left = self.insert_node(root.left, value)
        self.number_of_values += 1
        return root

    def remove(self, value):
        """
        calls helper method to remove given value, and node, from tree
        :param value: value to be removed
        :return: the new tree
        """
        self.root = self.remove_node(self.root, value)

    def get_max(self, root):
        """
        return the maximum value associated to the given root node
        :param root: node to be searched
        :return: maximum node
        """
        if root.right is None:
            return root
        return self.get_max(root.right)

    def delete_max(self, root):
        """
        removes the maximum value from the given root
        :param root: node to be traversed
        :return: the new tree
        """
        if root.right is None:
            return root.left
        root.right = self.delete_max(root.right)
        return root

    def remove_node(self, root, value):
        """
        helper method to handle removal of given value
        :param root: current root being traversed
        :param value: value to be removed
        :return: the new tree
        """
        if root is None:
            return None
        if root.value > value:
            root.left = self.remove_node(root.left, value)
        elif root.value < value:
            root.right = self.remove_node(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                temp = self.get_max(root.left)
                root.value = temp.value
                root.left = self.delete_max(root.left)
        self.number_of_values -= 1
        return root

    def order(self, order_type):
        """
        method to return the order specified by the user
        :param order_type: can be pre, post, or in
        :return: the designated order of the tree
        """
        return self.order_output(self.root, order_type)

    def order_output(self, root, order_type):
        """
        helper method to output the respective order
        :param root: current node in tree
        :param order_type: the designated order of the tree
        :return: the designated order of the tree, "" if tree is empty
        """
        if root is not None:
            if order_type == "pre":
                return root.value + self.order_output(root.left, order_type) + self.order_output(root.right, order_type)
            elif order_type == "post":
                return self.order_output(root.left, order_type) + self.order_output(root.right, order_type) + root.value
            elif order_type == "in":
                return self.order_output(root.left, order_type) + root.value + self.order_output(root.right, order_type)
        return ""

    def position_of(self, value):
        """
        method to find the position of a value within the tree, only if the value exists within the tree

        :param value: value being found
        :return: the position of the value in the tree
        """
        return self.position_of_node(self.root, value, 0)

    def position_of_node(self, root, value, current_position):
        """

        :param root:
        :param value:
        :param current_position:
        :return:
        """
        if self.find(value):
            if root.value == value:
                return current_position
            elif root.value > value:
                return self.position_of_node(root.left, value, ((2 * current_position) + 1))
            else:
                return self.position_of_node(root.right, value, ((2 * current_position) + 2))
        else:
            return -1

    def height(self):
        """
        calls helper method to determine the max height of the tree
        :return: the max height of the tree
        """
        return self.height_of_tree(self.root)

    def height_of_tree(self, root):
        """
        helper method that compares the height of the left and right subtrees to determine max height
        :param root: current root
        :return: height of the tree
        """
        if root is None:
            return 0
        return 1 + max(self.height_of_tree(root.left), self.height_of_tree(root.right))
