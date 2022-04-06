lst = [4, 5, 2, 9]
def square_num(n):
    return n * n
print("Original list :", lst)
result = map(square_num, lst)
print("\nSquare the elements of the list :", list(result))