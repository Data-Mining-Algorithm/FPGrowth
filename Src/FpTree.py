import pandas as pd
import main

class Node:

    def __init__(self, item, parent = None):
        self.item = item
        self.count = 0
        self.parent = parent
        self.children = {} # child[item], means `item` is a child, and that's a pointer to it's node
class Tree:

    def __init__(self, parent=None):
        self.item_count = {}  # { item, count }
        self.item_list = [] # vector<Node>
        self.occurrences = {}  # (item : list of nodes where the item appeared at the tree)
        self.conditional_items = [] # list of conditional items
    def insert(self, transaction, frequent_count):
        cur = self
        transaction.sort(key=lambda x: -cur.items_count[x])

        while self.item_count[transaction[len(transaction) - 1]] < frequent_count:
            transaction.pop()

        for item in transaction:
            if item not in self.occurrences:
                self.occurrences[item] = []

            if item not in cur.children:
                cur.children[item] = Tree(cur)
                self.occurrences[item].append(cur.children[item])

            cur = cur.children[item]
            cur.visits_count += 1

    def get_path_to_root(self, node): # return list of nodes
        path = []
        path.append(node)
        while (node.parent):
            node = node.parent
            path.append(node)
        return path


def build_tree(transactions, frequent_count, old_conditional_items = [], new_condition_item = None):
    tree = Tree()
    tree.conditional_items = old_conditional_items
    tree.conditional_items.append(new_condition_item)
    for transaction in transactions:
        for item in transaction:
            tree.item_counts[item] = tree.item_counts.get(item, 0) + 1

    # items with higher frequent count are first # to help in building the sub-trees
    tree.item_list.sort(key=lambda x: -tree.item_count[x])

    while tree.item_count[tree.item_list[len(tree.item_list) - 1]] < frequent_count:
        tree.item_list.pop()

    for transaction in transactions:
        tree.insert_branch(transaction)

    return tree
