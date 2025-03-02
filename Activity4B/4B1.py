A_only       = {'a', 'g'}
A_and_B      = {'b'}
A_and_C      = {'d', 'f'}
B_only       = {'l', 'm', 'o'}
B_and_C      = {'h'}
C_only       = {'k', 'i', 'j'}
A_and_B_and_C= {'c'}   

A = A_only.union(A_and_B, A_and_C, A_and_B_and_C)
B = B_only.union(A_and_B, B_and_C, A_and_B_and_C)
C = C_only.union(A_and_C, B_and_C, A_and_B_and_C)

print("Set A:", A)
print("Set B:", B)
print("Set C:", C)

union_AB = A.union(B)
print("\nA. Number of elements in A ∪ B:", len(union_AB))
print("Elements in A ∪ B:", union_AB)

B_exclusive = B.difference(A.union(C))
print("\nB. Elements in B not in A ∪ C:", B_exclusive)
print("Number of such elements:", len(B_exclusive))

set_i = B_and_C.union(C_only)
print("\nC.I. [h, i, j, k]:", sorted(list(set_i)))

set_ii = A_and_B_and_C.union(A_and_C)
print("C.II. [c, d, f]:", sorted(list(set_ii)))

set_iii = A_and_B.union(B_and_C, A_and_B_and_C)
print("C.III. [b, c, h]:", sorted(list(set_iii)))

set_iv = A_and_C
print("C.IV. [d, f]:", sorted(list(set_iv)))

set_v = A_and_B_and_C
print("C.V. [c]:", sorted(list(set_v)))

set_vi = B_only
print("C.VI. [l, m, o]:", sorted(list(set_vi)))