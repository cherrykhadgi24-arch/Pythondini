print("hello world")

name = "Dinita"
faculty = "Computer Science"
dob = "16/11/2006"

# string concatenation
print("Hello, " + name + "! You are a student of " + faculty +
      " and your date of birth is " + dob)

# f-string
print(f"Hello, {name}! You are a student of {faculty} and your date of birth is {dob}")

age = 19
is_student = True
gpa = 4.0

# check datatype
print(f"type of name: {type(name)}")
print(f"type of faculty: {type(faculty)}")
print(f"type of dob: {type(dob)}")
print(f"type of age: {type(age)}")
print(f"type of is_student: {type(is_student)}")
print(f"type of gpa: {type(gpa)}")

# multiple assignments
name, faculty, dob, age, is_student, gpa = (
    "Dini", "BCA", "05/01/2006", 19, True, 4.0
)

print(
    f"Hello, {name}! "
    f"You are a student of {faculty} "
    f"and your date of birth is {dob}. "
    f"Your age is {age}. "
    f"Student status: {is_student}. "
    f"GPA is {gpa}"
)

# swap variables
x, y = 10, 20
print("Before swap: x =", x, "y =", y)

x, y = y, x  # swap without temporary variable

print("After swap: x =", x, "y =", y)

# unpack lists
student_info = ["charlie", 21, 88.0]

name, age, score = student_info
print("Unpacked:", name, age, score)

name1, *others = student_info

print("Name:", name1)
print("Others:", others)  # age and score will be stored in a list

#creating list
student_name=["Alice","bob","charlie","diana"]
student_scores=[85,73,89,95]

print("student names:",student_name)
print("student Score:",student_scores)

#aceessing elements (indexing starts at 0)
print("\n First student:",student_name[0])
print("\n Last student:",student_name[-1])
print("\n First three:",student_name[0:3])
#all studentsfrom index 1 to end 
print("every student:",student_name[:])
print("every second std:",student_name[::2])

#list operations 
student_name.append("eve") #add to end 
print("\n after adding eve:",student_name)

student_name.insert(1, "Frank")#insert at position
print("\n after inserting frank :",student_name)

student_name.remove("bob") #remove by value 
print("\n after removing bob :",student_name)

#list compreshion (powerful feature!)
passing_scores=[score for score in student_scores if score>=80]
print("\npassing scores(>=80):",passing_scores)

#common methods
print("number of students:",len(student_name))
print("highest score of students:",max(student_scores))
print("lowest score of students:",min(student_scores))
