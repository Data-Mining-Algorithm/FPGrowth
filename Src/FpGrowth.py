# TODO: write recursive function to be the fpgrowth algorithm

"""
Description of the function's purpose.

    Args:
        parameter1: FpTree
        parameter2: min_sup

    Returns:
        List of frequent item sets as {itemset, frequency}
    Hint: Use python
"""

from FpTree import build_tree,get_path_to_root,Node,Tree

def FpGrowth(tree: Tree, min_sup):

    if not tree.item_list: # if nothing is inside the tree's item list then exit
        return []

    frequent_itemsets = []

    for item in tree.item_list: 
        nodes = tree.occurrences.get(item, []) # get the list of nodes where the current items appears in the tree
        
        support = 0
        for node in nodes:
            support += node.count # add the number of nodes to know the support of the current item

        if support < min_sup: # if the current item's support is less than the minimum support then go back to the start of the loop and start with the next item
            continue

        frequent_itemsets.append(([item], support))

        conditional_transactions = [] # empty list to store the conditional transactions

        for node in nodes:
            path_to_root = get_path_to_root(node)
            path_to_root = [n.item for n in reversed(path_to_root[:-1])]
            conditional_transactions.append(path_to_root)

        print(f"Conditional Transactions for {item}: {conditional_transactions}")

        conditional_tree = build_tree(conditional_transactions, min_sup)

        print(f"Conditional Tree for {item}: {conditional_tree.item_list}")

        conditional_frequent_itemsets = FpGrowth(conditional_tree, min_sup)

        for itemset, count in conditional_frequent_itemsets:
            frequent_itemsets.append(([item] + itemset, count))

    return frequent_itemsets


"""
Description of the function's purpose.

    Args:
        parameter1: frequent_item_set list

    Just print the list
"""


def print_frequent_itemsets(itemsets):
    for itemset, count in itemsets:
        print(f"Itemset: {itemset}, Count: {count}")
