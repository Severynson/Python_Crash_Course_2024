from name_function import get_formated_name


def test_first_last_name():
    "Do names like Janis Joplin' work?"
    formated_name = get_formated_name("janis", "joplin")
    assert formated_name == "Janis Joplin"


def test_first__midle_and_last_name():
    "Do names like Wolfgang Amadeus Mozart' work?"
    formatted_name = get_formated_name("wolfgang", "amadeus", "mozart")
    assert formatted_name == "Wolfgang Amadeus Mozart"
