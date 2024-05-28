def create_address(city_title, street_address, country=None):
    "Create a single address string in a proper format."

    if country != None:
        return f"{country}, {city_title}, {street_address} st.".title()
    else:
        return f"{city_title}, {street_address} st.".title()


# print(create_address("lviv", "naukova 22A"))
# print(create_address(city_title="lviv", street_address="naukova 22A"))
# print(create_address("lublin", "pilsutskiego 65", "poland"))
