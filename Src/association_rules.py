def calculate_confidence_helper(tot_supp, h1, h2, frequent_itemsets):
    return tot_supp / frequent_itemsets[tuple(h1)]


def calculate_lift_helper(tot_supp, h1, h2, frequent_itemsets, n):
    nom = tot_supp / n
    den = (frequent_itemsets[tuple(h1)] / n) * (frequent_itemsets[tuple(h2)] / n)
    return nom / den


def calculate_association_rules(fi, _n, mc):
    rules = {}
    all_lift = {}
    for itemset, supp in fi.items():
        n = len(itemset)
        for mask in range(1, 1 << n):
            h1, h2 = [], []
            for i in range(n):
                if (1 << i) & mask:
                    h1.append(itemset[i])
                else:
                    h2.append(itemset[i])
            if len(h1) > 0 and len(h2) > 0:
                rules[(tuple(h1), tuple(h2))] = calculate_confidence_helper(
                    supp, h1, h2, fi
                )
                all_lift[(tuple(h1), tuple(h2))] = calculate_lift_helper(
                    supp, h1, h2, fi, _n
                )
    return rules, all_lift


def print_all_rules(rules, all_lift):
    print("\n------ All Association Rules ------\n")
    for (h1, h2), confidence in rules.items():
        lift = all_lift.get((h1, h2), None)
        print(f"Rule: {h1} -> {h2}, Confidence: {confidence:.2f}", end="")
        if lift is not None:
            print(f", Lift: {lift:.2f}")
        else:
            print("")


def print_strong_rules(rules, all_lift, min_conf):
    print(f"\n------ Strong Association Rules (Confidence >= {min_conf}) ------\n")
    for (h1, h2), confidence in rules.items():
        if confidence >= min_conf:
            lift = all_lift.get((h1, h2), None)
            print(f"Rule: {h1} -> {h2}, Confidence: {confidence:.2f}", end="")
            if lift is not None:
                print(f", Lift: {lift:.2f}")
            else:
                print("")
