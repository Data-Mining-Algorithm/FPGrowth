import pandas as pd
import main


class Node:

    def __init__(self, item, parent=None):
        self.item = item
        self.count = 0
        self.parent = parent
        self.children = {}  # child[item], means `item` is a child, and that's a pointer to it's node


def get_path_to_root(node):  # return list of nodes
    path = [node]
    while node.parent:
        node = node.parent
        path.append(node)
    return path


class Tree:

    def __init__(self, parent=None):
        self.item_count = {}  # { item, count }, utilized for item_list creation
        self.item_list = []  # vector<Node>, to iterate over
        self.occurrences = {}  # (item : list of nodes where the item appeared at the tree)
        self.conditional_items = []  # list of conditional items

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
    tree.item_list.sort(key=lambda x: -tree.item_count[x])

    while tree.item_count[tree.item_list[len(tree.item_list) - 1]] < frequent_count:
        tree.item_list.pop()

    for transaction in transactions:
        tree.insert(transaction, frequent_count)

    return tree
