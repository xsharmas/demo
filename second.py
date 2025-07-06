#write code to implement array functions like append, pop, insert, remove, and sort and input from the user to perform these operations on an array.
def append(arr, value):
    arr.append(value)
    return arr
def pop(arr):
    if arr:
        return arr.pop()
    else:
        return "Array is empty, cannot pop element"
def insert(arr, index, value):
    if index < 0 or index > len(arr):
        return "Index out of bounds"
    arr.insert(index, value)
    return arr
def remove(arr, value):
    if value in arr:
        arr.remove(value)
        return arr
    else:
        return "Value not found in array"
def sort(arr):
    return sorted(arr)
def main():
    arr = []
    while True:
        print("\nArray Operations:")
        print("1. Append")
        print("2. Pop")
        print("3. Insert")
        print("4. Remove")
        print("5. Sort")
        print("6. Exit")
        
        choice = input("Choose an operation (1-6): ")
        
        if choice == '1':
            try:
                value = int(input("Enter value to append: "))
                arr = append(arr, value)
                print(f"Array after append: {arr}")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == '2':
            popped_value = pop(arr)
            print(f"Popped value: {popped_value}")
            print(f"Array after pop: {arr}")
        elif choice == '3':
            try:
                index = int(input("Enter index to insert at: "))
                value = int(input("Enter value to insert: "))
                arr = insert(arr, index, value)
                print(f"Array after insert: {arr}")
            except ValueError:
                print("Invalid input. Please enter integers for index and value.")
        elif choice == '4':
            try:
                value = int(input("Enter value to remove: "))
                arr = remove(arr, value)
                print(f"Array after remove: {arr}")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == '5':
            arr = sort(arr)
            print(f"Sorted array: {arr}")
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == "__main__":
    main()
# This code implements basic array operations like append, pop, insert, remove, and sort.
# It allows the user to perform these operations interactively through a menu-driven interface.
