def binary_search(arr, target):
    low_index = 0
    high_index = len(arr) - 1

    while low_index <= high_index:
        mid_index = (low_index + high_index) // 2  # Calculate mid point
        # Check if target is present at mid
        if arr[mid_index] == target:
            return mid_index
        # If target is greater, ignore left half
        elif arr[mid_index] < target:
            low_index = mid_index + 1
        # If target is smaller, ignore right half
        else:
            high_index = mid_index - 1
    
    # Target is not present in array
    return -1

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} is present at index {result}.")
else:
    print(f"Element {target} is not present in the array.")

def busqueda_lineal_recursiva(lista, objetivo, indice=0):
    """Realiza una búsqueda lineal recursiva."""
    if indice >= len(lista):
        return -1
    if lista[indice] == objetivo:
        return indice
    return busqueda_lineal_recursiva(lista, objetivo, indice + 1)

def search_element(lst, target):
    index = 0
    for element in lst:
        index += 1
        if element == target:
            return index
    return -1

print(search_element([0,2,5,4,78,5,3], 5))