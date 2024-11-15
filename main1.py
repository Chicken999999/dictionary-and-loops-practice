import student_data

students = student_data.students

common_lname = []
last_names =[]
for last_name in students:
    last_name = last_name['LName']
    last_names.append(last_name)

print(last_names)

for last_name in last_names:
    for last_name2 in last_names:
        if last_name == last_name2:
            common_lname.append(last_name)

for name in common_lname:
    print(f"{name} is a last name found more than once. ")
            