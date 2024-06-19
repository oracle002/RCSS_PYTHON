#1.10. Dictionary to store student details and find student with highest total marks

students = {
    'Majo': {'roll_no': 30, 'total_marks': 450},
    'Anusree': {'roll_no': 8, 'total_marks': 480},
    'Nihal': {'roll_no': 37, 'total_marks': 410},
    'Hari':{'roll_no': 1, 'total_marks': 410}
}

max_student = max(students, key=lambda x: students[x]['total_marks'])
print(f"Details of student with highest marks:")
print(f"Name: {max_student}, Roll No: {students[max_student]['roll_no']}, Total Marks: {students[max_student]['total_marks']}")


