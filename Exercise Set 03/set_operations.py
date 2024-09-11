set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

set_diff1 = set1 - set2
set_diff2 = set2 - set1

set_union = set1 | set2

set_sym_diff1 = set1 ^ set2
set_sym_diff2 = set2 ^ set1

set_intersection1 = set1 & set2
set_intersection2 = set2 & set1

print("Set Difference (set1 - set2):", set_diff1)
print("Set Difference (set2 - set1):", set_diff2)
print("Union of Sets (set1 | set2):", set_union)
print("Symmetric Difference (set1 ^ set2):", set_sym_diff1)
print("Symmetric Difference (set2 ^ set1):", set_sym_diff2)
print("Set Intersection (set1 & set2):", set_intersection1)
print("Set Intersection (set2 & set1):", set_intersection2)
