# Created by vidit.singh at 14-05-2022

def choose_one_using_dict(option):
    switcher = {
        0: "Sunday",
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday"
    }
    return switcher.get(option, "Invalid Option")  # Returns Invalid Option if no match found.


"""
# match is supported after python 3.10 version
def number_to_string(agrument):
    match agrument:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case default:
            return "something"
"""
print(choose_one_using_dict(31))
