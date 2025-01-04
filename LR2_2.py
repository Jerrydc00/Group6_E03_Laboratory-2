def navigate_file():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        return

    line_count = len(lines)
    print(f"The file contains {line_count} lines.")

    while True:
        try:
            line_number = int(input(f"Enter a line number (1-{line_count}, or 0 to quit): "))
            if line_number == 0:
                print("Exiting program.")
                break
            elif 1 <= line_number <= line_count:
                print(lines[line_number - 1].strip())
            else:
                print(f"Invalid line number. Please enter a number between 1 and {line_count}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    navigate_file()
