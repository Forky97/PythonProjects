from random import randint as ri
class Node :

    def __init__(self,value=None,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

class NodeFunction:

    def insert_node(self,tree,node):
        if tree.value > node.value:
            if tree.left is None:
                tree.left = node
            else:
                self.insert_node(tree.left,node)
        else:
            if tree.right is None:
                tree.right = node
            else:
                self.insert_node(tree.right,node)

    def search_value(self,tree,number,count=0):
        if tree is None:
            return f'Нет этого числа число обходов равно {count}'
        elif tree.value == number:
            return f'Нашли число , сделали {count} обходов '
        elif tree.value>number:
            return self.search_value(tree.left,number,count+1)
        else:
            return self.search_value(tree.right,number,count+1)


Tree = Node(50)
operator = NodeFunction()

for _ in range(100):
    operator.insert_node(Tree,Node(ri(1,100)))

num = int(input('введите число для поиска в бинарном дерево , чтобы протестировать алгоритм поиска O(log2**n) :   '))

print(operator.search_value(Tree,num))





