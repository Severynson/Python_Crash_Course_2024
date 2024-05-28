from city import create_address


def test_address_with_city_and_street():
    'Test type of addresses like "Lviv, Naukova 22A St."'
    formated_address = create_address("lviv", "naukova 22A")
    assert formated_address == "Lviv, Naukova 22A St."


def test_address_with_country_city_and_street():
    'Test type of addresses like "Poland, Lublin, Pilsutskiego 65 St."'
    formated_address = create_address("lublin", "pilsutskiego 65", "poland")
    assert formated_address == "Poland, Lublin, Pilsutskiego 65 St."
