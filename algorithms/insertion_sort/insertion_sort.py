def insertion_sort(input_arr: list) -> list:
    length = len(input_arr)
    for i in range(1,length):
        current = i - 1
        temp = input_arr[i]
        while current >= 0 and temp < input_arr[current]:
            input_arr[current + 1] = input_arr[current]
            current = current -1
        input_arr[current + 1] = temp
    return input_arr

if __name__ == "__main__":
    sample_list = [1,5,4,2,3,6,7,0,9,8]
    insertionSort(sample_list)
    print(sample_list)