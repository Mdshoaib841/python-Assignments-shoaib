# -----------------------------
# Step 1: Read marks function
# -----------------------------
def read_marks(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()[1:]  # skip header
        return lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    


# Step 2: Generate report function

def generate_report(lines):
    student_data={}

    for line in lines:  
     try:   
        student_id,student_name,subject,marks=line.strip().split(',') #line = '101,Arjun,Math,85\n'
        marks=int(marks)

        if student_id in student_data:  #(iteration 3)-->101 already exist   (iteration 4)-->102 alrady exist
            student_data[student_id]["marks"].append((subject,marks)) #student_data['101']['marks'].append(('Science', 92)) (iteration  3)
                                                                     #student_data['102]['marks].append(('Math', 88)) (iteration 4)
        else:
            student_data[student_id]={
                "name":student_name,
                "marks":[(subject,marks)]
            }    

                    #{
                    #   '101': {'name': 'Arjun', 'marks': [('Math', 85), ('Science', 92)]},
                    #   '102': {'name': 'Sneha', 'marks': [('English', 78), ('Math', 88)]},
                    #   '103': {'name': 'Ravi', 'marks': [('English', 56)]}  (iteraion 6)
                    # }  
                    
                    # (this is student_data)



     except ValueError:  
        print(f"Skipping malformed line: {line.strip()}")
    return student_data


input_file=input("enter a file name :")  #marks.txt
output_file=input("enter a file name to create a student report:")  #report.txt
lines = read_marks(input_file)  #function 1
if lines:
  student_data=generate_report(lines)  #function 2  

  with open(output_file,'w') as report:
    report.write("Student Marks Report Generator\n")
    for sid, data in student_data.items():
        report.write(f"Student ID: {sid}\n")
        report.write(f"Name: {data['name']}\n")
    
        total = 0
        marks_list = data["marks"]

        # assume first subject as highest and lowest
        highest = marks_list[0]
        lowest = marks_list[0]

        for subject, marks in marks_list:
            total += marks

            if marks > highest[1]:
                highest = (subject, marks)
            if marks < lowest[1]:
                lowest = (subject, marks)

        avg = total / len(marks_list)

        # print("Subjects and Marks:")
        # for subject, marks in marks_list:
            # print(f"   {subject} → {marks}")

        report.write(f"Total Marks: {total}\n")
        report.write(f"Average Marks: {avg:.2f}\n")
        report.write(f"Highest Scored Subject: {highest[0]} ({highest[1]})\n")
        report.write(f"Lowest Scored Subject: {lowest[0]} ({lowest[1]})\n")
        report.write("-" * 35+"\n")
    print(f"report successfully written to {output_file} ") 
else:
   print("no data found")     

     




