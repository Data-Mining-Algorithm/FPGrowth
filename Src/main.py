import pandas as pd
from FpTree import build_tree
from FpGrowth import FpGrowth, print_frequent_itemsets
from Src import association_rules
from Src.association_rules import calculate_association_rules, print_strong_rules, print_all_rules

# from association_rules import calculate_association_rules

min_sup = 0.6
min_conf = 0.7

file_path = "D:/Curriculum/Semester 5/Data Mining/Fpgrowth_Project/transactions.xlsx"  # replace with complete file path
data = pd.read_excel(file_path)
transactions = data['items'].apply(lambda x: x.split(","))  # list of lists
transactions = [list(set([item.strip() for item in transaction])) for transaction in transactions]  # make unique
frequent_count = 3  # round(min_sup * len(transactions))

# print(transactions)
print("fq:", frequent_count)
# -----------------------------------------------------
transactions = [sorted(sublist, reverse=True) for sublist in transactions]
tree = build_tree(transactions, frequent_count)

tree.display()
print("\n-------------------------------------\n")
frequent_itemsets = FpGrowth(tree, frequent_count)

print_frequent_itemsets(frequent_itemsets)
# -----------------------------------------------------
rules, all_lift = calculate_association_rules(frequent_itemsets, len(transactions), min_conf)
print_all_rules(rules, all_lift)
print_strong_rules(rules, all_lift, min_conf)
