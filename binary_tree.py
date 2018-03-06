# coding:utf-8
'''
二叉树的构造
递归实现先序遍历、中序遍历、后续遍历
堆栈实现先序遍历、中序遍历、后续遍历
队列实现层次遍历
'''

class Node(object):
    '''节点类'''
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    '''树类'''
    def __init__(self):
        self.root = Node()  # 树的结构用Node串起来
        self.myQueue = []  # 队列中只存当前'未满'的树节点

    def add(self, elem):
        node = Node(elem)
        if self.root.elem == -1:  # 若树为空
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]
            if treeNode.lchild is None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)

    '''递归实现'''
    def pre_order_recur(self, root):
        if root is None:
            return
        print root.elem,
        self.pre_order_recur(root.lchild)
        self.pre_order_recur(root.rchild)

    def in_order_recur(self, root):
        if root is None:
            return
        self.in_order_recur(root.lchild)
        print root.elem,
        self.in_order_recur(root.rchild)

    def post_order_recur(self, root):
        if root is None:
            return
        self.in_order_recur(root.lchild)
        self.in_order_recur(root.rchild)
        print root.elem,


    '''堆栈实现'''
    # def pre_order_stack(self, root):
    #     if root is None:
    #         return
    #     myNode = root
    #     myStack = []
    #     while myNode or myStack:
    #         if myNode:
    #             print myNode.elem,
    #             myStack.append(myNode)
    #             myNode = myNode.lchild
    #         else:
    #             myNode = myStack.pop()
    #             myNode = myNode.rchild

    def pre_order_stack(self, root):
        if root is None:
            return
        myNode = root
        myStack = []
        while myNode or myStack:
            while myNode:
                print myNode.elem,
                myStack.append(myNode)
                myNode = myNode.lchild
            myNode = myStack.pop()
            myNode = myNode.rchild


    def in_order_stack(self, root):
        if root is None:
            return
        myNode = root
        myStack = []
        while myNode or myStack:
            while myNode:
                myStack.append(myNode)
                myNode = myNode.lchild
            myNode = myStack.pop()
            print myNode.elem,
            myNode = myNode.rchild


    def post_order_stack(self, root):
        if root is None:
            return
        myNode = root
        myStack1 = []
        myStack2 = []
        myStack1.append(myNode)
        while myStack1:
            myNode = myStack1.pop()
            if myNode.lchild:
                myStack1.append(myNode.lchild)
            if myNode.rchild:
                myStack1.append(myNode.rchild)
            myStack2.append(myNode)

        while myStack2:
            print myStack2.pop().elem,


    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root is None:
            return
        queue = []
        myNode = root
        queue.insert(0, myNode)
        while queue:
            myNode = queue.pop()  # pop最后一个元素
            print myNode.elem,
            if myNode.lchild:
                queue.insert(0, myNode.lchild)
            if myNode.rchild:
                queue.insert(0, myNode.rchild)

    def level_queue1(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)  # pop第一个元素
            print node.elem,
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)


if __name__ == '__main__':
    """主函数"""
    elems = range(10)      # 生成十个数据作为树节点
    tree = Tree()          # 新建一个树对象
    for elem in elems:
        tree.add(elem)     # 逐个添加树的节点

    print '\n\n队列实现层次遍历:'
    tree.level_queue(tree.root)
    print '\n\n队列实现层次遍历:'
    tree.level_queue1(tree.root)

    print '\n\n递归实现先序遍历:'
    tree.pre_order_recur(tree.root)
    print '\n递归实现中序遍历:'
    tree.in_order_recur(tree.root)
    print '\n递归实现后序遍历:'
    tree.post_order_recur(tree.root)

    print '\n\n堆栈实现先序遍历:'
    tree.pre_order_stack(tree.root)
    print '\n堆栈实现中序遍历:'
    tree.in_order_stack(tree.root)
    print '\n堆栈实现后序遍历:'
    tree.post_order_stack(tree.root)