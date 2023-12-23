def mergeTwoLists(l1, l2):
    merged = []
    
    while l1 and l2:
        print(f"Comparing {l1[0]} from list1 and {l2[0]} from list2")
        if l1[0] < l2[0]:
            merged.append(l1.pop(0))
            print(f"Added {merged[-1]} from list1")
        else:
            merged.append(l2.pop(0))
            print(f"Added {merged[-1]} from list2")
    
    # Adding remaining elements if one of the lists is longer
    merged.extend(l1 or l2)
    print(f"Added remaining elements: {l1 or l2}")
    
    return merged

# Example usage
list1 = [1, 2, 4]
list2 = [1, 3, 4, 5]
print(mergeTwoLists(list1, list2))  # Expected to return [1, 1, 2, 3, 4, 4, 5]
