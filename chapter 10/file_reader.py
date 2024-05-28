# from pathlib import Path

# # PATH_TO_PI_NUM_TXT = Path.cwd() / "chapter 10" / "pi_digits.txt"
# # print(PATH_TO_PI_NUM_TXT)
# # contents = PATH_TO_PI_NUM_TXT.read_text()
# # lines = contents.splitlines()

# # pi_string = ""
# # for line in lines:
# #     pi_string += line

# # print(pi_string)
# # print(len(pi_string))

# # pi_num = float(pi_string.replace(" ", ""))
# # print(pi_num)

# PATH_TO_PI_NUM_TXT = Path.cwd() / "chapter 10" / "pi_digits.txt"


# def get_string_from_file(path):
#     pi_string = ""
#     for line in path.read_text().splitlines():
#         pi_string += line
#     return pi_string


# pi_string = get_string_from_file(PATH_TO_PI_NUM_TXT)


# def print_pi_with_precision(precision):
#     pi_float_with_precision = float(pi_string[: precision + 2])
#     print(pi_float_with_precision)


# print(pi_string)
# print(f"PI string length with a precision one milion: {len(pi_string)}")

# print_pi_with_precision(1)
# print_pi_with_precision(5)
# print_pi_with_precision(7)

# birthdayDateString = "".join(
#     input("Enter your birthday date in MM.DD.YYYY format: ").split(".")
# )


# if birthdayDateString in pi_string:
#     print(
#         f"Your birthday appears in the pi number under the precision one milion starting from the symbol at index {pi_string.index(birthdayDateString)} up to symbol at index {pi_string.index(birthdayDateString) + len(birthdayDateString)}"
#     )
# else:
#     print(
#         "Your birthday doesn't appears in the pi number under the precision one milion."
#     )

################################

from pathlib import Path


def file_reader(filename):
    try:
        path = Path.cwd() / "chapter 10" / filename
        text = path.read_text(encoding="utf-8")
        return text
    except FileNotFoundError:
        print(f'Sorry, the file "{path}" doesn\'t exist.')
