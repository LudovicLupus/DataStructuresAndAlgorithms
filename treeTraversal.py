# creating a Node class
class Node:
    def __init__(self, val):
        self.childleft = None
        self.childright = None
        self.nodedata = val


# Creating an instance of the Node class to construct the tree
root = Node(1)
root.childleft = Node(2)
root.childright = Node(3)
root.childleft.childleft = Node(4)
root.childleft.childright = Node(5)

# IN-ORDER TREE-TRAVERSAL
in_order = []
def inOrder(root):
    if root:
        inOrder(root.childleft)
        # print(root.nodedata)
        in_order.append(root.nodedata)
        inOrder(root.childright)
    return in_order


print("This is IN-ORDER")
print(inOrder(root))

# PRE-ORDER TREE-TRAVERSAL
pre_order = []
def preOrder(root):
    # pre_order = []
    if(root):
        # print(root.nodedata)
        pre_order.append(root.nodedata)
        preOrder(root.childleft)
        preOrder(root.childright)
    return pre_order


print("This is PRE-ORDER")
print(preOrder(root))

# POST-ORDER TREE-TRAVERSAL
post_order = []
def postOrder(root):
    if(root):
        postOrder(root.childleft)
        postOrder(root.childright)
        # print(root.nodedata)
        post_order.append(root.nodedata)
    return post_order


print("This is POST-ORDER")
print(postOrder(root))






