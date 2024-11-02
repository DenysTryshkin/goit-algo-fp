import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())

    def add_edges(self, graph, pos, x=0, y=0, layer=1):
        if self is not None:
            graph.add_node(self.id, label=self.val)
            if self.left:
                graph.add_edge(self.id, self.left.id)
                l = x - 1 / 2**layer
                pos[self.left.id] = (l, y - 1)
                self.left.add_edges(graph, pos, x=l, y=y - 1, layer=layer + 1)
            if self.right:
                graph.add_edge(self.id, self.right.id)
                r = x + 1 / 2**layer
                pos[self.right.id] = (r, y - 1)
                self.right.add_edges(graph, pos, x=r, y=y - 1, layer=layer + 1)
        return graph

    def depth_first_traversal(self, colors, visited):
        if self and self.id not in visited:
            visited.add(self.id)
            colors.append(self.generate_color(len(colors)))
            if self.left:
                self.left.depth_first_traversal(colors, visited)
            if self.right:
                self.right.depth_first_traversal(colors, visited)

    def breadth_first_traversal(self, colors):
        visited = set()
        queue = [self]

        while queue:
            node = queue.pop(0)
            if node.id not in visited:
                visited.add(node.id)
                colors.append(self.generate_color(len(colors)))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    def generate_color(self, index):
        # Генерація кольору в RGB
        r = min(255, 50 + index * 15)  # Червоний
        g = min(255, 100 + index * 10)  # Зелений
        b = 255 - index * 15  # Синій зменшується
        return f'#{r:02X}{g:02X}{b:02X}'  # Формат RGB

    def draw_tree(self, traversal_type):
        tree = nx.DiGraph()
        pos = {self.id: (0, 0)}
        tree = self.add_edges(tree, pos)

        colors = []
        if traversal_type == "depth":
            self.depth_first_traversal(colors, set())
        elif traversal_type == "breadth":
            self.breadth_first_traversal(colors)

        labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

        plt.figure(figsize=(8, 5))
        nx.draw(
            tree,
            pos=pos,
            labels=labels,
            arrows=False,
            node_size=2500,
            node_color=colors,
            font_color="white",
        )
        plt.title(f'Обхід у {"глибину" if traversal_type == "depth" else "ширину"}')
        plt.show()

def main():
    root = Node(0)
    root.left = Node(1)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.left.right.left = Node(9)
    root.left.right.right = Node(10)
    root.right = Node(2)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(11)
    root.right.left.right = Node(12)
    root.right.right.left = Node(13)
    root.right.right.right = Node(14)

    # Відображення дерева з обходом у глибину
    root.draw_tree(traversal_type="depth")

    # Відображення дерева з обходом в ширину
    root.draw_tree(traversal_type="breadth")

if __name__ == "__main__":
    main()
