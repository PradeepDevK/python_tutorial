def remove_duplicates(numbers):
    new_list = []
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
    
    return new_list;

def remove_duplicates2(numbers):
    return list(set(numbers))

ids = [1, 2, 3, 4, 5, 2, 1, 8, 9, 3, 4, 5, 11, 2 , 1]
result = remove_duplicates2(ids)
print(result)