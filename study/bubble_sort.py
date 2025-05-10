unordered_list = [4,8,1,0,3,7,9,2,15]
list_length = len(unordered_list)
ordered_list = unordered_list.copy()

for i in range(list_length):
    for j in range(list_length-i-1):
        if ordered_list[j] > ordered_list[j+1]:
            ordered_list[j], ordered_list[j+1] = ordered_list[j+1], ordered_list[j]
            
print(unordered_list)
print(ordered_list)


#SELECTION SORT
lst = [4,8,1,0,3,7,9,2,15]
list_length = len(lst)

for i in range(list_length):
    min_index = i
    for j in range(i,list_length):
        if lst[min_index] > lst[j]:
            min_index = j
    #swap
    lst[i],lst[min_index] = lst[min_index],lst[i]

print("list selection: ", lst)

#Insertion sort
list = [4,8,1,0,3,7,9,2,15]
list_length = len(list)

for i in range(1, list_length):
    num_to_compare = list[i]
    j = i-1
    while j >= 0:
        list[j+1] = list[j] #list[0:j] is the ordered list 
        if num_to_compare > list[j]:
            break
        j -= 1
    list[j+1] = num_to_compare

print(list)

#Quick SORT
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)
