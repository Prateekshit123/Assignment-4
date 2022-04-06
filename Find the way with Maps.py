int_list = [1, 2, 3, 4, 5, 6, 7]
print("Original list :", int_list)
triple_list = map(lambda a: a + a + a, int_list)
print("\nTriple of list numbers :", list(triple_list))