class Node:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None


def preorder(root):
    if root == None:
        return []
    res = []
    res.append(root.v)
    for x in preorder(root.left):
        res.append(x)
    for x in preorder(root.right):
        res.append(x)
    return res


def inorder(root):
    if root == None:
        return []
    res = []
    for x in inorder(root.left):
        res.append(x)
    res.append(root.v)
    for x in inorder(root.right):
        res.append(x)
    return res


def postorder(root):
    if root == None:
        return []
    res = []
    for x in postorder(root.left):
        res.append(x)
    for x in postorder(root.right):
        res.append(x)
    res.append(root.v)
    return res


def level_order(root):
    if root == None:
        return []
    res = []
    ochered = [root]
    while len(ochered) > 0:
        node = ochered.pop(0)
        res.append(node.v)
        if node.left != None:
            ochered.append(node.left)
        if node.right != None:
            ochered.append(node.right)
    return res


def find_min(root):
    if root == None:
        return 999999999
    res = root.v
    l_min = find_min(root.left)
    r_min = find_min(root.right)
    if l_min < res:
        res = l_min
    if r_min < res:
        res = r_min
    return res


def find_max(root):
    if root == None:
        return -999999999
    res = root.v
    l_max = find_max(root.left)
    r_max = find_max(root.right)
    if l_max > res:
        res = l_max
    if r_max > res:
        res = r_max
    return res


if __name__ == "__main__":
    t1 = Node(10)
    t1.left = Node(5)
    t1.right = Node(15)
    t1.left.left = Node(2)
    t1.left.right = Node(7)
    
    print("Preorder:", preorder(t1))
    print("Inorder:", inorder(t1))
    print("Postorder:", postorder(t1))
    print("Level_order:", level_order(t1))
    print("Min:", find_min(t1))
    print("Max:", find_max(t1))

    t2 = Node(50)
    t2.left = Node(30)
    t2.right = Node(70)
    
    print("Level_order:", level_order(t2))
    print("Min:", find_min(t2))
    print("Max:", find_max(t2))
