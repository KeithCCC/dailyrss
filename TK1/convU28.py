import sys  # Import sys to access command line arguments
import io
import json


# Example usage
if __name__ == "__main__":
    # Check if a command line argument is provided
    if len(sys.argv) > 1:
        filename = sys.argv[1]  # Get the Unicode string from command line
    else:
        print("Please provide a Unicode string as a command line argument.")
        sys.exit(1)  # Exit if no argument is provided

    with open(filename, 'r') as file:
        data = json.load(file)
    
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False)

