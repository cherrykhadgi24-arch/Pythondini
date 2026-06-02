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

#Day 2
#tuples cannot be changed after creation
student_record=("alice",20,85.5,"computer science")
print("student record typle:",student_record)

#accessing tuple elements
print("Name:" ,student_record[0] )
print("Name:" ,student_record[1] )

#tuple unpacking
name,age,score,department = student_record
print("\n unpacked  :" ,name ,"is" ,age,"years old,scored", score ,"in" , department)

#When to Use Tuples (Points)
#To store fixed data that should not change.
#To return multiple values from a function.
#To use as dictionary keys because tuples are immutable.

print("\n --sets--")
print("="*50)

#sets automatically remove duplicates 
course_A ={"alice","bob","charlie" ,"Diana"}
course_B={"charlie","diana","eve","frank"}

print("course A students:" , course_A)
print("courseB students:",course_B)

#set operations (great for finding overlaps)
print("\n students in both course:",course_A & course_B)
print("\n students in either course:",course_A |course_B)
print("only in course a:",course_A - course_B)
print("only in one course a:",course_A ^ course_B)

#remove duplicates from using set 
score_with_duplicates = [85,92,85,78,92,95,85]
unique_scores = list(set(score_with_duplicates))
print("\n Original Scores:",score_with_duplicates)
print("\n Unique scores:" , unique_scores)

print("\n--Dictionaries--")
print("=" * 50)

student = {
    "name": "Alice",
    "age": 20,
    "scores": [85, 92, 78],
    "department": "Computer Science",
    "is_active": True,
    "Hobbies": ["Football", "Music", "Gaming","Dancing"]
}

print("Student Dictionary:")
print(student)



alice = student['scores']
passing_scores = [score for score in alice if score > 80]
# Accessing values
print("Alice scores:", student_scores)
print("Alice scores > 80:", passing_scores)
print("\nStudent name :", student['name'])
print("Student scores :", student['scores'])
print("Average score :", sum(student['scores']) / len(student['scores']))
print("\npassing scores(>=80):",passing_scores)

# Adding and updating values
student["grade"] = "A"
student["age"] = 21

print("\nAfter Update:")
print(student)

#conditional statements
#function to determine grade based on score
def get_grade(scores):
 if scores >= 90:
    return "A"
 elif scores >= 80:
    return "B"
 elif scores >= 70:
    return "C"
 elif scores >= 60:
    return "D"
 else:
    return "F"
 


 test_scores = [95, 85, 75, 65, 55]

print("\nGrades:")
for score in student_scores:
    print(f"Score: {score} -> Grade: {get_grade(score)}")