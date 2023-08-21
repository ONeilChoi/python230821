def compare_data_structures():
    # Lists
    list_example = [1, 2, 3]
    list_example.append(4)
    list_example[0] = 0
    
    # Tuples
    tuple_example = (1, 2, 3)
    # Tuples are immutable, so no append or assignment like lists
    
    # Sets
    set_example = {1, 2, 3}
    set_example.add(4)
    set_example.discard(1)
    
    # Dictionaries
    dict_example = {'a': 1, 'b': 2, 'c': 3}
    dict_example['d'] = 4
    
    print("List:")
    print("Pros:", "Flexible size", "Can contain duplicate elements", "Mutable", sep="\n  - ")
    print("Cons:", "Slower for large datasets due to linear search", "No built-in hash support for elements", sep="\n  - ")
    
    print("\nTuple:")
    print("Pros:", "Immutable", "Faster than lists for iteration", "Can be used as dictionary keys", sep="\n  - ")
    print("Cons:", "Cannot modify elements after creation", sep="\n  - ")
    
    print("\nSet:")
    print("Pros:", "No duplicate elements allowed", "Fast membership testing (O(1))", "Mathematical set operations", sep="\n  - ")
    print("Cons:", "Unordered, no indexing", "Slower insertion/deletion than lists", sep="\n  - ")
    
    print("\nDictionary:")
    print("Pros:", "Key-value pairs for mapping", "Fast access to values (O(1))", "Keys are unique and hashable", sep="\n  - ")
    print("Cons:", "Unordered (Python 3.7+ preserves insertion order)", "Slower iteration than lists/tuples", sep="\n  - ")

compare_data_structures()