# Displays course info based on a dictionary of (prefix, course_number) as keys
courses = {
    ("COP", 1000): ("Intro to Programming", "Dr. Smith", "MWF 10:00"),
    ("MAC", 2311): ("Calculus I", "Dr. Jones", "TTh 14:00"),
}

prefix = input("Enter course prefix: ").upper()
number = int(input("Enter course number: "))

key = (prefix, number)
if key in courses:
    name, instructor, time = courses[key]
    print(f"{name} is taught by {instructor} at {time}")
else:
    print("Course not found.")