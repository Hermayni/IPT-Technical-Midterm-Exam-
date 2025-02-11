
def is_palindrome(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        return True
    else:
        return False

def check_numbers_file(filename):
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        file.close()
        
        for i in range(len(lines)):
            line = lines[i].strip()
            if line == "":
                continue  
            try:
                numbers = line.split(',')
                numbers = [int(n) for n in numbers]
            except:
                print(f"Line {i+1}: Invalid data - Skipped")
                continue
            
            total = sum(numbers)
            if is_palindrome(total):
                print(f"Line {i+1}: {line} (sum {total}) - Palindrome")
            else:
                print(f"Line {i+1}: {line} (sum {total}) - Not a palindrome")
    except:
        print("Error: Something went wrong with the file.")


# Run functions
filename = "numbers.txt"
check_numbers_file(filename)
