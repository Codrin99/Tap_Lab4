class BinaryTree:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def set_root(self, key):
        self.key = key

    def preorder(self):
        print(self.key, end=' ')
        if self.left is not None:
            self.left.preorder()
        if self.right is not None:
            self.right.preorder()



def construct_btree(postord, inord):
    if postord == [] or inord == []:
        return None
    key = postord[-1]
    node = BinaryTree(key)
    index = inord.index(key)
    node.left = construct_btree(postord[:index], inord[:index])
    node.right = construct_btree(postord[index:-1], inord[index + 1:])
    return node


postord = input('Input post-order: ').split()
postord = [int(x) for x in postord]
inord = input('Input in-order: ').split()
inord = [int(x) for x in inord]

btree = construct_btree(postord, inord)
print('Binary tree constructed.')
print('preordine:', end=' ')
btree.preorder()
print()
print('inordine:',inord)
print('postordine', postord)