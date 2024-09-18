def get_numbers():
    """Get a list of numbers from user input, ensuring correct format."""
    while True:
        numbers_input = input("Enter numbers separated by commas: ")
        try:
            numbers = [float(num) for num in numbers_input.split(',')]
            return numbers  
        except ValueError:
            print("Invalid input! Please make sure to enter numbers separated by commas.")

def calculate_mean(numbers):
    """Calculate and return the mean of a list of numbers."""
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    """Calculate and return the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    mid_index = len(sorted_numbers) // 2
    if len(sorted_numbers) % 2 == 0:
        return (sorted_numbers[mid_index - 1] + sorted_numbers[mid_index]) / 2
    else:
        return sorted_numbers[mid_index]

def calculate_mode(numbers):
    """Calculate and return the mode of a list of numbers."""
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
            
    mode = max(frequency, key=frequency.get)
    return mode

def calculate_range(numbers):
    """Calculate and return the range of a list of numbers."""
    return max(numbers) - min(numbers)

def display_results(statistic_name, value):
    """Display the calculated statistic."""
    print(f"{statistic_name}: {value}")

def main():
    """Main function to run the statistics calculator."""
    
    numbers = get_numbers()
    
    while True:
        print("\nChoose a statistic to calculate:")
        print("1. Mean")
        print("2. Median")
        print("3. Mode")
        print("4. Range")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            mean = calculate_mean(numbers)
            display_results("Mean", mean)
        elif choice == '2':
            median = calculate_median(numbers)
            display_results("Median", median)
        elif choice == '3':
            mode = calculate_mode(numbers)
            display_results("Mode", mode)
        elif choice == '4':
            range_value = calculate_range(numbers)
            display_results("Range", range_value)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

main()