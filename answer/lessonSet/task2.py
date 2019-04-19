"""
課題 集合型
"""

values1 = {0, 10, 200, 1000, 2, 100} 
values2 = {0, 0.01, 2, 600, 10, 100}
print("OR: %s" % (values1 | values2))   # OR: {0, 2, 100, 1000, 200, 10, 0.01, 600}
print("AND: %s" % (values1 & values2))  # AND: {0, 2, 10, 100}
print("DIFF: %s" % (values1 - values2)) # DIFF: {1000, 200}