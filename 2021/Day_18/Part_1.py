class node:
    def __init__(self, num=None, nest_level=0, parent=None, left=None, right=None):
        self.num = num
        self.nest_level = nest_level
        self.parent = parent
        self.left = left
        self.right = right

    def show(self):
        if self.num is not None:
            return str(self.num)
        else:
            return '[' + self.left.show() + ',' + self.right.show() + ']'

    def magnitude(self):
        if self.num is None:
            return 3*self.left.magnitude() + 2*self.right.magnitude()
        else:
            return self.num

def find_closest_parent_with_left_child(node):
    p = node.parent
    while p.parent:
        if p.parent.left is not None and p.parent.left != p:
            return p.parent.left
        p = p.parent
    return None

def find_closest_parent_with_right_child(node):
    p = node.parent
    while p.parent:
        if p.parent.right is not None and p.parent.right != p:
            return p.parent.right
        p = p.parent
    return None

def find_most_right_child(node):
    if not node:
        return None
    if node.right is not None:
        return find_most_right_child(node.right)
    return node

def find_most_left_child(node):
    if not node:
        return None
    if node.left is not None:
        return find_most_left_child(node.left)
    return node

def explode(node):
    left = find_most_right_child(find_closest_parent_with_left_child(node.left))
    right = find_most_left_child(find_closest_parent_with_right_child(node.right))
    if left: left.num += node.left.num
    if right: right.num += node.right.num

    node.num = 0
    node.left= None
    node.right = None

def split(n):
    a = n.num // 2
    b = n.num - a
    n.left = node(num=a, nest_level=n.nest_level + 1, parent=n)
    n.right = node(num=b, nest_level=n.nest_level + 1, parent=n)
    n.num = None

def search_for_explosions(n):
    exploded = False
    if n.num is None:
        if n.nest_level >= 4 and n.right.num is not None and n.left.num is not None:
            explode(n)
            exploded = True
        else:
            a = search_for_explosions(n.left)
            b = search_for_explosions(n.right)
            exploded = a or b
    return exploded

def search_for_split(n):
    done = False
    if n.num is not None:
        if n.num > 9:
            split(n)
            done = True
    else:
        done = search_for_split(n.left)
        if not done:
            done = search_for_split(n.right)
    return done


def reduce(tree):
    if search_for_explosions(tree):
        reduce(tree)
    if search_for_split(tree):
        reduce(tree)

def update_nest_level(n, val):
    if n is None:
        return
    n.nest_level += val
    update_nest_level(n.left, val)
    update_nest_level(n.right, val)

def sum_expressions(n1, n2):
    update_nest_level(n1, 1)
    update_nest_level(n2, 1)
    root = node(left=n1, right=n2)
    n1.parent = root
    n2.parent = root

    reduce(root)
    return root

def parse_string(n, message):
    a,b = message

    if isinstance(a, int):
        n.left = node(num=a, nest_level=n.nest_level + 1, parent=n)
    else:
        n.left = node(nest_level=n.nest_level + 1, parent=n)
        parse_string(n.left, a)

    if isinstance(b, int):
        n.right = node(num=b, nest_level=n.nest_level + 1, parent=n)
    else:
        n.right = node(nest_level=n.nest_level + 1, parent= n)
        parse_string(n.right, b)

    return n


if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip().split('\n')
    acc = parse_string(node(), eval(file[0]))

    for expr in file[1:]:
        x = parse_string(node(), eval(expr))
        acc = sum_expressions(acc, x)

    print(f'Part 1: {acc.magnitude()}')

