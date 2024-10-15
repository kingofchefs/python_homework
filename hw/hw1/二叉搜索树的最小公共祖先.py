class BinTreeNode:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None
        self.parent = None

def add_node(node, val):
    if node is None:
        return BinTreeNode(val)
    if val > node.val:
        node.right_child = add_node(node.right_child, val)
    elif val < node.val:
        node.left_child = add_node(node.left_child, val)
    return node

def find_mca(node, n1, n2):
    if node is None:
        return None
    if node.val > n1 and node.val > n2:
        return find_mca(node.left_child, n1, n2)
    elif node.val < n1 and node.val < n2:
        return find_mca(node.right_child, n1, n2)
    return node

parameter=list(map(int, input().split()))
num=list(map(int, input().split()))
node=None

for val in num:
    node=add_node(node, val)

result=[]
for a in range(parameter[1]):
    n1, n2=map(int, input().split())
    ancestor=find_mca(node, n1, n2)
    result.append(ancestor.val)

for a in result:
    print(a)