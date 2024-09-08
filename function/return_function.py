def is_adult(age):
    return age >= 17
    
adult = is_adult(1)
print(adult)

def convert_gender(gender="Unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else: # gender.upper() != "F" or not "M":
        return "Unknown"
    
print(convert_gender("m"))
print(convert_gender("f"))
print(convert_gender("hai"))
print(convert_gender("H"))
print(convert_gender())

def print_number(n, current=1):
    print(current, end=" ")
    if current < n:
        print_number(n, current+1)

print_number(20, 0)