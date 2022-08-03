# 并查集

# 1. find 判断 node1, node2是否相连， 判断两者的root node是否相同

# 2. merge 把两者的root node 相连, 两者的root node keep same

class DSU:

    def __init__(self, nums: int):
        """
        初始化root_nodes列表, 对应每个node的root_node
        """

        self.root_nodes = [-1] * nums

    def find(self, node):
        """
        找到 node 的 root_node
        """

        if self.root_nodes[node] == -1:
            return node
        return self.find(self.root_nodes[node])

    def merge(self, node1, node2):
        """
        连接node1 和 node2
        """

        node1_root = self.find(node1)
        node2_root = self.find(node2)

        if node2_root == node1_root:
            return
        self.root_nodes[node1_root] = node2_root