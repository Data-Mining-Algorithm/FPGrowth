"""
Description of the function's purpose.

    Args:
        parameter1: A list of itemsets

    Returns:
        Dictionary, key: {itemset1, itemset2}, value: {support, confidence, lift}

"""


def calculate_association_rules(itemsets):
    return


"""
Description of the function's purpose.

    Args:
        parameter1: itemsets -> list of all itemsets
        parameter2: i1 -> first itemset
        parameter3: i2 -> second itemset

    Expected Behaviour:
        support(x -> y) = support(y -> x) = p(x and y)
        so one may loop over all itemsets, to count the number of transactions where i1 and i2    
        happen together, let that be `count`
        then support = count / itemsets.size

    Returns:
        A floating point number, the support of the 2 itemsets
    Hint: Use python
"""


def calculate_support(itemsets, i1, i2):
    return 0


"""
Description of the function's purpose.

    Args:
        parameter1: i1 -> first itemset
        parameter2: i2 -> second itemset

    Expected Behaviour:
        Confidence (x -> y) = p(y | x) = p(x and y) / p(x)  
        so one may loop over all itemsets, to count the number of transactions where i1 and i2    
        happen together, let that be `count_both`, and also count  the number of transactions 
        where i2 is present, let the be `count_x`
        then confidence (x -> y) = count_both / count_x

    Returns:
        A floating point number, confidence(i1 -> i2)
"""


def calculate_confidence(i1, i2):
    return 0


"""
Description of the function's purpose.

    Args:
        parameter1: i1 -> first itemset
        parameter2: i2 -> second itemset

    Expected Behaviour:
        Lift (x -> y) = p(x and y) / (p(x)  * p(y))
        Get all probabilities same way described in the above functions.

    Returns:
        A floating point number, confidence(i1 -> i2)
"""


def calculate_lift(i1, i2):
    return 0


"""
Description of the function's purpose.

    Args:
        parameter1: rules -> Dictionary { key: {i1, i2}, value: {support, confidence, lift} }

    Expected Behaviour:
        let i1 be x and i2 be y
        then print the following:
        "Support(x -> y) = .. (only if Strong)
         Confidence (x -> y) = .. (only if Strong) "

    Returns:
        A floating point number, confidence(i1 -> i2)
"""


def print_strong_rules(rules):
    return
