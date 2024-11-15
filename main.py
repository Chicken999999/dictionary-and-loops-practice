# Alright, let's simplify and rephrase the problem set to avoid using functions:
import student_data

# print(student_data.students)
students = student_data.students
# print(len(students))
# print(students[3]['Combo,Name'])
# print(students[3]['Email'][0])
# print(studaim tiner\ents[3]['Email'][1])

# for student in students:

ू

# for loops allow us to
#iterate through the data
#and perform some function

#we are iterating through the data
#and printing the name and email of the students
#we are also printing a line of underscores to separate the students
#we are also printing a line of underscores to separate the students
# me
# for student in students:
#     print(student['Combo,Name'])
#     print(student['Email'][0])
#     print(student['Email'][1])
#     print("_"*25)

#     print(student['HR'])
#     print(student['GL'])
#     print("_"*25)

# # we are asking the user to input their name
# # then we are checking if the name is in the data
# # if the name is in the data we are printing the name and "this works"
# id = int(input("what is your id?")) 
# for student in students:
#     if id == student['CPSID']:
#         print(student['CPSID'])
#         print("this works")


# Let's try to print out the emails of the students:    
students = [
 "First_name": "mikey",
 "last_name": "alfaro",
 "emails": ["malfaro1@gmail.com", "malfaro2@gmail.com"]
 ################################################################################################################
#1 Print student Details By Miguel Chaidez
]
for student in students:
     first_name = student["first_name"] #Ask for user First name &
last_name = student["last_name"] #And last name 
print(f"Name:{first_name} {last_name}")
for i, email in range(student["emails"], start=1): #Print studnet's full name along with both emails
print(f"Email{i}: {email}")

################################################################################################################
#2 Search for Students in a specific Homeroom   By Miguel Chaidez

#Ask students for homeroom code
homeroom_code = []
for students in students:
    
     if student["homeroom"]==homeroom_code:
        found_students = True #Check to see if student are found within homeroom #
        print("Name: " + student['first_name'] + " " + student['last_name'])
        for i, email in range(student["emails"], start=1): #Print each students' email 
            print(f"Email") 
if not found_students: #If no students are found in the homeroom, print "No students found in this homeroom."
    print("No students found in this homeroom.")

################################################################################################################
# 3.) Check if a student is in a list   By Giovanni Aguayo
    
name = input("What is your first name")  #Asking the user for there first name.
for student in students:
    if name == student[ "FName"]:  #if the name they put matches our 'FName' in our list it will print out there 'HR'.
        print(student["HR"])
        print("YAY!")
   
################################################################################################################
# 4.) Filter students by grade level    By Giovanni Aguayo
        
for student in students:   
    if 10 == student['GL']:   #If there 'GL' matches grade 10 it will print out there "Combo,Name" and there 'CPSID'.
        print (student["Combo,Name"],student['CPSID'])

################################################################################################################

# 5 Format Email List for Newsletter     By Cristofer Alfaro

email_list = [] # declares an empty list to store emails
for student in students: #iterates through every student
    for email in student["Email"]: #iterates through every email found in a certain student
        email_list.append(email) #adds all emails from the student into the list
print(email_list) # prints all the emails

################################################################################################################

# 6 Find Students with Common Last Names     By Cristofer Alfaro

# declare a list to store the common last names
common_lname = []

# puts all last names in a list
last_names =[]
for last_name in students:
    last_name = last_name['LName']
    last_names.append(last_name)

# uses the list of last names to compare if a ceratain last name is found more than once in students and adds it to the common_lname list if it is.
for last_name in last_names: 
    for last_name2 in last_names:
        if last_name == last_name2:
            common_lname.append(last_name)

# prints all the names that are in the common_lname list
for name in common_lname:
    print(f"{name} is a last name found more than once. ")
            
            