def min_max_value(lst):
    minimum=min(lst)
    maximum=max(lst)
    min_index=lst.index(minimum)
    max_index=lst.index(maximum)
    return {
        "Min value":minimum,
        "Max value":maximum,
        "Min index":min_index,
        "Max Index":max_index}
    
lst=list(map(int,input("Enter the elements of the list seperated by spaces:").split()))
print(min_max_value(lst))
