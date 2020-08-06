"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = [] # create empty list
    for line in input_file:

        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        data.append(parts) # append each sublist "parts" to main list "data"
    return data # return data list


def print_subject_details(data):
    for subject_information in data:
        print("{:1} is taught by {:12} and has {:4} students.".format(*subject_information))
        # print subject information sentence with correct spacing from sublists in data
main()