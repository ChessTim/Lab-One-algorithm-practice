class Node:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None


def pryamoy(root):
    if root == None:
        return []
    res = []
    res.append(root.v)
    for x in pryamoy(root.left):
        res.append(x)
    for x in pryamoy(root.right):
        res.append(x)
    return res


def simmetr(root):
    if root == None:
        return []
    res = []
    for x in simmetr(root.left):
        res.append(x)
    res.append(root.v)
    for x in simmetr(root.right):
        res.append(x)
    return res


def obratniy(root):
    if root == None:
        return []
    res = []
    for x in obratniy(root.left):
        res.append(x)
    for x in obratniy(root.right):
        res.append(x)
    res.append(root.v)
    return res


def v_shirinu(root):
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


def poisk_min(root):
    if root == None:
        return 999999999 
    res = root.v
    l_min = poisk_min(root.left)
    r_min = poisk_min(root.right)
    if l_min < res:
        res = l_min
    if r_min < res:
        res = r_min
    return res


def poisk_max(root):
    if root == None:
        return -999999999
    res = root.v
    l_max = poisk_max(root.left)
    r_max = poisk_max(root.right)
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
    
    print("Прямой:", pryamoy(t1))
    print("Симметричный:", simmetr(t1))
    print("Обратный:", obratniy(t1))
    print("В ширину:", v_shirinu(t1))
    print("Минимум:", poisk_min(t1))
    print("Максимум:", poisk_max(t1))
