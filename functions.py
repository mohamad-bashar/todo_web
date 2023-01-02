def convert_number_to_words(number):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
            "eighteen", "nineteen"]

    if number < 10:
        return ones[number]
    elif number < 20:
        return teens[number - 10]
    else:
        return tens[number // 10] + ones[number % 10]
    
def get_todos(filepath = 'todos.txt'):
    with open(filepath, 'r') as file:
        todos = file.readlines()  
    return todos


def write_todos(todos, filepath = 'todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos)   
