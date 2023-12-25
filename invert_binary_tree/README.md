# Invert Binary Tree

## Problem Statement
The objective is to flip a binary tree, swapping all left and right children nodes.

## Examples
### Example 1:
![Example 1](example1.jpeg)

- **Input**: root = [4,2,7,1,3,6,9]
- **Output**: [4,7,2,9,6,3,1]

### Example 2:
![Example 2](example2.jpeg)

- **Input**: root = [2,1,3]
- **Output**: [2,3,1]

### Example 3:
- **Input**: root = []
- **Output**: []

## Constraints
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

## Approach
This solution uses a recursive function that swaps the left and right children of the current node before proceeding to invert the child subtrees.

1. Swap its left and right children.
2. Apply the inversion recursively to the left subtree.
3. Apply the inversion recursively to the right subtree.
This continues until all nodes are visited, effectively mirroring the tree's structure.
4. When a node has no children, it returns Null

## Solution
- [solution.py](./solution.py)
