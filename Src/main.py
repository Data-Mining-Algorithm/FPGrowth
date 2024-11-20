import pandas as pd

min_sup = 0.2
min_conf = 0.5
# items_count = {}  # (item : frequent_count)
# items_list = []  # array of items
# occurrences = {}  # (item : list of nodes where the item appeared at the main trie)
frequent_itemsets = {}  # (itemset : frequent_count)

file_path = "D:/Curriculum/Semester 5/Data Mining/Fpgrowth_Project/transactions.xlsx" # replace with complete file path
data = pd.read_excel(file_path)
transactions = data['items'].apply(lambda x: x.split(","))  # list of lists
transactions = [list(set([item.strip() for item in transaction])) for transaction in transactions]  # make unique
frequent_count = round(min_sup * len(transactions))
# print(transactions)

