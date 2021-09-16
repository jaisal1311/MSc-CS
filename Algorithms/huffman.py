class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def PrintTree(self, node):
        if(node.left):
            self.PrintTree(node.left)
        elif(node.right):
            self.PrintTree(node.right)
        print(self.data)


inputString = ['b', 'd', 'a', 'c']

inputFrequency = [1, 3, 5, 6]

nodes = []

for i in range(len(inputString)):
    nodes.append(Node(inputString[i]))

for i in nodes:
    i.left = Node('z')
    i.PrintTree(i.left)
    break
