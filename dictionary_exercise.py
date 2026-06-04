phone = input ("Enter your phone number: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)