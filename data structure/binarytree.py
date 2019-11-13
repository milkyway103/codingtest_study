# 파이썬으로 binary tree 구현하기
class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return self.data, self.left, self.right

class BinaryTree():
    def __init__(self):
        self.root = None

    # root를 계속 갱신해나가면서
    # root가 없다면
    def insert(self, node, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)

        return node

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key <= root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    def delete(self, key):
        return self._delete_value(self.root, key)

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            # 노드의 자식 노드가 둘 다 있을 때는
            if node.left and node.right:
                # replace the node to the leftmost of node.right
                # 오른쪽 자식의 가장 왼쪽 자식을 가져온다 (혹은 왼쪽 자식의 가장 오른쪽 자식도 ok)
                # 목적 : 트리의 변동성 최소
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                # child의 left에 node의 원래 left를 붙이고
                child.left = node.left
                # child의 right를 parent의 left로 올리고
                # child의 right에 node의 원래 right를 붙인 후
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                # child로 node를 대체
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self._delete_value(node.left, key)
        else:
            node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

