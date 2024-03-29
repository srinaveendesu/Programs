# Implementation of Binary Search Tree
# Recursion is used for most implementations
import functools as fn

class Node():
    def __init__(self, data=0):
        self.data = data
        self.right = None
        self.left = None


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

    def maxDepth(self, node) -> int:
        if node is None:
            return 0
        else:
            # Compute the depth of each subtree
            lDepth = self.maxDepth(node.left)
            rDepth = self.maxDepth(node.right)

            # Use the larger one
            if (lDepth > rDepth):
                return lDepth + 1
            else:
                return rDepth + 1

    # Traverses all the nodes in the tree
    def minDepth(self, node) -> int:
        # Corner Case.Should never be hit unless the code is
        # called on root = NULL
        if node is None:
            return 0

            # Base Case : Leaf node.This acoounts for height = 1
        if node.left is None and node.right is None:
            return 1

        # If left subtree is Null, recur for right subtree
        if node.left is None:
            return self.minDepth(node.right) + 1

        # If right subtree is Null , recur for left subtree
        if node.right is None:
            return self.minDepth(node.left) + 1

        return min(self.minDepth(node.left), self.minDepth(node.right)) + 1

    def levelOrder(self, root) :
        if root is None:
            return root
        queue = []
        return_list = []
        queue.append(root)
        while len(queue) > 0:
            ans = []
            l = len(queue)
            for l in range(l):
                node = queue.pop(0)
                ans.append(node.data)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            return_list.append(ans)
        return return_list


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

def buildTree_pre_in( preorder, inorder):
    # Recursive solution
    if inorder:
        # Find index of root node within in-order traversal
        index = inorder.index(preorder.pop(0))
        root = Node(inorder[index])

        # Recursively generate left subtree starting from
        # 0th index to root index within in-order traversal
        root.left = buildTree_pre_in(preorder, inorder[:index])

        # Recursively generate right subtree starting from
        # next of root index till last index
        root.right = buildTree_pre_in(preorder, inorder[index + 1:])
        return root

def buildTree_pre_in2(preorder, inorder) :
    if len(preorder) == 0:
        return None

    head = Node(preorder[0])
    stack = [head]
    i = 1
    j = 0

    while i < len(preorder):
        temp = None
        t = Node(preorder[i])
        while stack and stack[-1].data == inorder[j]:
            temp = stack.pop()
            j += 1
        if temp:
            temp.right = t
        else:
            stack[-1].left = t
        stack.append(t)
        i += 1

    return head

def buildTree_in_post(inorder, postorder):
    if inorder:
        ind = inorder.index(postorder.pop())
        root = Node(inorder[ind])
        root.right = buildTree_in_post(inorder[ind + 1:], postorder)
        root.left = buildTree_in_post(inorder[:ind], postorder)
        return root

def buildTree_in_post2( inorder, postorder):
    oi, pi = 0,0
    stack = []
    cur = None
    while pi < len(postorder):
        if len(stack) and stack[-1].data == postorder[pi]:
            stack[-1].right = cur
            cur = stack.pop()
            pi += 1
        else:
            stack.append(Node(inorder[oi]))
            stack[-1].left = cur
            cur = None
            oi += 1
    return cur



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


A = [8, 3, 6, 1, 10, 14, 13, 4, 7]

BST = Tree()
for val in A:
    BST.add_node(val)
    #print(BST)

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


# print(BST.display(BST.root))
#   ___8_
#  /     \
#  3_   10___
# /  \       \
# 1  6      14
#   / \    /
#   4 7   13


print(BST)
print ("Maximum depth of the tree",BST.maxDepth(BST.root))
# Maximum depth of the tree 4

print(BST)
print ("Minimum depth of the tree",BST.minDepth(BST.root))
# Minimum depth of the tree 3

print(BST)
print ("Level order traversal",BST.levelOrder(BST.root))
# Level order traversal [[8], [3, 10], [1, 6, 14], [4, 7, 13]]

preorder_inorder = buildTree_pre_in(BST.preorder(BST.root),BST.inorder(BST.root) )
print("Construct from preorder - inorder ")
print(BST.display(preorder_inorder))
# Construct from preorder - inorder
#   ___8_
#  /     \
#  3_   10___
# /  \       \
# 1  6      14
#   / \    /
#   4 7   13


preorder_inorder2 = buildTree_pre_in2(BST.preorder(BST.root),BST.inorder(BST.root) )
print("Construct from preorder - inorder ")
print(BST.display(preorder_inorder2))
# Construct from preorder - inorder
#   ___8_
#  /     \
#  3_   10___
# /  \       \
# 1  6      14
#   / \    /
#   4 7   13

inorder_postorder = buildTree_in_post(BST.inorder(BST.root),BST.postorder(BST.root) )
print("Construct from inorder - postorder ")
print(BST.display(inorder_postorder))
# Construct from inorder - postorder
#   ___8_
#  /     \
#  3_   10___
# /  \       \
# 1  6      14
#   / \    /
#   4 7   13


inorder_postorder = buildTree_in_post2(BST.inorder(BST.root),BST.postorder(BST.root) )
print("Construct from inorder - postorder ")
print(BST.display(inorder_postorder))
# Construct from inorder - postorder
#   ___8_
#  /     \
#  3_   10___
# /  \       \
# 1  6      14
#   / \    /
#   4 7   13