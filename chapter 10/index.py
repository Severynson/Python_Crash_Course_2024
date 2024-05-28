from pathlib import Path

alternative_perspectives = {
    "God": "Satan",
    "great": "terible",
    "love": "hate",
    "wonderful": "scary",
    "glory": "sin",
}


def split_via_couple_of_symbols(whole_string, *symbols_to_split_through):
    text_splited_by_words_and_symbols = [""]

    for symbol in whole_string:
        if symbol not in symbols_to_split_through:
            text_splited_by_words_and_symbols[-1] += symbol
        else:
            text_splited_by_words_and_symbols.append(symbol)
            text_splited_by_words_and_symbols.append("")

    return [x for x in text_splited_by_words_and_symbols if x != ""]


my_outlook_path = Path.cwd() / "chapter 10" / "world.txt"
my_outlook = my_outlook_path.read_text()


def change_perception_perspective():
    my_outlook_splited_4_analisys = split_via_couple_of_symbols(
        my_outlook, "!", ".", ",", " "
    )

    for word in my_outlook_splited_4_analisys:
        curr_word_index = my_outlook_splited_4_analisys.index(word)

        if word in alternative_perspectives.keys():
            antonim = alternative_perspectives[word]
            my_outlook_splited_4_analisys[curr_word_index] = antonim

        if word in alternative_perspectives.values():
            antonim = list(alternative_perspectives.keys())[
                list(alternative_perspectives.values()).index(word)
            ]
            my_outlook_splited_4_analisys[curr_word_index] = antonim

    print("".join(my_outlook_splited_4_analisys))

    my_outlook_path.write_text("".join(my_outlook_splited_4_analisys))


change_perception_perspective()


from word_count import words_in_file

filenames_to_count_words = [
    "alice_in_wonderland.txt",
    "unexisting_file.txt",
    "world.txt",
]

for filename in filenames_to_count_words:
    print(filename + ": ", end="")
    words_in_file(filename)
