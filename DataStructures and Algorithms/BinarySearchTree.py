# Implementation of Binary Search Tree
# Recursion is used for most implementations
import functools as fn
import re

class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        #up = '{}{}\n{}{}{}'.format(len(str(self.left))*' ',self.data,self.left,len(str(self.data))*' ',self.right)

        return ('[{}] <- {} -> [{}]'.format(self.left, self.data, self.right))
        #return up


class Tree():
    def __init__(self):
        self.root = None

    def add_node(self, data):
        if self.root != None:
            self.__add(data, self.root)
        else:
            self.root = Node(data)

    def __add(self, data, node):
        if node.data > data:
            if node.left == None:
                node.left = Node(data)
            else:
                self.__add(data, node.left)
        else:
            if node.right == None:
                node.right = Node(data)
            else:
                self.__add(data, node.right)

    def preorder(self,node):
        nodes = []
        if node:
            #print(node)
            nodes.insert(0,node.data)
            nodes = nodes + self.preorder(node.left)
            nodes = nodes + self.preorder(node.right)

        return nodes

    def inorder(self,node):
        nodes=[]
        if node:
            nodes = nodes + self.inorder(node.left)
            nodes.append(node.data)
            nodes = nodes + self.inorder(node.right)
        return nodes

    def postorder(self,node):
        nodes = []
        if node:
            nodes = nodes + self.postorder(node.left)
            nodes = nodes + self.postorder(node.right)
            nodes.append(node.data)
        return nodes

    # This code has been taken from Stackoverflow
    # This code print nodes in a Binary tree format
    def printBTree(self,node, nodeInfo=None, inverted=False, isTop=True):

        # node value string and sub nodes
        stringValue, leftNode, rightNode = nodeInfo(node)

        stringValueWidth = len(stringValue)

        # recurse to sub nodes to obtain line blocks on left and right
        leftTextBlock = [] if not leftNode else self.printBTree(leftNode, nodeInfo, inverted, False)

        rightTextBlock = [] if not rightNode else self.printBTree(rightNode, nodeInfo, inverted, False)

        # count common and maximum number of sub node lines
        commonLines = min(len(leftTextBlock), len(rightTextBlock))
        subLevelLines = max(len(rightTextBlock), len(leftTextBlock))

        # extend lines on shallower side to get same number of lines on both sides
        leftSubLines = leftTextBlock + [""] * (subLevelLines - len(leftTextBlock))
        rightSubLines = rightTextBlock + [""] * (subLevelLines - len(rightTextBlock))


        # compute location of value or link bar for all left and right sub nodes
        #   * left node's value ends at line's width
        #   * right node's value starts after initial spaces
        leftLineWidths = [len(line) for line in leftSubLines]
        rightLineIndents = [len(line) - len(line.lstrip(" ")) for line in rightSubLines]


        # top line value locations, will be used to determine position of current node & link bars
        firstLeftWidth = (leftLineWidths + [0])[0]
        firstRightIndent = (rightLineIndents + [0])[0]


        # width of sub node link under node value (i.e. with slashes if any)
        # aims to center link bars under the value if value is wide enough
        #
        # ValueLine:    v     vv    vvvvvv   vvvvv
        # LinkLine:    / \   /  \    /  \     / \
        #
        linkSpacing = min(stringValueWidth, 2 - stringValueWidth % 2)
        leftLinkBar = 1 if leftNode else 0
        rightLinkBar = 1 if rightNode else 0
        minLinkWidth = leftLinkBar + linkSpacing + rightLinkBar
        valueOffset = (stringValueWidth - linkSpacing) // 2

        # find optimal position for right side top node
        #   * must allow room for link bars above and between left and right top nodes
        #   * must not overlap lower level nodes on any given line (allow gap of minSpacing)
        #   * can be offset to the left if lower subNodes of right node
        #     have no overlap with subNodes of left node
        minSpacing = 2
        rightNodePosition = fn.reduce(lambda r, i: max(r, i[0] + minSpacing + firstRightIndent - i[1]), \
                                      zip(leftLineWidths, rightLineIndents[0:commonLines]), \
                                      firstLeftWidth + minLinkWidth)

        # extend basic link bars (slashes) with underlines to reach left and right
        # top nodes.
        #
        #        vvvvv
        #       __/ \__
        #      L       R
        #
        linkExtraWidth = max(0, rightNodePosition - firstLeftWidth - minLinkWidth)
        rightLinkExtra = linkExtraWidth // 2
        leftLinkExtra = linkExtraWidth - rightLinkExtra

        # build value line taking into account left indent and link bar extension (on left side)
        valueIndent = max(0, firstLeftWidth + leftLinkExtra + leftLinkBar - valueOffset)
        valueLine = " " * max(0, valueIndent) + stringValue
        slash = "\\" if inverted else "/"
        backslash = "/" if inverted else "\\"
        uLine = "¯" if inverted else "_"

        # build left side of link line
        leftLink = "" if not leftNode else (" " * firstLeftWidth + uLine * leftLinkExtra + slash)

        # build right side of link line (includes blank spaces under top node value)
        rightLinkOffset = linkSpacing + valueOffset * (1 - leftLinkBar)
        rightLink = "" if not rightNode else (" " * rightLinkOffset + backslash + uLine * rightLinkExtra)

        # full link line (will be empty if there are no sub nodes)
        linkLine = leftLink + rightLink

        # will need to offset left side lines if right side sub nodes extend beyond left margin
        # can happen if left subtree is shorter (in height) than right side subtree
        leftIndentWidth = max(0, firstRightIndent - rightNodePosition)
        leftIndent = " " * leftIndentWidth
        indentedLeftLines = [(leftIndent if line else "") + line for line in leftSubLines]

        # compute distance between left and right sublines based on their value position
        # can be negative if leading spaces need to be removed from right side
        mergeOffsets = [len(line) for line in indentedLeftLines]
        mergeOffsets = [leftIndentWidth + rightNodePosition - firstRightIndent - w for w in mergeOffsets]
        mergeOffsets = [p if rightSubLines[i] else 0 for i, p in enumerate(mergeOffsets)]

        # combine left and right lines using computed offsets
        #   * indented left sub lines
        #   * spaces between left and right lines
        #   * right sub line with extra leading blanks removed.
        mergedSubLines = zip(range(len(mergeOffsets)), mergeOffsets, indentedLeftLines)
        mergedSubLines = [(i, p, line + (" " * max(0, p))) for i, p, line in mergedSubLines]
        mergedSubLines = [line + rightSubLines[i][max(0, -p):] for i, p, line in mergedSubLines]

        # Assemble final result combining
        #  * node value string
        #  * link line (if any)
        #  * merged lines from left and right sub trees (if any)
        treeLines = [leftIndent + valueLine] + ([] if not linkLine else [leftIndent + linkLine]) + mergedSubLines

        # invert final result if requested
        treeLines = reversed(treeLines) if inverted and isTop else treeLines

        # return intermediate tree lines or print final result

        if isTop:
            #print("\n".join(treeLines))
            return treeLines
        else:
            return treeLines

    # Another implementation
    # Taken from StackOverflow
    def display(self, node):
        lines, _, _, _ = self._display_aux(node)
        for line in lines:
            print(line)
        return ''

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '%s' % node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = '%s' % node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def __str__(self):
        tree_output = self.printBTree(self.root, lambda node: (str(node.data), node.left, node.right),inverted=0)
        return '\n'.join(tree_output)

'''
    Example
                  8
                 / \
                3   10
               / \    \
              1   6    14
                 / \   /
                4   7 13 
'''


A = [8, 3, 6, 1, 10, 14, 13, 4, 7,5]

BST = Tree()
for val in A:
    BST.add_node(val)
    #print(BST.root)

print(BST.root)
# [[[None] <- 1 -> [None]] <- 3 -> [[[None] <- 4 -> [None]] <- 6 -> [[None] <- 7 -> [None]]]] <- 8 -> [[None] <- 10 -> [[[None] <- 13 -> [None]] <- 14 -> [None]]]

print(BST)
#       8
#    __/ \_
#   3      10
#  / \       \
# 1   6       14
#    / \     /
#   4   7  13

print (BST.preorder(BST.root))
# [8, 3, 1, 6, 4, 7, 10, 14, 13]
print(BST.inorder(BST.root))
# [1, 3, 4, 6, 7, 8, 10, 13, 14]
print((BST.postorder(BST.root)))
# [1, 4, 7, 6, 3, 13, 14, 10, 8]


print(BST.display(BST.root))
#   ___8_
#  /     \
#  3_   10___
# /  \       \
# 1  6      14
#   / \    /
#   4 7   13


def decorate_tree(func):
    fn.wraps(func)
    def modify(data):
        print (data,'in decorator',)
        data = str(data)
        reg = r'\[None\] <- (\d+) -> \[None\]'
        m = re.search(reg,data)
        while m:
            if m:
                data = re.sub(reg,m.group(1),data,1)
                m = re.search(reg, data)
        print (data)

        return func(data)
    return modify

def modify_tree(data):
    print (data,'in modify',)
    #data = str(data)
    reg = r'\[None\] <- (\d+) -> \[None\]'
    m = re.search(reg,data)
    while m:
        if m:
            data = re.sub(reg,m.group(1),data,1)
            m = re.search(reg, data)
    #print (data)

    return data

counter  =0
def printbtre(data):
    global counter
    counter +=1

    print(data,type(data))

    l_open_b = 0
    pos = 0
    for i in range(0,len(data)):
        if data[i] == '[':
            l_open_b = l_open_b +1
        if data[i] == ']':
            l_open_b = l_open_b -1
        if l_open_b ==0:
            pos = i
            break
    print(pos,data[pos+1:])



    m = re.findall('\d+',data[0:pos+1])
    if m:
        print(m)
        print(data[1:pos])
        printbtre(data[1:pos])
    pass

data = modify_tree(str(BST.root))
printbtre(data)
print (counter)