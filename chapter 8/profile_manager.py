def build_profile(first, last, **user_info):
    "Building a dictionary containinng everything we  know about the user"
    user_info["first_name"] = first.lower().title()
    user_info["last_name"] = last.lower().title()
    return user_info
