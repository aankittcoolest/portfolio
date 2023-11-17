


## Binary Tree traversal in inorder
- Traversal occurs as "Left Subtree" > "Root" > "Right Subtree"


### Recursive solution approach
- Ref: https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/3905894/python-easy-solution-100-iteration/
- Here we try to solve the problem using recusion.
- TC: O(N)
- SC: O(N)

```py
## Inorder Traversal = LeftSubtree -> RootNode -> Right subtree

from typing import Optional
from typing import List


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
        list = []
        output = self.inorderTraversal(root.left)
        if output is not None:
            list.extend(output)
        list.append(root.val)
        output = self.inorderTraversal(root.right)
        if output is not None:
            list.extend(output)
        return list



## Example
### Drinks > Hot > Cold

### Expected output: "Hot", "Drinks", "Cold"

def example1():
    leftNode = TreeNode("Hot")
    rightNode = TreeNode("Cold")
    rootNode = TreeNode("Drinks",leftNode,rightNode)

    solution = Solution()
    sol = solution.inorderTraversal(rootNode)
    print(sol)

example1()
```