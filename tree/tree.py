



tree = [None] * 10
 
 
def root(key):
    if tree[0] != None:
        print("Tree already had root")
    else:
        tree[0] = key
 
 
def set_left(key, parent):
    if tree[parent] == None:
        print("Can't set child at", (parent * 2) + 1, ", no parent found")
    else:
        tree[(parent * 2) + 1] = key
 
 
def set_right(key, parent):
    if tree[parent] == None:
        print("Can't set child at", (parent * 2) + 2, ", no parent found")
    else:
        tree[(parent * 2) + 2] = key
 
 
def print_tree():
    for i in range(10):
        if tree[i] != None:
            print(tree[i], end="")
        else:
            print("-", end="")
    print()
 
 
# Driver Code
root('A')
set_right('C', 0)
set_left('D', 1)
set_right('E', 1)
set_right('F', 2)
print_tree()












# SEARCH DATA
##########################



def search(root,key):
     
    # Finding whether root is null or key is present at root
    if root is None or root.val == key:
        return root
 
    # Finding whether Key is greater than root's key
    if root.val < key:
        return search(root.right,key)
   
    # Finding whether Key is smaller than root's key
    return search(root.left,key)











# INSERT DATA
##########################



def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root












# DELETE DATA
##########################



def deleteNode(root, key):
 
    # Finding whether the root is present or not.
    if root is None:
        return root
 

    #When the key to delete is smaller than the root key

    if key < root.key:
        root.left = deleteNode(root.left, key)
 


    #When the key to delete is greater than the root key

    elif(key > root.key):
        root.right = deleteNode(root.right, key)
 


    #When the key to delete is the root's key

    else:
 
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 
        # Node with two children:

        temp = minValueNode(root.right)

        root.key = temp.key
 
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
 
    return root