from file_reader import file_reader


def words_in_file(filename):
    "Prints the aproximated number of words in a file."
    text = file_reader(filename)
    if text != None:
        text_words = text.split()
        aproximated_num_of_words_in_text = len(text_words)

        print(
            f"There is aproximetly {aproximated_num_of_words_in_text} words in {filename} file."
        )
