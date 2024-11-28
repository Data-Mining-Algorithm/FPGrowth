import pandas as pd
from FpTree import build_tree
from FpGrowth import FpGrowth

min_sup = 0.6
min_conf = 0.8
# items_count = {}  # (item : frequent_count)
# items_list = []  # array of items
# occurrences = {}  # (item : list of nodes where the item appeared at the main trie)
frequent_itemsets = {}  # (itemset : frequent_count)

file_path = "D:/FPGrowth/transactions.xlsx" # replace with complete file path
data = pd.read_excel(file_path)
transactions = data['items'].apply(lambda x: x.split(","))  # list of lists
transactions = [list(set([item.strip() for item in transaction])) for transaction in transactions]  # make unique
frequent_count = round(min_sup * len(transactions))
tree = build_tree(transactions, frequent_count)
frequent_itemsets = FpGrowth(tree, frequent_count)
for itemset, support in frequent_itemsets:
    print(f"Itemset: {itemset}, Support: {support}")



