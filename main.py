class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return AVLNode(key)
    else:
        if key == root.key:
            print(f"The value {key} already exists in the tree, duplicates are not allowed.")
        elif key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def find_max(root):
    if root is None:
        return None
    while root.right:
        root = root.right
    return root.key  

def find_min(root):
    if root is None:
        return None
    while root.left:
        root = root.left
    return root.key  

def sum_tree(root):
    if root is None:
        return 0
    return root.key + sum_tree(root.left) + sum_tree(root.right)


root = None
root = insert(root, 10)
root = insert(root, 20)
root = insert(root, 5)
root = insert(root, 25)
root = insert(root, 15)

print("Найбільше значення у дереві:", find_max(root))
print("Найменше значення у дереві:", find_min(root))
print("Сума всіх значень у дереві:", sum_tree(root))
