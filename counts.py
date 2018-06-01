# Scenario 1

def count_upper_case(message):
    count = 0
    for c in message:
        if c.isupper():
            count += 1
    return count


assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%%^") == 0, "Special characters"
assert count_upper_case(".-_/\|;<,>") ==0, "More special characters"


print(count_upper_case("Let's see if it WORKS!"))
print(count_upper_case(" "))
print("All the tests passed")





#Scenario 2
"""
def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])

print(count_upper_case("Let's see if it WORKS!"))
print(count_upper_case(" "))
print("All the tests passed")

"""