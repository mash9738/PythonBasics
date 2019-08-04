number_to_text = {
    "1": "one",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten",
    ":": ""
}

a = input("enter number: \n")

output = ""
for number in a:
    output += number_to_text.get(number)
print(output)
