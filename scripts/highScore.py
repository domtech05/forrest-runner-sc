def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to check if any swaps are made in this pass
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the current element is greater than the next one
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped in the inner loop, the array is sorted
        if not swapped:
            break


def main():
    # Open the text file
    fileName = '../scores/allScores.txt'  # Change this to your file name
    with open(fileName, 'r') as file:
        # Read the list of numbers
        numbers = [int(line.strip()) for line in file]

    # Sort the numbers using bubble sort
    bubbleSort(numbers)

    # Output the top 6 highest numbers
    top_6 = numbers[-6:][::-1]  # Extract top 6 highest numbers and reverse for ascending order

    # Write the top 6 highest numbers to a new text file
    outputFileName = '../scores/highScores.txt'  # Change this to your desired output file name
    with open(outputFileName, 'w') as output_file:
        for num in top_6:
            output_file.write(str(num) + '\n')


if __name__ == "__main__":
    main()
