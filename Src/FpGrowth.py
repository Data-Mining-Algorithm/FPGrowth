from FpTree import build_tree, get_path_to_root, Node, Tree

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


def FpGrowth(tree, min_sup, call_num=0):
    if len(tree.item_list) == 0:  # if nothing is inside the tree's item list then exit
        # print("last cond items -> ")
        # print(tree.conditional_items, tree.cond_supp)
        return {tuple(tree.conditional_items): tree.cond_supp}

    if not hasattr(tree, 'item_list') or not hasattr(tree, 'occurrences'):
        raise ValueError("Input tree must have 'item_list' and 'occurrences' att    ributes")
    if not isinstance(min_sup, (int, float)) or min_sup <= 0:
        raise ValueError("min_sup must be a positive number")

    frequent_itemsets = {}
    if len(tree.conditional_items) > 0:
        frequent_itemsets = {tuple(tree.conditional_items): tree.cond_supp}

    # print("\n\n\n\n\n\n")
    # print_frequent_itemsets(frequent_itemsets)
    # print("\n\n\n\n\n\n")

    tree.item_list.sort(key=lambda x: tree.item_count[x])
    tree.item_list = list(set(tree.item_list))
    # for item in tree.item_list:
    #    print("item, count",item, tree.item_count[item])
    tl = tree.item_list
    for item in tl:
        #  print("item---------------->",item)
        nodes = tree.occurrences.get(item, [])

        support = 0
        for node in nodes:
            support += node.count  # add the number of nodes to know the support of the current item
        if support < min_sup:  # if the current item's support is less than the minimum support then go back to the start of the loop and start with the next item
            continue

        paths = []  # empty list to store the pattern paths

        if not callable(get_path_to_root):
            raise ValueError("get_path_to_root must be a callable function")

        for node in nodes:
            p, s = get_path_to_root(node.parent)
            s = node.count
            # print(tree.conditional_items, "s::::", item, s)
            while s > 0:
                paths.append(p)
                s = s - 1
        # print(tree.conditional_items,"::::::", paths)
        if not callable(build_tree):
            raise ValueError("build_tree must be a callable function")

        # print(item, support, get_path_to_root(nodes[0]))

        conditional_tree = build_tree(paths, min_sup, tree.cond_supp, tree.conditional_items, item, support)
        # print(item, "->", paths, ",", call_num)

        cl = tree.conditional_items.copy()
        cl.append(item)
        print("conditional tree of ", cl)
        conditional_tree.display()
        print("-------------------------------------")
        frequent_itemsets.update(FpGrowth(conditional_tree, min_sup, call_num + 1))

    return frequent_itemsets


"""
Description of the function's purpose.

    Args:
        parameter1: frequent_item_set list

    Just print the list
"""


def print_frequent_itemsets(itemsets):
    for itemset, support in itemsets.items():
        print(f" itemset: {itemset}, support: {support}")
