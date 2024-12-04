import pandas as pd


class Node:

    def __init__(self, item, parent=None):
        self.item = item
        self.count = 0
        self.parent = parent
        self.children = {}  # child[item], means `item` is a child, and that's a pointer to it's node


def get_path_to_root(node):  # return list of nodes
    path = []
    ms = 10
    while node is not None and node.item is not None:
        ms = min(ms, node.count)
        # print("ms, node.count:", ms, node.item, node.count)
        path.append(node.item)
        node = node.parent
    path.reverse()
    return path, ms


class Tree:

    def __init__(self):
        self.root = Node(item=None)  # initialize the root node (item=None for root)
        self.item_count = {}  # { item: count }, for counting item frequencies
        self.item_list = []  # List of items sorted by frequency
        self.occurrences = {}  # { item: [list of nodes where the item appears] }
        self.conditional_items = []  # Conditional items for conditional FP-trees
        self.cond_supp = 10

    def insert(self, transaction, frequent_count, p=0):
        cur = self.root  # Start at the root node

        # print("before->", transaction)
        transaction.sort(key=lambda x: self.item_count[x], reverse=True)
        while transaction and self.item_count[transaction[-1]] < frequent_count:
            transaction.pop()

        # if transaction:
        # for t in transaction:
        # print(frequent_count, t, self.item_count[t])
        # transaction = [item for item in transaction if self.item_count[item] >= frequent_count]

        if len(transaction) == 0:
            return

        # print("after->", transaction)

        # if p == 1:
        # print("Initial Tree build:")
        # print(transaction)

        for item in transaction:
            if item not in self.occurrences:
                self.occurrences[item] = []

            if item not in cur.children:
                cur.children[item] = Node(item, parent=cur)  # Add a new node for the item
                self.occurrences[item].append(cur.children[item])
            cur = cur.children[item]
            cur.count += 1  # Increment the count for the node

    def display(self, cur=None, indent=0):
        if cur is None:
            cur = self.root

        if cur is not None and cur.item is not None:
            print("    " * indent, cur.item, cur.count)
        for ch, ch_node in cur.children.items():
            self.display(ch_node, indent + 1)


def build_tree(transactions, frequent_count, old_cond_supp=10, old_conditional_items=None, new_condition_item=None,
               new_cond_supp=10):
    if old_conditional_items is None:
        old_conditional_items = []
    tree = Tree()
    tree.conditional_items = old_conditional_items[:]
    tree.cond_supp = min(old_cond_supp, new_cond_supp)
    # print("Old::", old_conditional_items, "New::", new_condition_item, transactions)
    if new_condition_item is not None:
        tree.conditional_items.append(new_condition_item)

    transactions = [transaction for transaction in transactions if transaction]
    for transaction in transactions:
        transaction = list(set(transaction))
        for item in transaction:
            tree.item_count[item] = tree.item_count.get(item, 0) + 1

    # items with higher frequent count are first # to help in building the sub-trees
    # print(tree.item_list)
    tree.item_list = [item for transaction in transactions for item in transaction if
                      tree.item_count[item] >= frequent_count]
    tree.item_list = list(set(tree.item_list))
    # print("treelist", tree.item_list)
    # if new_condition_item is not None:
    # print("item_list", tree.item_list)
    # print(new_condition_item, "first trans", transactions[0])

    for transaction in transactions:
        # print("ttt", transaction)
        tree.insert(transaction, frequent_count, 1)

    return tree
