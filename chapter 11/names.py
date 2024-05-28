from name_function import get_formated_name

print('Enter "q" at any time to quit.')
while True:
    first = input("\nPlease give me a first name: ").strip()
    if first == "q":
        break
    middle = input(
        '\nPlease give me a middle name if availible, or just press "Enter" if you don\'t have one: '
    ).strip()
    if middle == "q":
        break
    last = input("Please give me a last name: ").strip()
    if last == "q":
        break

    formated_name = get_formated_name(first, last, middle)
    print(f" Neatly formated name: {formated_name}")
