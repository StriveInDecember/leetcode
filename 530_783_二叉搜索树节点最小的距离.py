# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
#
#  注意：本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bs
# t/ 相同
#
#
#
#
#
#  示例 1：
#
#
# 输入：root = [4,2,6,1,3]
# 输出：1
#
#
#  示例 2：
#
#
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
#
#
#
#
#  提示：
#
#
#  树中节点数目在范围 [2, 100] 内
#  0 <= Node.val <= 105
#
#
#
#  Related Topics 树 深度优先搜索 递归
#  👍 172 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 二叉搜索树（BST）
# 在二叉搜索树中：
# 1.若任意结点的左子树不空，则左子树上所有结点的值均不大于它的根结点的值。
# 2. 若任意结点的右子树不空，则右子树上所有结点的值均不小于它的根结点的值。
# 3.任意结点的左、右子树也分别为二叉搜索树

# 树的遍历方式
## 1. 先序遍历：
# def dfs(root):
#     if not root:
#         return
#     执行操作
#     dfs(root.left)
#     dfs(root.right)
## 2. 中序遍历：
# def dfs(root):
#     if not root:
#         return
#     dfs(root.left)
#     执行操作
#     dfs(root.right)
## 3. 后序遍历
# def dfs(root):
#     if not root:
#         return
#     dfs(root.left)
#     dfs(root.right)
#     执行操作

# python数组实现差分操作
# np.diff

import numpy as np


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        # # method1: 数组保存中序遍历的结果，然后，对数组中相邻元素求差，得到所有差值的最小值
        # vals = list()
        # def inorder(root):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     vals.append(root.val)
        #     inorder(root.right)
        # inorder(root)
        # # return int(min(np.diff(np.array(vals)))) # 击败了10.80% 的Python3用户
        # return min([vals[i+1] - vals[i] for i in range(len(vals) -1)]) # 击败了10.80% 的Python3用户

        # method2: 在中序遍历的时候的两个被依次访问的节点。注意，这里说的不是 BST 的相邻节点，
        # 因为在中序遍历时，在访问根节点前，上一个被访问的节点是其左子树的最右下角的节点。
        # 所以，我们只需要一个变量prev保存在中序遍历时，上一次被访问的节点。因为在中序遍历的过程中，节点的值是依次递增的，
        # 因此求差值的方式应该是root.val - prev.val，对该值取最小，就是BST任意两个节点的最小差值。
        # 中序遍历时的第一个节点，并没有prev节点。此时应该不求第一个节点和上个节点的差值就行。
        # 可以把prev初始化为None，遍历时对prev进行一个判断，如果prev为None，说明当前遍历的是中序遍历的第一个节点，跳过求差值；
        # 此后的遍历中，在每次求完diff之后，把prev设置为当前遍历的节点。
        # 击败了10.80% 的Python3用户
        self.prev = None
        self.min_val = 1e5
        self.inorder(root)
        return self.min_val

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if self.prev:
            self.min_val = min(root.val - self.prev.val, self.min_val)
        self.prev = root
        self.inorder(root.right)

# leetcode submit region end(Prohibit modification and deletion)
