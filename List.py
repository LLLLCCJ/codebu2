class Node:
    def __init__(self, data):
        self.data = data
        self.p = None
        self.right = None
        self.left = None
        self.color = "R"


class RB_tree:
    def __init__(self):
        self.root = None
        self.count = 0

    def _insert(self, data):
        self.root = self.find(self.root, data)
        self.count = 0

    def find(self, node, data):
        if node is None:
            return Node(data)
        elif node.data > data:
            node.left = self.find(node.left, data)
            node.left.p = node
            node = node.left
        elif node.data < data:
            node.right = self.find(node.right, data)
            node.right.p = node
            node = node.right
        print("f", node.data)

        if self.count == 0:
            self.count += 1
            return self.color_balancing(node)
        exit()

    def color(self, node):
        if node is None:
            return "B"
        return node.color

    def color_balancing(self, node):
        if self.root:
            print(self.root.data, 'r')
        print('z', node.data)
        if node.p:
            print(node.p.data)
            if node.p.p:
                if node.p.color == node.color and node.p.color == "R":
                    if node.p.p.left == node.p:
                        u = node.p.p.right
                        if u != None:
                            if u.color == node.p.color:
                                node.p.color, node.p.p.right.color = "B", "B"
                                node.p.p.color = "R"
                                node = node.p.p

                            else:
                                if node.p.left == node:
                                    node = node.p.p
                                    node = self.LL(node)
                                else:
                                    node = node.p.p
                                    node.left = self.RR(node)
                                    node = self.LL(node)
                                node.right.color, node.color = node.color, node.right.color
                        else:
                            node = node.p.p
                            node = self.LL(node)
                            print(node.p)
                            print(node.color, node.right.color)

                            node.right.color, node.color = node.color, node.right.color
                    elif node.p.p.right == node.p:
                        u = node.p.p.left
                        if u != None:
                            if u.color == node.p.color:
                                node.p.color, node.p.p.left.color = "B", "B"
                                node.p.p.color = "R"
                                node = node.p.p
                            else:
                                if node.p.right == node:
                                    node = node.p.p
                                    node = self.RR(node)
                                else:
                                    node = node.p.p
                                    node.right = self.LL(node)
                                    node = self.RR(node)
                                node.left.color, node.color = node.color, node.left.color
                        else:
                            node = node.p.p
                            node = self.RR(node)
                            node.left.color, node.color = node.color, node.left.color
                    print("첫", node.data)
                    return self.color_balancing(node)
                print("A")
                return self.color_balancing(node.p.p)
            else:
                print("B")
                return self.color_balancing(node.p)
        else:
            print("C")
            node.color = "B"
            return node

    def LL(self, node):
        x = node.left
        x.p = node.p
        node.left = x.right
        x.right = node
        if node.left:
            node.left.p = node
        x.right.p = x
        return x

    def RR(self, node):
        x = node.right
        x.p = node.p
        node.right = x.left
        x.left = node
        if node.right:
            node.right.p = node
        x.left.p = x

        return x

    def show(self, node):
        print(node.color,end=" ")
        
        if node.left:
            self.show(node.left)
        if node.right:
            self.show(node.right)

x=RB_tree()
x._insert(20)
x._insert(15)
x._insert(12)
x.show(x.root)