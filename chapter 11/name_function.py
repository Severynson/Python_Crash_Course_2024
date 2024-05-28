def get_formated_name(firstname, secondname, middlename=""):
    "Generate a neatly formated fullname"
    if middlename == "":
        fullname = f"{firstname} {secondname}".title()
    else:
        fullname = f"{firstname} {secondname} {middlename}".title()
    return fullname
