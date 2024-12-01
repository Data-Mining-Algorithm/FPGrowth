import pandas as pd


class Node:

    def __init__(self, item, parent=None):
        self.item = item
        self.count = 0
        self.parent = parent
        self.children = {}  # child[item], means `item` is a child, and that's a pointer to it's node


def get_path_to_root(node):  # return list of nodes
    path = [node]
    while node.parent:
        #print(f"Node: {node.item}, Parent: {node.parent.item}")
        node = node.parent
        path.append(node)
    #print(f"Final path: {[n.item for n in path]}")
    return path


class Tree:

    def __init__(self):
        self.root = Node(item=None)  # initialize the root node (item=None for root)
        self.item_count = {}  # { item: count }, for counting item frequencies
        self.item_list = []  # List of items sorted by frequency
        self.occurrences = {}  # { item: [list of nodes where the item appears] }
        self.conditional_items = []  # Conditional items for conditional FP-trees

    def insert(self, transaction, frequent_count):
        cur = self.root  # Start at the root node

        # Sort transaction items by frequency (descending)
        transaction.sort(key=lambda x: -self.item_count[x])

        # Remove items that don't meet the frequent_count threshold
        while transaction and self.item_count[transaction[-1]] < frequent_count:
            transaction.pop()

        for item in transaction:
            if item not in self.occurrences:
                self.occurrences[item] = []

            if item not in cur.children:
                cur.children[item] = Node(item, parent=cur)  # Add a new node for the item
                self.occurrences[item].append(cur.children[item])

            cur = cur.children[item]
            cur.count += 1  # Increment the count for the node

def build_tree(transactions, frequent_count, old_conditional_items=None, new_condition_item=None):
    if old_conditional_items is None:
        old_conditional_items = []
    tree = Tree()
    tree.conditional_items = old_conditional_items
    tree.conditional_items.append(new_condition_item)
    for transaction in transactions:
        for item in transaction:
            tree.item_count[item] = tree.item_count.get(item, 0) + 1

    # items with higher frequent count are first # to help in building the sub-trees
    tree.item_list = list(tree.item_count.keys())
    tree.item_list.sort(key=lambda x: -tree.item_count[x])

    while tree.item_list and tree.item_count[tree.item_list[len(tree.item_list) - 1]] < frequent_count:
        tree.item_list.pop()

    for transaction in transactions:
        tree.insert(transaction, frequent_count)

    return tree
